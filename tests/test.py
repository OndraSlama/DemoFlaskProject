""" File for basic testing of flask API """
import requests

flask_endpoint = 'http://127.0.0.1:5000/export/123456'

# Put it here just for test sake
test_user = 'myUser123'
test_password = 'secretSecret'

def main():
    response = requests.get(flask_endpoint, auth=(test_user, test_password))
    assert response.status_code == 200, 'Request did not finished sucessfully'


if __name__ == '__main__':
    main()
