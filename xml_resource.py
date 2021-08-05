from flask_restful import Resource
from authentication import auth
from flask import jsonify

class XmlResource(Resource):
    @auth.login_required
    def get(self, annotation_id) -> str:
        return jsonify({
            "success": True,
            "content": f"Secret stuff! ID: {annotation_id}"            
            })

