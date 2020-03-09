#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Juelich Supercomputing Centre (JSC).
# Distributed under the terms of the Modified BSD License.

"""
This module creates a ParaViewWeb RemoteRenderer Widget 
in the output area below a cell in a Jupyter Notebook. 
This requires a VTK Web or ParaViewWeb server application, see 
https://kitware.github.io/paraviewweb/examples/RemoteRenderer.html#RemoteRenderer.
"""

from ipywidgets import DOMWidget, register
from traitlets import Int, Unicode
from ._frontend import module_name, module_version

@register
class SimpleRenderer(DOMWidget):
    """
    A simple ParaViewWeb RemoteRenderer Widget.

    It must be used with a VTK Web or ParaViewWeb server application, see
    https://kitware.github.io/paraviewweb/examples/RemoteRenderer.html#RemoteRenderer.

    Parameters
    ----------
        sessionURL: str
            URL where the server application is running
            Default = "ws://localhost:8080/ws"
        authKey: str
            authentication key for clients to connect to the server
            Default = "wslink-secret"
        viewID: str
            viewID of the view to connect to (only relevant if multiple views exist on the server side)
            Default = "-1"

    Examples
    --------
    From command line, start a ParaViewWeb server application.
    $ pvpython pv_server.py --port 8080 --authKey wslink-secret

    >>> from pvlink import SimpleRenderer
    >>> renderer = SimpleRenderer(sessionURL='ws://localhost:8080/ws, authkey='wslink-secret')
    >>> display(renderer)
    """
    _model_name = Unicode('RemoteRendererModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('RemoteRendererView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    sessionURL = Unicode('ws://localhost:8080/ws').tag(sync=True)
    authKey = Unicode('wslink-secret').tag(sync=True)
    viewID = Unicode('-1').tag(sync=True)
    # Placeholder to force rendering updates on change.
    _update = Int(0).tag(sync=True)

    def __init__(self, sessionURL='ws://localhost:8080/ws', authKey='wslink-secret', viewID='-1', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sessionURL = sessionURL
        self.authKey = authKey
        self.viewID = viewID

    def update_render(self):
        """Explicit call for the renderer on the javascript side to render."""
        self._update += 1