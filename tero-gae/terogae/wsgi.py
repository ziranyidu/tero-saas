"""
WSGI config for terogae project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

from terogae.boot import fix_path
fix_path()

import os
from django.core.wsgi import get_wsgi_application
from djangae.environment import is_production_environment
from djangae.wsgi import DjangaeApplication
from django.conf import settings as _settings
from werkzeug.debug import DebuggedApplication

settings = "terogae.settings_live" if is_production_environment() else "terogae.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

# Use werkzeug to be able to have runserver_plus , more info at:
# https://nvbn.github.io/2015/07/17/wekzeug-django-gae/
application = get_wsgi_application()
if _settings.DEBUG:
    app = DebuggedApplication(application, True)
    # Werkzeug won't work without exceptions propagation
    _settings.DEBUG_PROPAGATE_EXCEPTIONS = True