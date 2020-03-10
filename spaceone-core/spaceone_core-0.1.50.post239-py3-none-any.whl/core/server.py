#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os

from spaceone.core import config
from spaceone.core import pygrpc
from spaceone.core import scheduler
from spaceone.core.logger import set_logger


def _get_env():
    env = {
        'PORT': os.environ.get('SPACEONE_PORT', 50051),
        'CONFIG_FILE': os.environ.get('SPACEONE_CONFIG_FILE')
    }

    env['CONFIG_FILE'] = env['CONFIG_FILE'].strip() if env['CONFIG_FILE'] else None
    return env


def _set_grpc_command(subparsers, env):
    parser = subparsers.add_parser('grpc', description='Run gRPC Server',
                                   help='Run gRPC Server', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('SERVICE', metavar='<service>', help='Service Name. (identity, inventory, etc.)')
    parser.add_argument('-p', '--port', type=int, help='gRPC Server Port', default=env['PORT'], dest='PORT')
    parser.add_argument('-f', '--file', type=argparse.FileType('r'), help='Configuration File Path',
                        default=env['CONFIG_FILE'])


def _set_scheduler_command(subparsers, env):
    parser = subparsers.add_parser('scheduler', description='Run Scheduler Server',
                                   help='Run Scheduler Server', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('SERVICE', metavar='<service>', help='Service Name. (identity, inventory, etc.)')
    parser.add_argument('-p', '--port', type=int, help='CLI Server Port', default=env['PORT'], dest='PORT')
    parser.add_argument('-f', '--file', type=argparse.FileType('r'), help='Configuration File Path',
                        default=env['CONFIG_FILE'])


def _set_rest_command(subparsers, env):
    parser = subparsers.add_parser('rest', description='Run RESTful Server',
                                   help='Run RESTful Server', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('SERVICE', metavar='<service>', help='Service Name. (identity, inventory, etc.)')
    parser.add_argument('-p', '--port', type=int, help='RESTful Server Port', default=env['PORT'], dest='PORT')
    parser.add_argument('-f', '--file', type=argparse.FileType('r'), help='Configuration File Path',
                        default=env['CONFIG_FILE'])


def _set_file_config(params):
    if params['file'] and params['file'].name:
        path = params['file'].name
        config.set_file_conf(path)


def _set_remote_config(params):
    if params['file'] and params['file'].name:
        path = params['file'].name
        config.set_remote_conf_from_file(path)


def _set_default_config():
    config.set_default_conf()


def _initialize_config(args):
    params = vars(args)

    # set server type
    config.init_conf(
        service=params['SERVICE'],
        server_type=params['server_type'],
        port=params['PORT']
    )

    # The last called method winning prioritization
    # 1. get default config from global_conf.py
    _set_default_config()

    # 2. merge file conf
    _set_file_config(params)

    # 3. merge remote conf
    _set_remote_config(params)

    # 4. env vars

    # 5. args? (the most


def _run_server():
    service = config.get_service()
    server_type = config.get_server_type()
    # set_logger()

    if server_type == 'grpc':
        pygrpc.serve()
    elif server_type == 'scheduler':
        scheduler.serve(service)
    else:
        raise NotImplementedError(f"{server_type} not implemented!")


def _parse_argument():
    env = _get_env()
    parser = argparse.ArgumentParser(description='Cloud One Server Manager')
    subparsers = parser.add_subparsers(dest='server_type', metavar='<server_type>')

    _set_grpc_command(subparsers, env)
    _set_scheduler_command(subparsers, env)
    _set_rest_command(subparsers, env)

    args = parser.parse_args()

    if args.server_type is None:
        parser.print_help()
        parser.exit()

    return args


def main():
    args = _parse_argument()
    _initialize_config(args)
    _run_server()


if __name__ == '__main__':
    main()
