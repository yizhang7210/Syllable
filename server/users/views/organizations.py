from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers.organizations import OrganizationSerializer
from users.services.auth import ApiUserAuth, ApiOrgAuthentication
from users.services import organizations as orgs_service
from users.services import users as users_service

class OrganizationListView(APIView):

    serializer_class = OrganizationSerializer
    authentication_classes = (ApiUserAuth,)

    def post(self, request, *args, **kwargs):
        user_email = request.user.email
        if users_service.get_current_org(user_email) is not None:
            return Response(
                {'detail': 'One user can only belong to one organization.'},
                status=status.HTTP_400_BAD_REQUEST)

        new_org = orgs_service.create(request.data['name'], user_email)
        if new_org is None:
            return Response(
                {'detail': 'Organization with this name already exists.'},
                status=status.HTTP_400_BAD_REQUEST)

        users_service.make_admin(user_email, new_org)
        return Response(OrganizationSerializer(new_org).data)

class OrganizationDetailView(APIView):

    serializer_class = OrganizationSerializer
    authentication_classes = (ApiOrgAuthentication,)

    def patch(self, request, *args, **kwargs):
        user_org = request.auth
        org = orgs_service.update(user_org.organization.id, request.data)
        return Response(OrganizationSerializer(org).data)
