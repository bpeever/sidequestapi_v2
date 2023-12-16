from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
import uuid

#  Email redemption
#  QR Redemption
#  Mailed Redemption
#  How should this be structured?  Email or QRcode dont really change anything....theyre just features. 
#  qr_isnt a redemption method
#  No app to redeem, just taken to the page by the scanner and asked for the code.  Can also see in client dashboard. 

# uuid, fk_user, fk_prize, unique_prize_id, is_claimed, mailing_address (user account), phone_number (user account), is_collected
# claimed_at, created, updated,

User = get_user_model()

class PrizeRedemption(models.Model):
        
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        prize = models.ForeignKey("prize.Prize", on_delete=models.CASCADE, related_name='prize_redemption')
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        sequential_id = models.IntegerField(null=True, blank=True)
        is_claimed = models.BooleanField(default=False)
        claimed_at = models.DateTimeField(null=True, blank=True)
        is_viewed = models.BooleanField(default=False)
        viewed_at = models.DateField(null=True, blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
  
        def __str__(self):
                return str(self.prize)