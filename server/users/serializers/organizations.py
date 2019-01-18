from rest_framework import serializers
from users.models.organizations import Organization

class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ('name', 'domain')
