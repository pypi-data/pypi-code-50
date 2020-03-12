"""
Interpolation of raw images to Q map.
"""

from typing import List, Tuple, Union

import numpy as np
from .q_map import QMap

from .image import Image
from box_interpolation import box_interpolation

__all__ = ['ConvertedImage']


class ConvertedImage(object):
    @property
    def images(self):
        return self._raw_image_list

    def __init__(self, images: List[Image] = None):
        self._raw_image_list = images or []

    def append_image(self, image: Image) -> None:
        self.images.append(image)

    def remove_image(self, image: Union[Image, int]) -> None:
        if isinstance(image, Image):
            try:
                self.images.remove(image)
            except TypeError:
                raise TypeError(f'Image {image} not found and cannot be removed from the image list.')
        else:
            try:
                self.images.pop(image)
            except IndexError:
                raise IndexError(f'Index {image} is out of range.')

    def clear(self):
        self._raw_image_list = []

    def calculate_converted_image(self, q_map: QMap,
                                  qxy_window: float = None, qz_window: float = None) -> np.ndarray:
        if not self.images:
            return np.array([])
        if not qxy_window:
            qxy_window = self._default_window()
        if not qz_window:
            qz_window = self._default_window()

        q_xy, q_z, images = self._get_vectors()

        if images.size != q_xy.size or images.size != q_z.size:
            raise ValueError(f'Q arrays and intensity arrays should have the same sizes. '
                             f'Instead provided: {images.size}, {q_xy.size}, {q_z.size}')

        return box_interpolation(images, q_xy, q_z,
                                 q_map.qxy_num, q_map.qz_num,
                                 q_map.qxy_start, q_map.qxy_step, qxy_window,
                                 q_map.qz_start, q_map.qz_step, qz_window)

    def _get_vectors(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        if not self.images:
            raise ValueError(f'Image list is empty.')
        images = []
        q_xy = []
        q_z = []
        for image in self.images:
            images.append(image.image_vector)
            q_xy.append(image.q_xy)
            q_z.append(image.q_z)
        images = np.concatenate(images).astype(np.float)
        q_xy = np.concatenate(q_xy)
        q_z = np.concatenate(q_z)
        return q_xy, q_z, images

    def _default_window(self):
        if not self.images:
            raise ValueError('Image list is empty.')
        detector_geometry = self.images[0].detector_geometry
        instrument = detector_geometry.instrument
        return 1.3 * 2 * np.pi / instrument.wavelength * \
               instrument.pixel_size / detector_geometry.detector_distance
