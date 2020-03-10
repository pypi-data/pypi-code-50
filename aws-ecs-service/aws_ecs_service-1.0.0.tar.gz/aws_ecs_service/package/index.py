import json
from typing import Any, Dict

import boto3
import botocore
import logging

from botocore.exceptions import ClientError

try:
    from aws_ecs_service.package.action import Action
    from aws_ecs_service.package import cfnresponse
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


def __success(event, context, data):
    logger.info('SUCCESS: {}'.format(data))
    cfnresponse.send(event, context, cfnresponse.SUCCESS, data)


def __failed(event, context, data):
    logger.info('FAIL: {}'.format(data))
    cfnresponse.send(event, context, cfnresponse.FAILED, data)


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


def __handle(event, context):
    logger.info('Got new request. Event: {}, Context: {}'.format(event, context))

    kwargs = event['ResourceProperties']

    create_args = kwargs['onCreate']
    update_args = kwargs['onUpdate']
    delete_args = kwargs['onDelete']

    if event['RequestType'] == 'Delete':
        return __delete(**create_args)

    if event['RequestType'] == 'Create':
        return __create(**update_args)

    if event['RequestType'] == 'Update':
        return __update(**delete_args)

    raise KeyError('Unsupported request type! Type: {}'.format(event['RequestType']))


def handler(event, context):
    try:
        response = __handle(event, context)
    except ClientError as ex:
        return __failed(event, context, {'Error': str(ex.response)})
    except Exception as ex:
        return __failed(event, context, {'Error': str(ex)})

    __success(event, context, response)
