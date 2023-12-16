from django.urls import path
from . import views


urlpatterns = [
    path('test_award_prizes/', views.test_award_prizes, name='test_award_prizes'),
]