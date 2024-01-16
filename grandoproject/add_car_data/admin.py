from django.contrib import admin
from .models import UploadCarData

@admin.register(UploadCarData)
class UploadCarDataAdmin(admin.ModelAdmin):
    list_display = ['car_name', 'car_number', 'trailer_name', 'trailer_number']
    search_fields = ['car_name', 'trailer_name']
    save_on_top = True