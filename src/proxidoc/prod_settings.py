from .settings import *
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# debug turned off in production!
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['proxidoc.herokuapp.com']
# Application definition
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Database production settings
DATABASES['default'] = dj_database_url.config()
