"""
This is a helper module. It rewrites the `start_webserver` function
of the wslink.server module.

To enable starting a server from within a Jupyter Notebook without
blocking the kernel, the `reactor.run` function starts in 
a Python Thread. If a second webserver is started, we cannot start 
a new reactor, so we add a new connection to the running reactor.
Returns the `wslinkServer` object so that we can access its 
`sharedObjects` attribute.
"""

import logging, sys

from wslink import websocket as wsl
from wslink.server import *

from autobahn.twisted.resource  import WebSocketResource
from twisted.web.resource       import Resource
from twisted.python             import log

def start_webserver(options, protocol=wsl.ServerProtocol, disableLogging=False):
    """
    Starts the web-server with the given protocol. Options must be an object
    with the following members:
        options.host : the interface for the web-server to listen on
        options.port : port number for the web-server to listen on
        options.timeout : timeout for reaping process on idle in seconds
        options.content : root for web-pages to serve.
    """
    from twisted.internet import reactor
    from twisted.web.server import Site
    from twisted.web.static import File
    import sys
    
    if not disableLogging:
        # redirect twisted logs to python standard logging.
        observer = log.PythonLoggingObserver()
        observer.start()
        # log.startLogging(sys.stdout)
        # Set logging level.
        if (options.debug):
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.ERROR)

    contextFactory = None

    use_SSL = False
    if options.sslKey and options.sslCert:
        use_SSL = True
        wsProtocol = "wss"
        from twisted.internet import ssl
        contextFactory = ssl.DefaultOpenSSLContextFactory(options.sslKey, options.sslCert)
    else:
        wsProtocol = "ws"

    # Create default or custom ServerProtocol
    wslinkServer = protocol()

    # create a wslink-over-WebSocket transport server factory
    transport_factory = wsl.TimeoutWebSocketServerFactory(\
            url        = "%s://%s:%d" % (wsProtocol, options.host, options.port),    \
            timeout    = options.timeout )
    transport_factory.protocol = wsl.WslinkWebSocketServerProtocol
    transport_factory.setServerProtocol(wslinkServer)

    root = Resource()

    # Do we serve static content or just websocket ?
    if len(options.content) > 0:
        # Static HTTP + WebSocket
        root = File(options.content)

    # Handle possibly complex ws endpoint
    if not options.nows:
        wsResource = WebSocketResource(transport_factory)
        handle_complex_resource_path(options.ws, root, wsResource)

    if options.uploadPath != None :
        from wslink.upload import UploadPage
        uploadResource = UploadPage(options.uploadPath)
        root.putChild("upload", uploadResource)

    if len(options.fsEndpoints) > 3:
        for fsResourceInfo in options.fsEndpoints.split('|'):
            infoSplit = fsResourceInfo.split('=')
            handle_complex_resource_path(infoSplit[0], root, File(infoSplit[1]))

    site = Site(root)

    if use_SSL:
        reactor.listenSSL(options.port, site, contextFactory)
    else:
        reactor.listenTCP(options.port, site)

    # flush ready line
    sys.stdout.flush()

    # Work around to force the output buffer to be flushed
    # This allow the process launcher to parse the output and
    # wait for "Start factory" to know that the WebServer
    # is running.
    if options.forceFlush :
        for i in range(200):
            log.msg("+"*80, logLevel=logging.CRITICAL)

    # reactor.callWhenRunning(print_ready)

    # =============================================================
    # Modification: Run `reactor.run` in thread
    # =============================================================
    # Reactor already running, we are just adding a connection
    if reactor.running:
        return wslinkServer

    from threading import Thread
    if options.nosignalhandlers:
        Thread(target=reactor.run, kwargs={'installSignalHandlers':0}).start()
    else:
        Thread(target=reactor.run, args=(False,)).start()

    return wslinkServer