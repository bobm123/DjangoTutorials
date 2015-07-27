import sys, os
virt_binary = "/home/balsachi/.env/py27env/bin/python"
if sys.executable != virt_binary: os.execl(virt_binary, virt_binary, *sys.argv)
sys.path.append(os.getcwd())

os.environ['DJANGO_SETTINGS_MODULE'] = "superlists.settings"

#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()