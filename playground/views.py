from django.shortcuts import render

# Create your views here.

def test_websocket_connection(request):
    return render(request, 'websocket/test_websocket_connection.html')

def test_websocket_sending_template(request):
    return render(request, 'websocket/test_websocket_sending_template.html')