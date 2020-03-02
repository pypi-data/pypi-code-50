"""
The library settings and state
"""
import time
import logging
from multiprocessing import Queue, Pipe, Process
import requests

from .errors import TesLibError
from .test_event_store import event_store_run_loop
from .add_event_web_server import run_webserver
from .messages import ShutdownMessage, ResetMessage
from .constants import DEFAULT_LOG_LEVEL, DEFAULT_PORT, DEFAULT_IP, DEFAULT_LOG_FORMAT


class _TesLib:
    def __init__(self):
        self.queue = Queue()
        self.parent_conn, self.child_conn = Pipe()

        self.ip_address = DEFAULT_IP
        self.port = DEFAULT_PORT
        self.log_level = DEFAULT_LOG_LEVEL
        self.log_format = DEFAULT_LOG_FORMAT

        self.event_store_process = None
        self.webserver_process = None

        self.stream_handler = None

        self._initialised = False

    @staticmethod
    def wait_for_webserver(ip_address: str, port: int):
        """Wait for the webserver to be up and ready

        :param ip_address: The ip_address the webserver is listening
        :param port: The port the webserver is listening on
        :return: None
        """
        timeout = 5
        url = "http://{}:{}/ready".format(ip_address, port)
        for _ in range(timeout):
            try:
                response = requests.get(url=url)
                if response.status_code == requests.codes.ok:
                    return
            except requests.exceptions.ConnectionError:
                # Webserver may not be ready to listen yet - this is what we're trying to check
                # so is expected behaviour
                pass

            time.sleep(1)

        raise RuntimeError(
            "Failed to initialise library - no response from add event webserver before timeout"
        )

    def _setup_logger(self, log_level: int, log_format: str):
        """Setup a file logger for the library

        :param log_level: Logging level to use
        :param log_format: Format of the log messages to be used
        :return: None
        """
        logger = logging.getLogger("tes_lib")
        logger.setLevel(log_level)

        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setLevel(log_level)

        formatter = logging.Formatter(log_format)
        self.stream_handler.setFormatter(formatter)

        logger.addHandler(self.stream_handler)

    def initialise(self, ip_address: str, port: int, log_level: int, log_format: str):
        """Initialise the library

        :param ip_address: The ip_address the webserver should  listen on
        :param port: The port the webserver should listen on
        :param log_level: Logging level to use
        :param log_format: Format of the log messages to be used
        :return: None
        """
        if self._initialised:
            return

        self.ip_address = ip_address
        self.port = port
        self.log_level = log_level
        self.log_format = log_format

        self._setup_logger(log_level, log_format)

        self.event_store_process = Process(
            target=event_store_run_loop, args=(self.queue, self.child_conn)
        )
        self.event_store_process.start()
        self.webserver_process = Process(target=run_webserver, args=(self.queue, ip_address, port))
        self.webserver_process.start()

        self.wait_for_webserver(ip_address, port)

        self._initialised = True

    def reset(self, timeout=5):
        """Reset the event store ready for the next test run

        :param timeout: The amount of time to give the event store to reset
        :return: None
        """
        if not self._initialised:
            return

        self.queue.put(ResetMessage())

        from .event_helpers import wait_for_response

        try:
            _ = wait_for_response("Reset test event store", self.parent_conn, timeout=timeout)
        except TesLibError:
            # If we don't get a response reset the library
            logger = logging.getLogger("tes_lib")

            logger.error("No response from event store on reset - restarting processes")

            self.cleanup()
            self.initialise(self.ip_address, self.port, self.log_level, self.log_format)

    def cleanup(self):
        """Cleanup the library

        :return: None
        """
        if not self._initialised:
            return

        self.queue.put(ShutdownMessage())
        self.event_store_process.join(timeout=3)
        self.webserver_process.terminate()
        self.webserver_process.join(timeout=3)

        logger = logging.getLogger("tes_lib")
        logger.removeHandler(self.stream_handler)

        self._initialised = False


class _TesLibInstance:

    INSTANCE = None

    @staticmethod
    def get_instance():
        """Get an instance of the TesLib class

        :return: TesLib instance
        """
        if _TesLibInstance.INSTANCE is None:
            _TesLibInstance.INSTANCE = _TesLib()
        return _TesLibInstance.INSTANCE


def initialise(
    ip_address: str = DEFAULT_IP,
    port: int = DEFAULT_PORT,
    log_level: int = DEFAULT_LOG_LEVEL,
    log_format: str = DEFAULT_LOG_FORMAT,
):
    """Initialise the library - this will start the event store and webserver processes. Each call
    of initialise should be paired with a call to cleanup.

    Calling this function multiple times without calling cleanup between will have no effect

    :param ip_address: The IP address to be used by the add event webserver
    :param port: The port to be used by the add event webserver
    :param log_level: The Logging level to be used
    :param log_format: Format of the log messages to be used
    :return: None
    """
    _TesLibInstance.get_instance().initialise(ip_address, port, log_level, log_format)


def reset_event_store():
    """Reset the test event store removing all event. This function will call cleanup followed by
    initialise if it fails to reset the event store.

    Calling this function without first calling initialise will have no effect

    :return: None
    """
    _TesLibInstance.get_instance().reset()


def cleanup():
    """Cleanup the library - this will stop the event store and webserver processes

    Calling this function multiple times without calling initialise between will have no effect

    :return: None
    """
    _TesLibInstance.get_instance().cleanup()
