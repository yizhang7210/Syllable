import jwt
from google.oauth2 import id_token
from google.auth.transport import requests

from api.models import users

CLIENT_ID = "524164616554-qmh6kkofkqi3lg9873npjv0hgar04gft.apps.googleusercontent.com"
SECRET = 'syllable_secret'

def sign_in_with_google(family_name, given_name, email, token):
    user_id = verify_user(token)
    if user_id is None:
        return None

    persist_user(email, family_name, given_name)
    return generate_token(email)

def verify_user(token):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        userid = idinfo['sub']
        return userid
    except ValueError:
        # Invalid token
        return None

def persist_user(email, family_name, given_name):
    users.upsert(users.create_one(
        email=email, family_name=family_name, given_name=given_name
    ))

def generate_token(email):
    return jwt.encode({'email': email}, SECRET, algorithm='HS256')
