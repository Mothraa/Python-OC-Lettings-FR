import os

from pathlib import Path
from dotenv import load_dotenv  # python-dotenv
import sentry_sdk  # sentry-sdk
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.django import DjangoIntegration
import django.db.models.signals

load_dotenv(override=True)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# "conversion" de str en bool de la valeur de DEBUG.
DEBUG = os.getenv("DEBUG", "False").lower() in ["true", "1", "t", "yes", "y"]

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    os.getenv("RENDER_URL"),
]

# Sentry init
SENTRY_DSN = os.getenv("SENTRY_DSN")

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[
            DjangoIntegration(
                transaction_style="url",  # "function_name"
                middleware_spans=True,  # pour tracer les perfs du middleware
                signals_spans=True,  # pour tracer les signaux (ex: pre_save, post_save)
                signals_denylist=[  # pour exclure des signaux du tracage
                    django.db.models.signals.pre_init,
                    django.db.models.signals.post_init,
                ],
                cache_spans=False,  # pour tracer les opérations de cache
                http_methods_to_capture=("CONNECT", "GET", "POST", "DELETE",),
            ),
            LoggingIntegration(
                level="DEBUG",  # on capture tous les logs (DEBUG, INFO, WARNING, ERROR, CRITICAL)
                event_level="ERROR",  # Niveau minimum envoyé en évenement Sentry
            )
        ],
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for tracing.
        traces_sample_rate=1.0,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=1.0,
        send_default_pii=True,  # allow send personnal informations !
        debug=os.getenv("SENTRY_DEBUG", "False").lower() in ["true", "1", "t", "yes", "y"]
        # experiments desactivé pour la prod
        # _experiments={
        #     # Set continuous_profiling_auto_start to True
        #     # to automatically start the profiler on when
        #     # possible.
        #     "continuous_profiling_auto_start": True,
        # },
    )

# Application definition

INSTALLED_APPS = [
    'oc_lettings_site.apps.OCLettingsSiteConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lettings',
    'profiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oc_lettings_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'oc_lettings_site.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'oc-lettings-site.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "oc_lettings_site/static",]

# pour la compression et la mise en cache
ENV_DJANGO = os.getenv("ENV", "development")

if ENV_DJANGO == "production":
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        "sentry": {
            "level": "DEBUG",
            "class": "sentry_sdk.integrations.logging.EventHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "sentry"],
            "level": "INFO",  # "WARNING",
            "propagate": False,  # pour ne pas propager le log a la racine
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    }
}
