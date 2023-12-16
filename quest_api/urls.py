from django.urls import path
from . import views


urlpatterns = [
    path('get_quests/', views.get_quests, name= 'get_quests')
]
