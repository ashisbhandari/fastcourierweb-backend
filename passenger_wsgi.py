import os
import sys

project_home = "/home2/ashishbh/fastcourierbirtamode.com.np"

if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fccs.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()