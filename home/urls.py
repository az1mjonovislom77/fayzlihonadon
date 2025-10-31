from django.urls import path

from .views import (HomeGetAPIView, HomePostAPIView, BasementAPIView, CommonHouseAPIView, CommonHouseAboutAPIView,
                    InProgressAPIView)

urlpatterns = [
    path('all/', HomeGetAPIView.as_view(), name='home_list'),
    path('create/', HomePostAPIView.as_view(), name='home_post'),
    path('basement/', BasementAPIView.as_view(), name='basement_list'),
    path('commonhouse/', CommonHouseAPIView.as_view(), name='commonhouse_list'),
    path('commonhouse/about/', CommonHouseAboutAPIView.as_view(), name='commonhouseabout_list'),
    path('inprogress/', InProgressAPIView.as_view(), name='inprogress_list'),

]
