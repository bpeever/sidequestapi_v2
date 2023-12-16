import os
from .common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

REDIS_URL = os.environ['REDIS_URL']