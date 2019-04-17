from .base import *
import os

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
JWT_SECRET = os.environ['JWT_SECRET']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['RDS_DB_NAME'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
    }
}


ALLOWED_HOSTS = [".us-east-2.elasticbeanstalk.com", "localhost"]
