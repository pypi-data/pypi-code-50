from typing import Any, Dict, List

import pkg_resources

from fastapi.encoders import jsonable_encoder
from kisters.network_store.model_library.base import BaseElement

_object_parsers = {}
all_nodes: List[BaseElement] = []
all_links: List[BaseElement] = []
elements_mapping: Dict[str, Dict[str, Dict[str, BaseElement]]] = {}
for entry_point in pkg_resources.iter_entry_points(
    "kisters.network_store.model_library.util"
):
    ep = entry_point.load()
    elements_mapping[entry_point.name] = {
        "links": ep.all_links,
        "nodes": ep.all_nodes,
    }
    _object_parsers[entry_point.name] = ep.parse_object
    all_links.extend(ep.all_links.values())
    all_nodes.extend(ep.all_nodes.values())


def element_from_dict(obj: Dict[str, Any]) -> BaseElement:
    domain = obj.get("domain")
    if not domain:
        raise ValueError("Cannot instantiate: missing attribute 'domain'")
    parser = _object_parsers.get(domain)
    if not parser:
        raise ValueError(
            f"Cannot instantiate: attribute 'domain' value {domain} not recognized"
        )
    return parser(obj)


def element_to_dict(elem: BaseElement) -> Dict[str, Any]:
    return jsonable_encoder(elem, include_none=False)
