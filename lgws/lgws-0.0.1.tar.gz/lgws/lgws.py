from pywebostv.connection import WebOSClient
from pywebostv.controls import ApplicationControl, MediaControl, SourceControl, SystemControl, InputControl, TvControl
import os, json, logging

log = logging.getLogger(__name__)

class Client(object):
    @staticmethod
    def load_config(configFile="~/.config/lgtv"):
        log.debug("Loading config from " + configFile)
        if os.path.exists(os.path.expanduser(configFile)):
            with open(os.path.expanduser(configFile), 'r') as fp:
                config = json.load(fp)

            log.debug(config)
            return config

    def __init__(self, configFile="~/.config/lgtv"):
        log = logging.getLogger(__name__)
        self.config = self.load_config(configFile) or {}

        self.ws = WebOSClient(self.config.get('host'))
        self.ws.connect()
        assert(2 in self.ws.register(self.config)), "Not registered to TV yet"
        self.ac = ApplicationControl(self.ws)
        self.ic = InputControl(self.ws)
        self.mc = MediaControl(self.ws)
        self.sc = SystemControl(self.ws)
        self.srcc = SourceControl(self.ws)
        self.tv = TvControl(self.ws)

        self.apps = {a["id"]: a for a in self.ac.list_apps()}
        # self.ac.subscribe_get_current(self.__on_app_changed)        
        # self.mc.subscribe_get_volume(self.__on_volume_changed)

        self.current = self.volume = None

    def __on_app_changed(self, status, payload):
        self.log.debug(f'app: {payload}')
        self.current = self.apps[payload]

    def __on_volume_changed(self, status, payload):
        self.log.debug(f'volume :{payload}')
        self.volume = payload