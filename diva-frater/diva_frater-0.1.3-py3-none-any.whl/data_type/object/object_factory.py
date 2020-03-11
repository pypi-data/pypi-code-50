from typing import Dict
from uuid import UUID

from frater.dataset import dataset_factory
from .object import Object
from ..trajectory.trajectory_factory import *

__all__ = ['diva_format_to_object', 'object_to_diva_format']


def object_to_diva_format(obj: Object) -> Dict:
    return {
        'objectID': UUID(obj.object_id).int,
        'objectType': obj.object_type.label,
        'localization': {
            obj.source_video: {
                str(bounding_box.frame_index): {
                    'boundingBox': {
                        'x': bounding_box.x,
                        'y': bounding_box.y,
                        'w': bounding_box.w,
                        'h': bounding_box.h
                    },
                    'presenceConf': bounding_box.confidence
                } for bounding_box in obj.trajectory.bounding_boxes}}
    }


def diva_format_to_object(obj: Dict) -> Object:
    object_type = dataset_factory['diva_objects'].get_category_by_label(obj['objectType'])
    source_video = list(obj['localization'].keys())[0]
    trajectory = diva_format_to_trajectory(obj['localization'][source_video])
    object_id = str(UUID(int=obj['objectID']))
    return Object(object_id=object_id, object_type=object_type, trajectory=trajectory, source_video=source_video)
