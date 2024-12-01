"""
Django settings for Resee project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
import json
from django.core.exceptions import ImproperlyConfigured

from pathlib import Path
from datetime import timedelta

# 비밀 값 로드 함수
def get_secret(setting, secrets_file='.secrets.json'):
    """비밀 설정 값을 가져오거나 오류를 발생시킵니다."""
    try:
        with open(os.path.join(BASE_DIR, secrets_file)) as f:
            secrets = json.loads(f.read())
        return secrets[setting]
    except FileNotFoundError:
        raise ImproperlyConfigured(f"{secrets_file} 파일을 찾을 수 없습니다.")
    except KeyError:
        raise ImproperlyConfigured(f"{setting} 설정을 {secrets_file}에 추가해주세요.")


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =  get_secret('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 기본 앱들
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 생성한 앱들
    'custom_user',
    'book',
    'pots',
    # CORS
    'corsheaders',

    # Django REST Framework
    'django.contrib.sites',  # django-allauth를 위해 필요

    # 서드파티 앱들
    'rest_framework',
    'rest_framework.authtoken',  # dj-rest-auth를 위해 필요
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'rest_framework_simplejwt',  # JWT 인증 지원
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 가장 위에 추가
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'Resee.urls'

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

WSGI_APPLICATION = 'Resee.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# RESTAPI
SITE_ID = 1
AUTH_USER_MODEL = 'custom_user.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',  # 세션 인증
        'rest_framework.authentication.BasicAuthentication',
    ],
}

REST_USE_JWT = False  # JWT 대신 세션 기반 사용
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # 이메일로 로그인
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False  # 사용자명 비활성화


# CORS
# 모든 도메인 허용
CORS_ALLOW_ALL_ORIGINS = True

# 특정 도메인만 허용 (더 안전한 옵션)
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]