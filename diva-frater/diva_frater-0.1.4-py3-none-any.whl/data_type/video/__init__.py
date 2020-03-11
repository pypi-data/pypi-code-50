from frater.data_type import data_types
from .video import Video
from .video_summary import *

data_types.register_class(Video.data_type(), Video)

__all__ = ['Video', 'get_video_summary']
