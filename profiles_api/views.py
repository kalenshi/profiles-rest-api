from django.shortcuts import render
from rest_framework.response  import Response
from rest_framework.views import APIView
from rest_framework import status
from profiles_api.models import UserProfile
from profiles_api.serializers import UserProfileSerializer

# Create your views here.

class ProfilesView(APIView):
    serializer_class = UserProfileSerializer
    def get(self, request, format=None):
        """Retrieve all the profiles in our App"""
        queryset = UserProfile.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        """Handle the creation of userProfiles"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,format=None):
        pass
    def patch(self, request, format=None):
        pass
    def delete(self,request, pk=None):
        pass 
