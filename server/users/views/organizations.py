from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from users.serializers.organizations import OrganizationSerializer
from users.services.auth import ApiAuthentication
from users.services import organizations as orgs_service
from users.services import users as users_service

class OrganizationView(CreateAPIView):

    serializer_class = OrganizationSerializer
    authentication_classes = (ApiAuthentication,)

    def post(self, request, *args, **kwargs):
        user_email = request.user.email
        new_org = orgs_service.create(request.data['name'], user_email)
        if new_org is None:
            return Response(
                {'detail': 'Organization with this name already exists.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            users_service.make_admin(user_email, new_org)
            return Response(OrganizationSerializer(new_org).data)
