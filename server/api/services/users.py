from google.oauth2 import id_token
from google.auth.transport import requests

CLIENT_ID = "524164616554-qmh6kkofkqi3lg9873npjv0hgar04gft.apps.googleusercontent.com"

def process_sign_in(name, email, token):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        userid = idinfo['sub']
        return userid
    except ValueError:
        # Invalid token
        return None
