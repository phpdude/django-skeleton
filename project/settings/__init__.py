import inspect
import pkgutil
import os
from pprint import pformat
import sys

ordering = ('env', 'local_env', 'paths', 'middleware', 'debug_toolbar')

modules = [x[1] for x in pkgutil.walk_packages(__path__)]
modules.sort(key=lambda x: x in ordering and ordering.index(x) + 1 or sys.maxint)

sys.stderr.write('Loading project.settings submodules: %s\n' % (", ".join(modules)))

for module_name in modules:
    module = __import__(module_name, globals(), locals(), [])
    for var_name, val in inspect.getmembers(module):
        if var_name.isupper():
            locals().update({var_name: val})

try:
    # noinspection PyUnresolvedReferences
    from ..settings_local import *
except ImportError:
    pass

settingsraw = []
for s in locals().copy():
    if s.isupper():
        try:
            settingsraw.append("%s = %s\n" % (s, pformat(locals()[s], indent=0, width=100000)))
        except:
            pass

settingsfile = os.path.dirname(__file__) + '/../settings_compiled.py'
if not os.path.isfile(settingsfile) or open(settingsfile).readlines() != settingsraw:
    sys.stderr.write('Updating compiled settings file ...\n')
    file(settingsfile, 'wb').writelines(settingsraw)

sys.stderr.write("\n")
