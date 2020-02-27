from cautil.utils.storage import StorageUtilInterface
from cautil import ConfigDataException

from minio import Minio
from minio.error import ResponseError


class MinIO(StorageUtilInterface):

    def __init__(self, config):
        self.client = None
        self.config = config
        self.__validate_configuration(self.config)

    def upload_file(self, file_content, location, file_name, **kwargs):
        try:
            self.__get_minio_client().fput_object(location, file_name, file_content)
            return {"statusCode": 200, "body": {"msg": "File uploaded successfully"}}
        except ResponseError as err:
            return {"statusCode": 500, "body": {"msg": str(err)}}
        except Exception as e:
            return {"statusCode": 500, "body": {"msg": str(e)}}

    def download_file(self, location, file_name, destination, **kwargs):
        try:
            self.__get_minio_client().fget_object(location, file_name, self.config['sharedDriveLocation']+destination)
            return {"statusCode": 200, "body": {"msg": "File downloaded successfully", "filePath": self.config['sharedDriveLocation'] + file_name}}
        except Exception as e:
            return {"statusCode": 500, "body": {"msg": str(e)}}

    def copy_file(self, source, destination, file_name, remove_file_from_source, **kwargs):
        try:
            copy_result = self.__get_minio_client().copy_object(bucket_name=source, object_name=destination, object_source=file_name )
            if remove_file_from_source:
                self.delete_file(source, file_name.split('/', 1)[1])
            return {"statusCode": 200, "body": {"msg": "File copied successfully"}}
        except Exception as e:
            return {"statusCode": 500, "body": {"msg": str(e)}}

    def read_file(self, location, file_name, **kwargs):
        try:
            return self.__get_minio_client().get_object(location, file_name).read().decode('utf-8')
        except Exception as e:
            return None

    def delete_file(self, location, file_name, **kwargs):
        try:
            self.__get_minio_client().remove_object(location, file_name)
            return {"statusCode": 200, "body": {"msg": "File deleted successfully"}}
        except Exception as e:
            return {"statusCode": 500, "body": {"msg": str(e)}}

    def __validate_configuration(self, config, **kwargs):
        config_req_param_list = [
            "minIOHost",
            "minIOAccessKey",
            "minIOSecretKey",
            "sharedDriveLocation"
        ]
        for param in config_req_param_list:
            if(param not in self.config):
                raise ConfigDataException(
                    'Config param `{}` is missing'.format(param))
        return True

    def list_files(self, location, prefix, **kwargs):
        try:
            file_list = [
                file.object_name for file in self.__get_minio_client().list_objects(bucket_name=location, prefix=prefix, recursive=True)]
            return {"statusCode": 200, "body": {"msg": 'Files listed successfully', "fileList": file_list}}
        except Exception as e:
            return {"statusCode": 500, "body": {"msg": str(e)}}

    def __get_minio_client(self):
        if self.client is None:
            self.client = Minio(self.config['minIOHost'], access_key=self.config['minIOAccessKey'], secret_key=self.config['minIOSecretKey'], secure=False)
        return self.client