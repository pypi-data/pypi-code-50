#!/usr/bin/env python3
import sys
import os
import numpy as np
import pandas as pd
from numpy.linalg import norm
from math import ceil, sqrt
from scipy.spatial import cKDTree
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize, LinearSegmentedColormap
from matplotlib.collections import PatchCollection
import random
import time
import itertools
from datetime import timedelta
from copy import copy
from PIL import Image
import pkg_resources

from flatspin.grid import Grid
from flatspin.vertices import find_vertices, vertex_type
from flatspin.utils import get_default_params
from flatspin.plotting import plot_vectors

normalize_rad = Normalize(vmin=0, vmax=2*np.pi)
normalize_vertex_type = Normalize(vmin=1, vmax=4)
# Type 1: green, type 2: blue, type 3: red, type 4: gray
vertex_clist = [(0,1,0), (0,0,1), (1,0,0), (.5,.5,.5)]
vertex_cmap = LinearSegmentedColormap.from_list("vertex", vertex_clist, N=4)

class LabelIndexer:
    def __init__(self, labels):
        labels = np.array(labels)
        if len(labels.shape) == 1:
            labels.shape += (1,)

        self.index = pd.MultiIndex.from_arrays(labels.T)

    def __getitem__(self, label):
        try:
            index = self.index.get_locs(label)
        except TypeError:
            # single label
            index = self.index.get_locs([label])

        if len(index) == 1:
            # single index
            return index[0]

        # list of indices
        return index

    def __repr__(self):
        return repr(self.index)

