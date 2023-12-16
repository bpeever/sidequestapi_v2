from django.db import models
from django.contrib.auth.models import User


class PrizeEntree(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prize_entree')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


#TODO: Decide if you want to protect the PrizeAwardRecord from being deleted.  If so, uncomment the following code.
#class PrizeAwardRecord(models.Model):
#    quest = models.ForeignKey("traffic_quest.TrafficQuest", on_delete=models.CASCADE, related_name='prize_award_record')
#    number_of_participants = models.IntegerField(blank=True, null=True)
#    winners = models.ManyToManyField(User, related_name='prize_award_record')
#    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)