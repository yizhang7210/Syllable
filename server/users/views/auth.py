from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from users.serializers.auth import GoogleSignInSerializer
from users.services import auth as auth_service
from users.services import users as users_service

class GoogleSignInView(APIView):

    serializer_class = GoogleSignInSerializer

    def post(self, request, *args, **kwargs):
        google_token = request.data['token']
        user_email = request.data['email']

        jwt_token = auth_service.sign_in_with_google(
            request.data['family_name'],
            request.data['given_name'],
            user_email,
            google_token
        )
        if jwt_token is None:
            return Response(
                {"detail": "failed"},
                status=status.HTTP_401_UNAUTHORIZED)

        gsuite_domain = auth_service.get_gsuite_domain(google_token)
        users_service.update_org_info(user_email, gsuite_domain)

        return Response({"token": jwt_token})
