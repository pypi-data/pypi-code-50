# vim: set ft=python fileencoding=utf-8 tw=72 fdm=indent nowrap:
"""
    pynfact.server
    ~~~~~~~~~~~~~~

    Simple server for testing purposes.

    :copyright: (c) 2012-2020, J. A. Corbal
    :license: MIT
"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import sys


class Server:
    """Simple server."""

    def __init__(self, host='127.0.0.1', port=4000, path='_build',
            verbose=True):
        """Constructor."""
        self.port = port
        self.host = host
        self.path = path
        self.verbose = verbose


    def serve(self):
        """Serves in a specific directory and waits until keyboard
           interrupt.
        """
        try:
            os.chdir(self.path)
        except FileNotFoundError:
            sys.exit("pynfact.server: deploy directory not found")

        httpd = HTTPServer((self.host, self.port),
                    SimpleHTTPRequestHandler)
        if self.verbose:
            print("Serving", self.host, self.port, "at", self.path)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            if self.verbose:
                sys.stderr.write("Interrupted")

