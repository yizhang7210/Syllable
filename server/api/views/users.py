from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from api.serializers.users import LoginSerializer
from api.services import users as user_service

class UserAuthView(CreateAPIView):

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        is_successful = user_service.process_sign_in(
            request.data['family_name'],
            request.data['given_name'],
            request.data['email'],
            request.data['token']
        )
        if is_successful:
            return Response("success")

        return Response("failed", status=status.HTTP_401_UNAUTHORIZED)
