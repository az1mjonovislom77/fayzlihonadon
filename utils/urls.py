from django.urls import path
from .views import (HomePageAPIView)

urlpatterns = [
    path('homepage/', HomePageAPIView.as_view(), name='homepage_list'),

]
