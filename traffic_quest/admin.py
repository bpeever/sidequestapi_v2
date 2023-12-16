from django.contrib import admin
from .models import TrafficQuest, Participant
from prize.admin import PrizeInline

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['user', 'quest', 'created_at']


@admin.register(TrafficQuest)
class TrafficQuestAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'start_date', 'end_date']
    inlines = [PrizeInline]
