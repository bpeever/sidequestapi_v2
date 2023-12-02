from django.db import models


class Prize(models.Model):
    name = models.CharField(max_length=50)
    #quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    description = models.TextField(max_length=200, null=True, blank=True)
    expiry_date = models.DateTimeField()
    quantity = models.IntegerField()
    redemption_code = models.CharField(max_length=50, null=True, blank=True)
    # Redemption_coordinates
    # Prize thumbnail
