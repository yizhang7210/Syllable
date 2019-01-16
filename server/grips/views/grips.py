from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from grips.serializers.grips import GripSerializer
from grips.services import grips as grips_service
from users.services.auth import ApiAuthentication
from users.services import users as user_service
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


class GripDetailView(generics.UpdateAPIView, mixins.DestroyModelMixin):

    authentication_classes = (ApiGripAuthentication,)

    def delete(self, request, *args, **kwargs):
        grip = request.auth
        grips_service.delete(grip)

        return Response({'detail': 'success'})

    def patch(self, request, *args, **kwargs):
        grip = request.auth
        user_email = request.user.email
        to_share = request.data['is_shared']

        if to_share == grips_service.is_shared(grip):
            serializer = GripSerializer(grip, context={'user': user_email})
            return Response(serializer.data)

        if to_share:
            current_user_org = user_service.get_current_org(user_email)
            new_grip = grips_service.share(grip, current_user_org.id)
        else:
            new_grip = grips_service.unshare(grip)

        serializer = GripSerializer(new_grip, context={'user': user_email})

        return Response(serializer.data)


class GripSearchView(generics.ListAPIView):

    authentication_classes = (ApiAuthentication,)

    def list(self, request, *args, **kwargs):
        serach_term = request.GET.get('q', '')
        user_email = request.user.email
        grips = grips_service.get_by_search(user_email, serach_term)
        serializer = GripSerializer(grips, many=True, context={'user': user_email})
        return Response(serializer.data)
