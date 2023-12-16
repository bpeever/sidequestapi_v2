from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import TrafficQuest, Participant
from .serializers import TrafficQuestSerializer, ParticipantSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .signals import quest_completed

def test_unlock_websocket(request):
    return render(request, 'traffic_quest/test_unlock_websocket.html')

@api_view(['GET'])
def test_get_traffic_quests(request):
    traffic_quest = TrafficQuest.objects.all()
    serialized = TrafficQuestSerializer(traffic_quest, many=True)
    return Response(data=serialized.data)

def test_traffic_gauge_websocket(request):
    traffic_quests = TrafficQuest.objects.all()
    print("traffic_quests", traffic_quests)
    return render(request, 'traffic_quest/test_traffic_gauge_websocket.html', {'traffic_quests': traffic_quests})

@api_view(['GET', 'POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_num_participants(request):
    #quest_id = 1
    #user = request.user
    #goal = TrafficQuest.objects.get(id=quest_id).traffic_goal
    #participant = Participant.objects.create(user=request.user, quest_id=quest_id)
    return Response(data=38)

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def client_participate(request):
    data = {**request.data, 'user': request.user.id}
    serializer = ParticipantSerializer(data=data)

    if serializer.is_valid():
        traffic_quest = serializer.validated_data.get('quest') # returns "None" istead of an missing key-value error
        
        if TrafficQuest is None:
            return Response({'message': 'quest does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            #traffic_quest = get_object_or_404(TrafficQuest, id=quest)

        participants = Participant.objects.filter(quest=traffic_quest).count()

        if participants >= traffic_quest.traffic_goal:  # Could use "annotate" instead of (2) seperate queries
            quest_completed.send(sender=traffic_quest.__class__, quest_id=traffic_quest.id)
            return Response({'message': 'quest is full'}, status=status.HTTP_400_BAD_REQUEST)

        #TODO Make sure quest has started but not ended
        serializer.save()

        if participants + 1 == traffic_quest.traffic_goal:
            quest_completed.send(sender=traffic_quest.__class__, quest_id=traffic_quest.id)
            pass

        return Response({'message': 'success'}, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

