""" File for basic testing of flask API """
import requests

flask_endpoint = 'http://127.0.0.1:5000/secret'

# Put it here just for tests
test_user = 'myUser123'
test_password = 'secretSecret__'

def main():
    response = requests.get(flask_endpoint, auth=(test_user, test_password))
    print(response.text)

if __name__ == '__main__':
    main()
