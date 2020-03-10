#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Juelich Supercomputing Centre (JSC).
# Distributed under the terms of the Modified BSD License.

"""
This module creates a ParaViewWeb RemoteRenderer Widget in the output
area below a cell in a Jupyter Notebook. It automatically starts a 
ParaViewWeb server, which can optionally be connected to a pvserver. 
Views and sources can be manipulated from within the notebook.

Notes
-----
    This requires the ParaView Python module.
"""

import argparse
import binascii
import os

from ipywidgets import DOMWidget, register
from traitlets import Int, Unicode
from ._frontend import module_name, module_version

from .server import start_webserver
from .utility import find_next_free_port
from wslink import server
server.start_webserver = start_webserver

@register
class RemoteRenderer(DOMWidget):
    """
    A ParaViewWeb RemoteRenderer Widget which automatically starts a
    ParaViewWeb server. Optionally connects to a pvserver, 
    if a pvserver host is specified.

    The arguments for the ParaViewWeb server can be passed as kwargs.
    If no port and/or authentication key are specified, the server will
    be started on the next free port starting from 8080 and/or a 
    random authentication key will be generated.

    Parameters
    ----------
    pvserverHost: str
        if not None, create a connection to a pvserver at the given host
        upon start of the ParaViewWeb server.
        Default = None
    pvserverPort: str
        port on which the pvserver is listening 
        Default = 11111
    viewID: str
        viewID of the view to connect to 
        (only relevant if multiple views exist on the server side)
        Default = "-1"
    baseURL: str
        the baseURL under which the ParaViewWeb server will be started.
        If the notebook is running under `http://localhost:8888`, 
        the baseURL would be `localhost`.
        If Jupyter Server Proxy is being used, the baseURL is the part
        in front of "proxy". So if your notebook url is `http://localhost:8888`
        and you would access a process using `http://localhost:8888/proxy/8080`,
        the baseURL would be `localhost:8888`.
        Default = "localhost"
    useJupyterServerProxy: bool
        whether the connection should be established using Jupyter Server Proxy.
        If True, the baseURL needs to be adjusted accordingly.
        Default = False
    useJupyterServerProxyHttps: bool
        whether the connection should be established using Jupyter Server Proxy
        using wss. Use this if your notebook server is running on HTTPS.
        Beware, communication behind the proxy will still be unencrypted if
        your webserver was not started on HTTPS (using a SSL key and certificate).
        Default = False
    disableExternalPort: bool
        Disables port checking during the WebSocket opening handshake.
        Needed when using Jupyter Server Proxy to prevent a port mismatch error 
        since the notebook and the webserver do not run on the same port.
        Default = False
    protocol: pv_wslink.PVServerProtocol
        a custom PVServerProtocol class which handles clients requests and run
        a default pipeline exactly once
        Default = None
    **kwargs
        arguments, which would usually be passed to the ParaViewWeb 
        server application on the command line can be specified here. 
        For example, to specify a port, pass `port=1234` or `p=1234`.
        Flags, that are set without value, should be passed with 
        the value True. For example, `--debug` becomes `debug=True`.
        
        For help on all possible arguments, 
        use the `webserver_arguments_help` function.

    Examples
    --------
    >>> from pvlink import RemoteRenderer
    >>> from paraview import simple
    >>> from pvlink.utility import SetRecommendedRenderSettings
    >>> view = simple.CreateView('RenderView', 'ConeView')
    >>> SetRecommendedRenderSettings(view)
    >>> source = simple.Cone()
    >>> simple.Show(source, view)
    >>> renderer = RemoteRenderer(port=1234) # starts a server on port 1234
    >>> display(renderer)
    """
    _model_name = Unicode('RemoteRendererModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('RemoteRendererView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    sessionURL = Unicode().tag(sync=True)
    authKey = Unicode().tag(sync=True)
    viewID = Unicode('-1').tag(sync=True)
    # Placeholder to force rendering updates on change.
    _update = Int(0).tag(sync=True)

    def __init__(self, pvserverHost=None, pvserverPort=11111, viewID="-1", baseURL='localhost', useJupyterServerProxy=False, useJupyterServerProxyHttps=False, disableExternalPort=False, protocol=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.baseURL = baseURL
        self.viewID = viewID
        self.useJupyterServerProxy = useJupyterServerProxy
        self.useJupyterServerProxyHttps = useJupyterServerProxyHttps
        self.disableExternalPort = disableExternalPort
        self.pvserverHost = pvserverHost
        self.pvserverPort = pvserverPort
        self.protocol = protocol

        self.start_webserver(**kwargs)

    def start_webserver(self, **kwargs):
        """Start a ParaViewWeb server with the given arguments."""
        from paraview.web import pv_wslink
        from paraview.web import protocols as pv_protocols

        class _CustomServer(pv_wslink.PVServerProtocol):
            """Custom PVServerProtocol class to handle clients requests."""
            # authKey = 'wslink-secret'
            pv_host = None
            pv_port = 11111

            def initialize(self):
                # Bring used components
                self.registerVtkWebProtocol(pv_protocols.ParaViewWebMouseHandler())
                self.registerVtkWebProtocol(pv_protocols.ParaViewWebViewPort())
                self.registerVtkWebProtocol(pv_protocols.ParaViewWebViewPortImageDelivery())
                # Update authentication key to use
                self.updateSecret(_CustomServer.authKey)
                # Connect to paraview server if a server is specified
                if _CustomServer.pv_host != None:
                    from paraview.simple import Connect as PVConnect
                    PVConnect(_CustomServer.pv_host, _CustomServer.pv_port)
        
        protocol = _CustomServer if self.protocol == None else self.protocol

        # Create argument parser and add arguments (imitates command line)
        parser = argparse.ArgumentParser(description="ParaView Web Server")
        # Add default arguments
        server.add_arguments(parser)

        # Extract arguments from **kwargs
        arg_list = []
        for key, value in kwargs.items():
            # Set key
            key = key.replace('_', '-')
            if len(key) > 2:
                arg_list.append('--' + key)
            else:
                arg_list.append('-' + key)
            # Set value
            if key == 'p' or key == 'port':
                arg_list.append(str(value))
            elif value == True and (key != 'f' and key != 'force-flush'):
                pass
            else:
                arg_list.append(value)
        # If no port is given, check for the next free port starting from 8080
        if 'p' not in kwargs.keys() and 'port' not in kwargs.keys():
            port = find_next_free_port(8080)
            arg_list.append('-p')
            arg_list.append(str(port))
        # If no authKey is given, create a randon authentication key
        if 'a' not in kwargs.keys() and 'authKey' not in kwargs.keys():
            authKey = binascii.hexlify(os.urandom(24)).decode('ascii')
            arg_list.append('-a')
            arg_list.append(authKey)
        args = parser.parse_args(arg_list)
        
        # Start server
        if protocol == _CustomServer:
            _CustomServer.authKey = args.authKey
            if self.pvserverHost is not None:
                _CustomServer.pv_host = self.pvserverHost
                _CustomServer.pv_port = self.pvserverPort
        else:
            protocol.authKey = args.authKey
        self.protocol = server.start_webserver(options=args, disableExternalPort=self.disableExternalPort, protocol=protocol)
        # Set authKey and URL for the WebSocket connection
        self.authKey = args.authKey
        self.port = args.port
        self.sessionURL = '{wsProtocol}://{baseURL}{use_proxy}{port}/{ws_endpoint}'.format(
            wsProtocol='wss' if (args.sslKey and args.sslCert) or self.useJupyterServerProxyHttps else 'ws',
            use_proxy='/proxy/' if self.useJupyterServerProxy or self.useJupyterServerProxyHttps else ':',
            baseURL=self.baseURL, port=args.port, ws_endpoint=args.ws
        )

    def update_render(self):
        """Explicit call for the renderer on the javascript side to render."""
        self._update += 1
        
    def get_webserver_port(self):
      """Get the port, that can be used to reach the WebSocket."""
      return self.port
        
    def get_authKey(self):
      """Get the key, used for authentification for the WebSocket connection."""
      return self.authKey

    def webserver_arguments_help():
        """Returns a string with the possile arguments for the ParaViewWeb server."""
        parser = argparse.ArgumentParser(description="ParaView Web Server")
        server.add_arguments(parser)
        return (parser.format_help()[339:])
