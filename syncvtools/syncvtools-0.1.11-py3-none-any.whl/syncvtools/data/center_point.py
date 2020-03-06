from typing import Tuple
from syncvtools.data.image import ImgSize
from syncvtools.utils.center_point import normalize_point, validate_norm_coords, denormalize_point

class CenterPoint:
    '''
    Initially build for making detections on boxes after random angle rotation.
    It's impossible to recover bbox in initial coordinates, but it's possible to recover center point
    It was part of experiment with ensembles (rotations/flips) in 2019 and not used much since than.
    '''
    def __init__(self,
                point_norm: Tuple[float,float] = None,
                 point_abs: Tuple[int,int] = None,
                 img_size: ImgSize = None):
        self._point_norm = None
        self._img_size = None
        self._point_abs = point_abs
        if point_norm is not None:
            self._point_norm = validate_norm_coords(point_norm)

        if img_size is not None:
            self._img_size = img_size


    @property
    def point_abs(self):
        if self._point_abs is not None:
            return self._point_abs
        if self._img_size is None:
            return None
        if self._point_norm is None:
            raise Exception("Something went wrong. Box has neither abs nor normalized coordinates!")
        self._point_abs = denormalize_point(point=self._point_norm, img_size=self._img_size.as_tuple())
        return self._point_abs

    @point_abs.setter
    def point_abs(self, value):
        raise Exception("Object is immutable")

    @property
    def point_norm(self):
        if self._point_norm is not None:
            return self._point_norm
        if self._img_size is None:
            # raise Exception("Cannot infer norm box size! Call point.set_img_size((w,h)).point_norm to set img size first.")
            return None
        if self._point_abs is None:
            raise Exception("Something went wrong. Box has neither abs nor normalized coordinates!")
        self._point_norm = normalize_point(point=self._point_abs, img_size=self._img_size.as_tuple())
        return self._point_norm

    @point_norm.setter
    def point_norm(self, value):
        raise Exception("Object is immutable")

    @property
    def img_size(self):
        if self._img_size is None:
            return None
        return self._img_size

    @img_size.setter
    def img_size(self, value: ImgSize):
        self._img_size = value
