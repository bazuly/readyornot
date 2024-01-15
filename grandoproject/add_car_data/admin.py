from django.contrib import admin
from .models import UploadCarData

@admin.register(UploadCarData)
class UploadCarDataAdmin(admin.ModelAdmin):
    list_display = ['car_name', 'car_number']
    search_fields = ['car_name']
    save_on_top = True