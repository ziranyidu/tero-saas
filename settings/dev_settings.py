import os

from settings.base_settings import *

# from dotenv import load_dotenv
# dotenv_path = os.path.join(PROJECT_ROOT, '.env')
# load_dotenv(dotenv_path)

DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

TERO_ROOT_DIR = os.path.expanduser('~/.tero')
if not os.path.isdir(TERO_ROOT_DIR):
    os.makedirs(TERO_ROOT_DIR, exist_ok=True)

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tero',
        'USER': 'postgres',
        'PASSWORD': 'tero',
        'HOST': 'pgsql',
    }
}

IMAGES_PROXY_URL = 'http://localhost:8000/images/upload'

TERO_LOG_DIR = os.path.join(TERO_ROOT_DIR, 'logs')
if not os.path.exists(TERO_LOG_DIR):
    os.makedirs(TERO_LOG_DIR)
LOGGING_DEFAULT_LEVEL = 'DEBUG'
LOGGING_CONSOLE_HANDLER = 'console'
LOGGING_FILE_HANDLER = 'file_default'
LOGGING_DEFAULT_HANDLERS = [LOGGING_CONSOLE_HANDLER, LOGGING_FILE_HANDLER]

# Telegram app
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_API_URL = 'https://api.telegram.org/bot' + TELEGRAM_BOT_TOKEN + '/'

# Django channels
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [('redis', 6379)],
        },
        "ROUTING": "settings.routing.channel_routing",
    },
}

CORS_ORIGIN_ALLOW_ALL = True

# Logging config
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s %(levelname)s] (%(module)s): %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        LOGGING_CONSOLE_HANDLER: {
            'level': LOGGING_DEFAULT_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'filters': ['require_debug_true'],
        },
        LOGGING_FILE_HANDLER: {
            'level': LOGGING_DEFAULT_LEVEL,
            'class': 'logging.FileHandler',
            'filename': os.path.join(TERO_LOG_DIR, 'dj-tero.log'),
            'formatter': 'verbose',
            'filters': [],
        },
        'file': {
            'level': 'DEBUG',
            'class' : 'logging.handlers.RotatingFileHandler',
            'maxBytes' : 1024*1024*20, # 10MB
            'backupCount': 3,
            'formatter': 'simple',
            'filename': os.path.join(LOGDIR, 'debug.log'),
        },
        'mordor.handler': {
            'level': 'DEBUG',
            'class' : 'logging.handlers.RotatingFileHandler',
            'maxBytes' : 1024*1024*20, # 10MB
            'backupCount': 3,
            'formatter': 'simple',
            'filename': os.path.join(LOGDIR, 'mordor.log'),
        },
        'telegram.handler': {
            'level': 'DEBUG',
            'class' : 'logging.handlers.RotatingFileHandler',
            'maxBytes' : 1024*1024*20, # 10MB
            'backupCount': 3,
            'formatter': 'simple',
            'filename': os.path.join(LOGDIR, 'telegram.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': LOGGING_DEFAULT_HANDLERS,
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': LOGGING_DEFAULT_HANDLERS,
            'level': LOGGING_DEFAULT_LEVEL,
            'propagate': False,
        },
        'notifications': {
            'handlers': LOGGING_DEFAULT_HANDLERS,
            'level': LOGGING_DEFAULT_LEVEL,
            'propagate': False,
        },
        'mordor': {
            'handlers': ['console', 'mordor.handler'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'telegram': {
            'handlers': ['console', 'telegram.handler'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
