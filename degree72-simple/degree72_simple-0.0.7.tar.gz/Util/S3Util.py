import os
import subprocess
from sys import platform


class S3Util:

    def __init__(self, logger):
        self.log = logger

    def exec_cmd_str(self, cmd_str, retry_count=20):

        result = -1
        i = 0
        while i < retry_count and result != 0:
            i += 1
            self.log.info('try %s ' % str(i))
            try:
                result = subprocess.check_call(cmd_str, shell=True)
            except Exception as e:
                self.log.error('failed to upload list file result :%s' % str(result), str(e))

        if result != 0:
            self.log.error("retry all failed")
        else:
            self.log.info('success')

    def upload(self, file, s3_path):
        profile = s3_path.replace('s3://', '').split('/')[0]
        assert s3_path[-1] == '/', 'the target path must be a folder'


        if platform == 'win32':  # windows
            self.log.info("change to scripts directory")
            os.chdir("C:\Python27\Scripts")
            cmd_str = 'aws s3 cp {} {} --profile {}'.format(file, s3_path, profile)

        elif platform in ['linux2', 'darwin', 'linux']:  # ubuntu
            aws_path = '/usr/local/bin/'
            cmd_str = '{}aws s3 cp {} {} --profile {}'.format(aws_path, file, s3_path, profile)
        else:
            self.log.error('unknown platform', str(platform))
            return
        self.log.info('start to upload file')
        self.exec_cmd_str(cmd_str)

    def download(self, file, s3_path):
        profile = s3_path.replace('s3://', '').split('/')[0]
        if platform == 'win32':  # windows
            os.chdir("C:\Python27\Scripts")
            cmd_str = 'aws s3 cp {} {} --profile {}'.format(s3_path, file, profile)
            self.log.info("change to scripts directory")
        elif platform in ['linux2', 'darwin', 'linux']:  # ubuntu
            aws_path = '/usr/local/bin/'
            cmd_str = '{}aws s3 cp {} {} --profile {}'.format(aws_path, s3_path, file, profile)
        else:
            self.log.error('unknown platform', str(platform))
            return

        self.log.info('start to download file')
        self.exec_cmd_str(cmd_str)

