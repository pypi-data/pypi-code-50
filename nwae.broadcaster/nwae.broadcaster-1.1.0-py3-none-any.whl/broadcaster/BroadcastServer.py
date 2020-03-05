# -*- coding: utf-8 -*-

import sys
import os
import nwae.broadcaster.config.Config as cf
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
import threading
from nwae.utils.Log import Log
from inspect import getframeinfo, currentframe
from nwae.broadcaster.subscriber.SubscriberSharedSecret import SubscriberSharedSecret
from nwae.broadcaster.SubscriberList import SubscriberList
from nwae.broadcaster.FeedQueue import FeedQueue
from nwae.broadcaster.AggregateServer import AggregateServer
from nwae.broadcaster.BroadcastThread import BroadcastThread
from nwae.broadcaster.ClientWsHandler import ClientWsHandler
from nwae.broadcaster.CleanupThread import CleanupThread


#
# Feed aggregated by AggregateServer will be re-broadcasted by Broadcast Server
#
def Start_Broadcast_Server():
    obj = BroadcastServer()
    return obj

#
# Rebroadcasts feed aggregated in AggregateServer
#
class BroadcastServer:

    DEFAULT_CONFIG_FILE = '/usr/local/git/nwae/nwae.broadcaster/app.data/config/broadcaster.cf'

    class AggregateServerThread(threading.Thread):
        def __init__(self, config):
            self.config = config
            super().__init__()
            self.stoprequest = threading.Event()
            return

        def run(self):
            AggregateServer(
                feed_queue = FeedQueue.feed_queue,
                config = self.config
            ).run_aggregate_server()
            Log.important(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': Chat Aggregator API started successfully.'
            )

    #
    # Startup Initialization. Read configurations from command line.
    # The first thing we do is to process command line parameters, account, port, etc.
    # This function should be called first thing at __init__()
    #
    def __init_command_line_parameters(self):
        configfile = None
        try:
            #
            # Run like '/usr/local/bin/python3.6 -m nwae.broadcaster.BroadcastServer configfile=... port=...'
            #
            # Default values
            command_line_params = {
                cf.Config.PARAM_CONFIGFILE: None,
                cf.Config.PARAM_PORT_BROADCASTER: None
            }
            args = sys.argv

            for arg in args:
                arg_split = arg.split('=')
                if len(arg_split) == 2:
                    param = arg_split[0].lower()
                    value = arg_split[1]
                    if param in list(command_line_params.keys()):
                        command_line_params[param] = value

            return command_line_params
        except Exception as ex:
            errmsg = str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)\
                     + ': Error reading app config file "' + str(configfile)\
                     + '". Exception message ' + str(ex)
            Log.critical(errmsg)
            raise Exception(errmsg)

    def __init__(self):
        cmdline_params = self.__init_command_line_parameters()
        self.config = cf.Config.get_cmdline_params_and_init_config_singleton(
            Derived_Class = cf.Config,
            default_config_file = BroadcastServer.DEFAULT_CONFIG_FILE
        )

        #
        # Secret config of id/password must exist
        #
        secret_config_file_path = self.config.get_config(param=cf.Config.PARAM_SHARED_SECRET_FILE)
        if not os.path.isfile(secret_config_file_path):
            raise Exception(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': Secret config of id/password file "' + str(secret_config_file_path)
                + '" not exist!'
            )
        Log.important(
            str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
            + ': Secret id/password file path ok "' + str(secret_config_file_path) + '".'
        )
        SubscriberSharedSecret.singleton_config_file_path = secret_config_file_path
        SubscriberSharedSecret.init_singleton_config()

        #
        # Overwrite config file port if on command line, port is specified
        #
        if cmdline_params[cf.Config.PARAM_PORT_BROADCASTER] is not None:
            Log.important(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': Overwriting port in config file "'
                + str(self.config.get_config(param=cf.Config.PARAM_PORT_BROADCASTER))
                + '" with port specified on command line as "'
                + str(cmdline_params[cf.Config.PARAM_PORT_BROADCASTER]) + '".'
            )
            self.config.param_value[cf.Config.PARAM_PORT_BROADCASTER] = cmdline_params[cf.Config.PARAM_PORT_BROADCASTER]

        # For gunicorn to access, and will never change without a restart
        self.port = int(self.config.get_config(param=cf.Config.PARAM_PORT_BROADCASTER))
        self.host = '0.0.0.0'

        # Start Chat Aggregator in background
        BroadcastServer.AggregateServerThread(config=self.config).start()
        Log.important(
            str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
            + ': Aggregator Server starting in the background..'
        )

        # Broadcast Thread
        BroadcastThread(
            client_subscribers_list = SubscriberList.client_subscribers_list,
            mutex_client_subscribers_list = SubscriberList.mutex_client_subscribers_list,
            feed_queue = FeedQueue.feed_queue
        ).start()
        Log.important(
            str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
            + ': Broadcast Thread starting in the background..'
        )

        # Start Cleanup Thread in background
        self.cleanup_thread = CleanupThread(
            cleanup_folder = self.config.get_config(param=cf.Config.PARAM_FEED_CACHE_FOLDER),
            files_regex    = '.*.cache$',
            # 30 mins, then we clean
            max_age_secs   = 30*60
        )
        self.cleanup_thread.start()

        return

    def run(self):
        Log.info(
            str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
            + ': Starting Broadcast Server on ' + str(self.host) + ':' + str(self.port)
        )
        server = WSGIServer(
            (self.host, self.port),
            ClientWsHandler.ConnectionHandler,
            handler_class = WebSocketHandler
        )
        server.serve_forever()


if __name__ == '__main__':
    # One time initialization applies to all modules
    Log.LOGLEVEL = Log.LOG_LEVEL_INFO
    print(str(__name__) + ': Using log file path "' + str(Log.LOGFILE))
    Log.DEBUG_PRINT_ALL_TO_SCREEN = True

    svr = Start_Broadcast_Server()
    svr.run()
