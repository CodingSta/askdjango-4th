from .dev import *

DEBUG = False

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, "..", "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "..", "media")

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', SECRET_KEY)

INSTALLED_APPS += [
    # '',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ubuntu',
        'USER': 'ubuntu',
        'PASSWORD': 'withaskdjango!',
        'HOST': '127.0.0.1',
    }
}
