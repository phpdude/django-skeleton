import os
import sys

settings = sys.modules['project.settings']

# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # sqlite3, postgresql_psycopg2, mysql, oracle
        'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
# 'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': '{{ project_name }}',
#         'USER': '{{ project_name }}',
#         'PASSWORD': 'ENTER PASSWORD HERE',
#         'HOST': '127.0.0.1',
#         'CONN_MAX_AGE': 900
#     }
# }