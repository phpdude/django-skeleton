# Best place to change this env variables is project/settings/local_env.py file. It loads after this one specially to
# allow you manage env without touching project code.

PRODUCTION = False
DEBUG = True

print 'Application modes: DEBUG is %s, PRODUCTION is %s' % (DEBUG, PRODUCTION)
