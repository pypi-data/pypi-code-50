# -*- coding: utf-8 -*-
import logging

from google.protobuf.json_format import MessageToDict

from spaceone.core import pygrpc
from spaceone.core.connector import BaseConnector
from spaceone.core.utils import parse_endpoint
from spaceone.inventory.error import *

_LOGGER = logging.getLogger(__name__)


class CollectorPluginConnector(BaseConnector):

    def __init__(self, transaction, config):
        super().__init__(transaction, config)
        self.client = None

    def initialize(self, endpoint):
        if endpoint is None:
            raise ERROR_GRPC_CONFIGURATION
        endpoint = endpoint.replace('"', '')
        e = parse_endpoint(endpoint)
        protocol = e['scheme']
        if protocol == 'grpc':
            self.client = pygrpc.client(endpoint="%s:%s" % (e['hostname'], e['port']), version='plugin')
        elif protocol == 'http':
            # TODO:
            pass

        if self.client is None:
            _LOGGER.error(f'[initialize] Cannot access gRPC server. '
                          f'(host: {e.get("hostname")}, port: {e.get("port")}, version: plugin)')
            raise ERROR_GRPC_CONFIGURATION

    def verify(self, options, credentials):
        params = {
            'options': options,
            'credentials': credentials
            }
        try:
            # TODO: meta (plugin has no meta)
            meta = []
            verify_info = self.client.Collector.verify(params, metadata=meta)
            return MessageToDict(verify_info)
        except Exception as e:
            raise ERROR_AUTHENTICATION_FAILURE_PLUGIN(messsage=str(e))

    def collect(self, options, credentials, filter, region_id=None, zone_id=None, pool_id=None):
        """ Collector Data base on param
        
        Unary/Stream Between This and Plugin

        return Job Result

        format of credential (for ec2 collector)
        credentials = {
            'aws_access_key_id': 'MY_AWS_ACCESS_KEYID',
            'aws_secret_access_key': 'MY_AWS_SECRET_ACCESS_KEY',
            'region': 'ap-northeast-2'
        }
        """
        params = {
            'options': options,
            'credentials': credentials,
            'filter': filter
            }
        #params = {'options':{'domain':'mz.co.kr'},'credentials':{}}
        #_LOGGER.debug('[collect] correct params: %s' % params)
        # TODO: meta (plugin has no meta)
        meta = []
        result_stream = self.client.Collector.collect(params, metadata=meta)
        return result_stream
