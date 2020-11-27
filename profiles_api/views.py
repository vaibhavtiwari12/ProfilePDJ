from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class= serializers.HelloSerializer

    def get(self, request, format= None):
        """returns a list of API View"""
        an_apiView = [
            'useus HTTp models',
            'is similar to traditional django view',
            'Gives you the most control over the application logic'
        ]
        return Response({'message':'hello','an_apiview': an_apiView})

    def post (self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name');
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put (self, request, pk=None):
        """Handle Updating an object"""
        return Response({'method': "put"});

    def patch (self, request, pk=None):
        """Handle partial update of the object"""
        return Response({'method': "patch"});

    def delete(self, request, pk=None):
        """handle the deletion requests"""
        return Response({'method': "delete"});