class SpinIce(object):
    """ Ising spin lattice """
    def __init__(self, *, size=(4,4), lattice_spacing=1, hc=10, alpha=1.0,
            disorder=0, h_ext=(0,0), neighbor_distance=1, switching='sw',
            sw_b=1, sw_c=1, sw_beta=3, sw_gamma=3, thermal_std=0,
            flip_mode='max', init='polarized',
            random_prob=0.5, random_seed=None,
            use_opencl=False, opencl_platform=0, opencl_device=0):
        """
        Parameters
        ----------
        size : tuple of int
            The size of the spin ice (width, height).
            Note that the size is geometry specific.
        lattice_spacing : float
            Spacing between each spin.
        hc : float
            Mean switching threshold.
        disorder : float
            Switching threshold disorder as percentage of hc. If non-zero,
            sample switching from a normal distribution with mean hc and
            standard deviation hc * disorder.
        h_ext : tuple of float
            External field (h_extx, h_exty).
        neighbor_distance : float
            Neighborhood to consider when calculating dipole interactions.
            All spins within lattice_spacing * neighbor_distance are considered
            neighbors. Set neighbor_distance=np.inf for a global neighborhood.
        switching : {'sw', 'budrikis'}
            Magnetic switching model:
                - 'sw': Extended Stoner-Wohlfarth model
                - 'budrikis': switching based on the paralell field component
        sw_b : float
            Height of the Stoner-Wohlfarth astroid (paralell axis).
        sw_c : float
            Width of the Stoner-Wohlfarth astroid (perpendicular axis).
        sw_beta : float
            Pointiness of the top/bottom of the Stoner-Wohlfarth astroid
            (paralell axis).
        sw_gamma : float
            Pointiness of the left/right of the Stoner-Wohlfarth astroid
            (perpendicular axis).
        thermal_std : float (positive)
            Standard deviation of the gaussian distribution which the thermal noise is sampled 
        flip_mode : {'single', 'max', 'max-rand', 'all'}
            Flip mode strategy:
                - 'single': single uniform random flip (Budrikis Monte Carlo)
                - 'max': flip the spin with maximum energy, break ties by index
                - 'max-rand': flip the spin with maximum energy, break ties randomly
                - 'all': flip all flippable spins
        init : {'polarized', 'random', 'image.png'} or ndarray
            Initial spin state.
        use_opencl : bool
            Use OpenCL acceleration.
        opencl_platform : int
            Select OpenCL platform (if multiple GPUs of different families are installed).
        opencl_device : int
            Select OpenCL device (if multiple GPUs of the same family are installed).
        """
        self.size = size
        self.lattice_spacing = lattice_spacing
        self.hc = hc
        self.alpha = alpha
        self.disorder = disorder
        self.switching = switching
        self.sw_params = (sw_b, sw_c, sw_beta, sw_gamma)
        self.thermal_std = thermal_std
        self.flip_mode = flip_mode
        self.neighbor_distance = neighbor_distance
        self.random_prob = random_prob
        assert switching in ('budrikis', 'sw')
        assert flip_mode in ('single', 'max', 'max-rand', 'all')
        assert neighbor_distance > 0

        self.labels = None

        self.cl = use_opencl
        self.cl_device = opencl_device
        self.cl_platform = opencl_platform
        self._cl_context = None

        if random_seed is not None:
            np.random.seed(random_seed)

        # geometry
        pos, angle = self._init_geometry()
        self.pos = pos.astype(float)
        self.angle = angle.astype(float)
        self.m = np.column_stack([np.cos(self.angle), np.sin(self.angle)])
        self.spin_count = len(self.pos)

        if self.labels is None:
            # No labels, labels = indices
            self.labels = np.arange(self.spin_count)

        self.L = LabelIndexer(self.labels)

        # thermal noise
        self.update_thermal_noise()

        # spin flip threshold
        self.threshold = np.zeros(self.spin_count)
        self._init_threshold()

        # spin state
        self.spin = np.ones(self.spin_count, dtype=np.int8)
        self._init_spin(init)

        # flat neighbor list (computed once)
        self._neighbor_list = self._init_neighbor_list()
        self.num_neighbors = self._neighbor_list.shape[-1]

        # dipolar fields between each spin and its neighbors
        # precomputed on demand by _h_dip/_init_cl
        self._h_dip_cache = None

        self.set_h_ext(h_ext)

    @property
    def N(self):
        """ Alias for self.spin_count """
        return self.spin_count

    def label(self, i):
        """ Get the label of a given spin index or list of indices """
        return tuple(self.labels[i])

    def indexof(self, label):
        """ Get the spin index of a given label or range of labels

        Alias for self.L[label]
        """
        return self.L[label]

    def indices(self):
        """ Get all spin indices """
        return range(self.spin_count)

    def all_indices(self):
        """ Get all spin indices as numpy integer array index
        See https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html#integer-array-indexing
        """
        return list(self.indices())

    def _init_spin(self, init):
        if isinstance(init, str) and init == 'random':
            self.randomize(self.random_prob)

        if isinstance(init, str) and init.endswith('png'):
            self.set_spin_image(init)

        if isinstance(init, np.ndarray):
            self.set_spin(init)

    def _init_geometry(self):
        nx, ny = self.size
        spin_count = nx * ny
        pos = np.zeros((spin_count, 2), dtype=float)
        angle = np.zeros(spin_count, dtype=float)

        # rotation of each spin
        angle[:] = np.pi/2

        # positions of each spin
        rows = np.arange(ny, dtype=int)
        cols = np.arange(nx, dtype=int)
        grid = np.array(np.meshgrid(rows, cols))
        grid = grid.T.reshape((-1, 2))
        pos = self.lattice_spacing * np.flip(grid.astype(float), axis=-1)
        pos[:] = pos
        self.labels = grid

        return pos, angle
        
    def _init_threshold(self):
        # spin flip threshold
        if self.disorder:
            std = self.hc * self.disorder
            threshold = np.random.normal(self.hc, std, self.threshold.shape)
            # all thresholds should be positive
            threshold = np.abs(threshold)
            self.threshold[:] = threshold
        else:
            self.threshold[:] = self.hc

    def _init_neighbor_list(self):
        # Calculate neighborhood matrix
        # print(f'_init_neighbor_list(size={self.size})')
        neighbors = []
        num_neighbors = 0

        # Construct KDTree for every position
        tree = cKDTree(self.pos)

        nd = self.lattice_spacing * self.neighbor_distance
        nd += 1e-5 # pad to avoid rounding errors

        for i in self.indices():
            p = self.pos[i]
            n = tree.query_ball_point([p], nd)[0]
            n.remove(i)
            neighbors.append(n)
            num_neighbors = max(num_neighbors, len(n))

        # print(f'num_neighbors={num_neighbors}')

        # Neighborhood list, -1 marks end of each list
        neighbor_list = np.full((self.spin_count, num_neighbors), -1, dtype=np.int32)
        for i, neighs in enumerate(neighbors):
            neighbor_list[i,:len(neighs)] = neighs

        return neighbor_list

    def _init_h_dip(self):
        # when use_opencl=1, the hdip cache is initialized by _init_cl()
        assert not self.cl

        # cache dipolar fields for the neighborhood of all magnets
        _h_dip = np.zeros((self.spin_count, self.num_neighbors, 2), dtype=np.float64)
        for i in self.indices():
            for jj, j in enumerate(self.neighbors(i)):
                # print(f'i={i} jj={jj} j={j}')
                _h_dip[i][jj] = self.alpha * np.array(self.spin_dipolar_field(i, j))

        return _h_dip

    def __getstate__(self):
        odict = copy(self.__dict__)
        # Don't pickle _cl attributes. They will be automatically
        # re-initialized by _init_cl() when needed
        for k in list(filter(lambda k: k.startswith('_cl'), odict)):
            odict[k] = None
        return odict

    def __eq__(self, other):
        state = self.__getstate__()
        other_state = other.__getstate__()
        for k in state:
            if np.any(state[k] != other_state[k]):
                return False
        return True

    @property
    def width(self):
        x = self.pos[:, 0]
        xmin, xmax = np.min(x), np.max(x)
        return xmax - xmin

    @property
    def height(self):
        y = self.pos[:, 1]
        ymin, ymax = np.min(y), np.max(y)
        return ymax - ymin

    @property
    def vectors(self):
        """ Spin vectors """
        spin = np.array(self.spin, dtype=float)
        spin.shape += (1,)
        mag = self.m * spin
        return mag

    def set_spin(self, spin):
        spin = np.array(spin, dtype=np.int8)
        assert spin.shape == (self.spin_count,)
        assert np.all(np.logical_or(spin == 1, spin == -1))
        self.spin = spin

    def set_spin_image(self, filename):
        """ Set spin state from image

        The image is resized to fit the default spin grid. Then the grayscale
        image is used to set spin state:
        * black maps to spin -1
        * non-black maps to spin 1
        """
        # Use default grid
        G = self.grid()
        # calculate size of grid
        height, width = G.size

        # load image
        img = Image.open(filename)
        img = img.convert('L') # convert to grayscale

        # flip it since (0,0) is top left in the image but (0,0) is bottom left
        # in our spin geometry
        img = img.transpose(Image.FLIP_TOP_BOTTOM)

        # resize image to the default grid size
        img = img.resize((width, height))
        img = np.array(img)

        img[img != 0] = 1  # map non-black to spin 1
        img[img == 0] = -1 # map black to spin -1

        # finally set all the spins
        self.set_grid('spin', np.array(img))

    def set_threshold(self, threshold):
        assert threshold.shape == (self.spin_count,)
        self.threshold = threshold

    def set_h_ext(self, h_ext):
        """
        Set external field to h_ext

        h_ext can either be a single vector for a uniform field (h_ext.shape==(2,))
        or a 2D array of vectors for a non-uniform field (h_ext.shape==(self.spin_count, 2))
        """
        h_ext = np.array(h_ext, dtype=np.float64)
        assert h_ext.shape == (2,) or h_ext.shape == (self.spin_count, 2)
        if h_ext.shape == (2,):
            h_ext = np.tile(h_ext, (self.spin_count, 1))
        self.h_ext = h_ext

    def set_h_ext_grid(self, h_ext):
        if h_ext.shape == (2,):
            # global
            self.set_h_ext(h_ext)
        else:
            # grid
            self.set_grid('h_ext', h_ext)

    def set_temperature(self,std):
        self.thermal_std = std

    def randomize(self, prob=0.5):
        self.spin = -1+2*np.random.binomial(1, 1-prob, self.spin_count)
        self.spin = self.spin.astype(np.int8)
        #self.spin = -1+2*np.random.randint(0, 2, self.shape, dtype=np.int8)

    def polarize(self):
        self.spin[:] = 1

    def update_thermal_noise(self):
        """ Resamples thermal noise.
        Samples x and y components of noise from normal distribution"""
        if self.thermal_std:
            self.h_therm = np.random.normal(0, self.thermal_std, (self.spin_count, 2))
        else:
            self.h_therm = 0

    def neighbors(self, i):
        neighs = self._neighbor_list[i]
        return neighs[neighs >= 0]

    def spin_dipolar_field(self, i, j):
        """ Calculate dipolar field between spin i and j relative to positive spin """
        r = self.pos[j] - self.pos[i]
        m = self.m
        dist = norm(r)
        h_dip_1 = -m[j] / dist**3
        h_dip_2 = 3 * r * m[j].dot(r) / dist**5
        h_dip = h_dip_1 + h_dip_2

        m_angle = np.arctan2(m[i][1], m[i][0])
        h_angle = np.arctan2(h_dip[1], h_dip[0])
        h = norm(h_dip)
        theta = h_angle - m_angle
        h_par = h*np.cos(theta)
        h_perp = h*np.sin(theta)
        return np.array([h_par, h_perp], dtype=float)

    def dipolar_field(self, i):
        """ Calculate total dipolar field parallell to spin i """
        if self.cl:
            # path only for testing
            return self._h_dip_local_cl()[i]
        return self._h_dip_local(i)

    def dipolar_fields(self):
        if self.cl:
            return self._h_dip_local_cl()

        h_dip = np.zeros((self.spin_count, 2))
        for i in self.indices():
            h_dip[i] = self.dipolar_field(i)
        return h_dip

    @property
    def _h_dip(self):
        if self._h_dip_cache is None:
            self._h_dip_cache = self._init_h_dip()
        return self._h_dip_cache

    def _h_dip_local(self, i):
        hdip = np.zeros(2) # h_par, h_perp
        for jj, j in enumerate(self.neighbors(i)):
            # print("h_dip", jj, j)
            hdip += self._h_dip[i][jj] * self.spin[i] * self.spin[j]
        return hdip

    def external_field(self, i):
        """ Calculate external field parallel and perpendicular to spin i """
        if self.cl:
            # path only for testing
            return tuple(self._external_fields_cl()[i])

        m = self.spin[i] * self.m[i]
        m_angle = np.arctan2(m[1], m[0])

        h_ext = self.h_ext[i]
        h = norm(h_ext)
        h_angle = np.arctan2(h_ext[1], h_ext[0])

        theta = h_angle - m_angle
        h_par = h*np.cos(theta)
        h_perp = h*np.sin(theta)

        return np.array([h_par, h_perp], dtype=np.float64)

    def external_fields(self):
        """ Calculate external fields parallel and perpendicular to all spins """
        if self.cl:
            return self._external_fields_cl()

        # todo: numpyfy
        h_ext = np.zeros((self.spin_count, 2))
        for i in self.indices():
            h_ext[i] = self.external_field(i)
        return h_ext

    def thermal_field(self, i):
        if self.h_therm is 0:
            return 0
        return (self.h_therm[i] * self.spin[i])

    def thermal_fields(self):
        if self.h_therm is 0:
            return np.zeros((self.spin_count, 2))
        return (self.h_therm.T * self.spin).T

    def total_field(self, i):
        """ Calculate the total field parallel to spin i """
        if self.cl:
            return self._total_fields_cl()[i] + self.thermal_field(i)
        return self.dipolar_field(i) + self.external_field(i) + self.thermal_field(i)

    def total_fields(self):
        therm_f = 0 if self.h_therm is 0 else self.thermal_fields() #TODO: make thermal_fields_cl
        if self.cl:
            return self._total_fields_cl() + therm_f
        return self.dipolar_fields() + self.external_fields() +  therm_f

    def flip(self, i):
        self.spin[i] *= -1

    # TODO: rename / discard?
    def _switching_energy_budrikis(self):
        h_tot = self.total_fields()
        h_par = h_tot[..., 0] # paralell components only
        E = -(h_par + self.threshold)
        return E

    def _switching_energy_sw(self):
        b, c, beta, gamma = self.sw_params

        h_tot = self.total_fields()
        h_par = h_tot[..., 0] / (b * self.threshold)
        h_perp = h_tot[..., 1] / (c * self.threshold)

        # Switching criteria 1: h_par**(2/3) + h_perp**(2/3) > hc**(2/3)
        # E > 0: switching is possible
        E = (h_par**2)**(1/gamma) + (h_perp**2)**(1/beta) - 1

        # Switching criteria 2: h_par < 0
        # make E negative when h_par >= 0
        # Use a very small number here instead of zero to avoid a corner case:
        # when the field is perfectly perpendicular to the magnet, rounding
        # errors can cause h_par to always be negative regardless of the spin,
        # resulting in an infinite switching loop.
        cond = h_par >= -1e-12
        E[cond] = -np.abs(E[cond])
        return E

    def switching_energy(self):
        if self.switching == 'budrikis':
            E = self._switching_energy_budrikis()
        else:
            E = self._switching_energy_sw()

        return E

    def flippable_energy(self):
        flippable = []
        energy = self.switching_energy()
        flippable = np.nonzero(energy > 0)
        energy = energy[flippable]
        flippable = flippable[0]
        return flippable, energy

    def flippable(self):
        return self.flippable_energy()[0]

    def step(self):
        """ Perform a flip of one or more flippable spins """
        flip, energy = self.flippable_energy()
        # print("flippable:", len(flip))
        if len(flip) == 0:
            return False

        # TODO: rename / parameterize?
        if self.flip_mode == 'single':
            # Glip a single random spin
            i = np.random.choice(flip)
            self.flip(i)

        elif self.flip_mode == 'max':
            # Flip the spin with maximum energy
            i = flip[np.argmax(energy)]
            self.flip(i)

        elif self.flip_mode == 'max-rand':
            # Flip the spin with maximum energy, ties broken by random choice
            # Break ties by random choice
            i = np.argmax(energy)
            ties, = np.nonzero(energy == energy[i])
            j = flip[np.random.choice(ties)]
            self.flip(j)

        # TODO: drop?
        elif self.flip_mode == 'all':
            for i in flip:
                self.flip(i)

        return True

    def relax(self):
        """ Flip spins until equilibrium, return number of calls to step() """
        steps = 0

        self.update_thermal_noise()

        while self.step():
            steps += 1
        return steps

    def energy(self):
        h_tot = self.total_fields()
        h_par = h_tot[..., 0] # paralell components only
        E = -h_par
        return E

    def total_energies(self):
        dip = -np.sum(self.dipolar_fields()[...,0])
        ext = -np.sum(self.external_fields()[...,0])

        tf = self.thermal_fields()
        therm = -np.sum(tf[...,0]) if tf is not 0 else 0

        total = np.sum((dip,therm,ext))
        return [dip, ext, therm, total]

    def total_energy(self):
        return np.sum(self.energy())

    def total_magnetization(self):
        mag = self.vectors
        return np.array(np.sum(mag, axis=0))

    # sub-classes can override this to specify the size of the vertex window
    # (see find_vertices)
    _vertex_size = (2, 1)

    def find_vertices(self):
        """ Find the vertices in this geometry

        Returns a tuple (vi, vj, indices) where vi, vj are the vertex indices
        and indices is a list of spin indices corresponding to each vertex
        index.
        """
        return find_vertices(self.grid(), self.angle, self._vertex_size)

    def vertices(self):
        """ Get the spin indices of all vertices """
        vi, vj, indices = self.find_vertices()
        return indices

    def vertex_indices(self):
        """ Get all vertex indices """
        vi, vj, indices = self.find_vertices()
        return vi, vj

    def vertex_type(self, v):
        """ Get the vertex type for a vertex where v are the spin indices
        of the vertex """
        return vertex_type(self.spin[v], self.angle[v])

    def vertex_count(self):
        """ Count the number of vertices of each type

        Returns a tuple (types, counts) where types are the different vertex
        types and counts are the corresponding counts. """
        vertex_types = [self.vertex_type(v) for v in self.vertices()]
        types, counts = np.unique(vertex_types, return_counts=True)
        return tuple(types), tuple(counts)

    def vertex_population(self):
        """ Calculate the vertex type population as a fraction of all vertices

        Returns a tuple (types, pops) where types are the different vertex
        types and pops are the corresponding fractions. """
        types, counts = self.vertex_count()
        counts = np.array(counts)
        pops = counts / np.sum(counts)
        return types, tuple(pops)

    def vertex_pos(self, v):
        """ Get the position of a vertex where v are the spin indices of the
        vertex """
        return np.mean(self.pos[v], axis=0)

    def vertex_mag(self, v):
        """ Get the direction of a vertex v """
        spin = self.spin[v]
        spin.shape += (1,)
        m = self.m[v]
        mag = m * spin
        return np.sum(mag, axis=0)

    @property
    def _default_cell_size(self):
        return (self.lattice_spacing, self.lattice_spacing)

    def grid(self, cell_size=None):
        """ Map spin indices onto a regular grid

        The spacing between each grid point is given by cell_size.
        If cell_size <= lattice_spacing, each grid cell will contain at
        most one spin.
        If cell_size > lattice_spacing, each grid cell may contain more
        than one spin.
        If cell_size is None, an optimal (geometry dependent) cell size is used

        Returns a Grid object which allows quick lookup of spin index to
        grid index
        """
        if cell_size is None:
            cell_size = self._default_cell_size
        if np.isscalar(cell_size):
            cell_size = (cell_size, cell_size)

        # Calculate optimal padding
        padx = min(self._default_cell_size[0]/2, cell_size[0]/2)
        pady = min(self._default_cell_size[1]/2, cell_size[1]/2)
        padding = (padx, pady)

        grid = Grid(self.pos, cell_size, padding)

        return grid

    def fixed_grid(self, grid_size):
        """ Map spin indices onto a regular grid of fixed size

        Like grid() but takes grid size (number of cells) as parameter
        instead of cell size.
        """
        padx = self._default_cell_size[0]/2
        pady = self._default_cell_size[1]/2
        xmax = np.max(self.pos[..., 0])
        ymax = np.max(self.pos[..., 1])
        width = xmax + 2 * padx
        height = ymax + 2 * pady
        cell_size = (width / grid_size[0]), (height / grid_size[1])
        return self.grid(cell_size)

    def set_grid(self, attr, values):
        """ Map grid values onto some spin attribute.

        Valid attributes: spin, h_ext
        """
        G = self.fixed_grid((values.shape[1], values.shape[0]))

        # spin indices as numpy integer array index
        spin_inds = self.all_indices()

        # map all spin indices to grid index
        grid_inds = G.grid_index(spin_inds)

        # determine shape of attr and the corresponding set-function
        set_attr = getattr(self, 'set_' + attr)
        oldattr = getattr(self, attr)
        newattr = oldattr.copy()
        newattr[spin_inds] = values[grid_inds]
        set_attr(newattr)

    def view_grid(self, attr, cell_size=None, method='sum'):
        """ Project some spin attribute onto a grid.

        Valid attributes: spin, vectors, h_ext, threshold, pos

        The spacing between each grid cell is given by cell_size.
        If cell_size <= lattice_spacing, each grid cell will contain at
        most one spin attribute.
        If cell_size > lattice_spacing, each grid cell will contain the
        sum of several spin attributes.
        """

        # make the grid
        G = self.grid(cell_size)

        # get the values we wish to view on the grid
        values = getattr(self, attr)

        return G.add_values(values, method=method)

    # TODO: return spin instead of vectors
    def spin_grid(self, cell_size=None):
        """ Project the spin vectors onto a grid.

        See view_grid() for information about cell_size
        """
        return self.view_grid('vectors', cell_size)

    def plot(self, arrows=True, **kwargs):
        return plot_vectors(self.pos, self.vectors, arrows=arrows, **kwargs)

    def plot_energy(self, arrows=True):
        E = self.energy()
        return plot_vectors(self.pos, self.vectors, C=E, arrows=arrows, cmap='bwr')

    def plot_vertices(self):
        size = self.lattice_spacing * 0.15
        vertices = self.vertices()
        circles = [plt.Circle(self.vertex_pos(v), size) for v in vertices]
        colors = np.array([self.vertex_type(v) for v in vertices])
        col = PatchCollection(circles, cmap=vertex_cmap, norm=normalize_vertex_type)
        col.set_array(colors)
        ax = plt.gca()
        ax.add_collection(col)
        ax.autoscale_view()
        return col

    def plot_vertex_mag(self, arrows=True, **kwargs):
        vertices = self.vertices()
        XY = np.array([self.vertex_pos(v) for v in vertices])
        UV = np.array([self.vertex_mag(v) for v in vertices])

        # Normalize vectors to unit length
        nmax = norm(UV, axis=-1).max()
        if nmax != 0:
            UV = UV / nmax

        return plot_vectors(XY, UV, arrows=arrows, **kwargs)

    def _init_h_dip_cl(self):
        # Only called by _init_cl()
        posr = self.pos.ravel()
        pos_g = cl.Buffer(self._cl_context, clmf.READ_ONLY | clmf.COPY_HOST_PTR, hostbuf=posr)
        res_g = cl.Buffer(self._cl_context, clmf.WRITE_ONLY, 2 * self.spin_count * self.num_neighbors * np.dtype(np.float64).itemsize)
        self._cl_prg.spin_dipolar_field(
                self._cl_queue,
                (self.spin_count, self.num_neighbors),
                None,
                pos_g, 
                res_g,
                self._cl_neighbors_g,
                self._cl_n_neighbors_g,
                self._cl_m_g
                )


        res = np.empty((self.spin_count, self.num_neighbors, 2), dtype=np.float64)

        cl.enqueue_copy(self._cl_queue, res, res_g)

        return self.alpha * res

    def _init_cl(self):
        assert self.cl
        if self._cl_context:
            # already initialized
            return

        global cl, clmf
        cl = __import__("pyopencl")
        clmf = cl.mem_flags

        platforms = cl.get_platforms()
        assert(len(platforms) > 0), "Couldn't find any platforms! Driver installed?"
        platform = platforms[self.cl_platform]

        devices = platform.get_devices()
        assert(len(devices) > 0), "No devices in platform"
        device = devices[self.cl_device]
        print("Using device {} on {}".format(device.name, platform.name))

        self._cl_context = cl.Context([device])
        self._cl_queue = cl.CommandQueue(self._cl_context)

        src = pkg_resources.resource_string(__name__, "flatspin_cl_kernels.c")
        src = src.decode("utf-8")

        self._cl_prg = cl.Program(self._cl_context, src).build(options=[])

        #preload some of the buffers.
        self._cl_spin_g = cl.Buffer(self._cl_context, clmf.READ_ONLY | clmf.COPY_HOST_PTR, hostbuf=self.spin)
        self._cl_res_g = cl.Buffer(self._cl_context, clmf.WRITE_ONLY,
                np.prod((self.spin_count, 2)) * np.dtype(np.float64).itemsize)

        self._cl_neighbors_g = cl.Buffer(self._cl_context, clmf.READ_ONLY | clmf.COPY_HOST_PTR, hostbuf=self._neighbor_list)
        self._cl_n_neighbors_g = cl.Buffer(self._cl_context, clmf.READ_ONLY | clmf.COPY_HOST_PTR, hostbuf=np.int32(self.num_neighbors))

        self._cl_m_g = cl.Buffer(self._cl_context, clmf.READ_ONLY | clmf.COPY_HOST_PTR, hostbuf=np.float64(self.m))
        self._cl_h_ext_g = cl.Buffer(self._cl_context, clmf.READ_ONLY | clmf.COPY_HOST_PTR, hostbuf=self.h_ext)

        # we are now ready to calculate h_dip cache on the GPU
        if self._h_dip_cache is None:
            self._h_dip_cache = self._init_h_dip_cl()

        self._cl_hdip_cache_g = cl.Buffer(self._cl_context, clmf.READ_ONLY | clmf.COPY_HOST_PTR, hostbuf=self._h_dip_cache)

    def _total_fields_cl(self):
        self._init_cl()

        #this will calcualte for all indices
        #copy the updated data to the device
        #print(self.spin.shape)

        cl.enqueue_copy(self._cl_queue, self._cl_spin_g, self.spin)
        cl.enqueue_copy(self._cl_queue, self._cl_h_ext_g, self.h_ext)

        self._cl_prg.total_fields(self._cl_queue, (self.spin_count,), None,
                self._cl_spin_g,
                self._cl_hdip_cache_g,
                self._cl_res_g,
                self._cl_neighbors_g,
                self._cl_n_neighbors_g,
                self._cl_m_g,
                self._cl_h_ext_g
        )

        res = np.empty((self.spin_count, 2), dtype=np.float64)
        cl.enqueue_copy(self._cl_queue, res, self._cl_res_g)

        return res

    def _h_dip_local_cl(self):
        self._init_cl()

        #this will calcualte for all indices
        cl.enqueue_copy(self._cl_queue, self._cl_spin_g, self.spin)


        self._cl_prg.test_h_dip_local(self._cl_queue, (self.spin_count,), None,
                self._cl_spin_g,
                self._cl_hdip_cache_g,
                self._cl_res_g,
                self._cl_neighbors_g,
                self._cl_n_neighbors_g
        )

        res = np.empty((self.spin_count, 2), dtype=np.float64)
        cl.enqueue_copy(self._cl_queue, res, self._cl_res_g)

        return res

    def _external_fields_cl(self):
        self._init_cl()

        #this will calcualte for all indices
        spin_g = cl.Buffer(self._cl_context, clmf.READ_ONLY | clmf.COPY_HOST_PTR, hostbuf=self.spin)

        cl.enqueue_copy(self._cl_queue, self._cl_spin_g, self.spin)
        cl.enqueue_copy(self._cl_queue, self._cl_h_ext_g, self.h_ext)


        self._cl_prg.test_h_ext(self._cl_queue, (self.spin_count,), None,
                self._cl_spin_g,
                self._cl_m_g,
                self._cl_h_ext_g,
                self._cl_res_g,
        )

        res = np.empty((self.spin_count, 2), dtype=np.float64)
        cl.enqueue_copy(self._cl_queue, res, self._cl_res_g)

        return res



