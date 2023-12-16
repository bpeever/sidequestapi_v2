from django.contrib import admin
from .models import PrizeRedemption

# Register your models here.
@admin.register(PrizeRedemption)
class PrizeRedmeptionAdmin(admin.ModelAdmin):
    list_display = ['prize', 'user', 'id', 'sequential_id']