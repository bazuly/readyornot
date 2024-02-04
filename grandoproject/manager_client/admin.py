from django.contrib import admin
from .models import Tag, Client

# admin.site.register(Tag, Client)
#
#
# class Tag(admin.ModelAdmin):
#     list_display = ['name']
#     save_on_top = True
#
#
# @admin.register(Client)
# class Client(admin.ModelAdmin):
#     list_display = ['name', 'inn', 'manager']
