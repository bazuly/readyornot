from django.urls import path
from .views import *

app_name = 'get_car_data'

urlpatterns = [
    path('download/<int:car_id>/', download_car_data, name='download_car_data'),
    path('download/<int:trailer_id>/', download_trailer_data, name='download_trailer_data'),
    path('', get_car_data, name='get_car_data'),
]
