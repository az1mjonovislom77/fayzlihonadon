from django.urls import path
from .views import (HomePageAPIView, AdvertisementBannerAPIView, ReviewsAPIView, WaitListAPIView, SocialMediaAPIView,
                    ContactsAPIView)

urlpatterns = [
    path('homepage/', HomePageAPIView.as_view(), name='homepage_list'),
    path('advertisementbanner/', AdvertisementBannerAPIView.as_view(), name='advertisementbanner_list'),
    path('reviews/', ReviewsAPIView.as_view(), name='reviews_list'),
    path('waitlist/', WaitListAPIView.as_view(), name='wait-list'),
    path('social-media/', SocialMediaAPIView.as_view(), name='social_media_list'),
    path('contacts/', ContactsAPIView.as_view(), name='contacts_list'),

]
