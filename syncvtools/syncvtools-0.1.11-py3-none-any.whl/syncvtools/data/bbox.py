from typing import Tuple
import json
from syncvtools.utils.bbox import normalize_bbox, validate_norm_coords, denormalize_bbox, abs_x1y1x2y2_to_abs_x1y1wh
from syncvtools.data.image import ImgSize
from typing import Union, Tuple, Optional
import numpy as np


class Bbox:
    '''
    Class which contains bounding box coordinates. It doesn't contain things like label, since label goes as
    a property of parent class - DetectionEntity, which might also include mask or any other
    feature of that detection object.
    '''

    def __init__(self,
                 bbox_norm: Tuple[float, float, float, float] = None,
                 bbox_abs: Tuple[int, int, int, int] = None,
                 img_size: ImgSize = None):
        '''
        Either bbox_norm or bbox_abs should be set
        :param bbox_norm: x1,y1,x2,y2 coordinates in float32 [0..1] scale
        :param bbox_abs: x1,y1,x2,y2 coordinates in integer pixels scale
        :param img_size: necessary to set for conversion between norm and abs types
        '''
        if bbox_norm is None and bbox_abs is None:
            raise ValueError("Either bbox_norm or bbox_abs should be set")

        self._bbox_norm = None
        if bbox_norm is not None:
            self._bbox_norm = validate_norm_coords(bbox_norm)
        self._bbox_abs = bbox_abs

        if img_size is not None:
            self._img_size = img_size
        else:
            self._img_size = None

    def bbox_abs_x1y1wh(self) -> Union[list, tuple, np.ndarray]:
        '''
        Converting into center poing + width,height format
        :return:(x1,y1,w,h) - x,y center, and width, height
        '''
        return abs_x1y1x2y2_to_abs_x1y1wh(box_coords=self.bbox_abs)

    @property
    def bbox_abs(self) -> Optional[Tuple[int, int, int, int]]:
        '''
        If not set, will be inferred from bbox_norm. But img_size should be set for inference, otherwise None returned.
        :return:
        '''
        if self._bbox_abs is not None:
            return self._bbox_abs
        if self._img_size is None:
            # raise Exception("Cannot infer abs box size! Call bbox.set_img_size((w,h)).bbox_abs to set img size first.")
            return None
        if self._bbox_norm is None:
            raise Exception("Something went wrong. Box has neither abs nor normalized coordinates!")
        self._bbox_abs = denormalize_bbox(bbox=self._bbox_norm, img_size=self._img_size.as_tuple())
        return self._bbox_abs

    @bbox_abs.setter
    def bbox_abs(self, value):
        '''
        Bbox coordinates are immutable.
        :param value:
        :return:
        '''
        raise Exception("Box coordinates are immutable. Create new object if you want to change bbox")

    @property
    def bbox_norm(self) -> Optional[Tuple[float, float, float, float]]:
        '''

        :return: Normalized coordinates in format (x1,y1,x2,y2) with vals [0..1]
        '''
        if self._bbox_norm is not None:
            return self._bbox_norm
        if self._img_size is None:
            # raise Exception("Cannot infer norm box size! Call bbox.set_img_size((w,h)).bbox_norm to set img size first.")
            return None
        if self._bbox_abs is None:
            raise Exception("Something went wrong. Box has neither abs nor normalized coordinates!")
        self._bbox_norm = normalize_bbox(bbox=self._bbox_abs, img_size=self._img_size.as_tuple())
        return self._bbox_norm

    @bbox_norm.setter
    def bbox_norm(self, value):
        raise Exception("Box coordinates are immutable. Create new object if you want to change bbox")

    @property
    def img_size(self) -> Optional[ImgSize]:
        '''
        In some cases img_size is not set (lazy loading). Expected behaivor to return None so it can be checked.
        :return:
        '''
        if self._img_size is None:
            return None
        return self._img_size

    @img_size.setter
    def img_size(self, value: ImgSize):
        self._img_size = value

    def __str__(self):
        return json.dumps({'bbox_abs': self._bbox_abs, 'bbox_norm': self._bbox_norm,
                           'img_size': self._img_size.as_tuple() if self._img_size is not None else "None"})
