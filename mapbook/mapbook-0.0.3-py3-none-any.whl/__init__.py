from mapbook.leafletInterface import (DivWindow, Map, imageOverlay, tileLayer, GeoJSON, vectorGrid, coordinatesControl, mapSync, show)
from IPython.display import display, Javascript, HTML, clear_output

__version__ = '0.0.3'
def _jupyter_server_extension_paths():
    return [{
        "module": "mapbook"
    }]

# Jupyter Extension points
def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        # the path is relative to the `my_fancy_module` directory
        src="static",
        # directory in the `nbextension/` namespace
        dest="mapbook",
        # _also_ in the `nbextension/` namespace
        require="mapbook/main")]

def load_jupyter_server_extension(nbapp):
    nbapp.log.info("mapbook enabled!")

