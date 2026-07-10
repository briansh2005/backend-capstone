## routes
### URL dispatcher

settings.py done



### project folder
- ROOT_URLCONF = 'littlelemon.urls'
- restaurant/views.py
- restaurant/urls.py
- ROOT_URLCONF = 'littlelemon.urls'


### static routes
- settings.BASE_DIR
- settings.TEMPLATES
- templates/index.html
- views.index
- restaurant/urls

### setup db connection
### setup models









```
import os
import sys

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restaurant',
    'rest_framework'
    'restaurant_authtoken',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'read_default_file': os.path.join(BASE_DIR, 'my.cnf'),
        },
    }
}

if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```






'''
ROOT_URLCONF = 'littlelemon.urls'

#Include 'templates' in 'DIRS' attribute
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

STATIC_URL = 'restaurant/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'restaurant/static'),
]

'''
