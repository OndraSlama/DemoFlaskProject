from flask_restful import Resource
from common.authentication import auth
from flask import jsonify
import requests
import os

class AnnotationResource(Resource):
    rossum_url = "https://api.elis.rossum.ai/v1/queues/{annotation_id}/export" 
    rossum_user = os.environ.get('ROSSUM_USER')
    rossum_pass = os.environ.get('ROSSUM_PASS')

    @auth.login_required
    def get(self, annotation_id:int) -> str:
        
        # Get the annotation from the rosum API
        credentials: tuple = (self.rossum_user, self.rossum_pass)
        params: dict = {"format": "xml", "status": "exported"}
        url: str = self.rossum_url.format(annotation_id=annotation_id)

        response = requests.get(url, auth=credentials, params=params)


        # Return response
        return jsonify({
            "success": True,
            "content": {"id": annotation_id, "response": response.text}            
            })

