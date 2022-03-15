"""
This is a django-split-settings main file.
"""

from split_settings.tools import include


_base_settings = (
    "components/apps.py",
    "components/commons.py",
    "components/middlewares.py",
    "components/logging.py",
    "components/csp.py",
    "components/caches.py",
    "components/storage.py",
)

# Include settings:
include(*_base_settings)
