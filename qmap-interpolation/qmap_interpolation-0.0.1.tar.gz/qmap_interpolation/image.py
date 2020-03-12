"""
Image class containing data and detector geometry.
"""

from numpy import ndarray

from .utils import lazy_property
from .detector_geometry import DetectorGeometry
from .typed_tuple import TypedTuple


class Image(TypedTuple):
    raw_image: ndarray
    detector_geometry: DetectorGeometry

    @lazy_property
    def image_vector(self) -> ndarray:
        if self.detector_geometry.mask is not None:
            return self.raw_image[self.detector_geometry.mask].flatten()
        else:
            return self.raw_image.flatten()

    @property
    def q_xy(self) -> ndarray:
        return self.detector_geometry.q_xy

    @property
    def q_z(self) -> ndarray:
        return self.detector_geometry.q_z
