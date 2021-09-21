from decouple import config

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

if config("DJANGO_USE_S3", cast=bool, default=False):
    # aws settings
    AWS_ACCESS_KEY_ID = config("DJANGO_S3_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = config("DJANGO_S3_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = config("DJANGO_S3_BUCKET_NAME")
    GS_BUCKET_NAME = config("DJANGO_S3_BUCKET_NAME")
    AWS_REGION = config("DJANGO_AWS_REGION", "eu-central-1")
    AWS_DEFAULT_ACL = config("DJANGO_S3_DEFAULT_ACL", default=None)
    AWS_S3_ENDPOINT_URL = config("DJANGO_S3_ENDPOINT_URL")
    AWS_S3_CUSTOM_DOMAIN = f"{config('AWS_S3_CUSTOM_DOMAIN', False)}/{AWS_STORAGE_BUCKET_NAME}"
    AWS_S3_USE_SSL = config("DJANGO_S3_USE_SSL", cast=bool, default=False)
    AWS_S3_SECURE_URLS = config("DJANGO_S3_SECURE_URLS", cast=bool, default=False)
    # s3 static settings
    DEFAULT_FILE_STORAGE = config("DEFAULT_FILE_STORAGE")
    STATIC_LOCATION = config("DJANGO_S3_STATIC_LOCATION", "static")
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/"
    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = config("DJANGO_S3_MEDIA_LOCATION", "media")
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/"
else:
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/

    STATIC_URL = config("DJANGO_STATIC_URL", default="/static/")
    STATIC_ROOT = config("DJANGO_STATIC_ROOT", default="/var/django/static")

    # Media files
    # Media root dir is commonly changed in production
    # (see development.py and production.py).
    # https://docs.djangoproject.com/en/2.2/topics/files/

    MEDIA_URL = config("DJANGO_MEDIA_URL", default="/media/")
    MEDIA_ROOT = config("DJANGO_MEDIA_ROOT", default="/var/django/media")
