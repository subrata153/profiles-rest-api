from rest_framework import serializers
from profile_api import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serailizer a user profile object"""
    """serialize using model serializer"""
    class Meta:
        model = models.UserProfile
        """Define all the fields those will be serialize"""
        fields = ('id', 'email', 'name', 'password')
        """For password security"""
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create a new user"""
        """create user through api, using the create_user function from UserProfile class"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user