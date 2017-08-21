from .settings_base import *

ALLOWED_HOSTS = ['192.168.1.50', '127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tmc',
        'USER': 'tmc',
        'PASSWORD': 'Hard24Get',
        'HOST': '192.1.1.50',
        'PORT': '5432',
    }
}
