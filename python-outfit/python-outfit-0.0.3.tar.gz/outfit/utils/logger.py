import yaml
import logging.config
import logging
from .io import load_yaml 

modules = ['development', 'production']

class Logger(object):
    mode = 'development'
    loggers = []
    info = logging.getLogger(mode).info
    debug = logging.getLogger(mode).debug
    error = logging.getLogger(mode).error
    critical = logging.getLogger(mode).critical

    @staticmethod
    def load_config_from_yaml_file(source_location):
        log_config = load_yaml(source_location)
        logging.config.dictConfig(log_config)
        
        loggers = [name for name in logging.root.manager.loggerDict]
        return loggers

        
    @staticmethod
    def load_config_from_consulkv(source_location = None, consul_con = None):

        from ..hashicorp.consul_config import ConsulCon

        consul_con = ConsulCon() if consul_con == None else consul_con
        consul_con.exception_dict['path'] = source_location

        config = consul_con.get_kv('yaml')

        logging.config.dictConfig(config)

        loggers = [name for name in logging.root.manager.loggerDict]
        return loggers
 

    @staticmethod
    def load_config_from_dict(source_location, config_dict = {}):
        log_config = {} 

        if config_dict == {}:
            import importlib

            temp = importlib.import_module(source_location)
            log_config = temp.logging
        else:
            log_config = config_dict

        logging.config.dictConfig(log_config)
        
        loggers = [name for name in logging.root.manager.loggerDict]
        return loggers


    @staticmethod
    def load_config_from_json_file(source_location):

        import json
        with open(source_location, 'rt') as f:
            log_config = json.loads(f.read())
        logging.config.dictConfig(log_config)

        loggers = [name for name in logging.root.manager.loggerDict]
        return loggers


    @staticmethod
    def setup_log(mode = 'development', source_type = None, 
                  source_location = None, consul_con = None, config_dict = None):

        mode_enum = {
            'yaml_file' : lambda x: Logger.load_config_from_yaml_file(x),
            'consulkv' : lambda x: Logger.load_config_from_consulkv(x),
            'dictionary' : lambda x: Logger.load_config_from_dict(x),
            'json_file' : lambda x: Logger.load_config_from_json_file(x)
        }

        Logger.loggers= mode_enum[source_type](source_location)

        if mode not in Logger.loggers:
            raise Exception('modules for mode '+ mode +' is not found!!')
        else:
            Logger.mode = mode
 
