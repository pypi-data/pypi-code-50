import copy
import json
import logging
import boto3

from typing import Dict, Any, Optional
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Response:
    def __init__(self, cluster: str, service_name: str, success: bool, metadata: Dict[str, Any]) -> None:
        self.__cluster = cluster
        self.__service_name = service_name
        self.__success = success
        self.__metadata = metadata

    @property
    def cluster(self) -> str:
        return self.__cluster

    @property
    def service_name(self) -> str:
        return self.__service_name

    @property
    def metadata(self) -> Dict[str, Any]:
        return copy.deepcopy(self.__metadata)

    @property
    def success(self) -> bool:
        return self.__success

    @property
    def service_arn(self) -> Optional[str]:
        try:
            response = boto3.client('ecs').describe_services(
                cluster=self.__cluster,
                services=[self.__service_name],
            )
        except ClientError as ex:
            logger.error(f'Failed to describe ecs services. Reason: {repr(ex)}, {ex.response}.')
            return None

        try:
            return response['services'][0]['serviceArn']
        except (KeyError, IndexError) as ex:
            logger.error(f'Failed to parse ecs response. Reason: {repr(ex)}.')
            return None

    def to_dict(self) -> Dict[str, Any]:
        response = {
            'arn': self.service_arn,
            'name': self.service_name,
            'success': self.success,
            'meta': self.metadata
        }

        return response
