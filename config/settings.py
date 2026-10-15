"""
Django settings for SatVex project.
Production and Local deployment configuration.
"""

from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

# ========================
# BASE DIR & ENV LOADING
# ========================

BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env if present
load_dotenv(BASE_DIR / ".env")

# ========================
# SECURITY & SECRETS
# ========================

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-dev-key-change-in-production-satvex-2026"
)

DEBUG = os.environ.get("DEBUG", "False").lower() in ("true", "1", "t", "yes")

# Allowed Hosts
# In production, specify: satvex.deepaksinghdev.in, .onrender.com, etc.
raw_allowed_hosts = os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1,satvex.deepaksinghdev.in,satvex-api.deepaksinghdev.in,.onrender.com")
ALLOWED_HOSTS = [h.strip() for h in raw_allowed_hosts.split(",") if h.strip()]

# CSRF Trusted Origins
raw_csrf_origins = os.environ.get(
    "CSRF_TRUSTED_ORIGINS",
    "https://satvex.deepaksinghdev.in,https://satvex-api.deepaksinghdev.in,https://*.onrender.com"
)
CSRF_TRUSTED_ORIGINS = [o.strip() for o in raw_csrf_origins.split(",") if o.strip()]

# Reverse Proxy / HTTPS detection (Render terminates SSL at edge)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = "DENY"
else:
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False

# CORS & CSRF Origins for Vercel Frontend
raw_cors_origins = os.environ.get(
    "CORS_ALLOWED_ORIGINS",
    "https://satvex.deepaksinghdev.in"
)
CORS_ALLOWED_ORIGINS = [o.strip() for o in raw_cors_origins.split(",") if o.strip()]
CORS_ALLOW_CREDENTIALS = True

# External N2YO API Key
N2YO_API_KEY = os.environ.get("N2YO_API_KEY", "M8PZCZ-5ELM7M-DE5LRK-531A")

# ========================
# APPLICATION DEFINITION
# ========================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "corsheaders",

    # Local apps
    "satTrack",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
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
        "DIRS": [BASE_DIR / "templates"],
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

# ========================
# DATABASE
# ========================

database_url = os.environ.get("DATABASE_URL")
if database_url:
    DATABASES = {
        "default": dj_database_url.config(
            default=database_url,
            conn_max_age=600,
            conn_health_checks=True
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# ========================
# PASSWORD VALIDATION
# ========================

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ========================
# INTERNATIONALIZATION
# ========================

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ========================
# STATIC & MEDIA FILES
# ========================

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# WhiteNoise storage for compressed and cached static files
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ========================
# DEFAULT PRIMARY KEY
# ========================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

