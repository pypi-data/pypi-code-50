from typing import Any, Dict

import pytest

from kisters.network_store.model_library.util import (
    all_links,
    all_nodes,
    element_from_dict,
    element_to_dict,
)
from kisters.network_store.model_library.water.util import all_links as all_links_water
from kisters.network_store.model_library.water.util import all_nodes as all_nodes_water

elements = [
    {
        "uid": "channel",
        "source_uid": "junction",
        "target_uid": "storage",
        "stations": [
            {
                "roughness": 10.0,
                "cross_section": [
                    {"z": 0, "lr": -5},
                    {"z": 0, "lr": 5},
                    {"z": 10, "lr": -5},
                    {"z": 10, "lr": 5},
                ],
            }
        ],
        "length": 100.0,
        "model": "saint-venant",
        "roughness_model": "chezy",
        "display_name": "channel",
        "element_class": "Channel",
        "domain": "water",
    },
    {
        "uid": "delay",
        "created": "2020-03-04T11:02:16.790000+00:00",
        "source_uid": "junction",
        "target_uid": "storage",
        "transit_time": 10.0,
        "display_name": "delay",
        "element_class": "Delay",
        "domain": "water",
    },
    {
        "uid": "flow_controlled_structure",
        "source_uid": "junction",
        "target_uid": "storage",
        "min_flow": -1.0,
        "max_flow": 1.0,
        "display_name": "flow_controlled_structure",
        "element_class": "FlowControlledStructure",
        "domain": "water",
    },
    {
        "uid": "orifice",
        "source_uid": "junction",
        "target_uid": "storage",
        "model": "free",
        "coefficient": 1.0,
        "aperture": 10.0,
        "display_name": "orifice",
        "element_class": "Orifice",
        "domain": "water",
    },
    {
        "uid": "pipe",
        "source_uid": "junction",
        "target_uid": "storage",
        "diameter": 1.0,
        "length": 10.0,
        "roughness": 10.0,
        "model": "hazen-williams",
        "check_valve": False,
        "display_name": "pipe",
        "element_class": "Pipe",
        "domain": "water",
    },
    {
        "uid": "pump",
        "source_uid": "junction",
        "target_uid": "storage",
        "speed": [
            {"flow": 1, "head": 1, "speed": 1},
            {"flow": 3, "head": 3, "speed": 1},
        ],
        "min_speed": 1.0,
        "max_speed": 1.0,
        "display_name": "pump",
        "element_class": "Pump",
        "domain": "water",
    },
    {
        "uid": "turbine",
        "source_uid": "junction",
        "target_uid": "storage",
        "speed": [
            {"flow": 1, "head": 1, "speed": 1},
            {"flow": 3, "head": 3, "speed": 1},
        ],
        "min_speed": 1.0,
        "max_speed": 1.0,
        "display_name": "turbine",
        "element_class": "Turbine",
        "domain": "water",
    },
    {
        "uid": "valve",
        "source_uid": "junction",
        "target_uid": "storage",
        "diameter": 10.0,
        "model": "prv",
        "coefficient": 1.0,
        "setting": 0.0,
        "display_name": "valve",
        "element_class": "Valve",
        "domain": "water",
    },
    {
        "uid": "weir",
        "source_uid": "junction",
        "target_uid": "storage",
        "model": "free",
        "coefficient": 1.0,
        "min_crest_level": 0.0,
        "max_crest_level": 0.0,
        "crest_width": 10.0,
        "display_name": "weir",
        "element_class": "Weir",
        "domain": "water",
    },
    {
        "uid": "flow_boundary",
        "location": {"x": 0.0, "y": 0.0, "z": 0.0},
        "display_name": "flow_boundary",
        "schematic_location": {"x": 0.0, "y": 0.0, "z": 0.0},
        "element_class": "FlowBoundary",
        "domain": "water",
    },
    {
        "uid": "junction",
        "location": {"x": 0.0, "y": 1.0, "z": 0.0},
        "display_name": "junction",
        "schematic_location": {"x": 0.0, "y": 1.0, "z": 0.0},
        "element_class": "Junction",
        "domain": "water",
    },
    {
        "uid": "level_boundary",
        "location": {"x": 1.0, "y": 0.0, "z": 0.0},
        "display_name": "level_boundary",
        "schematic_location": {"x": 1.0, "y": 0.0, "z": 0.0},
        "element_class": "LevelBoundary",
        "domain": "water",
    },
    {
        "uid": "storage",
        "location": {"x": 1.0, "y": 1.0, "z": 0.0},
        "level_volume": [
            {"level": 0.0, "volume": 0.0},
            {"level": 10.0, "volume": 10.0},
        ],
        "display_name": "storage",
        "schematic_location": {"x": 1.0, "y": 1.0, "z": 0.0},
        "element_class": "Storage",
        "domain": "water",
    },
]


@pytest.mark.parametrize("element", elements)
def test_parse(element: Dict[str, Any]) -> None:
    instance = element_from_dict(element)
    reserialised = element_to_dict(instance)
    assert element == reserialised


def test_util_entry_point() -> None:
    assert all_links_water
    assert all_nodes_water
    assert set(all_links_water.values()).issubset(set(all_links))
    assert set(all_nodes_water.values()).issubset(set(all_nodes))


@pytest.mark.parametrize("element", elements)
def test_correct_element_class(element: Any) -> None:
    instance = element_from_dict(element)
    assert instance.element_class == instance.__class__.__name__
