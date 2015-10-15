"""
Django settings for HTScraping project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')^-=8-$+9es9)g84+f&q^qel&$*1ojf1g!=*+a!bo%&+1c!z^6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'API'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_DIRS = (
    BASE_DIR + '/API/templates/',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.getcwd() + '/static/', # for localhost
    #os.getcwd()
    #os.path.join(BASE_DIR, 'static'),
)


MYNETA_STATES_NAMES = [
    ["Andhra Pradesh","andhra"], 
    ["Arunachal Pradesh", "arunachal"], 
    ["Assam", "assam"], 
    ["Bihar", "bihar"], 
    ["Chattisgarh", "chattisgarh"], 
    ["Delhi", "delhi"], 
    ["Goa", "goa"], 
    ["Gujarat", "gujrat"], 
    ["Haryana", "haryana"], 
    ["Himachal Pradesh", "hp"], 
    ["Jammu And Kashmir", "jk"], 
    ["Jharkhand", "jharkhand"], 
    ["Karnataka", "karnataka"],
    ["Kerala", "kerala"],
    ["Madhya Pradesh", "mp"],
    ["Maharashtra", "maharashtra"], 
    ["Manipur", "manipur"], 
    ["Meghalaya", "meghalaya"],
    ["Mizoram", "mizoram"], 
    ["Nagaland", "nagaland"], 
    ["Odisha", "odisha"],
    ["Puducherry", "punducherry"], 
    ["Punjab", "punjab"],
    ["Rajasthan", "rajasthan"], 
    ["Sikkim", "sikkim"], 
    ["Tamil Nadu", "tamil"],
    ["Telangana", "telangana"], 
    ["Tripura", "tripura"],
    ["Uttarakhand", "utt"], 
    ["Uttar Pradesh", "up"],
    ["West Bengal", "westbengal"]
]

