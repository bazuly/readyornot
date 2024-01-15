from django.urls import path
from .views import *

app_name = 'get_driver_data'

urlpatterns = [
    path('download/<int:driver_id>/', download_driver_data, name='download_driver_data'),
    path('', get_driver_data, name='get_driver_data'),
]

# доабвить аналогиченое добавление данных, только на ТС и полуприцепы 
# добавить получение данных в шаблон get_driver_data, только на ТС 

# скачивание файла лучше пихнуть в разоврот 
# сделать отображение только zip файлов, чтобы загружать можно было только их