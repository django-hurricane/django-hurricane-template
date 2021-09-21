"""
Django settings for a Hurricane-based project.

For the full list of settings and their config, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from django.utils.translation import ugettext_lazy as _

from decouple import config

from configuration.components import BASE_DIR


DEBUG = config("DJANGO_DEBUG", cast=bool, default=False)


ROOT_URLCONF = "configuration.urls"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

engine = config("DATABASE_ENGINE", default="django.db.backends.postgresql")

# postgresql
if engine == "django.db.backends.postgresql":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": config("DATABASE_NAME"),
            "USER": config("DATABASE_USER"),
            "PASSWORD": config("DATABASE_PASSWORD"),
            "HOST": config("DATABASE_HOST"),
            "PORT": config("DATABASE_PORT", cast=int, default=5432),
            "CONN_MAX_AGE": config("CONN_MAX_AGE", cast=int, default=60),
            "ATOMIC_REQUESTS": config("DJANGO_ATOMIC_REQUESTS", cast=bool, default=True),
            "OPTIONS": {
                "connect_timeout": 10,
            },
        },
    }

# sqlite3 (e.g. for testing)
elif engine == "django.db.backends.sqlite3":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": config("DATABASE_NAME"),
        },
    }

else:
    raise Exception("DATABASES is invalid or not set.")

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

USE_I18N = True
USE_L10N = True

LANGUAGES = (("en", _("English")),)

LOCALE_PATHS = ("locale/",)

USE_TZ = True
TIME_ZONE = "UTC"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Templates

TEMPLATES = [
    {
        "APP_DIRS": True,
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # Contains plain text templates, like `robots.txt`:
            BASE_DIR.joinpath("templates"),
        ],
        "OPTIONS": {
            "context_processors": [
                # Default template context processors:
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
        },
    }
]


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Security
SECRET_KEY = config("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS", cast=list, default=["*"])
SESSION_COOKIE_HTTPONLY = config("DJANGO_SESSION_COOKIE_HTTPONLY", cast=bool, default=True)
CSRF_COOKIE_HTTPONLY = config("DJANGO_CSRF_COOKIE_HTTPONLY", cast=bool, default=True)
SECURE_CONTENT_TYPE_NOSNIFF = config("DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", cast=bool, default=True)
SECURE_BROWSER_XSS_FILTER = config("DJANGO_SECURE_BROWSER_XSS_FILTER", cast=bool, default=True)

X_FRAME_OPTIONS = config("DJANGO_X_FRAME_OPTIONS", default="DENY")

# https://github.com/DmytroLitvinov/django-http-referrer-policy
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy
REFERRER_POLICY = config("DJANGO_REFERRER_POLICY", default="same-origin")

EMAIL_TIMEOUT = 5

with open(os.path.join(BASE_DIR, "version.txt")) as v_file:
    VERSION = v_file.read()

HURRICANE_VERSION = VERSION
