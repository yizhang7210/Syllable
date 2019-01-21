import jwt
from django.utils import timezone
from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework import authentication
from rest_framework import exceptions
from users.models import users as users_dao
from users.services import users as users_service

CLIENT_ID = "524164616554-qmh6kkofkqi3lg9873npjv0hgar04gft.apps.googleusercontent.com"
SECRET = 'syllable_secret'

def sign_in_with_google(family_name, given_name, email, google_token):
    user_id = verify_google_user(google_token)
    if user_id is None:
        return None

    persist_user(email, family_name, given_name)
    return generate_jwt_token(email)

def get_gsuite_domain(google_token):
    try:
        idinfo = id_token.verify_oauth2_token(google_token, requests.Request(), CLIENT_ID)
        return idinfo['hd'] if 'hd' in idinfo else None

    except ValueError:
        # Invalid token
        return None

def verify_google_user(google_token):
    try:
        idinfo = id_token.verify_oauth2_token(google_token, requests.Request(), CLIENT_ID)

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        userid = idinfo['sub']
        return userid
    except ValueError:
        # Invalid token
        return None

def persist_user(email, family_name, given_name):
    print("yeah?")
    users_dao.upsert(users_dao.create_one(
        email=email, family_name=family_name, given_name=given_name,
        last_active_at=timezone.now()
    ))

def generate_jwt_token(email):
    return jwt.encode({'email': email}, SECRET, algorithm='HS256')

def decode_jwt_token(jwt_token):
    return jwt.decode(jwt_token, SECRET, algorithms=['HS256'])
