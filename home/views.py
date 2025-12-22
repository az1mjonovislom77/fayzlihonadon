from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView, ListAPIView
from .models import Home, Basement, CommonHouse, CommonHouseAbout, InProgress, DownPayment
from rest_framework.pagination import PageNumberPagination
from .serializers import HomeSerializerGet, HomeSerializerPost, BasementSerializer, CommonHouseSerializer, \
    CommonHouseAboutSerializer, InProgressSerializer, DownPaymentSerializer


class HomePagination(PageNumberPagination):
    page_size = 20


@extend_schema(tags=['Home'])
class HomeAPIView(ListAPIView):
    serializer_class = HomeSerializerGet
    pagination_class = HomePagination

    def get_queryset(self):
        return Home.objects.filter(is_active=True)


@extend_schema(tags=['Home'])
class HomeGetAPIView(ListAPIView):
    serializer_class = HomeSerializerGet

    def get_queryset(self):
        return Home.objects.filter(is_active=True).order_by('?')[:20]


@extend_schema(tags=['Home'])
class HomePostAPIView(CreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializerPost


@extend_schema(tags=['Basement'])
class BasementAPIView(ListCreateAPIView):
    queryset = Basement.objects.all()
    serializer_class = BasementSerializer


@extend_schema(tags=['CommonHouse'])
class CommonHouseAPIView(ListCreateAPIView):
    queryset = CommonHouse.objects.all()
    serializer_class = CommonHouseSerializer


@extend_schema(tags=['CommonHouseAbout'])
class CommonHouseAboutAPIView(ListCreateAPIView):
    queryset = CommonHouseAbout.objects.all()
    serializer_class = CommonHouseAboutSerializer


@extend_schema(tags=['InProgress'])
class InProgressAPIView(ListCreateAPIView):
    queryset = InProgress.objects.all()
    serializer_class = InProgressSerializer


@extend_schema(tags=['HomeDetail'])
class HomeDetailGetAPIView(RetrieveAPIView):
    queryset = Home.objects.filter(is_active=True)
    serializer_class = HomeSerializerGet
    lookup_field = 'pk'


@extend_schema(tags=['CommonHouseDetail'])
class CommonHouseDetailGetAPIView(RetrieveAPIView):
    queryset = CommonHouse.objects.all()
    serializer_class = CommonHouseSerializer
    lookup_field = 'pk'


@extend_schema(tags=['CommonHouseAboutDetail'])
class CommonHouseAboutDetailGetAPIView(RetrieveAPIView):
    queryset = CommonHouseAbout.objects.all()
    serializer_class = CommonHouseAboutSerializer
    lookup_field = 'pk'


@extend_schema(tags=['DownPayment'])
class DownPaymentAPIView(ListCreateAPIView):
    queryset = DownPayment.objects.all()
    serializer_class = DownPaymentSerializer
