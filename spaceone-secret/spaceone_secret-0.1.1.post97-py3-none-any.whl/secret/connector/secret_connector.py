# -*- coding: utf-8 -*-

import json

import boto3
from spaceone.core import config

__all__ = ['SecretConnector']


class SecretConnector(object):

    def __init__(self, *args, **kwargs):
        secret_conf = config.get_connector('SecretConnector')
        if secret_conf and secret_conf.get('aws_access_key_id') and secret_conf.get('aws_secret_access_key'):
            self.client = boto3.client('secretsmanager',
                                       aws_access_key_id=secret_conf.get('aws_access_key_id'),
                                       aws_secret_access_key=secret_conf.get('aws_secret_access_key'),
                                       region_name=secret_conf.get('region', 'ap-northeast-2')  # DEFAULT: SEOUL
                                       )
        else:
            self.client = boto3.client('secretsmanager',
                                       region_name=secret_conf.get('region', 'ap-northeast-2')  # DEFAULT: SEOUL
                                       )

    @staticmethod
    def _convert_tags(tags):
        return list(map(lambda k: {'Key': k, 'Value': tags[k]}, tags))

    @staticmethod
    def _response(response):
        if 'ResponseMetadata' in response and 'HTTPStatusCode' in response['ResponseMetadata'] and \
                response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return True

        return False

    @staticmethod
    def _response_value(response):
        data_string = response.get('SecretString', False)

        if data_string:
            return json.loads(data_string)

        return data_string

    def create_secret(self, credential_id, params):
        secret_params = {
            'Name': credential_id,
            'SecretString': json.dumps(params['data']),
        }

        return self._response(self.client.create_secret(**secret_params))

    def update_secret(self, credential_id, params):
        pass

    def delete_secret(self, credential_id):
        response = self.client.delete_secret(
            SecretId=credential_id,
            ForceDeleteWithoutRecovery=True
        )

        return self._response(response)

    def get_secret(self, credential_id):
        return self._response_value(self.client.get_secret_value(SecretId=credential_id))
