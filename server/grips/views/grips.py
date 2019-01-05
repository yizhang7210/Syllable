from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from grips.serializers.grips import GripSerializer
from grips.services import grips as grips_service
from grips.models import grips as grips_dao
from users.services.auth import ApiAuthentication

class GripListView(generics.ListCreateAPIView):

    serializer_class = GripSerializer
    authentication_classes = (ApiAuthentication,)

    def list(self, request, *args, **kwargs):
        grips = grips_service.get_all_by_user(request.user.email)
        serializer = GripSerializer(grips, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = GripSerializer(data=request.data)
        creator = request.user.email
        if serializer.is_valid():
            new_grip = grips_dao.save(grips_dao.create_one(
                title=serializer.validated_data['title'],
                content=serializer.validated_data['content'],
                created_by=creator
            ))
            return Response("success")
        return Response("failed", status=status.HTTP_400_BAD_REQUEST)


class GripDetailView(generics.DestroyAPIView):

    serializer_class = GripSerializer
    authentication_classes = (ApiAuthentication,)

    def delete(self, request, *args, **kwargs):
        grip = grips_service.get_by_id(kwargs['id'])

        if grip is None:
            return Response("failed", status=status.HTTP_400_BAD_REQUEST)

        if (grip.created_by != request.user.email):
            return Response("failed", status=status.HTTP_401_UNAUTHORIZED)

        grip.deleted = True
        grips_dao.save(grip)

        return Response("ok")

class GripSearchView(generics.ListAPIView):

    serializer_class = GripSerializer
    authentication_classes = (ApiAuthentication,)

    def list(self, request, *args, **kwargs):
        searchTerm = request.GET.get('q', '')
        grips = grips_service.get_by_search(request.user.email, searchTerm)
        serializer = GripSerializer(grips, many=True)
        return Response(serializer.data)
