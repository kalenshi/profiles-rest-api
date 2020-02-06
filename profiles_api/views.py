from django.shortcuts import render,get_object_or_404
from rest_framework.response  import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from profiles_api import permissions
from rest_framework.views import APIView
from rest_framework import status,viewsets,filters
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
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
                permissions.UpdateOwnBook,
                IsAuthenticated
    )
    queryset = Book.objects.all()

    def list(self, request):

        serializer = self.serializer_class(self.queryset,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
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
        book = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(book)
        return Response(serializer.data, status=status.HTTP_200_OK)



    # def perform_create(self,serializer):
    #     """Sets the owner to the current logged in user"""
    #     serializer.save(owner=self.request.user)


class UserProfilesViewset(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    # Authentication and Permissions
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email','first_name','last_name',)

class UserLoginView(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
