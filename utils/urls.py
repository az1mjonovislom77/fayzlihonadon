from django.urls import path
from .views import (HomePageAPIView, AdvertisementBannerAPIView, ReviewsAPIView)

urlpatterns = [
    path('homepage/', HomePageAPIView.as_view(), name='homepage_list'),
    path('advertisementbanner/', AdvertisementBannerAPIView.as_view(), name='advertisementbanner_list'),
    path('reviews/', ReviewsAPIView.as_view(), name='reviews_list'),

]
