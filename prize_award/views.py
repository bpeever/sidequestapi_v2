from django.shortcuts import render
from rest_framework.decorators import api_view
from traffic_quest.models import TrafficQuest
from rest_framework.response import Response
import random
from django.core.exceptions import ObjectDoesNotExist
from .signals import prize_winner_selected


#TODO Move this to handlers
#TODO Remove users that are flagged for cheating
@api_view(['GET'])
def test_award_prizes(request):
   
    quest_id = 1

    try:
        quest = TrafficQuest.objects.get(id=quest_id)
    except ObjectDoesNotExist:
        return Response(data="Quest not found")

    if not quest.prizes.exists():
        return Response(data="No prizes available")

    if quest.participants.count() == 0:
        return Response("There are no participants")
    
    #TODO Check if a prize has already been awarded. Block award code if so. 
    
    participants = list(quest.participants.all())

    #TODO Make sure a winner can only be selected once by calling unique on the participants query
   
    for prize in quest.prizes.all():
        sequential_id = 0
        number_of_participants = len(participants)  # Count the number of participants
        number_of_prizes = prize.quantity
        number_to_award = min(number_of_participants, number_of_prizes)
        winners = random.sample(participants, number_to_award)
        
        for winner in winners:
            sequential_id += 1
            prize_winner_selected.send(sender=prize.__class__ , sequential_id=sequential_id, prize=prize, winner=winner)
            print("participant", winner)
            participants.remove(winner)
    
    return Response(data="Prize award complete!")
