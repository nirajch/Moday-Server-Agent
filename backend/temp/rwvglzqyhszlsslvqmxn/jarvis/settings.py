# -*- coding: utf-8 -*-
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5v)#089q5$+tampfwaxxixy%cw2*oz#-o1$n9vy8#aq@j!z%^u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [

	'django.contrib.contenttypes',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django_extensions',
	'rest_framework',
	'corsheaders',
	'django_archive',
	'common',
	'users',
	'polls',
]

MIDDLEWARE = [

	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jarvis.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'jarvis.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {

	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join('./main.db'),
	}
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# CORS

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = (

	'GET',
	'POST',
	'PATCH',
	'DELETE',
	'OPTIONS',
)

CORS_ALLOW_HEADERS = (

	'accept',
	'accept-encoding',
	'authorization',
	'content-type',
	'dnt',
	'origin',
	'user-agent',
	'x-csrftoken',
	'x-requested-with',
	'accesstoken',
	'request-from-type',
	'app-name'
)

ARCHIVE_FILENAME = 'Backup'

REST_FRAMEWORK = {

	'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
	'UNAUTHENTICATED_USER': None
}

ARCHIVE_EXCLUDE = ()

	