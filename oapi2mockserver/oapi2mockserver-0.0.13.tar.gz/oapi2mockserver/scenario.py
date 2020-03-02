import hashlib
import json

from jsonschema import ValidationError
from json import JSONDecodeError
from .open_api_schema import OpenAPISchema

class Scenario(object):
    def __init__(self, path, operation, status_code, response_body=None, content_type=None):
        self.path = normalize_path(path)
        self.operation = normalize_operation(operation)
        self.status_code = normalize_status_code(status_code)
        self.response_body = response_body
        self.content_type = content_type

    def matches(self, path, operation):
        path = normalize_path(path)
        return path == self.path and normalize_operation(operation) == self.operation

    def get_expected_response(self):
        response = {
            'statusCode': self.status_code,
        }
        if self.response_body is not None:
            response['responseBody'] = self.response_body
        if self.content_type is not None:
            response['contentType'] = self.content_type

        return response


class Validator(object):
    def __init__(self, contract):
        self.paths = []
        self.operations = {}
        self.statusCodes = {}
        self.contentTypes = {}
        self.schemas = {}

        self.__initialize_contract_data(contract)
    
    def validate(self, scenarios):
        schema = OpenAPISchema()

        for scenario in scenarios:
            if scenario.path not in self.paths:
                raise EndpointNotDefinedException(scenario.path, 'Path %s is not defined in contract' % (scenario.path))
            if scenario.operation not in self.operations[scenario.path]:
                raise EndpointNotDefinedException(scenario.path, 'Operation %s is not defined for path %s in contract' % (scenario.operation, scenario.path))
            if scenario.status_code not in self.statusCodes[self.__index_key(scenario.path, scenario.operation)]:
                raise EndpointNotDefinedException(scenario.path, 'Status-code %s is not defined for path %s and operation %s in contract' % (scenario.status_code, scenario.path, scenario.operation))

            contentType = 'application/json'
            if 'contentType' in scenario.get_expected_response():
                contentType = scenario.get_expected_response()['contentType']
                operationIndex = self.__index_key(scenario.path, scenario.operation)
                if operationIndex in self.contentTypes:
                    if contentType not in self.contentTypes[operationIndex]:
                        raise InvalidResponseContentTypeException(scenario.operation, 'Content-Type %s is not defined for operation %s' % (contentType, scenario.operation))
                elif 'global' in self.contentTypes:
                    if contentType not in self.contentTypes['global']:
                        raise InvalidResponseContentTypeException(scenario.operation, 'Content-Type %s is not defined in contract' % (contentType))

            if 'responseBody' in scenario.get_expected_response() and contentType == 'application/json':
                statusCodeIndex = self.__index_key(scenario.path, scenario.operation, scenario.status_code)
                scenario_json = scenario.get_expected_response()['responseBody']
                try:
                    schema.validate_json(json.dumps(self.schemas[statusCodeIndex]), scenario_json)
                except ValidationError as validationError:
                    raise InvalidResponseBodySchemaException(scenario_json, 'Scenario response body does not validate against schema in contract. Original error message: %s' % (validationError.message))
                except JSONDecodeError as decodeError:
                    raise InvalidResponseContentTypeException(scenario_json, 'Invalid json given to decode. Original error message: %s' % decodeError.msg)
        return True

    def __index_key(self, path, operation, statusCode=None):
        if statusCode is None:
            return hashlib.sha256((path + operation).encode()).hexdigest()
        return hashlib.sha256((path + operation + str(statusCode)).encode()).hexdigest()
    
    def __initialize_contract_data(self, contract):
        if 'produces' in contract:
            self.contentTypes['global'] = contract['produces']
        self.__collect_paths(contract['paths'])
    
    def __collect_paths(self, paths):
        for path, pathData in paths.items():
            normalizedPath = normalize_path(path)
            self.paths.append(normalizedPath)
            self.operations[normalizedPath] = []
            
            self.__collect_operations(normalizedPath, pathData)

    def __collect_operations(self, pathName, pathData):
        for operation, operationData in pathData.items():
            normalizedOperation = normalize_operation(operation)
            self.operations[pathName].append(normalizedOperation)
            index = self.__index_key(pathName, normalizedOperation)
            self.statusCodes[index] = []

            if 'produces' in operationData:
                self.contentTypes[index] = operationData['produces']
            
            self.__collect_status_codes(pathName, normalizedOperation, index, operationData['responses'])

    def __collect_status_codes(self, path, operation, index, statusCodes):
        for statusCode, statusCodeData in statusCodes.items():
            self.statusCodes[index].append(normalize_status_code(statusCode))
            statusCodeIndex = self.__index_key(path, operation, statusCode)
            if 'schema' in statusCodeData:
                self.schemas[statusCodeIndex] = statusCodeData['schema']


class EndpointNotDefinedException(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class InvalidResponseBodySchemaException(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class InvalidResponseContentTypeException(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


def normalize_path(path):
    if path.endswith('/'):
        path = path[:-1]
    return path

def normalize_operation(operation):
    return operation.upper()

def normalize_status_code(statusCode):
    return int(statusCode)
