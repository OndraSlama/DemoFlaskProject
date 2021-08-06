from flask import json
from flask_restful import Resource
import requests
import os
import base64


from common.authentication import auth
from common.annotation_parser import AnnotationParser

class AnnotationResource(Resource):
    """ Resource for /export endpoint - exporting XML format to another  """

    # Rossum api data
    rossum_url = "https://api.elis.rossum.ai/v1/annotations/{annotation_id}" 
    rossum_user = os.environ.get('ROSSUM_USER')
    rossum_pass = os.environ.get('ROSSUM_PASS')

    # My little endpoint data
    mle_url = "https://my-little-endpoint.ok/rossum"

    @auth.login_required
    def get(self, annotation_id:int) -> str:
        
        # Get the annotation from the rossum API
        credentials: tuple = (self.rossum_user, self.rossum_pass)
        params: dict = {"format": "xml"}
        url: str = self.rossum_url.format(annotation_id=annotation_id)
        rossum_response = requests.get(url, auth=credentials, params=params)

        # Parse the downloaded annotation
        if rossum_response.status_code != 200:
            from resources import dummy_response
            parser = AnnotationParser(dummy_response)
        else:
            parser = AnnotationParser(rossum_response.content)
        from common.xml_templates import invoices_template
        parsed_annotation: str = parser.parse(invoices_template)

        # Send the annotation to the my-little-endpoint
        parsed_annotation_b64_encoded = base64.b64encode(parsed_annotation.encode('utf-8')).decode('utf-8')
        try:
            mle_response = requests.post(self.mle_url, json={"annotationId": annotation_id, "content": parsed_annotation_b64_encoded})
            success = mle_response.status_code == 200
        except requests.exceptions.ConnectionError:
            success = False

        # Return response
        return {
                "success": success,          
            }, 200 if success else 400

