release: python manage.py migrate
web: daphne sidequestapi.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2
worker: celery -A sidequestapi worker