from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test api view"""

    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to traditional django view', 
            'Gives yoiu the most control over your application',
            'Is mapped manually to URLS',
        ]

        return Response({'message':'Hello django api', 'api_view':an_apiview})