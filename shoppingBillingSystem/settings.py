"""
Django settings for shoppingBillingSystem project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gylek4&$v=wsu$673nd8-rxe3-o63iba^b32%d&vivknrgm5*f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'shoppingbillingsystem-92a472164483.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'drf_spectacular',
    'rest_framework',
    'billingSystem',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shoppingBillingSystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'shoppingBillingSystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Postgres database link got from Heroku
# It structure is
# postgres://<username>:<password>@<host>:<port>/<database name>
# postgres://ufgdrtdhgu5ko2:p82fb18d4e7e76af002dac430dfe0d1c2ec1a910f82eabdd8522a0d6be1cb6093@c7gljno857ucsl.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d3aom2490s967b

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd3aom2490s967b',
        'USER': 'ufgdrtdhgu5ko2',
        'PASSWORD': 'p82fb18d4e7e76af002dac430dfe0d1c2ec1a910f82eabdd8522a0d6be1cb6093',
        'HOST': 'c7gljno857ucsl.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com',  # or another host if your db is not local
        'PORT': '5432',  # default PostgreSQL port
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# drf-spectacular settings
SPECTACULAR_SETTINGS = {
    'TITLE': 'Shopping Mall Billing System API',
    'DESCRIPTION': 'Backend API for managing a small-scale shopping mall billing system. '
                   'It supports operations on products, customers, and bills, allowing for '
                   'employee authentication, product management, customer management, and '
                   'generation of bills for cash payments.',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,  # Optionally exclude the raw schema from the rendered documentation
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'persistAuthorization': True,
    },
    # 'SWAGGER_UI_FAVICON_HREF': 'your_favicon_url',
    'CONTACT': {
        'name': 'Kiran Kasana project',
        'url': 'https://www.<No Url>.com',
        'email': 'kkasanacoder@ygmail.com',
    },
    'LICENSE': {
        'name': 'MIT',
        'url': 'https://opensource.org/licenses/MIT',
    },
    'TAGS': [
        {'name': 'Products', 'description': 'Operations with products'},
        {'name': 'Customers', 'description': 'Operations with customers'},
        {'name': 'Bills', 'description': 'Creating and managing bills'},
        {'name': 'Authentication', 'description': 'User authentication and authorization'},
    ],
    # Additional settings can be added as needed
}
