from django.contrib import admin
from .models import Prize


@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'expiry_date']
