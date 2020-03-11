from dataclasses import dataclass, field
from uuid import uuid4

from frater.category import Category
from frater.data_type import DataType
from frater.logging import get_summary
from .object_summary import get_object_detection_summary
from ..bounding_box import BoundingBox


@dataclass
class ObjectDetection(DataType):
    object_detection_id: str = field(default_factory=lambda: str(uuid4()))
    object_type: Category = field(default_factory=lambda: Category(0, 'null', 'diva_objects'))
    bounding_box: BoundingBox = field(default_factory=BoundingBox)
    source_image: str = ''
    source_video: str = ''
    experiment: str = ''

    @property
    def confidence(self):
        return self.bounding_box.confidence

    @property
    def frame_index(self):
        return self.bounding_box.frame_index

    def summary(self, multiline=True):
        return get_summary(self, get_object_detection_summary, multiline)
