from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from grips.serializers.grips import GripSerializer
from grips.services import grips as grips_service
from grips.middleware.auth import ApiGripWriteAuth, ApiGripReadAuth
from users.middleware.auth import ApiUserAuth

GRIP_SIZE_LIMIT = 365

class GripListView(APIView):
    authentication_classes = (ApiUserAuth,)

    def get(self, request, *args, **kwargs):
        pinned = bool(request.GET.get('pinned', False))
        user_email = request.user.email
        grips = grips_service.get_all_visible_by_user(user_email)
        serializer = GripSerializer(grips, many=True, context={'user': user_email})

        response = serializer.data
        if pinned:
            response = [grip for grip in response if grip['is_pinned']]

        return Response(response)

    def post(self, request, *args, **kwargs):
        user_email = request.user.email
        if len(request.data['content']) > GRIP_SIZE_LIMIT:
            msg = "Grip must be at most {0} charaters.".format(GRIP_SIZE_LIMIT)
            return Response(
                {'detail': msg},
                status=status.HTTP_400_BAD_REQUEST)

        new_grip = grips_service.create(
            request.data['title'],
            request.data['content'],
            request.data['source'],
            user_email,
            request.data['is_shared'])
        return Response(GripSerializer(new_grip, context={'user': user_email}).data)


class GripDetailView(APIView):
    authentication_classes = (ApiGripWriteAuth,)

    def delete(self, request, *args, **kwargs):
        grip = request.auth
        grips_service.delete(grip)

        return Response({'detail': 'success'})

    def patch(self, request, *args, **kwargs):
        user_email = request.user.email
        grip = request.auth

        if 'share' in request.data:
            grip = grips_service.set_sharing(grip, user_email, request.data['share'])

        serializer = GripSerializer(grip, context={'user': user_email})

        return Response(serializer.data)


class GripActionView(APIView):
    authentication_classes = (ApiGripReadAuth,)

    def post(self, request, *args, **kwargs):
        user_email = request.user.email
        grip = request.auth

        if 'vote' in request.data:
            grips_service.set_voting(grip, user_email, request.data['vote'])

        if 'pin' in request.data:
            grips_service.set_pin(grip, user_email, request.data['pin'])

        serializer = GripSerializer(grip, context={'user': user_email})

        return Response(serializer.data)


class GripSearchView(APIView):
    authentication_classes = (ApiUserAuth,)

    def get(self, request, *args, **kwargs):
        serach_term = request.GET.get('q', '')
        user_email = request.user.email
        grips = grips_service.get_by_search(user_email, serach_term)
        serializer = GripSerializer(grips, many=True, context={'user': user_email})
        return Response(serializer.data)
