from django.urls import path
from . import views

urlpatterns = [
    path('test_unlock_websocket/', views.test_unlock_websocket, name='test_unlock_websocket'),
    path('test_get_traffic_quests/', views.test_get_traffic_quests, name='test_get_traffic_quests'),
    path('test_traffic_gauge_websocket/', views.test_traffic_gauge_websocket, name='test_traffic_gauge_websocket'), 

    path('api/v1.0/get_num_participants/', views.get_num_participants, name='get_num_participants') ,
    path('api/v1.0/client_participate/', views.client_participate, name='client_participate')

]