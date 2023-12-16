from django.urls import re_path, path
from . import consumers


websocket_urlpatterns = [
    #re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    path('ws/traffic_quest/test_unlock_websocket/', consumers.TrafficQuestConsumer.as_asgi())
]