from django.shortcuts import render
from django.http import HttpResponse
from .tasks import fake_celery_task
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def test_drf(request):
    return Response({"message": "Hello, world!"})

def test_websocket_connection(request):
    return render(request, 'websocket/test_websocket_connection.html')

def test_websocket_sending_template(request):
    return render(request, 'websocket/test_websocket_sending_template.html')

def test_celery_task(request):
    fake_celery_task.delay()
    return HttpResponse(request, 'celery test complete')