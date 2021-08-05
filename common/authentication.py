from flask_httpauth import HTTPBasicAuth
import os

USER_DATA = {
    os.environ.get("USER_NAME"): os.environ.get("USER_PASS")
}

auth = HTTPBasicAuth()
@auth.verify_password
def verify(username, password):

    if not (username and password):
        return False
        
    return USER_DATA.get(username) == password
