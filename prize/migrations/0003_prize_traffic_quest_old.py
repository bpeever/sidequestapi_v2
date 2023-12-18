# Generated by Django 4.2.7 on 2023-12-17 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_quest', '0007_rename_uuid_trafficquest_id'),
        ('prize', '0002_prize_traffic_quest_alter_prize_expiry_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='traffic_quest_old',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='prizes_old', to='traffic_quest.trafficquest'),
            preserve_default=False,
        ),
    ]