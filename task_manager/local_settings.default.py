# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'developing'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'task_manager',
        'USER': 'postgres',
        'PASSWORD': 'developing',
        'HOST': 'db',
        'PORT': '5432',
    }
}
