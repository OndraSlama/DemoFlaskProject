from flask_httpauth import HTTPBasicAuth
import os

from werkzeug.utils import validate_arguments

USER_DATA = {
    os.environ.get("USER_NAME"): os.environ.get("USER_PASS")
}

auth = HTTPBasicAuth()
@auth.verify_password
def verify(username, password):
    print("validating")
    if not (username and password):
        return False

    print(USER_DATA)
    print(username, password)

    return USER_DATA.get(username) == password
