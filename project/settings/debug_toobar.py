import sys

settings = sys.modules['project.settings']

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TEMPLATE_CONTEXT': True,
    'ENABLE_STACKTRACES': True,
}

if settings.DEBUG:
    settings.INSTALLED_APPS += (
        'debug_toolbar',
    )

    settings.MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

