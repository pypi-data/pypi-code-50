from abc import ABCMeta, abstractmethod
import importlib
config = {}

class CAUtil:
    def __init__(self):
        self.config = config

    def init(self):
        print(config)
        return "a"

class EmailUtilInterface(CAUtil):
    def send(self):
        return None

def get_resource(resource_name):
    cls_name = config[resource_name]['vendor']
    cls = importlib.import_module('cautil.utils.{}.{}'.format(resource_name,cls_name))
    cls = getattr(cls, cls_name)
    obj = cls()
    obj.config = config[resource_name]
    return obj

def cautil_init(config_file_path):
    print(config_file_path)
    config['Email'] = {'vendor':'SMTP'}
    return None