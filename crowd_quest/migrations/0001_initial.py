# Generated by Django 4.2.7 on 2023-11-29 02:40

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ParticipateCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_code', models.CharField(max_length=50)),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participate_codes', to='crowd_quest.quest')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipateArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, geography=True, null=True, srid=4326)),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participate_areas', to='crowd_quest.quest')),
            ],
        ),
    ]
