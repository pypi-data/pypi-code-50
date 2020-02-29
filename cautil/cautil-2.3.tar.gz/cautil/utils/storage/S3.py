from cautil.utils.storage import StorageUtilInterface
from cautil import ConfigDataException

import boto3


class S3(StorageUtilInterface):

    def __init__(self, config):
        self.client = None
        self.resource = None
        self.config = config
        self.__validate_configuration(self.config)
        self.bucket_name = self.config['s3BucketName']

    def upload_file(self, file_content, location, file_name, **kwargs):
        try:
            boto3_client = self.__get_boto3_client()
            response = boto3_client.put_object(
                Body=file_content, Bucket=self.bucket_name, Key=location+file_name)
            return {"statusCode": 200, "body": {"msg": "File uploaded successfully"}}
        except Exception as e:
            return {"statusCode": 500, "body": {"msg": str(e)}}

    def download_file(self, location, file_name, **kwargs):
        try:
            boto3_resource = self.__get_boto3_resource()
            bucket_object = boto3_resource.Bucket(self.bucket_name)
            bucket_object.download_file(
                location+file_name, self.config['s3SharedDriveLocation'] + file_name)
            return {"statusCode": 200, "body": {"msg": "File downloaded successfully", "filePath": self.config['s3SharedDriveLocation'] + file_name}}
        except Exception as e:
            return {"statusCode": 500, "body": {"msg": str(e)}}

    def copy_file(self, source, destination, file_name, remove_file_from_source, **kwargs):
        try:
            boto3_resource = self.__get_boto3_resource()
            bucket_object = boto3_resource.Bucket(self.bucket_name)
            source_object = {
                'Bucket': self.bucket_name,
                'Key': source+file_name
            }
            bucket_object.copy(source_object, destination+file_name)
            if remove_file_from_source:
                self.delete_file(source, file_name)
                return {"statusCode": 200, "body": {"msg": "File moved successfully"}}
            return {"statusCode": 200, "body": {"msg": "File copied successfully"}}
        except Exception as e:
            return {"statusCode": 500, "body": {"msg": str(e)}}

    def read_file(self, location, file_name, **kwargs):
        try:
            boto3_client = self.__get_boto3_client()
            return boto3_client.get_object(Bucket=self.bucket_name, Key=location+file_name)['Body'].read().decode('utf-8')
        except Exception as e:
            return None

    def delete_file(self, location, file_name, **kwargs):
        try:
            boto3_resource = self.__get_boto3_resource()
            s3_object = boto3_resource.Object(
                self.bucket_name, location+file_name)
            s3_object.delete()
            return {"statusCode": 200, "body": {"msg": "File deleted successfully"}}
        except Exception as e:
            return {"statusCode": 500, "body": {"msg": str(e)}}

    def __validate_configuration(self, config, **kwargs):
        config_req_param_list = [
            "s3AccessKey",
            "s3SecretKey",
            "s3BucketName",
            "sharedDriveLocation"
        ]
        for param in config_req_param_list:
            if(param not in self.config):
                raise ConfigDataException(
                    'Config param `{}` is missing'.format(param))
        return True

    def list_files(self, location, **kwargs):
        try:
            boto3_resource = self.__get_boto3_resource()
            bucket_object = boto3_resource.Bucket(self.bucket_name)
            file_list = [
                file.key for file in bucket_object.objects.filter(Prefix=location)]
            return {"statusCode": 200, "body": {"msg": 'Files listed successfully', "fileList": file_list}}
        except Exception as e:
            return {"statusCode": 500, "body": {"msg": str(e)}}

    def __get_boto3_client(self):
        if self.client is None:
            self.client = boto3.client('s3', aws_access_key_id=self.config['s3AccessKey'],
                                       aws_secret_access_key=self.config['s3SecretKey'])
        return self.client

    def __get_boto3_resource(self):
        if self.resource is None:
            self.resource = boto3.resource('s3', aws_access_key_id=self.config['s3AccessKey'],
                                           aws_secret_access_key=self.config['s3SecretKey'])
        return self.resource
