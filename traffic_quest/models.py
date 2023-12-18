from django.db import models
from django.contrib.auth.models import User
import uuid


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="participants")
    quest = models.ForeignKey('TrafficQuest', on_delete=models.CASCADE, related_name="participants")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class TrafficQuest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateField()
    traffic_goal = models.IntegerField()
    #prizes = models.ForeignKey('prize.Prize', on_delete=models.CASCADE, related_name="traffic_quest")
    # image

    def __str__(self):
        return self.name

# Need a model for traffic count