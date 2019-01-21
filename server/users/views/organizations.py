from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers.organizations import OrganizationSerializer
from users.middleware.auth import ApiUserAuth, ApiOrgAdminAuth, ApiOrgMemberAuth
from users.services import organizations as orgs_service
from users.services import users as users_service

class OrganizationListView(APIView):
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
    authentication_classes = (ApiOrgAdminAuth,)

    def patch(self, request, *args, **kwargs):
        org_id = request.auth
        org = orgs_service.update(org_id, request.data)
        return Response(OrganizationSerializer(org).data)

class OrganizationInviteView(APIView):
    authentication_classes = (ApiOrgMemberAuth,)

    def post(self, request, *args, **kwargs):
        org_id = request.auth
        orgs_service.invite(request.user, org_id, request.data['emails'])
        return Response(status=status.HTTP_201_CREATED)
