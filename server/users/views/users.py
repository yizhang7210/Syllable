from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers.users import UserSerializer
from users.services.auth import ApiUserAuth
from users.services import users as users_service

class UserDetailView(APIView):

    serializer_class = UserSerializer
    authentication_classes = (ApiUserAuth,)

    def get(self, request, *args, **kwargs):
        current_user = users_service.get_by_email(request.user.email)
        serializer = UserSerializer([current_user], many=True)
        return Response(serializer.data)
