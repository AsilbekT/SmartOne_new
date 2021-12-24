"""
Django settings for SmartOne project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _
import pymysql
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+5wu_@&jm3n(5(13)e8!q((3v3(!yh_w*5@42ar)bt*10hz@6n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products.apps.ProductsConfig',
    'contact.apps.ContactConfig',
    'store.apps.StoreConfig',
    'statistics_page.apps.StatisticsPageConfig',
    'payments',
    'clickuz',
    'PaycomUz',
    'rest_framework'
]

CLICK_SETTINGS = {
    'service_id': 19552,
    'merchant_id': 14057,
    'secret_key': "VJQxhIV6fO",

}

PAYCOM_SETTINGS = {
    "HOST": "https://checkout.test.paycom.uz/api",
    "ID": "61c051b10dd0408a5b235b18",
    "SECRET_KEY": "n5U#8s6Rn4BKiXzjZCp2@D9%65yzKTNoN5As",
    "PATH_CLASS": "store.views",
    "ACCOUNTS": {
        "KEY1": "order_id",
        "KEY2": None
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
PAYMENT_HOST = '<your_ip_address>:<your_port>'
PAYMENT_USES_SSL = False  # set the True value if you are using the SSL
PAYMENT_MODEL = '<your_payment_model>'
# payment model format like this :: '<app_name>.<model_name>'
PAYMENT_VARIANTS = {
    'click': ('click.ClickProvider', {
        'merchant_id': 1111,
        'merchant_service_id': 11111,
        'merchant_user_id': 11111,
        'secret_key': 'AAAAAA'
    })
}

ROOT_URLCONF = 'SmartOne.urls'

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

WSGI_APPLICATION = 'SmartOne.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/


LANGUAGE_CODE = 'ru'

LANGUAGES = (
    ('ru', _('Russian')),
    ('uz', _('Uzbek')),
    ('en', _('English')),

)

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = '/'
