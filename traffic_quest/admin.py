from django.contrib import admin
from .models import TrafficQuest


@admin.register(TrafficQuest)
class TrafficQuestAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date']
