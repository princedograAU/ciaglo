import os
from pathlib import Path

from decouple import config
from dj_database_url import parse as db_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG")

ALLOWED_HOSTS = []

LOCAL_APPS = [
    "common.apps.CommonConfig",
    "utils.apps.UtilsConfig",
    "agency.apps.AgencyConfig",
    "listing.apps.ListingConfig",
    "gql.apps.GqlConfig",
]

THIRD_PARTY_APPS = [
    "django_extensions",
    "rest_framework",
    "drf_spectacular",
    "graphene_django",
    "phonenumber_field",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ciaglo.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ciaglo.wsgi.application"

# Database
DATABASES = {
    "default": config("DATABASE_URL", cast=db_url),
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# REST FRAMEWORK
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# drf-spectacular
SPECTACULAR_SETTINGS = {
    "TITLE": "CIAGLO API",
    "DESCRIPTION": "CIAGLO: Your Home, Your Future, Simplified",
    "VERSION": "0.1.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

# debug-toolbar
# DEBUG_TOOLBAR_ENABLED = config("DEBUG_TOOLBAR_ENABLED")
# if DEBUG_TOOLBAR_ENABLED:
#     # Configure Internal IPs
#     # allow from docker networks
#     ip = socket.gethostbyname(socket.gethostname())
#     INTERNAL_IPS = [ip[:-1] + "1"]

#     MIDDLEWARE.append(
#         "debug_toolbar.middleware.DebugToolbarMiddleware",
#     )
#     INSTALLED_APPS.append(
#         "debug_toolbar",
#     )

GRAPHENE = {"SCHEMA": "gql.schema.schema", "SCHEMA_OUTPUT": "gql/base.graphql"}

# Internationalization
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
