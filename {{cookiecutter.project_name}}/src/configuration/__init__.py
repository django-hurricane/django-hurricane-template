"""
This is a django-split-settings main file.
"""

from os import environ

from split_settings.tools import include


_base_settings = (
    "components/apps.py",
    "components/common.py",
    "components/middlewares.py",
    "components/logging.py",
    "components/csp.py",
    "components/caches.py",
    "components/storage.py",
)

# Include settings:
include(*_base_settings)