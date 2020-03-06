import boto3
from botocore.exceptions import ClientError
import json
import os

# represents AWS Secrets manager service in AWS with
# convenient methods to interact with the stored secrets
class Secretsmanager(object):
    def __init__(self):
        region_name = os.environ['AWS_DEFAULT_REGION']
        session = boto3.session.Session(
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])
        self.client = session.client(service_name='secretsmanager',region_name=region_name)

    # returns true if the secret with name "name" exists
    # returns false otherwise
    def exists(self,name):
        try:
            get_secret_value_response = self.client.get_secret_value(SecretId=name)
        except ClientError as e:
            if e.response['Error']['Code'] == 'InvalidParameterException':
                # You provided an invalid value for a parameter.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response['Error']['Code'] == 'InvalidRequestException':
                # You provided a parameter value that is not valid for the current state of the resource.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response['Error']['Code'] == 'ResourceNotFoundException':
                # We can't find the resource that you asked for.
                # Deal with the exception here, and/or rethrow at your discretion.
                return False
        else:
            return True


    # returns true if the secret referenced by "name" stores
    # the key "key". Returns false otherwise
    def keyPresent(self,**kwargs):
        try:
            get_secret_value_response = self.client.get_secret_value(SecretId=kwargs['name'])
        except ClientError as e:
            if e.response['Error']['Code'] == 'InvalidParameterException':
                # You provided an invalid value for a parameter.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response['Error']['Code'] == 'InvalidRequestException':
                # You provided a parameter value that is not valid for the current state of the resource.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response['Error']['Code'] == 'ResourceNotFoundException':
                # We can't find the resource that you asked for.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
        else:
            secret_json = json.loads(get_secret_value_response['SecretString'])
            for k,v in secret_json.items():
                if k == kwargs['key']:
                    return True
            return False


    # store a new secret with name "name" and key/value content
    # "key" and "value"
    def create(self,**kwargs):
        secret_string = json.dumps({"{}".format(kwargs['key']):"{}".format(kwargs['value'])})
        try:
            result = self.client.create_secret(Name=kwargs['name'],SecretString='{}'.format(secret_string))
            return result
        except ClientError as e:
            if e.response['Error']['Code'] == 'InvalidParameterException':
                # You provided an invalid value for a parameter.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response['Error']['Code'] == 'InvalidRequestException':
                # You provided a parameter value that is not valid for the current state of the resource.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e

    def read(self,**kwargs):
        try:
            get_secret_value_response = self.client.get_secret_value(SecretId=kwargs['name'])
        except ClientError as e:
            if e.response['Error']['Code'] == 'InvalidParameterException':
                # You provided an invalid value for a parameter.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response['Error']['Code'] == 'InvalidRequestException':
                # You provided a parameter value that is not valid for the current state of the resource.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response['Error']['Code'] == 'ResourceNotFoundException':
                # We can't find the resource that you asked for.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
        else:
            return get_secret_value_response['SecretString']

    # update existing secret "path" with additional key/value
    # pair "key" and "value"
    def update(self,**kwargs):
        try:
            get_secret_value_response = self.client.get_secret_value(SecretId=kwargs['name'])
        except ClientError as e:
            if e.response['Error']['Code'] == 'InvalidParameterException':
                # You provided an invalid value for a parameter.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response['Error']['Code'] == 'InvalidRequestException':
                # You provided a parameter value that is not valid for the current state of the resource.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response['Error']['Code'] == 'ResourceNotFoundException':
                # We can't find the resource that you asked for.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
        else:
            secret_json = json.loads(get_secret_value_response['SecretString'])
            secret_json[kwargs['key']] = kwargs['value']
            try:
                update_secret_value_response = self.client.update_secret(SecretId=kwargs['name'],SecretString='{}'.format(json.dumps(secret_json)))
                return update_secret_value_response
            except ClientError as e:
                if e.response['Error']['Code'] == 'InvalidParameterException':
                    # You provided an invalid value for a parameter.
                    # Deal with the exception here, and/or rethrow at your discretion.
                    raise e
                elif e.response['Error']['Code'] == 'InvalidRequestException':
                    # You provided a parameter value that is not valid for the current state of the resource.
                    # Deal with the exception here, and/or rethrow at your discretion.
                    raise e

    # get the list of keys for secret "name"
    def getKeys(self,**kwargs):
        try:
            get_secret_value_response = self.client.get_secret_value(SecretId=kwargs['name'])
        except ClientError as e:
            if e.response['Error']['Code'] == 'InvalidParameterException':
                # You provided an invalid value for a parameter.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response['Error']['Code'] == 'InvalidRequestException':
                # You provided a parameter value that is not valid for the current state of the resource.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response['Error']['Code'] == 'ResourceNotFoundException':
                # We can't find the resource that you asked for.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
        else:
            secret_json = json.loads(get_secret_value_response['SecretString'])
            return list(secret_json.keys())
