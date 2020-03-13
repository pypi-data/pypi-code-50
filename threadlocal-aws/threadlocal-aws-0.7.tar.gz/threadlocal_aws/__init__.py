import json
from os import environ
from os.path import isfile
import sys
import boto3
import requests
from urllib3.util.retry import Retry
from threading import local
from requests.adapters import HTTPAdapter

LOCAL = local()
INSTANCE_IDENTITY_URL = 'http://169.254.169.254/latest/dynamic/instance-identity/document'
PY37 = sys.version_info >= (3, 7)

def _get_retry(url, retries=5, backoff_factor=0.3,
               status_forcelist=(500, 502, 504), session=None, timeout=5):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session.get(url, timeout=5)

def session(**kwargs):
    param_name = _param_name("session", **kwargs)
    if not hasattr(LOCAL, param_name):
        setattr(LOCAL, param_name, boto3.session.Session(**kwargs))
    return getattr(LOCAL, param_name)

def _kwarg_session(**kwargs):
    if "session" in kwargs and kwargs["session"]:
        sess = kwargs["session"]
    else:
        sess = session()
    return sess

def _get_local_client(name, **kwargs):
    sess = _kwarg_session(**kwargs)
    return _get_local(name, sess.client, **kwargs)

def _get_local_resource(name, **kwargs):
    sess = _kwarg_session(**kwargs)
    return _get_local(name, sess.resource, **kwargs)

def _get_local(name, session_func, **kwargs):
    if 'region' in kwargs:
        kwargs['region_name'] = kwargs['region']
        del kwargs['region']
    if not 'region_name' in kwargs:
        # region() has one benefit over default resolving - defaults to
        # ec2 instance region if on ec2 and otherwise unset
        kwargs['region_name'] = region()
    param_name = _param_name(session_func.__name__ + "_" + name, **kwargs)
    if "session" in kwargs:
        del kwargs["session"]
    if not hasattr(LOCAL, param_name):
        setattr(LOCAL, param_name, session_func(name, **kwargs))
    return getattr(LOCAL, param_name)

def _param_name(suffix, **kwargs):
    return hex(hash(frozenset(kwargs.items())))[3:13] + "_" + suffix

def region():
    """ Get default region - the region of the instance if run in an EC2 instance
    """
    # If it is set in the environment variable, use that
    if 'AWS_DEFAULT_REGION' in environ:
        return environ['AWS_DEFAULT_REGION']
    elif 'AWS_REGION' in environ:
        return environ['AWS_REGION']
    elif 'REGION' in environ:
        return environ['REGION']
    else:
        # Otherwise it might be configured in AWS credentials
        if session().region_name:
            return session().region_name
        # If not configured and being called from an ec2 instance, use the
        # region of the instance
        elif is_ec2():
            info = json.loads(_get_retry(INSTANCE_IDENTITY_URL).text)
            return info['region']
        # Otherwise default to Ireland
        else:
            return 'eu-west-1'

def regions():
    return session().get_available_regions("s3")

def is_ec2():
    if sys.platform.startswith("win"):
        import wmi
        systeminfo = wmi.WMI().Win32_ComputerSystem()[0]
        return "EC2" == systeminfo.PrimaryOwnerName
    elif sys.platform.startswith("linux"):
        if _read_if_readable("/sys/hypervisor/uuid").startswith("ec2"):
            return True
        elif _read_if_readable("/sys/class/dmi/id/product_uuid").startswith("EC2"):
            return True
        elif _read_if_readable("/sys/devices/virtual/dmi/id/board_vendor").startswith("Amazon EC2"):
            return True
        elif _read_if_readable("/sys/devices/virtual/dmi/id/sys_vendor").startswith("Amazon EC2"):
            return True
        elif _read_if_readable("/sys/devices/virtual/dmi/id/sys_vendor").startswith("Amazon EC2"):
            return True
        elif _read_if_readable("/sys/devices/virtual/dmi/id/bios_vendor").startswith("Amazon EC2"):
            return True
        elif _read_if_readable("/sys/devices/virtual/dmi/id/chassis_vendor").startswith("Amazon EC2"):
            return True
        elif _read_if_readable("/sys/devices/virtual/dmi/id/chassis_asset_tag").startswith("Amazon EC2"):
            return True
        elif "AmazonEC2" in _read_if_readable("/sys/devices/virtual/dmi/id/modalias"):
            return True 
        elif "AmazonEC2" in _read_if_readable("/sys/devices/virtual/dmi/id/uevent"):
            return True
        else:
            return False

def _read_if_readable(filename):
    try:
        if isfile(filename):
            with open(filename) as read_file:
                return read_file.read()
        else:
            return ""
    except:
        return ""
