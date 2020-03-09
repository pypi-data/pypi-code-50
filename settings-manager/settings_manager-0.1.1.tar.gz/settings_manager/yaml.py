import yaml
import re
import os
from typing import Dict, Any

path_matcher = re.compile(r'.*\$\{([^}^{]+)\}.*')

def path_constructor(loader, node):
    return os.path.expandvars(node.value)

class EnvVarLoader(yaml.SafeLoader):
    pass

EnvVarLoader.add_implicit_resolver('!path', path_matcher, None)
EnvVarLoader.add_constructor('!path', path_constructor)

def load_yaml_file_data(filepath: str) -> Dict[str, Any]: 
    with open(filepath, 'r') as fp:
        data = yaml.load(fp, Loader=EnvVarLoader)
    return data