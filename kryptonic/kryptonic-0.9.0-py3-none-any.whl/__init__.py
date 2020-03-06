# Main unit test definitions. Mimicks python's unittest
from .krtest import *
from . import keys

import unittest

from pprint import pprint
import inspect
from .options import Config
from unittest import TestLoader, TextTestRunner
from os import path, getcwd
import logging
import json


def main(pattern='test*.py', config={}, argv=None, start_directory='.', config_file=None, config_args=None,
         config_json=None, test_runner=TextTestRunner()):
    """
    Arguments in main should map to the cli arguments in __main__.py, so that kryptonic suites can run via
    cli or python.

    :param pattern: files to match when discovering unit tests.
    :param config: Dict of config options
    :param argv:
    :param start_directory: the start directory to search in, default '.'
    :param config_file: json file to load config options from
    """
    if config is None:
        config = {}

    # _CALLEE__FILE__ = inspect.getmodule(inspect.stack()[1][0]).__file__  # https://stackoverflow.com/a/13699329
    config_options = Config()
    config_options.__init__(**config)
    update_config_from_environment_variables(config_options)
    update_config_form_json(config_options, config_json)
    update_config_from_args(config_options, config_args)

    resolve_config_arguments(config_options)

    test_loader = TestLoader()
    tests = test_loader.discover(f'{getcwd()}/{start_directory}', pattern=pattern)

    print()
    print('⚗️ Pytonium Test config:\n')
    print(json.dumps(config_options.options, indent=2))

    test_runner.run(tests)


def resolve_config_arguments(config: Config):
    update_config_from_environment_variables(config)


def update_config_from_environment_variables(config: Config):
    config_environment_variables = map(lambda x: f'KR_{x.upper()}', config.DEFAULT_OPTIONS.keys())

    for env in config_environment_variables:
        value = os.environ.get(env)
        if value is not None:
            try:
                key = env.replace('KR_', '').lower()
                config.DEFAULT_OPTIONS[key] = value
            except KeyError:
                logging.warning(f'KR_WARNING: Config option {key} tried to be set from environment variable {env} but is not a valid option. Skipping.')


def update_config_from_file(file):
    pass


def update_config_form_json(config: Config, jsn: str):
    if jsn is None:
        return
    args = json.loads(jsn)
    config.overwrite_options(**args)


def update_config_from_args(config: Config, args: str):
    if args is None:
        return
    _args = {key: value for key, value in [pair.split('=') for pair in args.split(',')]}
    # _args = map(lambda x: x.split(','), args.split('='))
    config.overwrite_options(**_args)
