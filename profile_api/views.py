from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profile_api import serializers
from profile_api import models
from profile_api import permissions

class HelloApiView(APIView):
    """Test api view"""
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to traditional django view', 
            'Gives yoiu the most control over your application',
            'Is mapped manually to URLS',
        ]

        return Response({'message':'Hello django api', 'api_view':an_apiview})


    """Get data from url using post method"""
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            #use f to concate variable eith string
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )    


    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})               


class HelloViewSet(viewsets.ViewSet):
    """Test api viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'Uses action (list, create, retrive, update, partial_update',
            'Automatically ,maps to urls using routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello', 'a_viewset':a_viewset})

    def create(self, request):
        """create a new hello message, data is default"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )    

    def retrieve(self, request, pk=None):
        """Handle getting an object by its id"""
        return Response({'http_method': 'GET'})   

    def update(self, request, pk=None):
        """handle updating am object"""
        return Response({'http_mrthod': 'PUT'})        

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'httmp_method': 'PATCH'})    

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method':'DELETE'})     

"""using ModelViewSet""" 
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    """Using queryset automatically configur out the baseame in the router"""
    queryset = models.UserProfile.objects.all()
    """using rest freamwork authentication and search filters"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handle creating, rteading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        """Set persmission the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)