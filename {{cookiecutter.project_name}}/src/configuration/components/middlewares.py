from typing import Tuple

from decouple import config

from configuration.components.commons import DEBUG

MIDDLEWARE: Tuple[str, ...] = (
    # Content Security Policy:
    "csp.middleware.CSPMiddleware",
    # Django:
    "django.middleware.security.SecurityMiddleware",
    # django-permissions-policy
    "django_permissions_policy.PermissionsPolicyMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Django HTTP Referrer Policy:
    "django_http_referrer_policy.middleware.ReferrerPolicyMiddleware",
)

# Django debug toolbar:
# https://django-debug-toolbar.readthedocs.io
if DEBUG:
    if config("DJANGO_SHOW_TOOLBAR", cast=bool, default=False):
        MIDDLEWARE += (
            "debug_toolbar.middleware.DebugToolbarMiddleware",
            # https://github.com/bradmontgomery/django-querycount
            # Prints how many queries were executed, useful for the APIs.
            "querycount.middleware.QueryCountMiddleware",
        )


def _custom_show_toolbar(request):
    """Only show the debug toolbar to users with the superuser flag."""
    return DEBUG and config("DJANGO_SHOW_TOOLBAR", cast=bool, default=False)


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": "server.settings.environments.development._custom_show_toolbar",
}
