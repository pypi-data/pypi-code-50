INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'obfuscator',
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

SECRET_KEY = 'something_random'
