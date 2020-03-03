import logging
import boto3
import requests
from botocore.client import Config
from botocore.exceptions import ClientError


INSTANCE_IDENTITY_URL = 'http://169.254.169.254/2016-09-02/dynamic/instance-identity/document'


def get_region():
    # try to get configured region from the AWS environment
    region = boto3.session.Session().region_name

    # if we don't have one, try to figure it out from the INSTANCE_IDENTITY_URL
    if region is None:
        try:
            res = requests.get(INSTANCE_IDENTITY_URL, timeout=0.2)
        except Exception:
            logging.exception(f"Couldn't get {INSTANCE_IDENTITY_URL}")
            return region
        if res.status_code == 200:
            region = res.json().get('region', region)
        else:
            logging.error(f"Got {res.status_code} for {INSTANCE_IDENTITY_URL}")
    return region


class ServiceWrapper(object):
    """Wraps an AWS service behind a temporarily held and renewed if necessary
    STS token, which makes it possible to switch roles
    """

    def __init__(self, service, RoleArn=None, RoleSessionName='s1crets',
                 DurationSeconds=3600, aws_region=None,
                 boto_config=Config(connect_timeout=60, read_timeout=60,
                                    retries={'max_attempts': 3})):
        self.service = service
        self.RoleArn = RoleArn
        self.DurationSeconds = DurationSeconds
        self.RoleSessionName = RoleSessionName
        self.session = boto3.session.Session()
        self.sts = self.session.client('sts')
        self.aws_region = aws_region or get_region()
        self.boto_config = boto_config
        self.init_service()

    def init_service(self):
        kw = {}
        if self.RoleArn is not None:
            creds = self.sts.assume_role(RoleArn=self.RoleArn,
                                         RoleSessionName=self.RoleSessionName,
                                         DurationSeconds=self.DurationSeconds)
            creds = creds['Credentials']
            kw['aws_access_key_id'] = creds['AccessKeyId']
            kw['aws_secret_access_key'] = creds['SecretAccessKey']
            kw['aws_session_token'] = creds['SessionToken']
        self.wrapped_service = self.session.client(self.service,
                                                   config=self.boto_config,
                                                   region_name=self.aws_region, **kw)

    def __getattr__(self, name):
        obj = getattr(self.wrapped_service, name)
        if not callable(obj):
            return obj
        return lambda *args, **kw: self.wrapper(name, *args, **kw)

    def wrapper(self, name, *args, **kw):
        for i in range(2):
            f = getattr(self.wrapped_service, name)
            try:
                return f(*args, **kw)
            except ClientError as e:
                # on the first ExpiredTokenException try to reinit the wrapped
                # service with a new token. The session token may have expired.
                if i == 0 and e.response['Error']['Code'] == 'ExpiredTokenException':
                    self.init_service()
                # on subsequent and other exceptions just raise
                else:
                    raise
