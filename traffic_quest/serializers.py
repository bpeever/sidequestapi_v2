from rest_framework import serializers
from .models import TrafficQuest, Participant


class TrafficQuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficQuest
        fields = '__all__'


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'