import os
import pathlib
import errno


class LocalClient():

    def __init__(self):
        """ """
        self.bucket = ""
        self.base_dir = ""

    def upload_file(self, file_data, path, filename, params_dict):
        """ Save Bytes array data into file and return FileManager Params."""
        abs_path = os.path.join(self.base_dir, 'file_manager', self.bucket, path)
        if not os.path.exists(abs_path):
            try:
                os.makedirs(abs_path)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise e

        with open(os.path.join(abs_path, filename), 'wb') as file:
            file.write(file_data)
            file.close()

        # params_dict['Filename'] = os.path.join(self.bucket, path, filename)
        return_params_dict = params_dict.copy()
        return_params_dict['Bucket'] = self.bucket
        return_params_dict['Key'] = '%s/%s' % (path, filename)
        return return_params_dict

    def download_file(self, params_dict):
        """ Return file data as a Bytes array"""
        filename = params_dict.get('Key')
        bucket = params_dict.get('Bucket')
        abs_path = os.path.join(self.base_dir, 'file_manager', bucket, filename)

        file_data = b''
        if filename:
            try:
                with open(abs_path, 'rb') as file:
                    # if file.exists():
                    file_data = file.read()
                    file.close()
            except:
                file_data = b''

        return file_data

    def get_url(self, params_dict):
        """ Return local file as a url resource"""
        filename = params_dict.get('Key')
        bucket = params_dict.get('Bucket')
        abs_path = os.path.join(self.base_dir, 'file_manager', bucket, filename)
        url = ''
        if filename:
            url = pathlib.Path(abs_path).as_uri()

        return url

    def delete_file(self, params_dict):
        """ Delete file """
        filename = params_dict.get('Key')
        bucket = params_dict.get('Bucket')
        abs_path = os.path.join(self.base_dir, 'file_manager', bucket, filename)
        master_bucket = os.path.join(self.base_dir, 'file_manager', self.bucket)
        file_path = os.path.dirname(abs_path)

        if filename is not None:
            try:
                os.remove(abs_path)
                params_dict["Key"] = ""

                # delete subfolders if they are empty
                for root, dirs, files in os.walk(master_bucket, topdown=False):
                    
                    # for macosx
                    try:
                        os.remove(os.path.join(root, '.DS_Store'))
                    except:
                        pass

                    if len(os.listdir(root)) == 0 and root != master_bucket:
                        os.rmdir(root)

                return params_dict
            except OSError:  ## if failed, report it back to the user ##
                return params_dict
        else:
            params_dict["Key"] = ""
            return params_dict

    def create_bucket(self, bucket_name):
        """
        Create a bucket. Handle exception if bucket already exists
        """
        full_path = os.path.join(self.base_dir, 'file_manager', bucket_name)
        try:
            os.makedirs(full_path)
        except OSError as e:
            raise e

        return full_path

    def put_object(self, key):
        """ Put a key into a Bucket. """
        abs_path = os.path.join(self.base_dir, 'file_manager', self.bucket, key)
        if not os.path.exists(abs_path):
            try:
                os.makedirs(abs_path)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise e

        return abs_path
