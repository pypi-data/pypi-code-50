from frater.data_type import data_types
from .bouding_box_summary import *
from .bounding_box import BoundingBox
from .bounding_box_factory import *
from .bounding_box_functions import *

data_types.register_class(BoundingBox.data_type(), BoundingBox)

__all__ = ['BoundingBox', 'combine_bounding_boxes', 'compute_spatial_iou', 'convert_descriptors_to_bounding_box',
           'linear_interpolate_bounding_boxes', 'scale_bounding_box', 'get_bounding_box_summary']
