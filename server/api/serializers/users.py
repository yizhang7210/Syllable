from rest_framework import serializers

class GoogleSignInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    family_name = serializers.CharField(max_length=100)
    given_name = serializers.CharField(max_length=100)
    token = serializers.CharField()

    def create(self, validated_data):
        # Override abstract base class
        pass

    def update(self, instance, validated_data):
        # Override abstract base class
        pass
