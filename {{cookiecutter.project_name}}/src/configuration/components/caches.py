# Caching

CACHES = {
    "default": {
        # Todo add Redis cache backend
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    },
}
