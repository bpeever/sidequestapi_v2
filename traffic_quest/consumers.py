import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Participant
from channels.layers import get_channel_layer


class TrafficQuestConsumer(WebsocketConsumer):
    
    def connect(self):
        print("websocket connection accepted", self.channel_name)
        self.quest_name = "sidequest_test_quest"
        async_to_sync(self.channel_layer.group_add)(self.quest_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        print("websocket connection closed", self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(self.quest_name, self.channel_name)
        self.close()
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print("recieved!", message)
        self.send(text_data=json.dumps({"message": message}))

    def send_message(self, event):
        print("message sent")
        message = event["message"]
        self.send(text_data=json.dumps({"message": message}))


@receiver(post_save, sender=Participant)
def notify(sender, instance, created, **kwargs):
    group_name = "sidequest_test_quest"  # Replace with the actual group name
    message = "Notification message"  # Replace with the actual message
    participant_count = Participant.objects.filter(quest=instance.quest).count()
    print("particpant_count", participant_count)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            "type": "send_message",
            "message": participant_count,
        }
    )