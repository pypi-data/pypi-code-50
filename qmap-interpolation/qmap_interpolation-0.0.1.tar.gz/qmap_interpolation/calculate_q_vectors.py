"""
Functions for calculating q vectors.
"""

from typing import Tuple

import numpy as np

from .utils import Size, BeamCenter

__all__ = ['calc_coordinates', 'calc_angle_vectors', 'calc_rotation_matrix', 'transform_angles_to_q']


def calc_coordinates(size: Size, beam_center: BeamCenter,
                     pixel_size: float, detector_distance: float,
                     mask: np.ndarray = None) -> np.ndarray:
    z_indices = np.arange(size.z) - beam_center.z
    y_indices = np.arange(size.y) - beam_center.y
    yy, zz = np.meshgrid(y_indices, z_indices)
    if mask is not None:
        yy, zz = yy[mask], zz[mask]

    z_coordinates = zz.flatten() * pixel_size
    y_coordinates = yy.flatten() * pixel_size
    x_coordinates = np.ones_like(y_coordinates) * detector_distance

    normalization = np.sqrt(x_coordinates ** 2 +
                            y_coordinates ** 2 +
                            z_coordinates ** 2)

    return np.array([x_coordinates,
                     y_coordinates,
                     z_coordinates]) / normalization


def calc_rotation_matrix(angle_gamma: float, angle_delta: float,
                         sample_tilt_angle: float) -> np.ndarray:
    gamma_angle = angle_gamma * np.pi / 180
    delta_angle = angle_delta * np.pi / 180
    sample_tilt_angle = sample_tilt_angle * np.pi / 180

    r_matrix_gamma = np.array([[np.cos(gamma_angle), 0, - np.sin(gamma_angle)],
                               [0, 1, 0],
                               [np.sin(gamma_angle), 0, np.cos(gamma_angle)]])
    r_matrix_delta = np.array([[np.cos(delta_angle), - np.sin(delta_angle), 0],
                               [np.sin(delta_angle), np.cos(delta_angle), 0],
                               [0, 0, 1]])
    r_matrix_chi = np.array([[np.cos(sample_tilt_angle), 0, - np.sin(sample_tilt_angle)],
                             [0, 1, 0],
                             [np.sin(sample_tilt_angle), 0, np.cos(sample_tilt_angle)]])

    return r_matrix_delta.dot(r_matrix_gamma).dot(r_matrix_chi)


def calc_angle_vectors(coordinates: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    vertical_angles = np.arcsin(coordinates[2])
    horizontal_angles = np.sign(coordinates[1]) * np.arccos(
        coordinates[0] / np.sin(np.pi / 2 - vertical_angles)
    )
    return vertical_angles, horizontal_angles


def transform_angles_to_q(vertical_angles: np.ndarray, horizontal_angles: np.ndarray,
                          angle_of_incidence: float, k0: float) -> Tuple[np.ndarray, np.ndarray]:
    angle_of_incidence = angle_of_incidence * np.pi / 180
    xy_sign = np.sign(horizontal_angles)

    q_xy = xy_sign * k0 * np.sqrt(
        (
                np.cos(vertical_angles) * np.cos(horizontal_angles) -
                np.cos(angle_of_incidence)
        ) ** 2 +
        (
                np.cos(
                    vertical_angles) * np.sin(horizontal_angles)
        ) ** 2
    )

    q_z = k0 * (np.sin(vertical_angles) + np.sin(angle_of_incidence))
    return q_xy, q_z
