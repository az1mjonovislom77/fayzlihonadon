from django.shortcuts import get_object_or_404
from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Home, Basement, CommonHouse, CommonHouseAbout, InProgress
from .serializers import HomeSerializerGet, HomeSerializerPost, BasementSerializer, CommonHouseSerializer, \
    CommonHouseAboutSerializer, InProgressSerializer


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
class BasementAPIView(APIView):
    serializer_class = BasementSerializer

    def get(self, request):
        try:
            basement = Basement.objects.all()
        except Basement.DoesNotExist:
            return Response({"error": "Basement topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BasementSerializer(basement, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = BasementSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['CommonHouse'])
class CommonHouseAPIView(APIView):
    serializer_class = CommonHouseSerializer

    def get(self, request):
        try:
            commonhouse = CommonHouse.objects.all()
        except CommonHouse.DoesNotExist:
            return Response({"error": "CommonHouse topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommonHouseSerializer(commonhouse, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = CommonHouseSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['CommonHouseAbout'])
class CommonHouseAboutAPIView(APIView):
    serializer_class = CommonHouseAboutSerializer

    def get(self, request):
        try:
            commonhouseabout = CommonHouseAbout.objects.all()
        except CommonHouseAbout.DoesNotExist:
            return Response({"error": "CommonHouseAbout topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommonHouseAboutSerializer(commonhouseabout, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = CommonHouseAboutSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['InProgress'])
class InProgressAPIView(APIView):
    serializer_class = InProgressSerializer

    def get(self, request):
        try:
            inprogress = InProgress.objects.all()
        except InProgress.DoesNotExist:
            return Response({"error": "InProgress topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = InProgressSerializer(inprogress, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = InProgressSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['HomeDetail'])
class HomeDetailGetAPIView(APIView):
    serializer_class = HomeSerializerGet

    def get(self, request, pk):
        home = get_object_or_404(Home, pk=pk)
        serializer = HomeSerializerGet(home, context={'request': request})
        return Response(serializer.data)


@extend_schema(tags=['CommonHouseDetail'])
class CommonHouseDetailGetAPIView(APIView):
    serializer_class = CommonHouseSerializer

    def get(self, request, pk):
        commonhouse = get_object_or_404(CommonHouse, pk=pk)
        serializer = CommonHouseSerializer(commonhouse, context={'request': request})
        return Response(serializer.data)


@extend_schema(tags=['CommonHouseAboutDetail'])
class CommonHouseAboutDetailGetAPIView(APIView):
    serializer_class = CommonHouseAboutSerializer

    def get(self, request, pk):
        commonhouseabout = get_object_or_404(CommonHouseAbout, pk=pk)
        serializer = CommonHouseAboutSerializer(commonhouseabout, context={'request': request})
        return Response(serializer.data)
