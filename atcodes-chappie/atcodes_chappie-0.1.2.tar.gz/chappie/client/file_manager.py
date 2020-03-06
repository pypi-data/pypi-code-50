import os
import errno


from chappie.client.aws import S3Client
from chappie.client.local import LocalClient
from chappie.utils.random_value import RandomValue

class FileManager():

    def __init__(self, settings=None):
        """
            - settings parameter contain a dict with some specifications for storage service
            - Client is selected by CHAPPIE_STORAGE_SERVICE value, defined in the settings file
        """
        self.settings = settings
        self.storage_service = os.environ.get('CHAPPIE_STORAGE_SERVICE', 'local')
        self.bucket = os.environ.get('CHAPPIE_STORAGE_BUCKET_NAME', 'main-storage-bucket-nqhnuwm4u8jakcxu')

        # FileManager class has support for aws s3 and the local system
        if self.storage_service  == "local":
            self.client = LocalClient()
        elif self.storage_service == "s3":
            self.client = S3Client()
            try:
                self.client.client.head_bucket(Bucket=self.bucket)
            except ClientError:
                self.client.create_bucket(self.bucket)
        else:
            self.client = None
            raise ValueError("Storage Service (%s) is not supported"%(self.storage_service))

        self.params_dict = {"Service": self.storage_service}
        if self.settings:
            self.client.bucket = self.settings.get('Bucket')
        else:
            self.client.bucket = self.bucket

        self.client.base_dir = os.environ.get('CHAPPIE_BASE_PROJECT_DIR', os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), '..')))

        if self.storage_service == "local":
            try:
                os.makedirs(os.path.join(self.client.base_dir, 'file_manager', self.bucket))
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise e

    def generate_file_path(self, company_id, branch_id, app_name):
        """
        Create a FileManager instance with proper Settings (dependent on the storage Service)
        Call generate_file_path() to cerate standard path to file.
        Input: company_id, branch_id, app_name. (app_name is used to organize data in the storage service)
        Return value: string
        """
        self.file_path = "%s/%s/%s"%(company_id, branch_id, app_name)
        return self.file_path

    def upload_file(self, file_data, path, filename):
        """
        Create a FileManager instance with proper Settings (dependent on the storage Service)
        Call generate_file_path() to cerate standard path to file - In rare cases, set custom path
        Call upload_file() - This calls appropriate Service client's upload file method.
        input: file_data as a bytes array. path, filename as strings
        return value: dict with parameters indicating storage location
        """
        if isinstance(file_data, bytes):
            return self.client.upload_file(file_data, path, filename, self.params_dict)
        else:
            raise ValueError("file_data should be a bytes array")

    def download_file(self, params_dict):
        """
        Create a FileManager instance with proper Settings (dependent on the storage Service)
        Call generate_file_path() to cerate standard path to file - In rare cases, set custom path
        Call download_file() - This calls appropriate Service client's download file method.
        Input: dict with parameters indicating storage location
        return value: filedata as a bytes array
        """
        return self.client.download_file(params_dict)

    def get_url(self, params_dict):
        """
        Create a FileManager instance with proper Settings (dependent on the storage Service)
        Input: dict with parameters indicating storage location
        return value: a temporary authenticated url to download file data.
        NOTE: do not store this url for future use. Call get_url whenever needed
        """
        return self.client.get_url(params_dict)

    def delete_file(self, params_dict):
        """
        Create a FileManager instance with proper Settings (dependent on the storage Service)
        Input: dict with parameters indicating storage location
        return value: Boolean indicating success or failure.
        """
        return self.client.delete_file(params_dict)

    def create_bucket(self, bucket_name):
        """
        Create a FileManager instance with proper Settings (dependent on the storage Service)
        Input: bucket name
        return value: path to new created bucket
        """
        return self.client.create_bucket(bucket_name)

    def put_object(self, key):
        """
        Create a Key object inside a Bucket
        Input: Key
        return value: path to new created object
        """
        return self.client.put_object(key)
