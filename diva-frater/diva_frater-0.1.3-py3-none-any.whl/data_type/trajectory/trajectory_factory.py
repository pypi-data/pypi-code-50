from typing import Dict

from .trajectory import Trajectory
from ..bounding_box.bounding_box_factory import *

__all__ = ['diva_format_to_trajectory']


def diva_format_to_trajectory(trajectory: Dict) -> Trajectory:
    bounding_boxes = list()
    for bounding_box in trajectory.items():
        if 'boundingBox' not in bounding_box[1] or 'presenceConf' not in bounding_box[1]:
            continue
        bounding_boxes.append(diva_format_to_bounding_box(bounding_box))

    return Trajectory(bounding_boxes)
