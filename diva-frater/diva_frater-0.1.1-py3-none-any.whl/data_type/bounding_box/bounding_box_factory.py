from typing import Dict, Tuple

from .bounding_box import BoundingBox

__all__ = ['diva_format_to_bounding_box']


def diva_format_to_bounding_box(bounding_box: Tuple[str, Dict]) -> BoundingBox:
    frame_index, data = bounding_box
    frame_index = int(frame_index)
    x = data['boundingBox']['x']
    y = data['boundingBox']['y']
    w = data['boundingBox']['w']
    h = data['boundingBox']['h']
    confidence = data['presenceConf']
    return BoundingBox(x, y, w, h, confidence, frame_index)
