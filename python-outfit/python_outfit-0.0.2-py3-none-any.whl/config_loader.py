import logging
from .utils.logger import Logger
from .utils.io import load_yaml

class Outfit(object):
    
    path = None 
    content = None
    
    @staticmethod
    def setup(path):
        Outfit.content = load_yaml(path)
        log_config = Outfit.content['logconfig'] if 'logconfig' in Outfit.content else None

        Logger.mode = 'root'

        if log_config != None:
            mode = log_config['mode'] if 'mode' in log_config else 'root'
            source_type = log_config['source_type'] if 'source_type' in log_config else None
            source_location = log_config['source_location'] if 'source_location' in log_config else None
            Logger.setup_log(mode = mode, source_type = source_type, source_location = source_location)
        
