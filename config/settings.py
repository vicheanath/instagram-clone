
import os
import ast
from pathlib import Path
from datetime import timedelta
from typing import Optional
from django.core.validators import URLValidator


def get_list(text):
    return [item.strip() for item in text.split(",")]


def get_bool_from_env(name, default_value):
    if name in os.environ:
        value = os.environ[name]
        try:
            return ast.literal_eval(value)
        except ValueError as e:
            raise ValueError(f"{value} is an invalid value for {name}") from e
    return default_value


def get_url_from_env(name, *, schemes=None) -> Optional[str]:
    if name in os.environ:
        value = os.environ[name]
        message = f"{value} is an invalid value for {name}"
        URLValidator(schemes=schemes, message=message)(value)
        return value
    return None

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    "django-insecure-$227hjjmuq2e!)o^@2&#2v#+(-=@$v362o@8g#s9!2)tjn1)1a"
)
DEBUG = get_bool_from_env("DEBUG", True)

ALLOWED_HOSTS = []
ALLOWED_HOSTS.extend(get_list(os.environ.get("ALLOWED_HOSTS", "")))

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # internal apps
    "apps.core",
    "apps.users",
    "apps.posts",
    "apps.comments",
    "apps.interactions",
    "apps.medias",
    "apps.notifications",
    # external apps
    "debug_toolbar",
    "graphene_django",
    "graphql_jwt.refresh_token.apps.RefreshTokenConfig",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

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

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / "media"
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DEBUG = True

AUTH_USER_MODEL = "users.User"

GRAPHENE = {
    "SCHEMA": "apps.graphql.api.schema",
    "MIDDLEWARE": [
        "graphql_jwt.middleware.JSONWebTokenMiddleware",
    ],
}
GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_EXPIRATION_DELTA": timedelta(minutes=5),
    "JWT_REFRESH_EXPIRATION_DELTA": timedelta(days=7),
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
}

AUTHENTICATION_BACKENDS = [
    "graphql_jwt.backends.JSONWebTokenBackend",
    "django.contrib.auth.backends.ModelBackend",
]
