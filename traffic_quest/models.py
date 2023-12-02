from django.db import models


class TrafficQuest(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateField()
    traffic_goal = models.IntegerField()
    prizes = models.ForeignKey('prize.Prize', on_delete=models.CASCADE, related_name="traffic_quest")
    # image


# Need a model for traffic count