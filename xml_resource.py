from flask_restful import Resource
from authentication import auth
from flask import jsonify


class XmlResource(Resource):
    @auth.login_required
    def get(self) -> str:
        return jsonify({
            "success": True,
            "content": "Secret stuff!"            
            })

