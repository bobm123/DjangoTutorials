#!/home/balsachi/.env/py27env/bin/python

import sys
import os

sys.path.insert(0, '/home/balsachi/.env/py27env/lib/python2.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'myproj.settings'

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")