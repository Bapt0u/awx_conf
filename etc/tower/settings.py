import os
import socket
# Import all so that extra_settings works properly
from django_auth_ldap.config import *

def get_secret():
    if os.path.exists("/etc/tower/SECRET_KEY"):
        return open('/etc/tower/SECRET_KEY', 'rb').read().strip()

ADMINS = ()
STATIC_ROOT = '/var/lib/awx/public/static'
STATIC_URL = '/static/'
PROJECTS_ROOT = '/var/lib/awx/projects'
JOBOUTPUT_ROOT = '/var/lib/awx/job_status'

IS_K8S = True



SECRET_KEY = get_secret()

ALLOWED_HOSTS = ['*']

INTERNAL_API_URL = 'http://127.0.0.1:8052'


# Container environments don't like chroots
AWX_PROOT_ENABLED = False

# Automatically deprovision pods that go offline
AWX_AUTO_DEPROVISION_INSTANCES = True

CLUSTER_HOST_ID = socket.gethostname()
SYSTEM_UUID = os.environ.get('MY_POD_UID', '00000000-0000-0000-0000-000000000000')

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

SERVER_EMAIL = 'root@localhost'
DEFAULT_FROM_EMAIL = 'webmaster@localhost'
EMAIL_SUBJECT_PREFIX = '[AWX] '

EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False

USE_X_FORWARDED_PORT = True
BROADCAST_WEBSOCKET_PORT = 8052
BROADCAST_WEBSOCKET_PROTOCOL = 'http'


RECEPTOR_LOG_LEVEL = 'info'