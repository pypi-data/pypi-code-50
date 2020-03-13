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

    def __init__(self, *args, **kwargs):
        super().__init__()
        assert self.wavelength > 0, 'Wavelength should be positive.'
        assert self.pixel_size > 0, f'pixel_size should be a positive number, ' \
                                    f'provided {self.pixel_size} instead.'
        if self.hot_pixel_threshold is not None:
            assert self.hot_pixel_threshold > 0, f'Hot pixel threshold should be positive, provided ' \
                                                 f'{self.hot_pixel_threshold} instead.'
