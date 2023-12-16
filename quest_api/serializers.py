from rest_framework import serializers
from traffic_quest.models import TrafficQuest

class TrafficQuestSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = TrafficQuest
        fields = '__all__'  # Add your fields here
