from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from users.serializers.organizations import OrganizationSerializer
from users.services.auth import ApiAuthentication
from users.models import organizations as orgs_dao

class OrganizationView(CreateAPIView):

    serializer_class = OrganizationSerializer
    authentication_classes = (ApiAuthentication,)

    def post(self, request, *args, **kwargs):
        orgs_dao.save(orgs_dao.create_one(
            name=request.data['name'],
            created_by=request.user.email
        ))
        creator = request.data
        return Response({'detail': 'success'})
