from typing import Tuple

from configuration.components.commons import DEBUG

INSTALLED_APPS: Tuple[str, ...] = (
    # Default django apps:
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # django-admin:
    "django.contrib.admin",
    "django.contrib.admindocs",
    # Hurricane for Kubernetes integration:
    "hurricane",
    # Extensions and 3rd Party Apps:
    "django_extensions",
    # Your Apps:
)

if DEBUG:
    INSTALLED_APPS += ("debug_toolbar",)
