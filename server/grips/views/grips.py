from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from grips.serializers.grips import GripSerializer
from grips.services import grips as grips_service

class GripsView(ListCreateAPIView):

    def list(self, request, *args, **kwargs):
        grips = grips_service.get_all_by_user(request.user.email)
        serializer = GripSerializer(grips, many=True)
        return Response(serializer.data)
