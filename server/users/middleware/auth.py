import jwt
from rest_framework import authentication
from rest_framework import exceptions
from users.models import users as users_dao
from users.services import users as users_service
from users.services import auth as auth_service

class ApiUserAuth(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            raise exceptions.AuthenticationFailed('No auth header')

        jwt_token = auth_header.split(' ')[-1] # Bearer xxxx
        if not auth_header:
            raise exceptions.AuthenticationFailed('Incorrect auth header')

        try:
            user_email = auth_service.decode_jwt_token(jwt_token)['email']
        except jwt.exceptions.InvalidSignatureError:
            raise exceptions.AuthenticationFailed('Incorrect auth header')

        user = users_dao.get_by_email(user_email)
        if user is None:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)

class ApiOrgAdminAuth(authentication.BaseAuthentication):
    api_auth = ApiUserAuth()
    def authenticate(self, request):
        user, _ = self.api_auth.authenticate(request)

        org_id = request.path.split('/')[-1]
        if not users_service.is_admin(user.email, org_id):
            raise exceptions.AuthenticationFailed('User not authoized')

        return (user, org_id)

class ApiOrgMemberAuth(authentication.BaseAuthentication):
    api_auth = ApiUserAuth()
    def authenticate(self, request):
        user, _ = self.api_auth.authenticate(request)

        org_id = request.path.split('/')[-2]
        if not users_service.is_in_org(user.email, org_id):
            raise exceptions.AuthenticationFailed('User not authoized')

        return (user, org_id)
