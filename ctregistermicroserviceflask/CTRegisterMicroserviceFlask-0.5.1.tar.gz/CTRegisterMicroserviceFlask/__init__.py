import json
import os
import threading

from CTRegisterMicroserviceFlask.errors import NotFound
from flask import jsonify
from requests import post, Session, Request

AUTOREGISTER_MODE = 'AUTOREGISTER_MODE'
NORMAL_MODE = 'NORMAL_MODE'

CT_URL = os.getenv('CT_URL')
CT_TOKEN = os.getenv('CT_TOKEN')
API_VERSION = os.getenv('API_VERSION')


def ct_register(name, ct_url, url, active):
    """Autoregister method"""
    payload = {'name': name, 'url': url, 'active': active}

    try:
        r = post(ct_url + '/api/v1/microservice', json=payload, timeout=10)
    except Exception as error:
        os._exit(1)

    if r.status_code >= 400:
        os._exit(1)


def register(app, name, info, swagger, mode, ct_url=False, url=False, active=True, delay=5.0):
    """Register method"""
    if mode == AUTOREGISTER_MODE:
        t = threading.Timer(delay, ct_register, [name, ct_url, url, active])
        t.start()

    @app.route('/info')
    def get_info():
        info['swagger'] = swagger
        return jsonify(info)

    @app.route('/ping')
    def get_ping():
        return 'pong'


def request_to_microservice(config):
    """Request to microservice method"""
    try:
        session = Session()
        request = Request(
            method=config.get('method'),
            url=CT_URL + config.get('uri') if config.get(
                'ignore_version') or not API_VERSION else CT_URL + '/' + API_VERSION + config.get('uri'),
            headers={
                'content-type': 'application/json',
                'Authorization': 'Bearer ' + CT_TOKEN,
                'APP_KEY': config.get('application', 'rw')
            },
            data=json.dumps(config.get('body'))
        )
        prepped = session.prepare_request(request)

        response = session.send(prepped)
    except Exception as error:
        raise error

    try:
        return response.json()
    except Exception:
        raise NotFound(response.text)
