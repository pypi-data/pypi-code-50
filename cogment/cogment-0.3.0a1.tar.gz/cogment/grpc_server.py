import os
import atexit
import signal
import threading

from cogment.hooks_service import HooksService, TrialHooks
from cogment.agent_service import AgentService, Agent
from cogment.env_service import EnvService, Environment
from cogment.utils import list_versions

from cogment.api.hooks_pb2_grpc import add_TrialHooksServicer_to_server
from cogment.api.environment_pb2_grpc import add_EnvironmentServicer_to_server
from cogment.api.agent_pb2_grpc import add_AgentServicer_to_server

from cogment.api.environment_pb2 import _ENVIRONMENT as env_descriptor
from cogment.api.agent_pb2 import _AGENT as agent_descriptor
from cogment.api.hooks_pb2 import _TRIALHOOKS as hooks_descriptor

from cogment.errors import ConfigError
from cogment.reloader import run_with_reloader

from grpc_reflection.v1alpha import reflection
from concurrent.futures import ThreadPoolExecutor
import grpc

from distutils.util import strtobool

ENABLE_REFLECTION_VAR_NAME = 'COGMENT_GRPC_REFLECTION'
ENABLE_GRPC_SERVER_AUTORELOAD_VAR_NAME = 'COGMENT_GRPC_SERVER_RELOAD'
DEFAULT_PORT = 9000
MAX_WORKERS = 10


# A Grpc endpoint serving a cogment service
class GrpcServer:
    def __init__(self, service_type, settings, port=DEFAULT_PORT):
        print("Versions:")
        for v in list_versions(service_type).versions:
            print(f'  {v.name}: {v.version}')

        self._port = port
        self._grpc_server = grpc.server(ThreadPoolExecutor(
            max_workers=MAX_WORKERS))

        # Register service
        if issubclass(service_type, Agent):
            self._service_type = agent_descriptor
            add_AgentServicer_to_server(
                AgentService(service_type, settings), self._grpc_server)
        elif issubclass(service_type, Environment):
            self._service_type = env_descriptor
            add_EnvironmentServicer_to_server(
                EnvService(service_type, settings), self._grpc_server)
        elif issubclass(service_type, TrialHooks):
            self._service_type = hooks_descriptor
            add_TrialHooksServicer_to_server(
                HooksService(service_type, settings), self._grpc_server)
        else:
            raise ConfigError('Invalid service type')

        # Enable grpc reflection if requested
        if strtobool(os.getenv(ENABLE_REFLECTION_VAR_NAME, 'false')):
            service_names = (self._service_type.full_name, reflection.SERVICE_NAME,)
            reflection.enable_server_reflection(service_names, self._grpc_server)

        self.__auto_reload = strtobool(os.getenv(ENABLE_GRPC_SERVER_AUTORELOAD_VAR_NAME, 'false'))

        # Give the server a chance to properly shutdown when running in auto_reload mode. Note, we cannot do this
        # by capturing signals as the server is not running in the main thread, when auto_reload is on.
        if self.__auto_reload:
            self.__exit_handler = self.stop
            atexit.register(self.__exit_handler)

        # This check is required because when auto_reload is requested is on the grpc_server won't be launched from
        # the main thread so attempting to capture any of the signals below will just raise an exception.
        if threading.current_thread() is threading.main_thread():
            for sig in ('TERM', 'HUP', 'INT'):
                signal.signal(getattr(signal, 'SIG' + sig), self.stop)

    def __run(self):
        self._grpc_server.add_insecure_port(f'[::]:{self._port}')
        self._grpc_server.start()
        self._grpc_server.wait_for_termination()

        print(f"{self._service_type.full_name} service"
              f" listening on port {self._port}")

    def serve(self):
        if self.__auto_reload:
            run_with_reloader(self.__run)
        else:
            self.__run()

    def stop(self):
        if self.__exit_handler:
            atexit.unregister(self.__exit_handler)
            self.__exit_handler = None

        self._grpc_server.stop(0)
