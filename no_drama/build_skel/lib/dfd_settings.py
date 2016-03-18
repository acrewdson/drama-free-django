import os
import dfd

real_settings = os.environ.get('REAL_DJANGO_SETTINGS')

if real_settings:
    exec("from %s  import *" % real_settings)

else:
    raise ImportError

DEBUG = False

static_in = dfd.get_path('static_in')
build_static_in = dfd.get_path('build_static_in')
static_out = dfd.get_path('static_out')


EXTENDED_STATICFILES_DIRS = []

for location in [l for l in [static_in, build_static_in] if os.path.exists(l)]:
    for filename in os.listdir(location):
        path = os.path.join(location, filename)
        if os.path.isdir(path):
            EXTENDED_STATICFILES_DIRS.append(path)

if EXTENDED_STATICFILES_DIRS:
    if 'STATICFILES_DIRS' in locals():
        STATICFILES_DIRS.extend(EXTENDED_STATICFILES_DIRS)
    else:
        STATICFILES_DIRS = EXTENDED_STATICFILES_DIRS

STATIC_ROOT = static_out
