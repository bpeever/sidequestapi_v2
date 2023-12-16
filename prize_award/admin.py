from django.contrib import admin
from .models import PrizeEntree

@admin.register(PrizeEntree)
class PrizeEntreeAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')