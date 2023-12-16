from django.dispatch import receiver
from traffic_quest.signals import quest_completed

@receiver(quest_completed)
def test_reciever(sender, **kwargs):

    # Get the quest. 
    # Get the associated prizes.
    # Loop throught the prizes and pick winners for each object. 
    # Make sure each user can only win once. 
    # Send a notification to the winner.

    print("test_reciever")