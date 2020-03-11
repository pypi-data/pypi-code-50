from frater.data_type import data_types
from .object import Object
from .object_detection import ObjectDetection
from .object_factory import *
from .object_functions import *
from .object_summary import *

data_types.register_class(Object.data_type(), Object)
data_types.register_class(ObjectDetection.data_type(), ObjectDetection)

__all__ = ['Object', 'ObjectDetection', 'objects_have_temporal_overlap',
           'objects_have_spatiotemporal_overlap', 'temporally_segment_object']
