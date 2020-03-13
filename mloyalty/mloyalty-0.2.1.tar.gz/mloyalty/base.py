from mloyalty.utils.module_loading import import_string
from datetime import datetime
from dotenv import load_dotenv

import requests
import jwt
import json
import sys
import os
import time
import logging

logger = logging.getLogger('mloyalty')
formatter = logging.Formatter(
    '%(asctime)s (%(filename)s:%(lineno)d %(threadName)s) %(levelname)s - %(name)s: "%(message)s"'
)
console_output_handler = logging.StreamHandler(sys.stdout)
console_output_handler.setFormatter(formatter)
console_output_handler.setLevel(logging.DEBUG)
logger.addHandler(console_output_handler)
logger.setLevel(logging.DEBUG)
logger.propagate = False


load_dotenv()

CONNECT_TIMEOUT = 3.5
READ_TIMEOUT = 9999
RETRIES = 3
WAIT_DELAY = 3


class Mloyalty:
    """
    Базовый класс для работы с API Mloyalty.
    """
    def __init__(self, username=None, password=None, base_url=None, db_backend=None):
        self.username = username or os.getenv('MLOYALTY_USERNAME')
        self.password = password or os.getenv('MLOYALTY_PASSWORD')
        self.base_url = base_url or os.getenv('MLOYALTY_BASE_URL')

        if db_backend:
            self.db_backend = db_backend
        elif os.getenv('MLOYALTY_DB_BACKEND'):
            self.db_backend = os.getenv('MLOYALTY_DB_BACKEND')
        else:
            self.db_backend = 'mloyalty.db.backends.tinydb.MloyaltyTinyDB'

    def get_access_token(self):
        """
        Получение токена доступа.
        :return: id записи в базе данных
        """
        method_url = 'managerlogin'
        request_url = self.base_url + '/%s' % method_url

        payload = {
            'username': self.username,
            'password': self.password,
            'grant_type': 'password',
        }

        logger.debug("Request: method={0} url={1} params={2}".format('post', request_url, payload))
        result = requests.post(url=request_url, data=payload)
        logger.debug("The server returned: {0}".format(result.text))

        return self._save_data(method_url, result)

    def refresh_token(self, refresh_token):
        """
        Обновление токена с помощью refresh_token
        :param refresh_token:
        :return: id записи в базе данных
        """
        method_url = 'managerlogin'
        request_url = self.base_url + '/%s' % method_url

        payload = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
        }

        logger.debug("Request: method={0} url={1} params={2}".format('post', request_url, payload))
        result = requests.post(url=request_url, data=payload)
        logger.debug("The server returned: {0}".format(result.text))

        return self._save_data(method_url, result)

    def get_connection(self):
        klass = import_string(self.db_backend)
        return klass()

    def _save_data(self, method_url, result):
        if result.ok and isinstance(result.json(), dict):
            db = self.get_connection()
            db.data = result.json()
            return db.save()

        else:
            msg = 'The server returned HTTP {0} {1}. Response body:\n[{2}]' \
                .format(result.status_code, result.reason, result.text)
            raise ApiException(msg, method_url, result)

    def get_request_params(self):
        """
        Получение параметров для запроса.
        :return: словарь с параметрами: token, operator_id, partner_id, pos_id, pos_code
        """
        db = self.get_connection()
        data = db.get()

        if data is None:
            doc_id = self.get_access_token()
            data = db.get(doc_id)

        token = data['access_token']
        params = jwt.decode(token, verify=False)

        dt_now = datetime.now()
        dt_exp = datetime.fromtimestamp(params['exp'])
        delta = dt_exp - dt_now
        if delta.total_seconds() < (5 * 60):
            doc_id = self.refresh_token(data['refresh_token'])
            data = db.get(doc_id)
            token = data['access_token']
            params = jwt.decode(token, verify=False)

        return {
            'token': token,
            'operator_id': params['oper'],
            'partner_id': params['partner'],
            'pos_id': params['pos'],
            'pos_code': params['poscode'],
        }

    def _make_request(self, token, method_url, method='get', params=None):
        """
        Делает запрос к API Mloyalty
        :param token:
        :param method_url: метод
        :param method: HTTP метод (по умолчанию 'get')
        :param params: параметры запроса (пары ключ-значение)
        :return:
        """
        request_url = self.base_url + '/%s' % method_url
        logger.debug("Request: method={0} url={1} params={2}".format(method, request_url, params))
        headers = {'Authorization': 'Bearer %s' % token}

        connect_timeout = CONNECT_TIMEOUT
        read_timeout = CONNECT_TIMEOUT
        retries = RETRIES
        wait_delay = WAIT_DELAY
        result = None

        while retries > 0:
            result = requests.request(method=method, url=request_url, headers=headers, data=params,
                                      timeout=(connect_timeout, read_timeout))
            logger.debug("The server returned: {0}".format(result.text))

            if result.ok:
                break

            elif result.status_code == 401:
                request_params = self.get_request_params()
                headers = {'Authorization': 'Bearer %s' % request_params.get('token')}
                logger.info("Token updated ({0} retries left)".format(retries - 1))

            else:
                time.sleep(wait_delay)
                logger.info("Waited {0} seconds ({1} retries left)".format(wait_delay, retries - 1))

            retries -= 1

        if retries == 0:
            msg = 'Exceeded the number of attempts to send a request. ' \
                  'The server returned HTTP {0} {1}. Response body:\n[{2}]' \
                .format(result.status_code, result.reason, result.text)
            raise ApiException(msg, method_url, result)

        if result is None:
            msg = 'The result cannot be None'
            raise ApiException(msg, method_url, result)

        return self._check_result(method_url, result)

    @staticmethod
    def _check_result(method_url, result):
        """
        Проверяет, является ли `result` верным ответом API.
        Результат считается неверным, если:
            - сервер вернул код ответа HTTP отличный от 200
            - содержимое ответа невалидный JSON
            - вызов метода был с ошибкой (поле 'ErrorCode' не равно 0)
        :raises ApiException: если применим один из выше перечисленных случаев
        :param method_url: метод
        :param result: возращаемый результат запроса метода
        :return: словарь данных полученный из JSON ответа
        """
        if result.status_code != 200:
            msg = 'The server returned HTTP {0} {1}. Response body:\n[{2}]' \
                .format(result.status_code, result.reason, result.text)
            raise ApiException(msg, method_url, result)

        try:
            result_json = result.json()
        except json.decoder.JSONDecodeError:
            msg = 'The server returned an invalid JSON response. Response body:\n[{0}]' \
                .format(result.text)
            raise ApiException(msg, method_url, result)

        if result_json['ErrorCode'] != 0:
            msg = 'Код ошибки: {0} Сообщение: {1}' \
                .format(result_json['ErrorCode'], result_json['Message'])
            raise ApiException(msg, method_url, result)

        return result_json


class ApiException(Exception):
    """
    Класс представляет исключение, которое вызывается при сбое вызова API Mloyalty.
    В дополнениеи к информационному сообщению имеет атрибуты `method_url` и `result`, которые содержат вызываемый метод
    и возвращаемый результат.
    """
    def __init__(self, msg, method_url, result):
        super(ApiException, self).__init__('{0}'.format(msg))
        self.method_url = method_url
        self.result = result
