import sys

# to allow api client save environment state to database.
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

settings = sys.modules['project.settings']

# we use cached_db backend for longlive and fast sessions.
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_COOKIE_NAME = 'sid'
SESSION_COOKIE_AGE = 86400 * 60  # 2 months. Very important to remember users.

if settings.PRODUCTION:
    SESSION_COOKIE_DOMAIN = '.your production hostname prepended with dot (RFC)'
