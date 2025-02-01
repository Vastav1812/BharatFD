# frequently_asked_questions/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'frequently_asked_questions.settings')
application = get_wsgi_application()
