import os
import sys

settings = sys.modules['project.settings']

TEMPLATE_DEBUG = settings.DEBUG

# default basic context processors.
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

# Use project/templates/ as templates folder.
TEMPLATE_DIRS = (os.path.join(settings.BASE_DIR, 'templates'), )

# Cachable template loader. caches processed templates in memory, very fast next use. workflow like jinja2. Important
# to use in production.
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

# django-render library template processor engine. By default uses django templates. Can use jinja2 via coffin backend.
# RENDER_ENGINE = 'coffin'

if settings.DEBUG:
    # slow, but refreshable every request template loader. Debug only.
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )
