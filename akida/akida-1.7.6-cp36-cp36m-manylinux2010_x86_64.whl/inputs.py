import numpy as np
from .core import Sparse

def coords_to_sparse(coords, shape):
    """Converts a list of coordinates to a Sparse input.

    Akida expects the spikes to be encoded as a Sparse object, where
    each coordinate corresponds to the following information:

    - first spatial coordinate (typically x, the pixel column),
    - second spatial coordinate (typically y, the pixel line),
    - a feature index representing the spike (starting from index zero)

    This function converts a numpy array of event coordinates to a Sparse object
    where the event values are set to 1.

    Args:
      coords (:obj:`numpy.ndarray`): a (n,3) array of input coordinates.
      shape (:obj:`tuple[int]`): the three dimensions of the input space.

    Returns:
      :obj:`Sparse`: the events corresponding to the specified coordinates.

    """
    if (len(coords.shape) != 2):
        raise ValueError("Coordinates array must have a (n,3) shape")
    if (coords.shape[1] != 3):
        raise ValueError("Input coordinates must have 3 dimensions")
    if (len(shape) != 3):
        raise ValueError("Input space must have 3 dimensions")
    # Set event values to 1
    data = np.ones(coords.shape[0], dtype=np.int32)
    return Sparse(shape, coords, data)

def dense_to_sparse(in_array):
    """Converts a hollow dense array to a Sparse input.

    Akida expects the spikes to be encoded as a Sparse object, where
    each coordinate corresponds to the following information:

    - first spatial coordinate (typically x, the pixel column),
    - second spatial coordinate (typically y, the pixel line),
    - a feature index representing the spike (starting from index zero)

    The input array will simply be converted to a list of events corresponding
    to its active (non-zero) coordinates.
    The event values extracted from the input array will be converted to 32 bits
    integers.

    Args:
      in_array (:obj:numpy.ndarray): an array of 1D, 2D or 3D coordinates.

    Returns:
      :obj:`Sparse`:  the events corresponding to non-null values.

    """
    if (len(in_array.shape) > 3):
        raise ValueError("Input space must have at most 3 dimensions")
    # Reshape to obtain a 3-dimensional output
    if len(in_array.shape) == 2:
        in_array = in_array[:, :, np.newaxis]
    elif len(in_array.shape) == 1:
        in_array = in_array[:, np.newaxis, np.newaxis]
    # Extract indices of non-zero pixels in the array
    coords = np.where(in_array)
    # Extract data and convert them to int32
    data = in_array[coords].astype(np.int32)
    events = Sparse(in_array.shape, np.vstack(coords).transpose(), data)
    return events
