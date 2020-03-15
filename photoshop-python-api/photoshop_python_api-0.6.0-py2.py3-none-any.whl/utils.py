from contextlib import contextmanager

from photoshop.errors import COMError
from photoshop.errors import PhotoshopPythonAPIError
from photoshop.action_descriptor import ActionDescriptor
from photoshop.action_refrence import ActionReference
from photoshop.application import Application


@contextmanager
def safe_context_document(self):
    try:
        active_document = self.activeDocument.duplicate("active_context")
        try:
            yield active_document
        finally:
            active_document.close()
    except COMError:
        yield


@contextmanager
def context_document(file_path=None):
    app = Application()
    if file_path:
        yield app.open(file_path)
