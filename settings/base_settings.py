import os

# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# /tero/app
BASE_DIR = os.path.abspath(
    os.path.join(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

# /tero
PROJECT_ROOT = BASE_DIR  # os.path.abspath(os.path.join(BASE_DIR, os.path.pardir))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'alarm',
    'telegram',
    'mordor',
]

INSTALLED_APPS += [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_extensions',
    'channels',
    'bootstrapform',
    'dashboard',
    'corsheaders'
]

MIDDLEWARE_CLASSES = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    # 'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'data', 'db.sqlite3'),
    # }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

# Fixtures
FIXTURE_DIRS = [os.path.join(PROJECT_ROOT, 'fixtures')]

LOGGING_DEFAULT_LEVEL = 'ERROR'

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

LOGDIR = os.getenv('DJANGO_LOGS', '/logs')
os.makedirs(LOGDIR, exist_ok=True)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
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
        'alarm.handler': {
            'level': 'DEBUG',
            'class' : 'logging.handlers.RotatingFileHandler',
            'maxBytes' : 1024*1024*20, # 10MB
            'backupCount': 3,
            'formatter': 'simple',
            'filename': os.path.join(LOGDIR, 'alarm.log'),
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
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'mordor': {
            'handlers': ['console', 'mordor.handler'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'alarm': {
            'handlers': ['console', 'alarm.handler'],
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
