from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

class HelloAPIView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Retrun some dump list to donistarte APIView feature."""
        qoutes = [
            "I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best.",
            "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.",
            "Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind.",
            "You know you're in love when you can't fall asleep because reality is finally better than your dreams.",
        ]
        return Response({"Message": "Common Qoutes", "qoutes": qoutes})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )