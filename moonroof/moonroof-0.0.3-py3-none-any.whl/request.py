import requests
import logging
import json
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
import zlib
from gzip import GzipFile
from io import BytesIO

if not hasattr(settings, 'MOONROOF_API_KEY'):
    raise ImproperlyConfigured('MOONROOF_API_KEY must be declared in settings.py')

MOONROOF_URL = getattr(settings, 'MOONROOF_API_ENDPOINT', 'https://moonroof-api-prod.herokuapp.com/api/events-bulk')
MOONROOF_API_KEY = settings.MOONROOF_API_KEY
MOONROOF_SEND_EVENTS = getattr(settings, 'MOONROOF_SEND_EVENTS', True)

HEADERS = {
    'Authorization': 'Bearer {0}'.format(settings.MOONROOF_API_KEY),
    'Content-Type': 'application/json',
    'Content-Encoding': 'gzip'
}

log = logging.getLogger('moonroof')

def _gzipped(data):
    buf = BytesIO()
    with GzipFile(fileobj=buf, mode='w') as gz:
        # 'data' was produced by json.dumps(),
        # whose default encoding is utf-8.
        gz.write(data.encode('utf-8'))
    return buf.getvalue()

def post(items):
    if not MOONROOF_SEND_EVENTS:
        log.debug('Sending events is off, not sending data to API')
        return
    data = json.dumps({'events': [{'data': i} for i in items]})
    log.debug('Sending data to Moonroof API. {0} {1}'.format(MOONROOF_URL, data))
    response = requests.post(
        MOONROOF_URL,
        data=_gzipped(data),
        headers=HEADERS
    )
    if response.status_code == 201:
        log.debug('Succesfully sent data.')
    else:
        log.error('Failed to send data to Moonroof API. {0} - {1}'.format(
            response.status_code,
            response.text
        ))
