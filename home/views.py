from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Home
from .serializers import HomeSerializerGet, HomeSerializerPost


@extend_schema(tags=['Home'])
class HomeGetAPIView(APIView):
    serializer_class = HomeSerializerGet

    def get(self, request):
        try:
            home = Home.objects.all()
        except Home.DoesNotExist:
            return Response({"error": "Homelar topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = HomeSerializerGet(home, many=True, context={'request': request})
        return Response(serializer.data)


@extend_schema(tags=['Home'])
class HomePostAPIView(APIView):
    serializer_class = HomeSerializerPost

    def post(self, request):
        serializer = HomeSerializerPost(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['Basement'])
class BasementGetAPIView(APIView):
    serializer_class = HomeSerializerGet

    def get(self, request):
        try:
            home = Home.objects.all()
        except Home.DoesNotExist:
            return Response({"error": "Homelar topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = HomeSerializerGet(home, many=True, context={'request': request})
        return Response(serializer.data)


@extend_schema(tags=['Home'])
class HomePostAPIView(APIView):
    serializer_class = HomeSerializerPost

    def post(self, request):
        serializer = HomeSerializerPost(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
