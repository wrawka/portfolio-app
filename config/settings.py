from pathlib import Path
from dotenv import load_dotenv
from os import environ as env

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env.get('SECRET_KEY') or 'wow_so_secret'

DEBUG = env.get('DEBUG') == 'True'

ENVIRONMENT = env.get('ENVIRONMENT')

ALLOWED_HOSTS = env.get('ALLOWED_HOSTS', '*').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'projects',
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.joinpath('config').joinpath('templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': env.get('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': env.get('DB_NAME', BASE_DIR / 'db.sqlite3'),
        'USER': env.get('DB_USER', 'postgres'),
        'PASSWORD': env.get('DB_PASSWORD', 'postgres'),
        'HOST': env.get('DB_HOST', '127.0.0.1'),
        'PORT': env.get('DB_PORT', 5432),
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

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR.joinpath('static')

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')

IMAGES_ROOT = BASE_DIR.joinpath('projects').joinpath('img')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if DEBUG:
    INSTALLED_APPS += [
        "debug_toolbar",
    ]
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]
    INTERNAL_IPS = [
        "127.0.0.1",
    ]

if ENVIRONMENT == 'prod':
    CSRF_TRUSTED_ORIGINS = env.get('CSRF_TRUSTED_ORIGINS', 'http://localhost').split(',')

    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn="https://fed170e81b3341dc98cfb4a7bab26bee@o4504971180441600.ingest.sentry.io/4504971183390720",
        integrations=[
            DjangoIntegration(),
        ],

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True
    )
