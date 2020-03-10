# -*- coding: utf-8 -*-

from spaceone.api.secret.v1 import credential_pb2, credential_pb2_grpc
from spaceone.core.pygrpc import BaseAPI


class Credential(BaseAPI, credential_pb2_grpc.CredentialServicer):

    pb2 = credential_pb2
    pb2_grpc = credential_pb2_grpc

    def create(self, request, context):
        params, metadata = self.parse_request(request, context)

        with self.locator.get_service('CredentialService', metadata) as credential_service:
            return self.locator.get_info('CredentialInfo', credential_service.create(params))

    def update(self, request, context):
        params, metadata = self.parse_request(request, context)

        with self.locator.get_service('CredentialService', metadata) as credential_service:
            return self.locator.get_info('CredentialInfo', credential_service.update(params))

    def delete(self, request, context):
        params, metadata = self.parse_request(request, context)

        with self.locator.get_service('CredentialService', metadata) as credential_service:
            credential_service.delete(params)
            return self.locator.get_info('EmptyInfo')

    def issue(self, request, context):
        params, metadata = self.parse_request(request, context)

        with self.locator.get_service('CredentialService', metadata) as credential_service:
            issue_type, secret = credential_service.issue(params)
            return self.locator.get_info('IssueInfo', issue_type, secret)

    def get(self, request, context):
        params, metadata = self.parse_request(request, context)

        with self.locator.get_service('CredentialService', metadata) as credential_service:
            return self.locator.get_info('CredentialInfo', credential_service.get(params))

    def list(self, request, context):
        params, metadata = self.parse_request(request, context)

        with self.locator.get_service('CredentialService', metadata) as credential_service:
            credential_vos, total_count = credential_service.list(params)
            return self.locator.get_info('CredentialsInfo', credential_vos, total_count,
                                         minimal=self.get_minimal(params))