class SquareSpinIce(SpinIce):
    pass

class SquareSpinIceClosed(SquareSpinIce):
    def __init__(self, *, lattice_spacing=2*np.cos(np.pi/4), edge="symmetric", **kwargs):
        kwargs['lattice_spacing'] = lattice_spacing

        assert edge in ("symmetric", "asymmetric")
        self.edge = edge

        super().__init__(**kwargs)

    def _init_geometry(self):
        nx, ny = self.size
        sym = 1 if self.edge is "symmetric" else 0
        spin_count = (ny + sym) * nx + ny * (nx + sym)
        pos = np.zeros((spin_count, 2), dtype=float)
        angle = np.zeros(spin_count, dtype=float)

        labels = []

        a = self.lattice_spacing
        y = 0
        i = 0
        for row in range(0, 2 * ny + sym):
            is_vert = row % 2 # 1 for vert, 0 for horiz
            ncols = nx
            x = 0

            if is_vert:
                # vertical row
                ncols += sym
            else:
                # horizontal row
                x += a/2

            for col in range(0, ncols):
                if is_vert:
                    angle[i] = np.pi/2
                pos[i] = [x, y]

                label = (row, col)
                labels.append(label)

                x += a
                i += 1

            y += a / 2

        self.labels = np.array(labels)

        return pos, angle

    def _init_spin(self, init):
        if isinstance(init, str) and init == 'ground':
            for row, col in self.labels:
                i = self.L[row, col]
                if row % 4 == 0 and col % 2 == 1:
                    self.flip(i)
                elif row % 4 == 2 and col % 2 == 0:
                    self.flip(i)
                elif row % 4 == 1 and col % 2 == 0:
                    self.flip(i)
                elif row % 4 == 3 and col % 2 == 1:
                    self.flip(i)
        else:
            super()._init_spin(init)

    _vertex_size = (3, 3)

    @property
    def _default_cell_size(self):
        return (self.lattice_spacing/2, self.lattice_spacing/2)

