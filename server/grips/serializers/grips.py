from rest_framework import serializers
from grips.models.grips import Grip
from grips.services import grips as grips_service

class GripSerializer(serializers.ModelSerializer):

    is_shared = serializers.SerializerMethodField('get_shared')
    is_pinned = serializers.SerializerMethodField('get_pinned')
    is_editable = serializers.SerializerMethodField('get_editable')
    has_voted = serializers.SerializerMethodField('get_voted')
    votes = serializers.SerializerMethodField()

    # pylint: disable=no-self-use
    def get_shared(self, grip):
        return grips_service.is_shared(grip)

    def get_pinned(self, grip):
        return grips_service.is_pinned_by(grip, self.context['user'])

    def get_editable(self, grip):
        return grips_service.is_editable_by(grip, self.context['user'])

    def get_voted(self, grip):
        return grips_service.has_voted_by(grip, self.context['user'])

    def get_votes(self, grip):
        return grips_service.get_votes(grip)

    class Meta:
        model = Grip
        fields = ('id', 'title', 'content', 'created_by', 'source', \
            'is_shared', 'is_editable', 'has_voted', 'votes', 'is_pinned')
