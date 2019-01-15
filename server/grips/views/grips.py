from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from grips.serializers.grips import GripSerializer
from grips.services import grips as grips_service
from users.services.auth import ApiAuthentication
from grips.services.auth import ApiGripAuthentication

GRIP_SIZE_LIMIT = 365

class GripListView(generics.ListCreateAPIView):

    authentication_classes = (ApiAuthentication,)

    def list(self, request, *args, **kwargs):
        user_email = request.user.email
        grips = grips_service.get_all_visible_by_user(user_email)
        serializer = GripSerializer(grips, many=True, context={'user': user_email})
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user_email = request.user.email
        if len(request.data['content']) > GRIP_SIZE_LIMIT:
            msg = "Grip must be at most {0} charaters.".format(GRIP_SIZE_LIMIT)
            return Response(
                {'detail': msg},
                status=status.HTTP_400_BAD_REQUEST)

        new_grip = grips_service.create(
            request.data['title'],
            request.data['content'],
            user_email,
            request.data['is_shared'])
        return Response(GripSerializer(new_grip, context={'user': user_email}).data)


class GripDetailView(generics.DestroyAPIView):

    authentication_classes = (ApiGripAuthentication,)

    def delete(self, request, *args, **kwargs):
        grip = request.auth
        grips_service.delete(grip)

        return Response({'detail': 'success'})


class GripSearchView(generics.ListAPIView):

    authentication_classes = (ApiAuthentication,)

    def list(self, request, *args, **kwargs):
        serach_term = request.GET.get('q', '')
        user_email = request.user.email
        grips = grips_service.get_by_search(user_email, serach_term)
        serializer = GripSerializer(grips, many=True, context={'user': user_email})
        return Response(serializer.data)
