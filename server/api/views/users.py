from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from api.serializers.users import LoginSerializer
from api.services import users as user_service
from rest_framework import status

class UserAuthView(CreateAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        user_id = user_service.process_sign_in(
            request.data['name'],
            request.data['email'],
            request.data['token']
        )
        if user_id:
            return Response("success")
        else:
            return Response("failed", status=status.HTTP_401_UNAUTHORIZED)
