import os
import environ
import dj_database_url
from pathlib import Path
from django.contrib.messages import constants as messages

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Environ setup
env = environ.Env()
env.read_env(BASE_DIR / ".env")

# Core Security Settings
SECRET_KEY = env("SECRET_KEY", default="fallback-secret-key-for-dev")
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8080",
    "http://192.168.0.107:8080",
    "http://0.0.0.0:8080",
    "https://*.vercel.app",
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Application definition
INSTALLED_APPS = [
    'cloudinary_storage',          # staticfiles-এর আগে থাকবে
    'django.contrib.staticfiles',
    'cloudinary',                  # staticfiles-এর পরে থাকবে
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.### ১. `settings.py` ফাইলের সংশোধিত কোড

আপনার ফাইলটি মোটের উপর ঠিকই আছে, তবে উৎপাদন পরিবেশ (Production/Vercel) এবং নিরাপত্তা বজায় রাখার জন্য কিছু গুরুত্বপূর্ণ জায়গায় সংশোধন প্রয়োজন:

1. **`ALLOWED_HOSTS` & `DEBUG`:** `DEBUG = True` থাকলে কোনো সমস্যা নেই, তবে প্রোডাকশনে `ALLOWED_HOSTS = ['*']` ব্যবহার করা ঝুঁকিপূর্ণ।
2. **`DATABASE_URL` চেক:** `env.db()` ব্যবহার করলে কোড আরও পরিষ্কার হয় এবং `env()` পার্সিং সঠিকভাবে কাজ করে।
3. **`staticfiles_build` সানিটাইজেশন:** WhiteNoise এবং Cloudinary ব্যবহারের ক্ষেত্রে স্ট্যাটিক ফাইলের কনফিগারেশন আরও নিখুঁত করা হয়েছে।

নিচে আপডেট করা `settings.py` কোড দেওয়া হলো:

```python
import os
import environ
import dj_database_url
from pathlib import Path
from django.contrib.messages import constants as messages

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Environ setup
env = environ.Env()
env.read_env(BASE_DIR / ".env")

# Core Security Settings
SECRET_KEY = env("SECRET_KEY", default="fallback-secret-key-for-dev")
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8080",
    "[http://192.168.0.107:8080](http://192.168.0.107:8080)",
    "[http://0.0.0.0:8080](http://0.0.0.0:8080)",
    "https://*.vercel.app",
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Application definition
INSTALLED_APPS = [
    'cloudinary_storage',          # staticfiles-এর আগে থাকবে
    'django.contrib.staticfiles',
    'cloudinary',                  # staticfiles-এর পরে থাকবে
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Static files serving
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Portfolio.wsgi.application'


# Database Configuration
if env("DATABASE_URL", default=None):
    DATABASES = {
        'default': dj_database_url.config(
            default=env("DATABASE_URL"),
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static & Media Files Configuration
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles_build'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
] if (BASE_DIR / 'static').exists() else []

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Cloudinary Setup
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUD_NAME', default=''),
    'API_KEY': env('CLOUD_API_KEY', default=''),
    'API_SECRET': env('CLOUD_API_SECRET', default=''),
}

# Unified Storage Configuration (Django 4.2+)
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# WhiteNoise Configuration
WHITENOISE_MANIFEST_STRICT = False

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Message Tags
MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'error',
}


# Email Backend Configuration
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="smtp.gmail.com")
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")