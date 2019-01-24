import jwt
from django.utils import timezone
from google.oauth2 import id_token
from google.auth.transport import requests
from users.models import users as users_dao
from users.signals import users as user_signals

CLIENT_ID = "524164616554-qmh6kkofkqi3lg9873npjv0hgar04gft.apps.googleusercontent.com"
SECRET = 'syllable_secret'

def sign_in_with_google(family_name, given_name, email, google_token):
    user_id = verify_google_user(google_token)
    if user_id is None:
        return None

    existing_user = users_dao.get_by_email(email)
    is_first_time = existing_user is None or existing_user.last_active_at is None

    user = users_dao.upsert(email, family_name=family_name,
        given_name=given_name, last_active_at=timezone.now())

    if is_first_time:
        user_signals.USER_SIGNED_UP.send_robust(sender=__name__, user=user)

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

def generate_jwt_token(email):
    return jwt.encode({'email': email}, SECRET, algorithm='HS256')

def decode_jwt_token(jwt_token):
    return jwt.decode(jwt_token, SECRET, algorithms=['HS256'])
