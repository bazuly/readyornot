from django.urls import path
from .views import * 


app_name = 'add_car_data'


urlpatterns = [
    path('', add_car_data, name='add_car_data'),
]
