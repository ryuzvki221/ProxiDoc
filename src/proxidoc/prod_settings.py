from .settings import *
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c*6zjk#s&!&$s-!djeycl772hbs4%m8js2$u&n$h9y&nsk&e(o'

# debug turned off in production!
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['proxidoc.herokuapp.com']
# Database production settings
DATABASES['default'] = dj_database_url.config()

# Application definition
MIDDLEWARE += [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

