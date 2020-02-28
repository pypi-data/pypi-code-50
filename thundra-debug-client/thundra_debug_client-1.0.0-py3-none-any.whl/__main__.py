import sys
import logging
import threading

from thundradebugclient.debugger_config import DebuggerConfig
from thundradebugclient.debugger_agent import logger, ThreadedTCPServer, ThundraRequestHandler


def main():
    try:
        config = DebuggerConfig()
    except Exception as e:
        print("Exception on config init:" + e)
    if config.verbose:
        logger.setLevel(logging.DEBUG)
    server_threads = []

    for port in config.session_ports:
        server = ThreadedTCPServer(("localhost", port), ThundraRequestHandler)
        server.broker_host = config.broker_host
        server.broker_port = config.broker_port
        server.auth = config.auth_token
        server.session_name = config.session_ports.get(port)
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        server_threads.append(server_thread)
    
    for t in server_threads:
        t.join()


if __name__ == "__main__":
    sys.exit(main())