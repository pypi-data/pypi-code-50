from lxml.etree import tostring
from .composer import Composer


def json_to_xml(data, namespaces=None):
    composer = Composer(namespaces=namespaces)
    return tostring(composer.compose(data))
