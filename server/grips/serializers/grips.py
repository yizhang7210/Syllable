from rest_framework import serializers
from grips.models.grips import Grip

class GripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grip
        fields = '__all__'
