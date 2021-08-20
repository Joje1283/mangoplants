from django.contrib import admin
from .models import Plant


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'updated_at', 'created_at']
