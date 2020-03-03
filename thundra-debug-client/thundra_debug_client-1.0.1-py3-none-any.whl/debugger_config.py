import json
import argparse
import os
import sys

from shutil import copyfile
from os.path import expanduser

from thundradebugclient.constants import CONFIG_FILE_NAME, THUNDRA_CONFIG_DIR

home = expanduser("~")

class DebuggerConfig():

    def __init__(self):
        self.ensure_config_exists()
        self.broker_host = "debug.thundra.io"
        self.broker_port = 443
        self.auth_token = None
        self.verbose = False
        self.session_ports = {}
        self.config_file_path = None
        self.profile = "default"
        config_from_args = self.load_config_from_args()
        config = {}
        if self.config_file_path:
            config = self.load_config_from_file_path(self.config_file_path, self.profile)
        else:
            config = self.load_config_from_file_path(self.get_default_config_path(), self.profile)

        config.update(config_from_args)
        if config.get("brokerHost"):
            self.broker_host = config.get("brokerHost")
        if config.get("brokerPort"):
            self.broker_port = config.get("brokerPort")
        if config.get("authToken"):
            self.auth_token = config.get("authToken")
        if config.get("verbose"):
            self.verbose = config.get("verbose")
        if config.get("sessions"):
            self.session_ports = config.get("sessions")


    def get_default_config_path(self):
        return home + os.sep +  THUNDRA_CONFIG_DIR + os.sep + CONFIG_FILE_NAME

    def get_default_config_dir(self):
        return home + os.sep +  THUNDRA_CONFIG_DIR + os.sep

    def ensure_config_exists(self):
        if os.path.isfile(self.get_default_config_path()):
            return
        if getattr(sys, 'frozen', False):
            config_dir = sys._MEIPASS
        else:
            config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
        if not os.path.exists(self.get_default_config_dir()):
            os.makedirs(self.get_default_config_dir())
        copyfile(os.path.join(config_dir, 'debug-client.json'), self.get_default_config_path())


    def load_config_from_args(self):
        parser = argparse.ArgumentParser(description='Thundra debugger proxy agent', conflict_handler='resolve')
        group = parser.add_argument_group()

        group.add_argument('-h', '--host', action='store', type=str, help="Debug broker host")
        group.add_argument('-p', '--port', action='store', type=int, help="Debug broker port")
        group.add_argument('-a', '--auth', action='store', help="Authentication token")
        group.add_argument('-f', '--file', action='store', help="Config file path")
        group.add_argument('-r', '--profile', action='store', help="Config profile")
        group.add_argument('-v', '--verbose', action='store_true', help="Verbose mode", default=False)
        group.add_argument('-sp', nargs='+', action=DictAppendAction, metavar="KEY=VALUE", help="Session port mappings in '-sp<port>=<session-name> format'")

        args = parser.parse_args()
        config = {}

        if args.host:
            config["brokerHost"] = args.host
        if args.port:
            config["brokerPort"] = args.port
        if args.auth:
            config["authToken"] = args.auth
        if args.verbose:
            config["verbose"] = args.verbose
        if args.sp:
            config["sessions"] = args.sp
        if args.file:
            self.config_file_path = args.file
        if args.profile:
            self.profile = args.profile
        return config


    def load_config_from_file_path(self, config_file_path, profile):
        config= {}
        with open(config_file_path, 'r') as stream:
            data = json.load(stream)
            profiles = data.get('profiles')
            default_profile_config = profiles.get('default')
            config_from_file = default_profile_config
            if default_profile_config is None and profile is None:
                raise Exception('Neither default profile exist, nor profile specified')
            
            profile_config = profiles.get(profile)
            if profile_config:
                config_from_file.get('debugger').update(profile_config.get('debugger'))

            if default_profile_config is None and profile_config is None:
                raise Exception("Neither default profile exist, nor specified profile is valid")

            config_from_file = config_from_file.get('debugger')

            if config_from_file.get('brokerPort') and isinstance(config_from_file.get('brokerPort'), int):
                config["brokerPort"] = config_from_file.get('brokerPort')
            if config_from_file.get('brokerHost') and isinstance(config_from_file.get('brokerHost'), str):
                config["brokerHost"] = config_from_file.get('brokerHost')
            if config_from_file.get('authToken') and isinstance(config_from_file.get('authToken'), str):
                config["authToken"] = config_from_file.get('authToken')
            if config_from_file.get('verbose') and isinstance(config_from_file.get('verbose'), bool):
                config["verbose"] = config_from_file.get('verbose')
            if config_from_file.get('sessions') and isinstance(config_from_file.get('sessions'), dict):
                config["sessions"] = {}
                for session in config_from_file.get('sessions'):
                    config["sessions"][config_from_file['sessions'][session]] = session

        return config


class DictAppendAction(argparse.Action):
    """
    argparse action to split an argument into KEY=VALUE form
    """
    def __call__(self, parser, args, values, option_string=None):
        d = getattr(args, self.dest) or {}
        for value in values:
            try:
                k, v  = value.split('=')
                d[int(k)] = v
            except ValueError:
                raise argparse.ArgumentError(self, "could not parse argument \"{}\" as k=v format".format(k))
        setattr(args, self.dest, d)
