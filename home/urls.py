from django.urls import path
from .views import (HomeGetAPIView, HomePostAPIView)

urlpatterns = [
    path('all/', HomeGetAPIView.as_view(), name='home_list'),
    path('create/', HomePostAPIView.as_view(), name='home_post')

]

