
# Add this below import os in the top of the settings file
import django_heroku


# Add below in Installed apps list
INSTALLED_APPS = [
    'crispy_forms',
    'widget_tweaks',
]

# Add below in templates list
'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],


# Settings for static files, media and other stuff

django_heroku.settings(locals())


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# STATIC_ROOT = 'static'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGOUT_REDIRECT_URL = 'home'
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
