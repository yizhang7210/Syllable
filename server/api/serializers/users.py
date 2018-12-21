from rest_framework import serializers
from api.models.users import User

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)
    token = serializers.CharField()
