from django.contrib import admin
from .models import Details


@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ['name',]