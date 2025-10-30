from django.urls import path

from .views import (HomeGetAPIView, HomePostAPIView, BasementAPIView, CommonHouseAPIView)

urlpatterns = [
    path('all/', HomeGetAPIView.as_view(), name='home_list'),
    path('create/', HomePostAPIView.as_view(), name='home_post'),
    path('basement/', BasementAPIView.as_view(), name='basement_list'),
    path('commonhouse/', CommonHouseAPIView.as_view(), name='commonhouse_list'),

]
