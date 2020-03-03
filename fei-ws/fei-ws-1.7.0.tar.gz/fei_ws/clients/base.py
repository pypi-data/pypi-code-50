# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from six.moves.urllib.parse import urljoin

import logging
import os
import re

from zeep.transports import Transport
from zeep.cache import InMemoryCache
from zeep.client import Client
from zeep.exceptions import Fault
from requests import Session

from fei_ws.clients import errors as fei_errors
from fei_ws import config


logger = logging.getLogger('fei-ws.client')


cache = InMemoryCache(timeout=24*3600*7)


class FEIWSBaseClient(object):
    """FEI Base Client contains logic shared among FEI Clients. It should not
    be used on its own.

    """

    _NAME_REGEX = re.compile(r"(\b[A-Za-z']{1,3}\b|'[tT])", re.UNICODE)
    _ROMAN_REGEX = re.compile(r'\bM{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', re.IGNORECASE)

    def __init__(self, version, username=None, password=None):
        """ Initializes the base client.

        Params:
            version: A tuple containing the version numbering.
            username: The username used to authenticate. The username from the
                config file is used when it is not supplied.
            password: The password used to authenticate. The password from the
                config file is used when it is not supplied.

        """

        if config.FEI_WS_USE_LOCAL_WSDL:
            __wsdl_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'wsdl/')
            self.__AUTH_WSDL = os.path.join(__wsdl_path, 'auth.wsdl')
            self.__ORGANIZER_WSDL = os.path.join(__wsdl_path, 'org_1_2.wsdl')
            self.__COMMON_WSDL = os.path.join(__wsdl_path, 'common.wsdl')
        else:
            self.__AUTH_WSDL = urljoin(config.FEI_WS_BASE_URL,
                                       '/_vti_bin/Authentication.asmx?WSDL')
            self.__ORGANIZER_WSDL = urljoin(
                config.FEI_WS_BASE_URL, '/_vti_bin/FEI/OrganizerWS_%s_%s.asmx?WSDL'
                                        % version)

            self.__COMMON_WSDL = urljoin(config.FEI_WS_BASE_URL,
                                         '/_vti_bin/FEI/CommonWS.asmx?WSDL')

        self.normalize = config.FEI_WS_NORMALIZE_NAMES
        self._version = version
        self._common_data = {}
        self._username = username if username else config.FEI_WS_USERNAME
        self._password = password if password else config.FEI_WS_PASSWORD
        self._session = Session()
        self._ows_client = Client(self.__ORGANIZER_WSDL, transport=Transport(cache=cache, session=self._session))
        self._ows_factory = self._ows_client.type_factory('ns0')
        self._cs_client = Client(self.__COMMON_WSDL, transport=Transport(cache=cache, session=self._session))
        self._cs_factory = self._cs_client.type_factory('ns0')
        self._authenticate([self._cs_client, self._ows_client])
        logger.info('initialize finished')

    def _authenticate(self, clients):
        """Used to authenticate clients with the FEI WS.
        """
        auth_client = Client(self.__AUTH_WSDL, transport=Transport(cache=cache, session=self._session))
        if not self._username or not self._username:
            # Please provide a username and password to init or
            # set the username and password in the settings
            # file.
            raise fei_errors.FEIWSConfigException("Could not login: username and password are empty.")
        auth_login = auth_client.service.Login(self._username, self._password)
        if auth_login['ErrorCode'] != 'NoError':
            raise fei_errors.FEIWSAuthException('Could not login: %s' % auth_login['ErrorCode'])
        logger.info('client authenticated')
        for client in clients:
            client.set_default_soapheaders({'AuthHeader': self._cs_factory.AuthHeader(UserName=self._username, Language='en')})

    def _request(self, service, method, **kwargs):
        try:
            logger.info('Calling service: %s' % method)
            response = getattr(service, method)(**kwargs)
            self._handle_messages(response)
            if hasattr(response.body, '%sResult' % method):
                return getattr(response.body, '%sResult' % method)
            return response.body
        except Fault as ex:
            raise fei_errors.FEIWSApiException(ex.message, ex.code)

    def _handle_messages(self, result):
        """Generic message handler, used to determine if an exception needs to
        be thrown.

        """
        if not 'Messages' in result['body'] or not result['body']['Messages']:
            return
        warnings = ''    
        for message in result['body']['Messages'].Message:
            message_type = fei_errors.FEI_MESSAGE_TYPE_DICT.get(message.UID)
            if not message_type:
                raise fei_errors.FEIWSApiException('Unknown message type: %s' % message.UID, code='MessageTypeUnknown')
            description = ('%s: %s\nDetails: %s' %
                           (message_type['Id'], message_type['Description'], message.Detail))
            if message_type['IsCritical'] or message_type['IsError']:
                logger.exception(description)
                raise fei_errors.FEIWSApiException(message.Detail, code=message_type['Id'])
            warnings += '%s\n' % description
        if warnings:
            logger.warning(warnings)

    def _normalize_name(self, value, roman_nummerals=False):
        def _transform(match):
            word = match.group()
            if word.lower() in config.FEI_WS_LOWER_CASE_WORDS:
                return word.lower()
            if word.upper() in config.FEI_WS_UPPER_CASE_ACRONYMS:
                return word.upper()
            return word

        if not value:
            return value
        value = value.title()
        value = self._NAME_REGEX.sub(_transform, value)
        if roman_nummerals:
            value = self._ROMAN_REGEX.sub(
                lambda match: match.group().upper() if match.group() else match.group(), value)
        return value[0].upper() + value[1:]

    def get_common_data(self, method, **kwargs):
        """Generic method for retrieving data from the common data web service.

        Params:
            method: The name of the common data WS method you want to use.
            **kwargs: Contains the keyword arguments you want to pass to the
                method you are calling.

        Return value: The raw result from the Common Data WS.

        """
        if not kwargs and method in self._common_data:
            return self._common_data[method]
        result = self._request(self._cs_client.service, method, **kwargs)
        self._common_data[method] = result
        return result

    def get_organizer_data(self, method, **kwargs):
        return self._request(self._ows_client.service, method, **kwargs)
