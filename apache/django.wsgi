import os
import sys

path = '/srv/project/PCS'
if path not in sys.path:
    sys.path.insert(0, '/srv/project/PCS')

    os.environ['DJANGO_SETTINGS_MODULE'] = 'PCS.settings'

    import django.core.handlers.wsgi
    application = django.core.handlers.wsgi.WSGIHandler()
