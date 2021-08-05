import flask
import os

app = flask.Flask(__name__)

@app.route('/')
def index():
    return f'Hello, World!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)