import configparser
import logging
import os
import datetime

from smartgetenv import get_bool, get_list, get_env

logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_PATH = os.path.join(BASE_DIR, 'config')
if not os.path.exists(CONFIG_PATH):
    os.makedirs(CONFIG_PATH)

CONFIG_FILE = os.path.join(CONFIG_PATH, 'config.ini')
config = configparser.ConfigParser()
config.read(CONFIG_FILE)

try:
    SECRET_KEY = config.get('DJANGO', 'SECRET_KEY')
except:
    logger.warning('SECRET_KEY not found! Generating a new one...')
    import random

    SECRET_KEY = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$^&*(-_=+)") for i in range(50)])
    if not config.has_section('DJANGO'):
        config.add_section('DJANGO')
    config.set('DJANGO', 'SECRET_KEY', SECRET_KEY)
    with open(CONFIG_FILE, 'wt') as f:
        config.write(f)

DEBUG = get_bool('DEBUG', False)

ALLOWED_HOSTS = get_list('ALLOWED_HOSTS', ['localhost', '127.0.0.1', '.iswn.pro'])

INSTALLED_APPS = [
    'api.apps.ApiConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djoser'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'iswn.urls'

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

WSGI_APPLICATION = 'iswn.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': get_env('DATABASE_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': get_env('DATABASE_NAME', 'postgres'),
        'USER': get_env('DATABASE_USER', 'postgres'),
        'PASSWORD': get_env('DATABASE_PASSWORD', ''),
        'HOST': get_env('DATABASE_HOST', 'db'),
        'PORT': get_env('DATABASE_PORT', '5432'),
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=12),
    'JWT_ALLOW_REFRESH': True,
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_ROOT = os.path.join(BASE_DIR, 'www', 'static')

AUTH_USER_MODEL = 'api.MyUser'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        }
    },
    'root': {
        'handlers': ['console'],
        'level': get_env('DJANGO_LOG_LEVEL', 'DEBUG'),
    }
}
