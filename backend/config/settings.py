"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Log File Path
log_path = os.path.join(os.path.dirname(__file__), '../logs')
os.makedirs(log_path, exist_ok=True)
LOG_FILE = os.path.join(log_path, 'backend.log')

# .env load
env = environ.Env(DEBUG=(bool, False))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
CSRF_COOKIE_SAMESITE = 'Strict'
SESSION_COOKIE_SAMESITE = 'Strict'
CSRF_COOKIE_HTTPONLY = True  # False since we will grab it via universal-cookies
SESSION_COOKIE_HTTPONLY = True

DEBUG = env('DJANGO_DEBUG')
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')
CORS_ALLOWED_ORIGINS = env.list("ALLOWED_ORIGINS")
CSRF_TRUSTED_ORIGINS = env.list("ALLOWED_ORIGINS")

# Application definition
INSTALLED_APPS = [
	"django.contrib.admin",
	"django.contrib.auth",
	"django.contrib.contenttypes",
	"django.contrib.sessions",
	"django.contrib.messages",
	"django.contrib.staticfiles",
	"corsheaders",
	"rest_framework",
	"django_apscheduler",
	"apps.core",
	"apps.users",
	"apps.announcement",
	"apps.archive",
	"apps.report"
]

MIDDLEWARE = [
	'corsheaders.middleware.CorsMiddleware',
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

# DRF settings
REST_FRAMEWORK = {
	'DEFAULT_RENDERER_CLASSES': [
		'rest_framework.renderers.JSONRenderer',
		'rest_framework.renderers.BrowsableAPIRenderer',
	],
	'DEFAULT_PARSER_CLASSES': [
		'rest_framework.parsers.JSONParser',
	]
}

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': env('POSTGRES_DB'),
		'USER': env('POSTGRES_USER'),
		'PASSWORD': env('POSTGRES_PASSWORD'),
		'HOST': env('POSTGRES_HOST'),
		'PORT': env('POSTGRES_PORT'),
	}
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Use custom Auth User model
# AUTH_USER_MODEL = 'settingapp.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# file setting
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_PUBLIC_ROOT = os.path.join(MEDIA_ROOT, 'public')
MEDIA_PRIVATE_ROOT = os.path.join(MEDIA_ROOT, 'private')

LOGGING = {
	'version': 1,
	'disable_existing_loggers': True, # db debug False
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse',
		},
		'require_debug_true': {
			'()': 'django.utils.log.RequireDebugTrue',
		},
	},
	'formatters': {
		'django.server': {
			'()': 'django.utils.log.ServerFormatter',
			'format': '[{server_time}] {message}',
			'style' : '{',
			
		},
		'standard': {
			'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
		}
	},
	'handlers': {
		# 'console': { # db debug
		# 	'level': 'DEBUG',
		# 	'filters': ['require_debug_true'],
		# 	'class': 'logging.StreamHandler',
		# 	'formatter': 'standard',
		# },
		'console': {
			'level': 'INFO',
			'filters': ['require_debug_true'],
			'class': 'logging.StreamHandler',
			'formatter': 'standard',
		},
		'django.server': {
			'level': 'INFO',
			'class': 'logging.StreamHandler',
			'formatter': 'django.server',
		},
		'file': {
			'level': 'DEBUG',
			'filters': ['require_debug_false'],
			'class': 'logging.handlers.TimedRotatingFileHandler',
			'filename': LOG_FILE,
			'when': "midnight",	# 매 자정마다
			'backupCount': 100,
			'formatter': 'standard',
		}
	},
	'root': {
		'handlers': ['console'],
		'level': 'INFO',
	},
	'loggers': {
		'django': {
			'handlers': ['console', 'file'],
			'level': 'INFO',
		},
		'django.db.backends': { # db debug
			'handlers': ['console', 'file'],
			'level': 'DEBUG',
			'propagate': False
		},
	}
}
