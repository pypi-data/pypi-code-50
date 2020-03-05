"""
Vertex analysis
"""
import numpy as np
from skimage.util import view_as_windows

# List of patterns used to detect vertices
# Each element are spin angles on a grid
vertex_patterns = [
    np.deg2rad([[90], [90]]), # ising
    np.deg2rad([[0, 90, 0],[0, 0, 0], [0, 90, 0]]), # square closed
    np.deg2rad([[45.0, 135.0], [135.0, 45.0]]), # square open
    np.deg2rad([[0, -45, 0],[45, 0, 45], [0, -45, 0]]), # pinwheel diamond
    np.deg2rad([[0, 45, 0],[-45, 0, -45], [0, 45, 0]]), # pinwheel diamond
    np.deg2rad([[0, 45, 0],[135, 0, 135], [0, 45, 0]]), # pinwheel diamond
    np.deg2rad([[0, 135, 0],[45, 0, 45], [0, 135, 0]]), # pinwheel diamond
    np.deg2rad([[0, 90.0, 0], [-30.0, 0, 30.0]]), # kagome Y
    np.deg2rad([[30.0, 0, -30.0], [0, 90.0, 0]]), # kagome inverted Y
]

def find_vertices(grid, angle, win_size):
    """
    Find the vertices of a geometry

    Parameters
    ----------
    grid : Grid object
        The grid of the spin positions
    angle : 1D array
        The angles of each spin
    win_size : (height, width)
        The window size to scan the grid

    Returns a tuple (vi, vj, indices) where vi, vj are the vertex indices
    and indices is a list of spin indices corresponding to each vertex
    index.
    """
    index_grid = grid.map_values(np.arange(len(angle)), -1)
    angle_grid = grid.map_values(angle)
    angle_window = view_as_windows(angle_grid, win_size)
    index_window = view_as_windows(index_grid, win_size)

    is_vertex = np.zeros(angle_window.shape[:2], dtype=bool)
    for pattern in vertex_patterns:
        if pattern.shape == win_size:
            # compatible pattern
            match = np.all(angle_window == pattern, axis=(2,3))
            is_vertex = np.logical_or(is_vertex, match)

    vertex_indices = is_vertex.nonzero()

    spin_indices = index_window[is_vertex]
    spin_indices = [i[i>=0] for i in spin_indices]

    return vertex_indices + (spin_indices,)

def vertex_type_ising(spin, angle):
    if spin[0] == spin[1]:
        return 1
    return 2

def vertex_type_square(spin, angle):
    dir_in = [1, 1, -1, -1]
    spin = spin * dir_in
    if spin[0] == -1:
        # flipping the spins in a vertex won't change its type
        spin *= -1
    num_in = np.count_nonzero(spin == 1)

    if num_in == 2:
        if tuple(spin) == (1, -1, -1, 1):
            # Type I
            return 1
        # Type II
        return 2

    if num_in == 3 or num_in == 1:
        # Type III
        return 3

    # Type IV
    return 4

def vertex_type_tri(spin, angle):
    if angle[-1] == np.pi/2:
        # inverted Y vertex
        dir_in = [1, -1, -1]
    else:
        # Y vertex
        dir_in = [1, 1, -1]

    spin *= dir_in
    if spin[0] == -1:
        # flipping the spins in a vertex won't change its type
        spin *= -1

    num_in = np.count_nonzero(spin == 1)
    if num_in == 3:
        # Type II
        return 2

    # Type I
    return 1

def vertex_type(spin, angle):
    """ Determine the type of a vertex given its spins and angles """
    if len(spin) == 2:
        return vertex_type_ising(spin, angle)
    elif len(spin) == 3:
        return vertex_type_tri(spin, angle)
    elif len(spin) == 4:
        return vertex_type_square(spin, angle)

    raise NotImplementedError(f"Don't know about vertices of size {len(spin)}, sorry.")

def vertex_pos(pos, vertices):
    return np.array([pos[v].mean(axis=0) for v in vertices])

def vertex_mag(mag, vertices):
    return np.array([mag[v].sum(axis=0) for v in vertices])