class SquareSpinIceOpen(SquareSpinIce):
    def __init__(self, *, neighbor_distance=sqrt(2), **kwargs):
        kwargs['neighbor_distance'] = neighbor_distance

        super().__init__(**kwargs)

    def _init_geometry(self):
        pos, angle = super()._init_geometry()

        angle[:] = np.pi/4

        for i in range(len(pos)):
            row, col = self.labels[i]
            if row % 2 == 0 and col % 2 == 1:
                angle[i] += np.pi/2
            elif row % 2 == 1 and col % 2 == 0:
                angle[i] += np.pi/2

        return pos, angle

    _vertex_size = (2, 2)

class PinwheelSpinIceDiamond(SquareSpinIceClosed):
    def __init__(self, *, spin_angle=45, neighbor_distance=10, **kwargs):
        self.spin_angle = spin_angle
        kwargs['neighbor_distance'] = neighbor_distance

        super().__init__(**kwargs)

    def _init_geometry(self):
        pos, angle = super()._init_geometry()

        # rotate each island by spin_angle
        angle[:] -= np.deg2rad(self.spin_angle)

        return pos, angle

class PinwheelSpinIceLuckyKnot(SquareSpinIceOpen):
    def __init__(self, *, spin_angle=45, neighbor_distance=10*sqrt(2), **kwargs):
        self.spin_angle = spin_angle
        kwargs['neighbor_distance'] = neighbor_distance

        super().__init__(**kwargs)

    def _init_geometry(self):
        pos, angle = super()._init_geometry()

        # rotate each island by spin_angle
        angle[:] -= np.deg2rad(self.spin_angle)

        return pos, angle

