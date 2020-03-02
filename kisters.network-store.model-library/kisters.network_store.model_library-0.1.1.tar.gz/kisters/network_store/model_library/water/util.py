from typing import Any, Dict, Set

from kisters.network_store.model_library.base import BaseElement

from .links import _Link
from .nodes import _Node


def _get_all_subclasses(cls: Any) -> Set[Any]:
    return set(cls.__subclasses__()).union(
        (s for c in cls.__subclasses__() for s in _get_all_subclasses(c))
    )


all_links = {
    element_class.__name__: element_class
    for element_class in _get_all_subclasses(_Link)
    if not element_class.__name__.startswith("_")
}

all_nodes = {
    element_class.__name__: element_class
    for element_class in _get_all_subclasses(_Node)
    if not element_class.__name__.startswith("_")
}


def parse_object(obj: Dict[str, Any]) -> BaseElement:
    is_link = obj.get("source_uid")
    if is_link:
        elems = all_links
    else:
        elems = all_nodes
    class_name = obj.get("element_class")
    if not class_name:
        raise ValueError("Cannot instantiate: missing attribute 'element_class'")
    element_class = elems.get(class_name)
    if not element_class:
        raise ValueError(f"'{class_name}' not recognized in domain 'water'")
    return element_class.parse_obj(obj)
