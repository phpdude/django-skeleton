# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR = os.path.realpath(os.path.dirname(PROJECT_DIR))

print 'settings.BASE_DIR is "%s", settings.PROJECT_DIR is "%s"' % (BASE_DIR, PROJECT_DIR)
