from django.db import models
from datetime import datetime


class Prize(models.Model):
    name = models.CharField(max_length=50)
    #quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    description = models.TextField(max_length=200, null=True, blank=True)
    expiry_date = models.DateTimeField(default=datetime(2010, 1, 1, 0, 0, 0, 0))
    quantity = models.IntegerField(default=1)
    redemption_code = models.CharField(max_length=50, null=True, blank=True)
    traffic_quest = models.ForeignKey('traffic_quest.TrafficQuest', on_delete=models.CASCADE, related_name="prizes")

    # Redemption_coordinates
    # Prize thumbnail
