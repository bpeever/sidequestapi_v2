from django.contrib.gis.db import models
import uuid


class ParticipateCode(models.Model):
    quest = models.ForeignKey('Details', on_delete=models.CASCADE, related_name="participate_codes")
    join_code = models.CharField(max_length=50)


class ParticipateArea(models.Model):
    quest = models.ForeignKey('Details', on_delete=models.CASCADE, related_name='participate_areas')
    area = models.MultiPolygonField(geography=True, srid=4326, null=True, blank=True)


class Details(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    #  quest_coordinates
    #  quest_image

    def __str__(self):
        return self.name
