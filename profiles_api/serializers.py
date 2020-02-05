from rest_framework import serializers
from profiles_api.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta():
        model = UserProfile
        fields = ['first_name','last_name','email','id']
