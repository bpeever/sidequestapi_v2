from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from traffic_quest.models import TrafficQuest
from .serializers import TrafficQuestSerializer


@api_view(["GET"])
def get_quests(request):
    
    traffic_quest = TrafficQuest.objects.all()
    print("traffic_quests", traffic_quest)
    serialized = TrafficQuestSerializer(data=traffic_quest, many=True)
    serialized.is_valid()

    return Response(serialized.data)