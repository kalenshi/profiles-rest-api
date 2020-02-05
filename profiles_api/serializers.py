from rest_framework import serializers
from profiles_api.models import UserProfile,Book,Author

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta():
        model = UserProfile
        fields = ['first_name','last_name','email','id']

class BookSerializer(serializers.ModelSerializer):

    class Meta():
        model = Book
        exclude =('id',)

class AuthorSerializer(serializers.ModelSerializer):

    class Meta():
        model = Author
        exclude =('id',)
