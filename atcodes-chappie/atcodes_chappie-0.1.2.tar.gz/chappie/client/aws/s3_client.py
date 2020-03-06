import os


import boto3
from io import BytesIO
from datetime import datetime
from dateutil.relativedelta import relativedelta

class S3Client():

    def __init__(self):
        boto3.setup_default_session(profile_name=os.environ.get('CHAPPIE_AWS_PROFILE', 'default'))
        self.client = boto3.client('s3')
        self.bucket = None
        self.expires = None # make sure this is None or number of hours

    def upload_file(self, file_data, path, filename, params_dict):
        """ Save Bytes array data into a bucket and return FileManager Params."""
        if self.expires:
            self.client.put_object(
                            Body=file_data,
                            Bucket=self.bucket,
                            Key='%s/%s' % (path, filename),
                            Expires=datetime.now() + relativedelta(hours=self.expires),
                        )
        else:
            self.client.put_object(
                            Body=file_data,
                            Bucket=self.bucket,
                            Key='%s/%s' % (path, filename),
                        )

        waiter = self.client.get_waiter('object_exists')
        try:
            waiter.wait(
                    Bucket=self.bucket,
                    Key='%s/%s' % (path, filename),
                )
        except Exception as e:
            print(e)
            return None

        return_params_dict = params_dict.copy()
        return_params_dict['Bucket'] = self.bucket
        return_params_dict['Key'] = '%s/%s' % (path, filename)

        return return_params_dict

    def download_file(self, params_dict):
        """ Return file data as a Bytes array"""
        file_data = BytesIO()
        self.client.download_fileobj(params_dict.get('Bucket'),
                                    params_dict.get('Key'),
                                    file_data)
        return file_data.getvalue()

    def get_url(self, params_dict):
        """ Get presigned url. Expires in 300 sec."""
        url = self.client.generate_presigned_url(
                ClientMethod='get_object',
                Params={
                    "Bucket": params_dict.get('Bucket'),
                    "Key": params_dict.get('Key')
                },
                ExpiresIn=300
            )  # generate file url

        return url

    def delete_file(self, params_dict):
        """ Delete file"""
        try:
            status = self.client.delete_object(
                        Bucket=params_dict.get('Bucket'),
                        Key=params_dict.get('Key')
            )
            params_dict['Bucket'] = ''
            params_dict['Key'] = ''
            return True
        except Exception as e:
            print(e, 'while trying to delete', params_dict)
            return False

    def create_bucket(self, bucket_name):
        """
        Create a bucket. Handle exception if bucket already exists
        """
        try:
            boto_session = boto3.session.Session()
            self.client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': boto_session.region_name
                }
            )
        except Exception as e:
            print(e)

        s3_bucket_exists_waiter = self.client.get_waiter('bucket_exists')

        try:
            s3_bucket_exists_waiter.wait(Bucket='mybucket')
            return True
        except Exception as e:
            print(e)
            return False


    def put_object(self, key):
        """ Put a key into a Bucket. """
        try:
            self.client.put_object(Bucket=self.bucket, Key=key,)
        except Exception as e:
            return False

        return key
