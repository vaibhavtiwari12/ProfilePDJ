from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format= None):
        """returns a list of API View"""
        an_apiView = [
            'useus HTTp models',
            'is similar to traditional django view',
            'Gives you the most control over the application logic'
        ]
        return Response({'message':'hello','an_apiview':an_apiView})


