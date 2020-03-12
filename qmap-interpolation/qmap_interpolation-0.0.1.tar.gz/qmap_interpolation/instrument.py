"""
Instrument - a container for all constant experimental parameters:
wavelength, detector size, pixel size, hot pixel threshold.
"""
from .typed_tuple import TypedTuple
from .utils import Size


class Instrument(TypedTuple):
    wavelength: float
    size: Size
    pixel_size: float
    hot_pixel_threshold: int = None

    # def _check_inputs(self):
    #     super()._check_inputs()
    #     if self.pixel_size <= 0:
    #         raise ValueError(f'pixel_size should be a positive number, provided {self.pixel_size} instead.')
    #     if self.hot_pixel_threshold <= 0:
    #         raise ValueError(f'Hot pixel threshold is negative: {self.hot_pixel_threshold}')
