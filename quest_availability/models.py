from django.contrib.gis.db import models


class ParticipateCode(models.Model):
    #quest = models.ForeignKey('quest.Quest', on_delete=models.CASCADE, related_name="participate_codes")
    join_code = models.CharField(max_length=50)


class ParticipateArea(models.Model):
    #quest = models.ForeignKey('quest.Quest', on_delete=models.CASCADE, related_name='participate_areas')
    area = models.MultiPolygonField(geography=True, srid=4326, null=True, blank=True)


