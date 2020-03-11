from frater.data_type import data_types
from .frame import Frame, CroppedFrame
from .frame_summary import *
from .modality import Modality

data_types.register_class(Frame.data_type(), Frame)
data_types.register_class(CroppedFrame.data_type(), CroppedFrame)

__all__ = ['Frame', 'CroppedFrame', 'Modality', 'get_frame_summary']
