from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False #프로필 구현에서 수정 True->False

ALLOWED_HOSTS = ['3.35.27.125']

DJANGO_APPS += [

]

PROJECT_APPS += [

]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]