from django.contrib import admin
from .models import Prize

class PrizeInline(admin.TabularInline):
    model = Prize
    extra = 1
    fk_name = 'traffic_quest'

@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'expiry_date']
