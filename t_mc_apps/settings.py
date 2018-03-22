"""
Django settings for t_mc_apps project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6=dy&^9bc85^lwyhi=2lm&#gqa@_*0n^-sl@2ao3ap5*5f99*)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INTERNAL_IPS = ['127.0.0.1']
ENVIRONMENT = 'dev'

ALLOWED_HOSTS = [
    'crm.t-mc.nl',
    'localhost',
    '127.0.0.1',
    '192.168.1.18',
    'django-test-host',
]


# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    # 'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_propeller',
    # 'bootstrap3',
    'bootstrapform',
    # 'crispy_forms',
    'phonenumber_field',
    'django_admin_listfilter_dropdown',
    # 'debug_toolbar',
    # T-MC Apps
    'base',
    'crm',
    'projecten',
    'producten',
    'notities',
    # 'pcoverzicht',
    # 'support',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 't_mc_apps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 't_mc_apps/templates')),
            os.path.join(BASE_DIR, 'support/templates'),
            os.path.join(BASE_DIR, 'pcoverzicht/templates'),
            os.path.join(BASE_DIR, 'crm/templates'),
            os.path.join(BASE_DIR, 'projecten/templates')]
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

WSGI_APPLICATION = 't_mc_apps.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 't_mc_crm',
        'USER': 't_mc_crm',
        'PASSWORD': 'Hard24Get',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'nl-nl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# STATICFILES_DIRS = [STATIC_DIR, ]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


CRISPY_TEMPLATE_PACK = 'bootstrap4'

PROPELLER = {

    # # The URL to the jQuery JavaScript file
    # 'jquery_url': '//code.jquery.com/jquery.min.js',

    # # The Bootstrap base URL
    # 'base_url': '//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/',

    # # The complete URL to the Bootstrap CSS file (None means derive it from base_url)
    # 'css_url': None,

    # # The complete URL to the Bootstrap CSS file (None means no theme)
    # 'theme_url': '/static/css/lavish-bootstrap.css',

    # # The complete URL to the Bootstrap JavaScript file (None means derive it from base_url)
    # 'javascript_url': None,

    # # Put JavaScript in the HEAD section of the HTML document (only relevant if you use propeller.html)
    # 'javascript_in_head': False,

    # # Include jQuery with Bootstrap JavaScript (affects django-propeller template tags)
    # 'include_jquery': False,

    # # Label class to use in horizontal forms
    'horizontal_label_class': 'col-md-2',

    # # Field class to use in horizontal forms
    'horizontal_field_class': 'col-md-10',

    # # Set HTML required attribute on required fields, for Django <= 1.8 only
    # 'set_required': True,

    # # Set HTML disabled attribute on disabled fields, for Django <= 1.8 only
    # 'set_disabled': False,

    # # Set placeholder attributes to label if no placeholder is provided
    # 'set_placeholder': True,

    # # Class to indicate required (better to set this in your Django form)
    # 'required_css_class': '',

    # # Class to indicate error (better to set this in your Django form)
    # 'error_css_class': 'has-error',

    # # Class to indicate success, meaning the field has valid input (better to set this in your Django form)
    # 'success_css_class': 'has-success',

    # # Renderers (only set these if you have studied the source and understand the inner workings)
    # 'formset_renderers':{
    #     'default': 'propeller.renderers.FormsetRenderer',
    # },
    # 'form_renderers': {
    #     'default': 'propeller.renderers.FormRenderer',
    # },
    # 'field_renderers': {
    #     'default': 'propeller.renderers.FieldRenderer',
    #     'inline': 'propeller.renderers.InlineFieldRenderer',
    # },
}

# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'T-MC Apps',
    'HEADER_DATE_FORMAT': 'l, j F Y',
    'HEADER_TIME_FORMAT': 'G:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
       'sites': 'icon-leaf',
       'auth': 'icon-lock',
    },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    # 'MENU': (
    #     'sites',
    #     {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
    #     {'app': 'crm', 'label': 'CRM', 'icon':'icon-user', 'models': ('bedrijf', 'contactpersoon')},
    #     {'app': 'projecten', 'label': 'Projecten', 'icon':'icon-coins', 'models': ('verkoopkans', 'order', 'verkoopstadium', 'orderstadium')},
    # #     {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     {'projecten': 'Projectadministratie', 'icon':'icon-cog', 'url': '/projecten/'},
    # ),

    # misc
    'LIST_PER_PAGE': 15
}
