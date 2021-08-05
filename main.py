import flask
import os
from flask_basicauth import BasicAuth

app = flask.Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = os.environ.get("USER_NAME")
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get("USER_PASS")
basic_auth = BasicAuth(app)

@app.route('/')
def index():
    return f'Hello, World! User {os.environ.get("USER_NAME")}'

@app.route('/secret')
@basic_auth.required
def secret_index():
    return f'Secret stuff! User {os.environ.get("USER_NAME")}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)