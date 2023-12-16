import os
from .common import *
import django_heroku
import dj_database_url


DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
CHANNEL_LAYER_REDIS_URL = os.environ['CHANNEL_LAYER_REDIS_URL']

MIDDLEWARE.insert(1,'whitenoise.middleware.WhiteNoiseMiddleware')

ALLOWED_HOSTS = ['*', "sidequestapi-v2-3ac308dc66da.herokuapp.com"]
CSRF_TRUSTED_ORIGINS = ["http://sidequestapi-v2-3ac308dc66da.herokuapp.com", "https://sidequestapi-v2-3ac308dc66da.herokuapp.com"]


django_heroku.settings(locals())

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=False)
}
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

# TODO Can maybe move this to common. 
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.pubsub.RedisPubSubChannelLayer",
        "CONFIG": {
            "hosts":[{
                "address": CHANNEL_LAYER_REDIS_URL,  # "REDIS_TLS_URL"
                "ssl_cert_reqs": None,
            }]
        }
    }
}

