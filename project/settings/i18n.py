# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/
import os
import sys

settings = sys.modules['project.settings']

LANGUAGE_CODE = 'en'

USE_I18N = True
USE_L10N = True

LOCALE_PATHS = (os.path.join(settings.PROJECT_DIR, 'conf/locale'),)
