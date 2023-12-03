from django.urls import path
from . import views

urlpatterns = [
    path('test_websocket_connection/', views.test_websocket_connection, name='test_websocket_connetion'),
    path("test_websocket_sending/", views.test_websocket_sending_template, name="test_websocket_sending"),
]