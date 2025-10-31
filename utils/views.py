from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HomePage, AdvertisementBanner, Reviews, WaitList, SocialMedia, Contacts
from .serializers import HomePageSerializer, AdvertisementBannerSerializer, ReviewsSerializer, WaitListSerializer, \
    SocialMediaSerializer, ContactsSerializer


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


@extend_schema(tags=['AdvertisementBanner'])
class AdvertisementBannerAPIView(APIView):
    serializer_class = AdvertisementBannerSerializer

    def get(self, request):
        try:
            homepage = AdvertisementBanner.objects.all()
        except AdvertisementBanner.DoesNotExist:
            return Response({"error": "AdvertisementBanner topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AdvertisementBannerSerializer(homepage, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = AdvertisementBannerSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['Reviews'])
class ReviewsAPIView(APIView):
    serializer_class = ReviewsSerializer

    def get(self, request):
        try:
            reviews = Reviews.objects.all()
        except Reviews.DoesNotExist:
            return Response({"error": "Reviews topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewsSerializer(reviews, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewsSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['WaitList'], request=WaitListSerializer, responses=WaitListSerializer)
class WaitListAPIView(APIView):
    serializer_class = WaitListSerializer

    def get(self, request):
        try:
            waitlist = WaitList.objects.all()
        except WaitList.DoesNotExist:
            return Response({"error": "WaitList topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(waitlist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['SocialMedia'], request=SocialMediaSerializer, responses=SocialMediaSerializer)
class SocialMediaAPIView(APIView):
    serializer_class = SocialMediaSerializer

    def get(self, request):
        try:
            socialmedia = SocialMedia.objects.all()
        except SocialMedia.DoesNotExist:
            return Response({"error": "SocialMedia topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(socialmedia, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['Contacts'], request=ContactsSerializer, responses=ContactsSerializer)
class ContactsAPIView(APIView):
    serializer_class = ContactsSerializer

    def get(self, request):
        try:
            contacts = Contacts.objects.all()
        except Contacts.DoesNotExist:
            return Response({"error": "Contacts topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(contacts, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
