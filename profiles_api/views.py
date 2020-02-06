from django.shortcuts import render,get_object_or_404
from rest_framework.response  import Response
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework.views import APIView
from rest_framework import status,viewsets
from profiles_api.models import UserProfile,Book, Author
from profiles_api.serializers import UserProfileSerializer,BookSerializer

# Create your views here.

class ProfilesView(APIView):
    serializer_class = UserProfileSerializer

    def get_object(self, pk):
        try:
            if not pk:
                return UserProfile.objects.all()
            else:
                return UserProfile.objects.get(id=pk)
        except:
            print('something went wrong')
            raise Http404

    def get(self, request, pk=None,format=None):
        """Retrieve all the profiles in our App"""
        queryset = self.get_object(pk)
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

class BookViewset(viewsets.ModelViewSet):

    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def list(self, request):

        serializer = self.serializer_class(self.queryset,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

    def retrieve(self,request,pk=None):
        if not pk:
            return Response({'Error': 'Invalid Request'},status=status.HTTP_204_NO_CONTENT)
        else:
            queryset = get_object_or_404(Book, pk=pk)
            print(queryset)
            serializer = self.serializer_class(data=queryset)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            print(serializer.data)
            return Response({})

class UserProfilesViewset(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    # Authentication and Permissions
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
