from .base import *

# Local configs
SECRET_KEY = env('DJANGO_SECRET_KEY', default='x(9h8htk+_j=56rnih)p117-6uooyp@78rpekekwn+anv!-kip')
DEBUG = env.bool('DJANGO_DEBUG', default=True)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'syllable',
        'USER': 'syllableuser',
        'PASSWORD': 'syllabledb',
        'HOST': 'localhost',
    }
}
