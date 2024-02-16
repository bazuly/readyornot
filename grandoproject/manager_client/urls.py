from django.urls import path
from .views import *

app_name = 'manager_client'

urlpatterns = [
    path('add_client/', ClientCreateView.as_view(), name='add_client'),
    path('new_client_success/', new_client_success, name='new_client_success'),
    path('list_client/', get_client_data, name='get_client_data')
]
