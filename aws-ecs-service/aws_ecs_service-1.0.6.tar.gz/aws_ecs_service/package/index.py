import json
import boto3
import botocore
import logging

from botocore.exceptions import ClientError
from typing import Any, Dict, List

try:
    from aws_ecs_service.package.action import Action
    from aws_ecs_service.package import cfnresponse
    from aws_ecs_service.package.response import Response
except ImportError:
    # Lambda specific import.
    # noinspection PyUnresolvedReferences
    import cfnresponse
    # noinspection PyUnresolvedReferences
    from action import Action
    # noinspection PyUnresolvedReferences
    from response import Response

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info(f'Version of boto3 lib: {boto3.__version__}.')
logger.info(f'Version of botocore lib: {botocore.__version__}.')


def __try_get_key(dictionary: Dict[str, Any], keys: List[str]) -> Any:
    for key in keys:
        value = dictionary.get(key)

        if value:
            return value

    raise KeyError(f'Non of the keys {keys} were found.')


def __success(event, context, data, reason=None):
    logger.info('SUCCESS: {}'.format(data))
    cfnresponse.send(event, context, cfnresponse.SUCCESS, data, reason=reason)


def __failed(event, context, data, reason=None):
    logger.info('FAIL: {}'.format(data))
    cfnresponse.send(event, context, cfnresponse.FAILED, data, reason=reason)


def __create(**kwargs) -> Response:
    response = Action.create(**kwargs)
    logger.info(json.dumps(response, default=lambda o: '<not serializable>'))
    return response


def __update(**kwargs) -> Response:
    response = Action.update(**kwargs)
    logger.info(json.dumps(response, default=lambda o: '<not serializable>'))
    return response


def __delete(**kwargs) -> Response:
    response = Action.delete(**kwargs)
    logger.info(json.dumps(response, default=lambda o: '<not serializable>'))
    return response


def __handle(event, context) -> Response:
    logger.info('Got new request. Event: {}, Context: {}'.format(event, context))

    kwargs = event['ResourceProperties']

    create_args = __try_get_key(kwargs, ['onCreate', 'OnCreate', 'oncreate', 'on_create'])
    update_args = __try_get_key(kwargs, ['onUpdate', 'OnUpdate', 'onupdate', 'on_update'])
    delete_args = __try_get_key(kwargs, ['onDelete', 'OnDelete', 'ondelete', 'on_delete'])

    if event['RequestType'] == 'Delete':
        return __delete(**delete_args)

    if event['RequestType'] == 'Create':
        return __create(**create_args)

    if event['RequestType'] == 'Update':
        return __update(**update_args)

    raise KeyError('Unsupported request type! Type: {}'.format(event['RequestType']))


def handler(event, context):
    try:
        response = __handle(event, context).to_dict()
    except ClientError as ex:
        return __failed(event, context, {'Error': str(ex.response)}, reason=f'{repr(ex)}:{ex.response}')
    except Exception as ex:
        return __failed(event, context, {'Error': str(ex)}, reason=repr(ex))

    __success(event, context, response)
