import os
from typing import (
    List,
    Dict,
    Any,
    Callable
)

from settings_manager.yaml import load_yaml_file_data
from settings_manager.json import load_json_file_data
from settings_manager.python import load_python_file_data

SETTINGS_FILETYPES = ['python', 'json', 'yaml', 'yml']

def settings_file_paths(settings_dir: str, environment: str, filetype: str) -> List[str]:
    if filetype == 'python':
        return [os.path.join(settings_dir, '{}.py'.format(environment))]
    elif filetype == 'json':
        return [os.path.join(settings_dir, '{}.json'.format(environment))]
    elif _is_yaml:
        return [
            os.path.join(settings_dir, '{}.yaml'.format(environment)),
            os.path.join(settings_dir, '{}.yml'.format(environment))
        ]
    else:
        raise ValueError('unrecognized filetype: `{}`'.format(filetype))

def _ensure_valid_filetype(filetype: str) -> str:
    if filetype not in SETTINGS_FILETYPES:
        raise ValueError('unrecognized filetype: `{}`'.format(filetype))
    return filetype

def _ensure_path_exists(filepath: str) -> str:
    if not os.path.exists(filepath):
        raise ValueError('filepath does not exist: `{}`'.format(filepath))
    return filepath

def _is_yaml(file_extension: str) -> bool:
    return file_extension in ['yaml', 'yml']
        

class SettingsManager(object):

    def __init__(self, 
        environment: str,
        filetype: str,
        settings_dir: str,
        python_settings_module: str = None,
        merge_base: bool = False
    ):
        self._environment = environment
        self._filetype = _ensure_valid_filetype(filetype)
        self._settings_dir = _ensure_path_exists(settings_dir)
        self._paths = settings_file_paths(self._settings_dir, self._environment, self._filetype)
        self._settings = None
        self._merge_base = merge_base

        self._python_settings_module = python_settings_module

        if filetype == 'python' and python_settings_module == None:
            raise Exception('for python settings a module path is required')

        self._existing_paths = list(filter(lambda x: os.path.exists(x), self._paths))

        if len(self._existing_paths) == 0:
            raise Exception('no settings files exist for environment: `{}`'.format(self._environment))

        if len(self._existing_paths) == 2:
            raise Exception('two settings files exist for environment: `{}`'.format(self._environment))


    def load(self):

        settings = None

        if self._filetype == 'python':
            settings = self.load_python_settings()
        elif self._filetype == 'json':
            settings = self.load_json_settings()
        elif _is_yaml(self._filetype):
            settings = self.load_yaml_settings()

        self._settings = settings

    def settings(self):
        return self._settings


    def load_python_settings(self) -> Dict[str, Any]:
        if self._python_settings_module:
            p = '{}.{}'.format(self._python_settings_module, self._environment)
        else:
            # for loading without a module path i.e. just environment `test` or `prod`
            p = '{}'.format(self._environment)

        env_data = load_python_file_data(p)

        if self._merge_base:
            return self._merge_base_data_with_env_data(
                env_data, 
                'base.py',
                '{}.base'.format(self._python_settings_module),
                load_python_file_data,
            )
        else:
            return env_data 

    def _merge_base_data_with_env_data(
        self,
        env_data: Dict[str, Any],
        filename: str,
        load_arg: str,
        load_fn: Callable[[str], Dict[str, Any]]
    ) -> Dict[str, Any]:
        
        base_file = os.path.join(self._settings_dir, filename)
    
        if not os.path.exists(base_file):
            raise Exception('No base file exists: `{}` not found.'.format(base_file))

        result = {}
        base_data = load_fn(load_arg)

        for k1 in base_data.keys():
            result[k1] = base_data[k1]
        for k2 in env_data.keys():
            result[k2] = env_data[k2]

        return result

    def load_json_settings(self) -> Dict[str, Any]:
        p = self._existing_paths[0]
        env_data = load_json_file_data(p)

        if self._merge_base:
            return self._merge_base_data_with_env_data(
                env_data,
                'base.json',
                os.path.join(self._settings_dir, 'base.json'),
                load_json_file_data
            )
        else:
            return env_data

    def load_yaml_settings(self) -> Dict[str, Any]:
        p = self._existing_paths[0]
        env_data = load_yaml_file_data(p)

        if self._merge_base:
            base_filename = 'base.{}'.format(self._filetype)
            
            return self._merge_base_data_with_env_data(
                env_data,
                base_filename,
                os.path.join(self._settings_dir, base_filename),
                load_yaml_file_data
            )
        else:
            return env_data