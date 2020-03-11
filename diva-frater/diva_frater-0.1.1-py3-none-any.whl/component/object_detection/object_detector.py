from dataclasses import dataclass, field
from typing import List, Set, Iterable

from frater.category import Category
from frater.component import BatchComponent, BatchComponentConfig
from frater.stream import OutputStream, InputStream
from ...data_store import FrameStoreConfig, FrameStore
from ...data_type import ObjectDetection, Frame


@dataclass
class ObjectDetectorConfig(BatchComponentConfig):
    frame_store_config: FrameStoreConfig = field(default_factory=FrameStoreConfig)
    batch_size: int = 8
    object_types: Set[Category] = field(default_factory=set)


class ObjectDetector(BatchComponent):
    def __init__(self, config: ObjectDetectorConfig, input_stream: InputStream, output_stream: OutputStream):
        super(ObjectDetector, self).__init__(input_stream, output_stream)
        self.frame_store = FrameStore.get_frame_store(config.frame_store_config)

    @property
    def object_types(self):
        return self.config.object_types

    def preprocess(self, frame):
        loaded_frame = self.frame_store.load_image_for_frame(frame)
        return super(ObjectDetector, self).preprocess(loaded_frame)

    def process(self, batch: List[Frame]) -> Iterable[ObjectDetection]:
        raise NotImplementedError
