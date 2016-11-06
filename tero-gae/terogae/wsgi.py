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
from django.conf import settings
from werkzeug.debug import DebuggedApplication

settings = "terogae.settings_live" if is_production_environment() else "terogae.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)



# But we can’t use this approach with gae, because it doesn’t use runserver, 
# it just works through wsgi. So instead we should wrap our wsgi application 
# with DebuggedApplication# application = DjangaeApplication(get_wsgi_application())
application = get_wsgi_application()
if settings.DEBUG:
    app = DebuggedApplication(app, True)
    # Werkzeug won't work without exceptions propagation
    settings.DEBUG_PROPAGATE_EXCEPTIONS = True