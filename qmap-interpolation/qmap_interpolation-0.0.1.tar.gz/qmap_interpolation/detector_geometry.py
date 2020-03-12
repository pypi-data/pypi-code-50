"""
Detector geometry container.
"""
from typing import Tuple

import numpy as np

from .instrument import Instrument
from .utils import lazy_property, BeamCenter
from .typed_tuple import TypedTuple
from .calculate_q_vectors import (calc_coordinates,
                                  calc_rotation_matrix,
                                  calc_angle_vectors,
                                  transform_angles_to_q)


class DetectorGeometry(TypedTuple):
    instrument: Instrument
    beam_center: BeamCenter
    angle_of_incidence: float
    detector_distance: float
    sample_tilt_angle: float = None
    angle_delta: float = 0
    angle_gamma: float = 0
    mask: np.ndarray = None

    @property
    def wavelength(self) -> float:
        """
        Wavelength in nm.
        :return:
        """
        return self.instrument.wavelength

    @lazy_property
    def k0(self) -> float:
        return 2 * np.pi / self.wavelength

    @lazy_property
    def number_of_pixels(self) -> int:
        return self.instrument.size.y * self.instrument.size.z

    def _check_inputs(self) -> None:
        if self.sample_tilt_angle is None:
            self.sample_tilt_angle = - self.angle_of_incidence

    @lazy_property
    def q_vectors(self):
        return self._calculate_q_map()

    @property
    def q_xy(self):
        return self.q_vectors[0]

    @property
    def q_z(self):
        return self.q_vectors[1]

    def _calculate_q_map(self) -> Tuple[np.ndarray, np.ndarray]:
        coordinates = calc_coordinates(self.instrument.size,
                                       self.beam_center,
                                       self.instrument.pixel_size,
                                       self.detector_distance,
                                       self.mask)
        rotation_matrix = calc_rotation_matrix(self.angle_gamma, self.angle_delta,
                                               self.sample_tilt_angle)
        coordinates = rotation_matrix.dot(coordinates)
        vertical_angles, horizontal_angles = calc_angle_vectors(coordinates)
        q_xy, q_z = transform_angles_to_q(
            vertical_angles, horizontal_angles, self.angle_of_incidence,
            self.k0)
        return q_xy, q_z

