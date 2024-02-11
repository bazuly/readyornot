from django.contrib import admin
from .models import Client

admin.site.register(Client)


class Client(admin.ModelAdmin):
    list_display = ['name', 'contacts', 'manager']
