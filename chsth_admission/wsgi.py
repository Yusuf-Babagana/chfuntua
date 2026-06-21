import os
import sys

# ===== PROJECT PATH (IMPORTANT) =====
path = '/home/chfuntua/chfuntua'
if path not in sys.path:
    sys.path.append(path)

# ===== DJANGO SETTINGS =====
os.environ['DJANGO_SETTINGS_MODULE'] = 'chsth_admission.settings'

# ===== WSGI APPLICATION =====
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
