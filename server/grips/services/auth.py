from rest_framework import authentication
from rest_framework import exceptions
from users.services.auth import ApiAuthentication
from users.services import users as user_service
from grips.services import grips as grips_service

class ApiGripAuthentication(authentication.BaseAuthentication):

    api_auth = ApiAuthentication()
    def authenticate(self, request):
        user, _ = self.api_auth.authenticate(request)

        grip_id = request.path.split('/')[-1]
        grip = grips_service.get_by_id(grip_id)

        if grip is None:
            raise exceptions.AuthenticationFailed('Grip does not exist')

        if grips_service.is_editable(user.email, grip):
            return (user, grip)

        raise exceptions.AuthenticationFailed('User not authorized')
