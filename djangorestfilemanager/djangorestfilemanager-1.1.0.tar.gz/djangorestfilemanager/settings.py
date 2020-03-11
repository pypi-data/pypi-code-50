from django.conf import settings

VERSION = '1.1.1'

REST_FILE_MANAGER = getattr(settings, 'REST_FILE_MANAGER', {})
UPLOADS_DIR = REST_FILE_MANAGER.get('UPLOADS_DIR', 'files/')
