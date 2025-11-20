from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from home.serializers import HomeSerializerGet
from .models import HomePage, AdvertisementBanner, Reviews, WaitList, SocialMedia, Contacts, AboutCompany, Location
from .serializers import HomePageSerializer, AdvertisementBannerSerializer, ReviewsSerializer, WaitListSerializer, \
    SocialMediaSerializer, ContactsSerializer, AboutCompanySerializer, HomeFilterSerializer, LocationSerializer


@extend_schema(tags=['HomePage'])
class HomePageAPIView(ListCreateAPIView):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer


@extend_schema(tags=['AdvertisementBanner'])
class AdvertisementBannerAPIView(ListCreateAPIView):
    queryset = AdvertisementBanner.objects.all()
    serializer_class = AdvertisementBannerSerializer


@extend_schema(tags=['Reviews'])
class ReviewsAPIView(ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


@extend_schema(tags=['WaitList'])
class WaitListAPIView(ListCreateAPIView):
    queryset = WaitList.objects.all()
    serializer_class = WaitListSerializer


@extend_schema(tags=['WaitList'])
class DailyWaitListAPIView(ListCreateAPIView):
    serializer_class = WaitListSerializer

    def get_queryset(self):
        today = datetime.now().date()
        return WaitList.objects.filter(date__date=today).order_by('-date')


@extend_schema(tags=['SocialMedia'])
class SocialMediaAPIView(ListCreateAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


@extend_schema(tags=['Contacts'])
class ContactsAPIView(ListCreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


@extend_schema(tags=['AboutCompany'])
class AboutCompanyAPIView(ListCreateAPIView):
    queryset = AboutCompany.objects.all()
    serializer_class = AboutCompanySerializer


@extend_schema(tags=['Search'])
class HomeSearchAPIView(APIView):
    serializer_class = HomeFilterSerializer

    def post(self, request):
        serializer = HomeFilterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        homes = serializer.filter_queryset().filter(is_active=True)
        result = HomeSerializerGet(homes, many=True, context={'request': request})
        return Response(result.data, status=status.HTTP_200_OK)


@extend_schema(tags=['Location'])
class LocationAPIView(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
