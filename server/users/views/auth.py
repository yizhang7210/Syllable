from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from users.serializers.auth import GoogleSignInSerializer
from users.services import auth as auth_service

class GoogleSignInView(CreateAPIView):

    serializer_class = GoogleSignInSerializer

    def post(self, request, *args, **kwargs):
        jwt_token = auth_service.sign_in_with_google(
            request.data['family_name'],
            request.data['given_name'],
            request.data['email'],
            request.data['token']
        )
        if jwt_token is not None:
            return Response({"token": jwt_token})

        return Response({"detail": "failed"}, status=status.HTTP_401_UNAUTHORIZED)
