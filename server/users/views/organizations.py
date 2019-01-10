from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from users.serializers.organizations import OrganizationSerializer
from users.services.auth import ApiAuthentication
from users.services import organizations as orgs_service

class OrganizationView(CreateAPIView):

    serializer_class = OrganizationSerializer
    authentication_classes = (ApiAuthentication,)

    def post(self, request, *args, **kwargs):
        result = orgs_service.create(request.data['name'], request.user.email)
        if result is None:
            return Response(
                {'detail': 'Organization with this name already exists.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            return Response(OrganizationSerializer(result).data)