class PinwheelSpinIceRandom(PinwheelSpinIceDiamond):
    def __init__(self, *, spin_angle_disorder=0, **kwargs):
        self.spin_angle_disorder = spin_angle_disorder

        super().__init__(**kwargs)

    def _init_geometry(self):
        pos, angle = super()._init_geometry()

        # rotate each island by spin_angle
        std = self.spin_angle_disorder
        angle[:] += np.deg2rad(np.random.normal(0, std, angle.shape))

        return pos, angle

class KagomeSpinIce(SpinIce):
    def _init_geometry(self):
        labels = []

        nx, ny = self.size

        n_top_bot = (2 * nx * 2)
        n_mid = (2 * nx + 1) * (ny - 1)
        n_vert = (nx + 1) * ny
        spin_count = n_top_bot + n_mid + n_vert

        pos = np.zeros((spin_count, 2), dtype=float)
        angle = np.zeros(spin_count, dtype=float)

        n_rows = 2 * ny + 1
        last_row = n_rows - 1

        a = self.lattice_spacing
        y = 0
        i = 0
        for row in range(0, n_rows):
            if row % 2 == 0:
                # "horizontal" magnets (+/-30 degree)
                n_cols = 2 * nx + 1
                if row == 0 or row == last_row:
                    # first and last row has 1 less element
                    n_cols -= 1

                x = a/2
                col0 = 0
                if ny % 2 == 0 and row == last_row:
                    # even number of magnets, skip first magnet
                    x += a
                    col0 += 1

                for col in range(col0, col0 + n_cols):
                    pos[i] = [x, y]
                    angle[i] = np.deg2rad(30)
                    if row % 4 == 0 and col % 2 == 0:
                        angle[i] *= -1
                    if row % 4 == 2 and col % 2 == 1:
                        angle[i] *= -1

                    label = (row, col)
                    labels.append(label)

                    x += a
                    i += 1
            else:
                # vertical magnets (90 degrees)
                n_cols = nx + 1
                x = 0
                if row % 4 == 3:
                    x += a
                for col in range(0, n_cols):
                    pos[i] = [x, y]
                    angle[i] = np.deg2rad(90)

                    label = (row, col)
                    labels.append(label)

                    x += 2 * a
                    i += 1

            y += a * sqrt(3) / 2

        self.labels = np.array(labels)

        return pos, angle

    _vertex_size = (2,3)

    @property
    def _default_cell_size(self):
        sizex = self.lattice_spacing/2
        sizey = sqrt(3)*self.lattice_spacing/2
        return (sizex, sizey)


