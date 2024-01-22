from django.urls import path
from .views import * 


app_name = 'add_car_data'


urlpatterns = [
    path('add_car/', add_car_data, name='add_car_data'),
    path('add_trailer/', add_trailer_data, name='add_trailer_data')
]
