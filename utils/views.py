from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HomePage
from .serializers import HomePageSerializer


@extend_schema(tags=['HomePage'])
class HomePageAPIView(APIView):
    serializer_class = HomePageSerializer

    def get(self, request):
        try:
            homepage = HomePage.objects.all()
        except HomePage.DoesNotExist:
            return Response({"error": "HomePage topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = HomePageSerializer(homepage, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = HomePageSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
