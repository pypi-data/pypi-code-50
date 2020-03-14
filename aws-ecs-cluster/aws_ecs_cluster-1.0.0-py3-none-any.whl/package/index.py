import json
import boto3
import botocore
import logging

from typing import Any, Dict
from botocore.exceptions import ClientError

try:
    from aws_ecs_cluster.package.action import Action
    from aws_ecs_cluster.package import cfnresponse
except ImportError:
    # Lambda specific import.
    # noinspection PyUnresolvedReferences
    import cfnresponse
    # noinspection PyUnresolvedReferences
    from action import Action

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info(f'Version of boto3 lib: {boto3.__version__}.')
logger.info(f'Version of botocore lib: {botocore.__version__}.')


def __success(event, context, data, reason=None):
    logger.info('SUCCESS: {}'.format(data))
    cfnresponse.send(event, context, cfnresponse.SUCCESS, data, reason=reason)


def __failed(event, context, data, reason=None):
    logger.info('FAIL: {}'.format(data))
    cfnresponse.send(event, context, cfnresponse.FAILED, data, reason=reason)


def __create(**kwargs) -> Dict[str, Any]:
    response = Action.create(**kwargs)
    logger.info(json.dumps(response, default=lambda o: '<not serializable>'))
    return response


def __update(**kwargs) -> Dict[str, Any]:
    response = Action.update(**kwargs)
    logger.info(json.dumps(response, default=lambda o: '<not serializable>'))
    return response


def __delete(**kwargs) -> Dict[str, Any]:
    response = Action.delete(**kwargs)
    logger.info(json.dumps(response, default=lambda o: '<not serializable>'))
    return response


def __handle(event, context) -> Dict[str, Any]:
    logger.info('Got new request. Event: {}, Context: {}'.format(event, context))

    kwargs = event['ResourceProperties']

    if event['RequestType'] == 'Delete':
        return __delete(**kwargs)

    if event['RequestType'] == 'Create':
        return __create(**kwargs)

    if event['RequestType'] == 'Update':
        return __update(**kwargs)

    raise KeyError('Unsupported request type! Type: {}'.format(event['RequestType']))


def handler(event, context):
    try:
        response = __handle(event, context)
    except ClientError as ex:
        return __failed(event, context, {'Error': str(ex.response)}, reason=f'{repr(ex)}:{ex.response}')
    except Exception as ex:
        return __failed(event, context, {'Error': str(ex)}, reason=repr(ex))

    __success(event, context, response)
