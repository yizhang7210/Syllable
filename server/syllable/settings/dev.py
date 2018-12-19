from .base import *
import os

DATABASES = {
    'default': {
        'NAME': os.environ['DB_NAME'],
        'HOST': os.environ['HOSTNAME'],
        'PORT': os.environ['PORT'],
        'USER': os.environ['USERNAME'],
        'PASSWORD': os.environ['PASSWORD'],
    }
}

ALLOWED_HOSTS = [".us-east-2.elasticbeanstalk.com", "localhost"]
