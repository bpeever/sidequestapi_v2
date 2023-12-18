# Generated by Django 4.2.7 on 2023-12-17 23:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_quest', '0005_trafficquest_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trafficquest',
            name='id',
        ),
        migrations.AlterField(
            model_name='trafficquest',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]