from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers.users import UserSerializer
from users.services.auth import ApiUserAuth
from users.services import users as users_service

class UserDetailView(APIView):
    authentication_classes = (ApiUserAuth,)

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(users_service.get_by_email(request.user.email))
        return Response(serializer.data)

class UserListView(APIView):
    authentication_classes = (ApiUserAuth,)

    def get(self, request, *args, **kwargs):
        users_in_org = users_service.get_all_in_org(request.user.email)
        serializer = UserSerializer(users_in_org, many=True)
        return Response(serializer.data)
