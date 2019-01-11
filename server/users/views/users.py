from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from users.serializers.users import UserSerializer
from users.services.auth import ApiAuthentication
from users.services import users as users_service

class UserDetailView(RetrieveAPIView):

    serializer_class = UserSerializer
    authentication_classes = (ApiAuthentication,)

    def get(self, request, *args, **kwargs):
        current_user = users_service.get_by_email(request.user.email)
        serializer = UserSerializer([current_user], many=True)
        return Response(serializer.data)
