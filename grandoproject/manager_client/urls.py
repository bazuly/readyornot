from django.urls import path
from .views import add_client

urlpatterns = [
    # path('manager/<int:manager_id>/', manager_clietns, name='manager_clietns')
    path('add_client/', add_client, name='add_client')
]
