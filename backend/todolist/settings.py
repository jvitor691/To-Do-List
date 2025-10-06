"""
Django settings for todolist project (DATABASE_URL sem dj-database-url).
"""
from pathlib import Path
from decouple import config
from urllib.parse import urlparse
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# --- Básico ---
SECRET_KEY = config("SECRET_KEY", default="django-insecure-change-me-in-production")
DEBUG = config("DEBUG", default=True, cast=bool)
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# --- Parse DATABASE_URL manualmente ---
_raw = config("DATABASE_URL", default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}")

# suporta formato SQLAlchemy "postgresql+psycopg://"
if _raw.startswith("postgresql+psycopg://"):
    _raw = _raw.replace("postgresql+psycopg://", "postgresql://", 1)

url = urlparse(_raw)

if url.scheme.startswith("postgres"):
    ENGINE = "django.db.backends.postgresql"
    NAME = url.path.lstrip("/") or "postgres"
    USER = url.username or ""
    PASSWORD = url.password or ""
    HOST = url.hostname or "127.0.0.1"
    PORT = str(url.port or "5432")
    DATABASES = {
        "default": {
            "ENGINE": ENGINE,
            "NAME": NAME,
            "USER": USER,
            "PASSWORD": PASSWORD,
            "HOST": HOST,
            "PORT": PORT,
        }
    }
elif url.scheme.startswith("sqlite"):
    # Suporta sqlite:///caminho/para/db.sqlite3
    # ou sqlite:///<abs_path>
    SQLITE_NAME = _raw.replace("sqlite:///", "")
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": SQLITE_NAME,
        }
    }
else:
    raise RuntimeError(f"DATABASE_URL com esquema não suportado: {url.scheme}")

# --- Apps ---
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd
    "rest_framework",
    "corsheaders",
    # local
    "tasks",
]

# --- Middleware ---
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "todolist.urls"

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

WSGI_APPLICATION = "todolist.wsgi.application"

# --- I18N / TZ ---
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Fortaleza"
USE_I18N = True
USE_TZ = True

# --- Static ---
STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- DRF ---
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
}

# --- CORS ---
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]
CORS_ALLOW_CREDENTIALS = True

# --- Evita redireciono que quebra POST /tasks sem barra final ---
APPEND_SLASH = False
