from flask import Flask
from flask_restful import Api
from xml_resource import XmlResource

app = Flask(__name__)
api = Api(app)

# add resource
api.add_resource(XmlResource, '/<int:annotation_id>')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)