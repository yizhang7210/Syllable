import jwt
from google.oauth2 import id_token
from google.auth.transport import requests
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import authentication
from rest_framework import exceptions
from users.models import users

CLIENT_ID = "524164616554-qmh6kkofkqi3lg9873npjv0hgar04gft.apps.googleusercontent.com"
SECRET = 'syllable_secret'

class ApiAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            raise exceptions.AuthenticationFailed('No auth header')

        jwt_token = auth_header.split(' ')[-1] # Bearer xxxx
        if not auth_header:
            raise exceptions.AuthenticationFailed('Incorrect auth header')

        try:
            user_email = decode_jwt_token(jwt_token)['email']
        except jwt.exceptions.InvalidSignatureError:
            raise exceptions.AuthenticationFailed('Incorrect auth header')

        try:
            user = users.get_by_email(user_email)
        except ObjectDoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)

def sign_in_with_google(family_name, given_name, email, google_token):
    user_id = verify_google_user(google_token)
    if user_id is None:
        return None

    persist_user(email, family_name, given_name)
    return generate_jwt_token(email)

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
    users.upsert(users.create_one(
        email=email, family_name=family_name, given_name=given_name
    ))

def generate_jwt_token(email):
    return jwt.encode({'email': email}, SECRET, algorithm='HS256')

def decode_jwt_token(jwt_token):
    return jwt.decode(jwt_token, SECRET, algorithms=['HS256'])
