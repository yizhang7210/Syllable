from rest_framework import serializers
from grips.models.grips import Grip
from grips.services import grips as grips_service

class GripSerializer(serializers.ModelSerializer):

    is_shared = serializers.SerializerMethodField('get_shared')
    is_editable = serializers.SerializerMethodField('get_editable')

    # pylint: disable=no-self-use
    def get_shared(self, grip):
        return grip.created_by != grip.owned_by

    def get_editable(self, grip):
        return grips_service.is_editable(self.context['user'], grip)

    class Meta:
        model = Grip
        fields = ('id', 'title', 'content', 'created_by', 'is_shared', 'is_editable')
