"""
Django settings for upload_file_manager project.

Generated by 'django-admin startproject' using Django 4.2.7.

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
SECRET_KEY = 'django-insecure-l!@3%l$p-gej0$d0d(n=7t9y5md3z=v^mroqck^e^3dcfqffya'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
ALLOWED_HOSTS = []

# DEBUG = False
# ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    # 'background_task',
    
    'apps.accounting.apps.AccountingConfig',
    'apps.main_app.apps.MainAppConfig',
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

ROOT_URLCONF = 'upload_file_manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.main_app.views.worldwide_action',
                # 'apps.main_app.views.display_name',
            ],
        },
    },
]


WSGI_APPLICATION = 'upload_file_manager.wsgi.application'



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'upload_file_manager',
        'USER': 'root',
        'PASSWORD': 'Soheil0014',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}



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

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=(os.path.join(BASE_DIR, 'static/'),)

MEDIA_URL = '/media/'
MEDIA_ROOT= os.path.join(BASE_DIR, 'media/')



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'accounting.CustomUser'


SESSION_COOKIE_AGE = 43200  # 1 day
# SESSION_COOKIE_AGE = 1296000 # 30 days


# LOGIN_REDIRECT_URL = "home"
# LOGOUT_REDIRECT_URL = "home"


REST_FRAMEWORK = {
	# 'DEFAULT_AUTHENTICATION_CLASSES': [
	# 	            'rest_framework.authentication.TokenAuthentication',
    #               'rest_framework.authentication.SessionAuthentication',
	# ],
 
    # 'DEFAULT_PERMISSION_CLASSES': [
    #                 'rest_framework.permissions.IsAuthenticated',
    # ],
    
	'DEFAULT_PAGINATION_CLASS': 
		            'rest_framework.pagination.PageNumberPagination',
	                'PAGE_SIZE': 5,
                 
	'DEFAULT_FILTER_BACKENDS': [
					'django_filters.rest_framework.DjangoFilterBackend',
					'rest_framework.filters.SearchFilter',
					'rest_framework.filters.OrderingFilter',
     ],
			
}



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

