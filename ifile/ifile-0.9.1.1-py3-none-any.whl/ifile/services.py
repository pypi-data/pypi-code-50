import logging
from multiprocessing import Process

from ifile.client import RpcService, FtpService
from ifile.apps.beat import BeatService

logger = logging.getLogger(__name__)

_SERVICES = {
    "rpc": RpcService,
    "ftp": FtpService,
    "beat": BeatService
}


class Services(object):
    def __init__(self):
        self.services = {}
        self._process = {}

    def register(self, name):
        service_cls = _SERVICES.get(name, None)
        service = service_cls(name)

        if service.name in self.services:
            logger.warn(f"service {service.name} already register.")
            return

        p = Process(target=service.start, name=service.name)
        self._process[service.name] = p
        self.services[service.name] = service

    def start(self, name):
        service = self.services[name]
        logger.info(f"{name} service started.")
        service.start()

    def start_all(self):
        for name, service in self.services.items():
            _process = self._process[name]
            _process.start()

            logger.info(
                f"Process {_process.pid} is running. "
                f"{name} service started.")

    def stop(self, name):
        service = self.services[name]
        service.stop()
        logger.info(f"{name} service stopped.")

    def stop_all(self):
        for name, service in self.services.items():
            service.stop()
            logger.info(f"{name} service stopped.")
