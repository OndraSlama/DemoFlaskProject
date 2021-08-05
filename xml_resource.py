from flask_restful import Resource
from authentication import auth

class XmlResource(Resource):
    @auth.login_required
    def get(self) -> str:
        print("returning response")
        return "Secret stuff!"

