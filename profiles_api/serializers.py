from rest_framework import serializers
from profiles_api.models import UserProfile,Book,Author

class UserProfileSerializer(serializers.ModelSerializer):
    #confirm_password = serializers.CharField(max_length=20,style={'input_type':'password'})
    class Meta():
        model = UserProfile
        fields = ['first_name','last_name','email','id', 'password']
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style': {
                    'input_type':'password'
                }
            },
            'id': {
                'read_only':True
            }
        }

    def create(self, validated_data):
        """Create and return a new User"""
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            password = validated_data['password']
        )
        return user

class BookSerializer(serializers.ModelSerializer):

    class Meta():
        model = Book
        exclude =('id',)

class AuthorSerializer(serializers.ModelSerializer):

    class Meta():
        model = Author
        exclude =('id', )
