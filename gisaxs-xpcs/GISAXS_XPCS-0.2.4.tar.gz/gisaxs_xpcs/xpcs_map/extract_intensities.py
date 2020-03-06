# -*- coding: utf-8 -*-
import re
from typing import Union, Tuple, List, Callable
from pathlib import Path

from h5py import File, Group
import numpy as np
from numpy import ndarray

__all__ = ['get_intensities', 'get_time_axis']

FileType = Union[File, Group, Path, str]


def get_intensities(h5file: FileType,
                    mask: ndarray, group_key: str = None,
                    time_key: str = 'time_of_frame',
                    preserve_shape: bool = False,
                    sum_along_axis: int = -1,
                    delta_time: int = 1) -> Tuple[ndarray, ndarray]:
    if mask.dtype != bool:
        raise TypeError(f'Mask dtype should be bool, provided {mask.dtype} instead.')

    return _process_file_types(h5file, func=_get_intensities_from_file,
                               mask=mask, group_key=group_key, time_key=time_key,
                               preserve_shape=preserve_shape, delta_time=delta_time,
                               sum_along_axis=sum_along_axis)


def get_time_axis(h5file: Union[File, Group, Path, str],
                  group_key: str = None,
                  time_key: str = 'time_of_frame',
                  delta_time: int = 1) -> ndarray:
    return _process_file_types(h5file, func=_get_time_axis_from_file,
                               group_key=group_key, time_key=time_key, delta_time=delta_time)


def _process_file_types(h5file: FileType, func: Callable, *args, **kwargs):
    if isinstance(h5file, (File, Group)):
        return func(h5file, *args, **kwargs)
    elif isinstance(h5file, str):
        path = Path(h5file)
    elif isinstance(h5file, Path):
        path = h5file
    else:
        raise TypeError(f'h5file should be of {FileType} type,'
                        f'provided {type(h5file)} instead.')
    if not path.is_file():
        raise FileNotFoundError(f'File {h5file} not found.')
    with File(path, 'r') as f:
        return func(f, *args, **kwargs)


def _get_time_axis_from_file(f: File, group_key: str = None,
                             time_key: str = 'time_of_frame',
                             delta_time: int = 1) -> ndarray:
    if group_key:
        f = f[group_key]

    keys = _get_sorted_keys(f, delta_time)
    t_array = np.empty(len(keys))

    for dset_number, dset_name in enumerate(keys):
        t_array[dset_number] = f[dset_name].attrs.get(time_key, dset_number)
    return t_array


def _get_intensities_from_file(f: File, mask: ndarray,
                               group_key: str = None,
                               time_key: str = 'time_of_frame',
                               preserve_shape: bool = False,
                               delta_time: int = 1,
                               sum_along_axis: int = -1) -> Tuple[ndarray, ndarray]:
    if group_key:
        f = f[group_key]

    dset_sorted_keys = _get_sorted_keys(f, delta_time)

    if preserve_shape:
        return _get_preserved_shape(f, dset_sorted_keys, mask, time_key, sum_along_axis)
    else:
        return _get_reduced_shape(f, dset_sorted_keys, mask, time_key)


def _get_preserved_shape(g: Group, keys: List[str], mask: np.ndarray,
                         time_key: str, sum_along_axis: int) -> Tuple[ndarray, ndarray]:
    time_size = len(keys)
    col_min, col_max, row_min, row_max = _get_shape(mask)

    if sum_along_axis == -1:
        intensity_array = np.empty((time_size, col_max - col_min, row_max - row_min))
    elif sum_along_axis == 0:  # sum along horizontal axis
        intensity_array = np.empty((time_size, col_max - col_min))
    elif sum_along_axis == 1:  # sum along vertical axis
        intensity_array = np.empty((time_size, row_max - row_min))
    else:
        raise ValueError(f'Sum along nonexistent axis {sum_along_axis}.')
    t_array = np.empty(time_size)

    for dset_number, dset_name in enumerate(keys):
        dataset = g[dset_name]
        intensity = dataset[row_min:row_max, col_min:col_max]
        if sum_along_axis in (0, 1):
            intensity = intensity.sum(axis=sum_along_axis)
        intensity_array[dset_number] = intensity
        t_array[dset_number] = dataset.attrs.get(time_key, dset_number)
    return intensity_array, t_array


def _get_reduced_shape(g: Group, keys: List[str], mask: ndarray,
                       time_key: str) -> Tuple[ndarray, ndarray]:
    time_size = len(keys)
    intensity_array = np.empty((time_size, np.sum(mask)))
    t_array = np.empty(time_size)

    for dset_number, dset_name in enumerate(keys):
        dataset = g[dset_name]
        intensity = dataset[mask]
        intensity_array[dset_number, :] = intensity
        t_array[dset_number] = dataset.attrs.get(time_key, dset_number)
    return intensity_array, t_array


_DIGITS_PATTERN = r'^([\s\d]+)$'


def _get_shape(mask: ndarray) -> Tuple[int, int, int, int]:
    col_sums, row_sums = mask.sum(axis=0), mask.sum(axis=1)
    col_inds = np.argwhere(col_sums == col_sums.max())
    row_inds = np.argwhere(row_sums == row_sums.max())
    col_min, col_max = col_inds.min(), col_inds.max() + 1
    row_min, row_max = row_inds.min(), row_inds.max() + 1
    if col_min == col_max or row_min == row_max:
        raise ValueError('Mask is incorrect, could not get rectangle shape.')
    return col_min, col_max, row_min, row_max


def _get_sorted_keys(f: File, delta_time: int = 1) -> List[str]:
    dset_keys = [k for k in f.keys() if re.search(_DIGITS_PATTERN, k)]
    return sorted(dset_keys, key=lambda x: int(x))[::delta_time]
