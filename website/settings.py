"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 1.10.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'SET IN LOCAL SETTINGS'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['voluntarios.com.br']

# E-mail configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'SET IN LOCAL SETTINGS'
EMAIL_HOST_USER = 'SET IN LOCAL SETTINGS'
EMAIL_HOST_PASSWORD = 'SET IN LOCAL SETTINGS'
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'SET IN LOCAL SETTINGS'
SERVER_EMAIL = 'SET IN LOCAL SETTINGS'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.gis',
    'django.contrib.postgres',
    'mptt',           # para representações hierárquicas no banco
    # 'bootstrapform',  # para renderizar formulários compatíveis com bootstrap
    'crispy_forms',  # para renderizar formulários (substituto do bootstrap_forms)
    'allauth',               #
    'allauth.account',       # para gerenciar autenticação
    'allauth.socialaccount', #
    'allauth.socialaccount.providers.facebook',  # login via Facebook
    'allauth.socialaccount.providers.google',    # login via Google
    'website.apps.MyFlatPagesConfig', # para customizar páginas planas
    'tinymce',       # para poder visualizar e gravar html em campos texto
    'notification',  # para encapsular notificações por e-mail
    'vol',           # app principal
    'trans',         # para sobrepor traduções de outros apps
    # 'debug_toolbar',
    # 'django_extensions', # para gerar diagramas dos modelos
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/vol')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'vol.context_processors.general',
            ],
        },
    },
]

CRISPY_TEMPLATE_PACK = 'bootstrap3'  # Precisa ser alterado quando atualizar a versão do Bootstrap

WSGI_APPLICATION = 'website.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'SET IN LOCAL SETTINGS',
    }
}

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Custom user model
AUTH_USER_MODEL = 'vol.Usuario'

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

LOGIN_URL = '/aut/login'
LOGIN_REDIRECT_URL = '/redirlogin'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGES = [
    ('pt-BR', u'Português'),
]

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = 'SET IN LOCAL SETTINGS'

STATIC_URL = '/static/'

MEDIA_ROOT = 'SET IN LOCAL SETTINGS'

MEDIA_URL = '/media/'

CSRF_FAILURE_VIEW = 'vol.views.csrf_failure'

# Sites app
SITE_ID = 1

# Django admin interface prefix
MY_ADMIN_PREFIX = 'SET IN LOCAL SETTINGS'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
         'require_debug_false': {
             '()': 'django.utils.log.RequireDebugFalse'
         }
    },
    'handlers': {
       #'file': {
       #     'level': 'ERROR',
       #     'class': 'logging.FileHandler',
       #     'filename': 'LOGFILE_PATH',
       # },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        #'django': {
        #    'handlers': ['file'],
        #    'level': 'ERROR',
        #    'propagate': True,
        #},
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Cache (SET IN LOCAL SETTINGS)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# TinyMCE configuration
TINYMCE_DEFAULT_CONFIG = {
    'plugins': 'table,paste,code',
    'theme': 'silver',
    'toolbar': 'undo redo styleselect bold italic alignleft aligncenter alignright bullist numlist outdent indent code',
    'custom_undo_redo_levels': 10,
    'convert_urls': False,
    'resize': 'both',
    'theme_advanced_resizing': True,
}

# Django allauth config
ACCOUNT_ADAPTER = 'vol.auth.MyAccountAdapter'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 10
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_SUBJECT_PREFIX = '\o/ '
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/anonconf'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/redirlogin'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL = '/aut/login'
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_FORM_CLASS = 'vol.forms.ExtendedSignupForm'
SOCIALACCOUNT_ENABLED = True
SOCIALACCOUNT_ADAPTER = 'vol.auth.MySocialAccountAdapter'
# Sempre redireciona para página de cadastro para que o usuário aceite os termos de uso
SOCIALACCOUNT_AUTO_SIGNUP = False
SOCIALACCOUNT_EMAIL_REQUIRED = True

# Google maps API
GOOGLE_MAPS_API_KEY = 'SET IN LOCAL SETTINGS'
GOOGLE_MAPS_GEOCODE_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

# Notification settings
SUPPORT_NOTIFICATION_ENABLED = True
SUBJECT_PREFIX = '[Voluntarios] '
NOTIFY_SUPPORT_FROM = 'SET IN LOCAL SETTINGS'
NOTIFY_SUPPORT_TO = 'SET IN LOCAL SETTINGS'
NOTIFY_USER_FROM = 'SET IN LOCAL SETTINGS'
NOTIFY_CSRF_ERROR = True

CONTACT_EMAIL = 'SET IN LOCAL SETTINGS'

# Configurações do serviço de recepção de entidades
ONBOARDING_EMAIL_FROM = 'SET IN LOCAL SETTINGS' # remetente das mensagens de boas vindas
ONBOARDING_IMAP_SERVER = 'SET IN LOCAL SETTINGS' # servidor IMAP para verificar caixa postal
ONBOARDING_EMAIL_HOST_USER = 'SET IN LOCAL SETTINGS' # usuário da caixa postal de envio (smtp)
ONBOARDING_EMAIL_HOST_PASSWORD = 'SET IN LOCAL SETTINGS' # senha da caixa postal de envio (smtp)
ONBOARDING_MAX_DAYS_WAITING_RESPONSE = 60 # número de dias em que se aguarda uma resposta da entidade
ONBOARDING_NOTIFY_RESPONSE_ARRIVAL = 'SET IN LOCAL SETTINGS' # endereço de email a ser notificado quando chega uma resposta
ONBOARDING_TEAM_EMAIL = 'SET IN LOCAL SETTINGS' # endereço(s) de email da(s) pessoa(s) do time de boas-vindas (separados por vírgula)

GDAL_LIBRARY_PATH = r'C:\OSGeo4W\bin\gdal306.dll'
GEOS_LIBRARY_PATH = r'C:\Program Files\PostgreSQL\15\bin\libgeos_c.dll'

##############################################################

# Sobrepõe configurações com configurações locais - caso existam
try:
    from .local_settings import *
except ImportError:
    try:
        from local_settings import *
    except ImportError:
        pass
