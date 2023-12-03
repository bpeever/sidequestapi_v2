from django.urls import re_path, path
from . import consumers


websocket_urlpatterns = [
    #re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    path('ws/playground/test_websocket_connection/', consumers.PlaygroundConsumer.as_asgi()),
    path('ws/playground/test_websocket_sending/', consumers.PlaygroundSendingConsumer.as_asgi()),

]