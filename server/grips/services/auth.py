from rest_framework import authentication
from rest_framework import exceptions
from users.services.auth import ApiUserAuth
from users.services import users as user_service
from grips.services import grips as grips_service

class ApiGripWriteAuth(authentication.BaseAuthentication):

    api_auth = ApiUserAuth()
    def authenticate(self, request):
        user, _ = self.api_auth.authenticate(request)

        grip_id = request.path.split('/')[-1]
        grip = grips_service.get_by_id(grip_id)

        if grip is None:
            raise exceptions.AuthenticationFailed('Grip does not exist')

        if grips_service.is_editable(grip, user.email):
            return (user, grip)

        raise exceptions.AuthenticationFailed('User not authorized')

class ApiGripReadAuth(authentication.BaseAuthentication):

    api_auth = ApiUserAuth()
    def authenticate(self, request):
        user, _ = self.api_auth.authenticate(request)

        grip_id = request.path.split('/')[-2]
        grip = grips_service.get_by_id(grip_id)

        if grip is None:
            raise exceptions.AuthenticationFailed('Grip does not exist')

        if grips_service.is_readable(grip, user.email):
            return (user, grip)

        raise exceptions.AuthenticationFailed('User not authorized')
