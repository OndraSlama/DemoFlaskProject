from flask_restful import Resource
from flask import jsonify
import requests
import os


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


        # Return response
        return {
                "success": True,
                "content": {"id": annotation_id, 
                            "response": rossum_response.text, 
                            "parsed_annotation": parsed_annotation
                        }            
            }, 200

