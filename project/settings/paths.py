# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import sys

PROJECT_DIR = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR = os.path.realpath(os.path.dirname(PROJECT_DIR))

sys.stderr.write('settings.BASE_DIR is "%s", settings.PROJECT_DIR is "%s"\n' % (BASE_DIR, PROJECT_DIR))
