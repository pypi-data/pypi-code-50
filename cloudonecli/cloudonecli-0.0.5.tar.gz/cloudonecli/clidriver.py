#  Copyright (c) 2020. Brendan Johnson. All Rights Reserved.

import sys
import signal
import json
import DeepSecurity
import SmartCheck
import argparse
from inspect import getmembers, isfunction

import logging
import __init__
from session import Session
LOG = logging.getLogger('awscli.clidriver')
LOG_FORMAT = (
    '%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s')

# Don't remove this line.  The idna encoding
# is used by getaddrinfo when dealing with unicode hostnames,
# and in some cases, there appears to be a race condition
# where threads will get a LookupError on getaddrinfo() saying
# that the encoding doesn't exist.  Using the idna encoding before
# running any CLI code (and any threads it may create) ensures that
# the encodings.idna is imported and registered in the codecs registry,
# which will stop the LookupErrors from happening.
# See: https://bugs.python.org/issue29288
u''.encode('idna')

def _set_user_agent_for_session(session):
    session.user_agent_name = 'cloudone-cli'
    session.user_agent_version = __init__.__version__


def main():
    driver = create_clidriver()
    rc = driver.main()
    return rc

def create_clidriver():
    session =  Session()
    _set_user_agent_for_session(session)
    #load_plugins(session.full_config.get('plugins', {}),
    #             event_hooks=session.get_component('event_emitter'))
    driver = CLIDriver(session=session)
    return driver

def setCLIParse():
    parser = argparse.ArgumentParser(description='Cloudone CLI')
    return parser


class CLIDriver(object):

    def __init__(self, session=None):
        #self._functions_list = [o for o in getmembers(deepsecurity) if isfunction(o[1])]
        self._functions = dir(DeepSecurity)
        if session is None:
            self.session = Session()
        else:
            self.session = session
        self._cli_data = None
        self._command_table = None
        self._argument_table = None
        self._parser = argparse.ArgumentParser(description='Cloudone CLI')
       # self.alias_loader = AliasLoader()

    def parseCommand(self):
        if len(sys.argv) < 2:
            print("Usage: <service> <command> (sub command arguments)")
            return
        self._command = sys.argv[2]
        for c in self._functions:
            if c.lower() == self._command.lower():
                self._command = c
                break
        #print(self._command)
        self._service = sys.argv[1]
        self._subcommand = sys.argv[3]
        self._arguments = sys.argv[4:]

    def FindClass(self, module):
        listing = dir (module)
        for c in listing:
            if c.lower() == self._command.lower():
                self._command = c
                break
        classToCall = getattr(module, self._command)
        return classToCall
    def FindFunction(self, rtv):
        listing = dir(rtv)
        for f in listing:
            if f.lower() == self._subcommand.lower():
                self._subcommand = f
                break
        method_to_call = getattr(rtv, self._subcommand)
        return method_to_call

    def ExecuteCommand(self):
        service = self._service.lower()
        if service == 'deepsecurity':
            config = self.session.BuildDSMConfig(profile="default")
            connection = DeepSecurity.connect.Connection(config=config)
            group_to_call = self.FindClass(module=DeepSecurity) #getattr(DeepSecurity, self._command)
            rtv = group_to_call(config=config, connection=connection)
            method_to_call = self.FindFunction(rtv=rtv)
            rtv = method_to_call(*self._arguments)
        if service == 'smartcheck':
            config = self.session.BuildSCConfig(profile="default")
            connection = SmartCheck.connect.Connection(config=config)
            group_to_call = self.FindClass(module=SmartCheck) # getattr(SmartCheck, self._command)
            rtv = group_to_call(config=config, connection=connection)
            method_to_call = self.FindFunction(rtv=rtv)
            rtv = method_to_call(*self._arguments)
        return rtv

    def printResults(self, results):
        print(json.dumps(results))
        #dic = vars(results)
        #for k in dic.keys():
        #    if isinstance(dic[k], list):
        #        #s = json.dumps(dic[k])
        #        #print(s)
        #        print(dic[k])
        #        return

    def main(self):
        self.parseCommand()
        results = self.ExecuteCommand()
        self.printResults(results)