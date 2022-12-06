"""
Django settings for Ecommerce project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)on(_yvt5%)^m=z!#tez+0&w=cto!yh$to%rk3gv2(jsk$a=4r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'product',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Ecommerce.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'static'

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

PIC_UP_PATH = 'pics/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# djangostripe/settings.py
# STRIPE_PUBLISHABLE_KEY = 'pk_test_51M9lXNAu20KPGQVKirUJ5qAntdAmiZfCLzt4ivVwkJHsguaEKJ0Og87y1ZsYVR8IP5Qa1EzVwEz2lmIWGySiqnvz00AByzAiTR'
# STRIPE_SECRET_KEY = 'sk_test_51M9lXNAu20KPGQVK493YE8SBmAmgv2uCGgWjkkth7puILci4xKYj8jw4h7QlKAjgBZuuUI5NSLsZT1AIF1xSGPQP00jfZx93u3'
# STRIPE_TEST_PUBLIC_KEY = os.environ.get("STRIPE_TEST_PUBLIC_KEY", "pk_test_51M9lXNAu20KPGQVKirUJ5qAntdAmiZfCLzt4ivVwkJHsguaEKJ0Og87y1ZsYVR8IP5Qa1EzVwEz2lmIWGySiqnvz00AByzAiTR")
# STRIPE_TEST_SECRET_KEY = os.environ.get("STRIPE_TEST_SECRET_KEY", "sk_test_51M9lXNAu20KPGQVK493YE8SBmAmgv2uCGgWjkkth7puILci4xKYj8jw4h7QlKAjgBZuuUI5NSLsZT1AIF1xSGPQP00jfZx93u3")
# STRIPE_LIVE_MODE = False


STRIPE_PUBLISHABLE_KEY = 'pk_test_51M9lXNAu20KPGQVKirUJ5qAntdAmiZfCLzt4ivVwkJHsguaEKJ0Og87y1ZsYVR8IP5Qa1EzVwEz2lmIWGySiqnvz00AByzAiTR'
STRIPE_SECRET_KEY = 'sk_test_51M9lXNAu20KPGQVK493YE8SBmAmgv2uCGgWjkkth7puILci4xKYj8jw4h7QlKAjgBZuuUI5NSLsZT1AIF1xSGPQP00jfZx93u3'

