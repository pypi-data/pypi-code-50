"""This module is in charge of managing the rook's module state.

The external interface for the module is Rook located in rook.rook."""

import os
import sys
import platform
import atexit
import uuid

# This must be the first import, otherwise enable_gevent_for_grpc will fail since grpc has already been imported
from rook.logger import logger

from rook.config import AgentComConfiguration

from rook.com_ws.output_ws import Output

from .augs.augs_manager import AugsManager
from .trigger_services import TriggerServices

from rook.exceptions import RookInterfaceException, RookVersionNotSupported
from rook.com_ws.agent_com_ws import AgentCom
from rook.com_ws.command_handler import CommandHandler

try:
    from .atfork import install_fork_handler, remove_fork_handler
except ImportError:
    pass


class _Singleton(object):
    """This is singleton is the class managing the module.

    It should never be referred to directly, instead use obj in this module."""

    def __init__(self):
        """Initialize the object, sets member variables."""
        self._check_version_supported()

        logger.info("Initializing Rook under process-%d", os.getpid())

        self._id = None
        self._services_started = False

        self._trigger_services = TriggerServices()
        self._command_handler = None
        self._aug_manager = None
        self._fork_handler = None

        self._agent_com = None

    def _start_trigger_services(self):
        """Start trigger services.

        Calling this method multiple times will have no effect.
        """
        # Don't double init services
        if self._services_started:
            return

        self._id = uuid.uuid4().hex
        self._output = Output(self._id)

        self._trigger_services.start()
        self._aug_manager = AugsManager(self._trigger_services, self._output)
        self._services_started = True

    def _stop_trigger_services(self):
        if not self._services_started:
            return

        self._aug_manager = None
        self._trigger_services.close()

        self._services_started = False

    def get_trigger_services(self):
        return self._trigger_services

    def connect(self, token, host, port, proxy, tags=None, labels=None, async_start=False):
        """Connect to the Agent."""
        if self._agent_com:
            raise RookInterfaceException("Multiple connection attempts not supported!")

        if install_fork_handler:
            install_fork_handler()

        logger.debug("Initiating AgentCom-\t%s:%d", host, int(port))

        labels = labels or {}
        tags = tags or []

        self._start_trigger_services()
        self._agent_com = AgentCom(self._id, host, port, proxy, token, labels, tags)
        self._command_handler = CommandHandler(self._agent_com, self._aug_manager)
        self._output.set_agent_com(self._agent_com)
        self._agent_com.start()
        if async_start is False:
            self._agent_com.wait_for_ready(AgentComConfiguration.TIMEOUT)

    def flush(self):
        self._output.flush_messages()

    def stop(self):
        logger.debug("Shutting down")

        if self._agent_com is not None:
            self._agent_com.stop()
        self._agent_com = None

        self._stop_trigger_services()

    def pre_fork(self):
        # AgentCom is fork safe (the child will lose the thread) so there's nothing we need to do with it
        self._trigger_services.pre_fork()

    def post_fork_recover(self):
        self._trigger_services.post_fork()

    def post_fork_clean(self):
        self._trigger_services.post_fork()

        self._command_handler = None

        if self._agent_com:
            self._agent_com.stop()
            self._agent_com = None

        self._stop_trigger_services()
        if remove_fork_handler:
            remove_fork_handler()

    @staticmethod
    def _check_version_supported():
        try:
            supported_platforms = ['pypy', 'cpython']
            supported_version = ['2.7', '3.5', '3.6', '3.7', '3.8']

            current_platform = platform.python_implementation().lower()
            if current_platform not in supported_platforms:
                raise RookVersionNotSupported("Rook is not supported in this platform: " + current_platform)

            major, minor, _, _, _ = sys.version_info
            current_version = "{}.{}".format(major, minor)
            if current_version not in supported_version:
                raise RookVersionNotSupported("Rook is not supported in this python version: " + current_version)

        except Exception as e:
            import traceback
            traceback.print_exc()

            raise e


singleton_obj = _Singleton()


def exit_handler():
    try:
        logger.info("Exit handler called - flushing and closing WebSocket")
        if singleton_obj._agent_com:
            singleton_obj.flush()
            singleton_obj._agent_com.stop()
    except:
        logger.exception("Flush and close failed")
    logger.info("Exit handler finished")


atexit.register(exit_handler)
