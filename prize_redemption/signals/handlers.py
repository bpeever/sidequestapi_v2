from django.dispatch import receiver
from prize_award.signals import prize_winner_selected
from ..models import PrizeRedemption
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# logger = logging.getogger(__name__)

@receiver(prize_winner_selected)
def create_prize_redemption(sender, **kwargs):

    prize = kwargs.get("prize")
    user = kwargs.get("winner")
    sequantial_id = kwargs.get("sequential_id")

    try:
        user_object = User.objects.get(username=user) 
    except ObjectDoesNotExist:
        # TODO: logger.error(f"No user found with username {user}"")
        return

    new_prize_redemption = PrizeRedemption.objects.create(
        user=user_object,
        prize=prize, 
        sequential_id=sequantial_id
    )

    print("test_receiver", prize, user)
    pass