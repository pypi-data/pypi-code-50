import logging
import json

from botocore.vendored import requests

SUCCESS = "SUCCESS"
FAILED = "FAILED"
MAXIMUM_RESPONSE_SIZE = 1024 * 4


def send(event, context, responseStatus, responseData, physicalResourceId=None, noEcho=False, reason=None):
    responseUrl = event['ResponseURL']

    logging.info(f'Sending response back to CloudFormation: {responseUrl}...')

    responseBody = {}

    responseBody['Status'] = responseStatus
    responseBody['Reason'] = reason or ('See the details in CloudWatch Log Stream: ' + context.log_stream_name)
    responseBody['PhysicalResourceId'] = physicalResourceId or context.log_stream_name
    responseBody['StackId'] = event['StackId']
    responseBody['RequestId'] = event['RequestId']
    responseBody['LogicalResourceId'] = event['LogicalResourceId']
    responseBody['NoEcho'] = noEcho
    responseBody['Data'] = responseData

    response_json = json.dumps(responseBody, default=lambda o: '<not serializable>')
    is_too_big = len(response_json.encode('utf-8')) >= MAXIMUM_RESPONSE_SIZE

    if is_too_big:
        responseBody['Data'] = None
        response_json = json.dumps(responseBody, default=lambda o: '<not serializable>')

    headers = {
        'content-type': '',
        'content-length': str(len(response_json))
    }

    try:
        response = requests.put(
            responseUrl,
            data=response_json,
            headers=headers
        )

        logging.info("Status code: " + response.reason)
    except Exception as e:
        logging.info("send(..) failed executing requests.put(..): " + str(e))
