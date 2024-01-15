from django.contrib import admin
from django.urls import path, include
from grandoproject import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('add_driver_data/', include('add_driver_data.urls', namespace='add_driver_data')),
    path('get_driver_data/', include('get_driver_data.urls', namespace='get_driver_data')),
    path('add_car_data/', include('add_car_data.urls', namespace='add_car_data'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