if __name__ == '__main__':
    # np.random.seed(0xdeadbeef)
    # random.seed(0xdeadbeef)

    hc = 11.25
    size = (8,8)
    # spin_ice = SpinIce(size, hc=hc, disorder=0.0)
    spin_ice = SquareSpinIceClosed(size=size, hc=hc, disorder=0.0)
    # spin_ice = SquareSpinIceOpen(size, hc=hc, disorder=0.0)

    # External field
    H = 1.1 * hc
    theta = np.pi/4
    h_extx = H * np.cos(theta)
    h_exty = H * np.sin(theta)
    h_ext = np.array([h_extx, h_exty])
    spin_ice.set_h_ext(h_ext)

    # Initial config
    spin_ice.randomize()

    print("Spin:")
    print(spin_ice.spin)
    print("Total energy:", spin_ice.total_energy())

    # Relax
    print("Relaxing", end='')
    t0 = time.time()
    steps = 0
    while spin_ice.step():
        steps += 1
        print(".", flush=True, end='')
    # steps = spin_ice.relax()
    dt = timedelta(seconds=time.time() - t0)
    print("{} steps in {}".format(steps, dt))
    print("Total energy:", spin_ice.total_energy())

    fig, axes = plt.subplots(1, 4, figsize=(16,9), subplot_kw={'aspect': 'equal'}, sharex=True, sharey=True)
    ax_spin, ax_energy, ax_vert, ax_mag  = axes.ravel()

    plt.sca(ax_spin)
    plt.title("Spin")
    spin_ice.plot()

    plt.sca(ax_energy)
    plt.title("Energy")
    spin_ice.plot_energy()

    plt.sca(ax_vert)
    plt.title("Vertex types")
    spin_ice.plot_vertices()

    '''
    plt.sca(ax_mag)
    plt.title("Vertex magnetization")
    spin_ice.plot_vertex_mag()
    '''

    plt.show()
