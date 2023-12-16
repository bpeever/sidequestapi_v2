import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class PlaygroundConsumer(WebsocketConsumer):
    
    def connect(self):
        print("websocket connection accepted", self.channel_name)
        self.quest_name = "sidequest_test_quest"
        async_to_sync(self.channel_layer.group_add)(self.quest_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
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


class PlaygroundSendingConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        print("Websocket connection accepted", self.channel_name)
        self.quest_name = "sidequest_test_quest"
        async_to_sync(self.channel_layer.group_add)(self.quest_name, self.channel_name)
        #return super().connect()
    
    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(self.quest_name, self.channel_name)
        self.close()
        #return super().disconnect(code)
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print("text_data_json", text_data_json)
        async_to_sync(self.channel_layer.group_send)(self.quest_name, {
            'type': 'send_message',
            'message': "this is a test"
        })
   
    # Note that the "send_message" functions for both classed can be called by receive() functions
    def send_message(self, event):
        #print("message sent")
        message = event["message"]
        self.send(text_data=json.dumps({"message": message}))
