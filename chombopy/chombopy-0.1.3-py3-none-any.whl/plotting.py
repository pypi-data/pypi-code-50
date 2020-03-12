import h5py
import numpy as np
from matplotlib import pyplot
import re
import os
import logging
import xarray as xr
from shapely.ops import cascaded_union
from shapely.geometry import Polygon
import geopandas as gpd
from chombopy.inputs import read_inputs
from itertools import product


# TODO: Fix: AMR plotting is broken at the moment


class PltFile:
    """

    Class to represent a Chombo plot file.

    """
    NUM_COMPS = "num_comps"
    DATA = "data"
    DX = "dx"
    DT = "dt"
    REF_RATIO = "ref_ratio"
    BOXES = "boxes"

    YT = "YT"
    NATIVE = "native"
    XARRAY = "xarray"

    # List of names for each direction to be used later
    INDEX_COORDS_NAMES = ["i", "j", "k", "l", "m"]  # add more here if more dimensions

    indices = None
    reflect = None
    ds_amr = None

    python_index_ordering = True

    def __init__(self, filename, load_data=False, inputs_file="inputs"):
        self.is_plot_file = False
        self.defined = False
        self.data_loaded = False
        self.ds = None

        self.data_load_method = self.XARRAY

        self.ds_levels = []

        # Initialise to bogus values
        self.iteration = -1
        self.max_level = -1
        self.num_levels = -1
        self.num_comps = -1
        self.space_dim = -1
        self.comp_names = []
        self.levels = []
        self.time = -1
        self.frame = -1
        self.prob_domain = None
        self.domain_size = []
        self.xarr_data = None
        self.level_outlines = []
        self.full_domain_size = None
        self.inputs = None

        # Now read all the component names
        self.data = {}

        if not os.path.exists(filename):
            logging.info('PltFile: file does not exist "%s"' % filename)
            return
        self.filename = filename

        # Get the plot prefix and frame number assuming a format
        prefix_format = r"([^\d\/]*)(\d+)\.\dd\.hdf5"
        plot_file_name = self.filename

        m = re.search(prefix_format, plot_file_name)

        if m and m.groups() and len(m.groups()) == 2:
            self.plot_prefix = m.group(1)
            self.frame = int(m.group(2))

        else:
            self.plot_prefix = None
            self.frame = -1

        # get inputs
        output_folder = os.path.abspath(os.path.join(self.filename, ".."))
        inputs_file_loc = os.path.join(output_folder, inputs_file)
        if os.path.exists(inputs_file_loc):
            self.inputs = read_inputs(inputs_file_loc)
        else:
            logging.info("Cannot find inputs file %s" % inputs_file_loc)
            self.inputs = None

        self.defined = True

        if load_data:
            self.load_data()

    def __repr__(self):
        return "<PltFile object for %s>" % self.filename

    def load_data(self, zero_x=False):
        """ Load the data for this plotfile.

        Not done automatically as it can be slow for large files.

        Parameters
        ----------
        zero_x : bool, optional
            Whether to shift the axes so that the bottom corner is at :math:`x=0`

        Returns
        -------

        """
        if self.data_loaded:
            return

        if self.data_load_method in (self.NATIVE, self.XARRAY):
            self.load_data_native(zero_x)
        # else:
        #     self.load_data_yt()

        self.data_loaded = True

    # def load_data_yt(self):
    #     self.ds = yt.load(self.filename)

    def unload_data(self):
        self.ds_levels = []
        self.data_loaded = False

    # noinspection PyUnresolvedReferences
    def load_data_native(self, zero_x=False):

        logging.info("Loading %s" % self.filename)
        h5_file = h5py.File(self.filename, "r")

        chombo_group = h5_file["Chombo_global"]
        global_attrs = chombo_group.attrs

        attrs = h5_file.attrs

        self.time = attrs["time"]
        self.iteration = int(attrs["iteration"])
        self.max_level = int(attrs["max_level"])
        self.num_levels = int(attrs["num_levels"])
        # self.regrid_interval = int(attrs['regrid_interval_0'])
        self.num_comps = int(attrs["num_components"])
        self.space_dim = int(global_attrs["SpaceDim"])

        # Now read all the component names
        self.data = {}

        for i in range(0, self.num_comps):
            name = attrs["component_" + str(i)]
            name = name.decode("UTF-8")

            # Some of my files have wierd xEnthalpy yEnthalpy fields, which we should skip
            if name == "xEnthalpy" or name == "yEnthalpy":
                continue

            # Previously, we treated vectors and scalars differently,
            # now we just store vector components as separate scalar fields
            # retained previous code (commented out below) in case I ever want it
            actual_name = name

            self.data[name] = {self.NUM_COMPS: 1, self.DATA: []}

            self.data[actual_name][self.DATA] = [np.nan] * self.num_levels
            self.comp_names.append(actual_name)

        ds_levels = []

        self.levels = [{}] * self.num_levels
        for level in range(0, self.num_levels):
            level_group = h5_file["level_" + str(level)]

            # Data is stored differently in plot files and chk files
            # much of what follows will be different as a result
            if "data:datatype=0" in list(level_group.keys()):
                self.is_plot_file = True

            group_atts = level_group.attrs
            boxes = level_group["boxes"]
            lev_dx = group_atts["dx"]
            self.levels[level] = {
                self.DX: lev_dx,
                self.DT: group_atts["dt"],
                self.REF_RATIO: group_atts["ref_ratio"],
                self.BOXES: list(boxes),
            }

            # Some attributes on level 0 apply to whole hierarchy
            if level == 0:
                self.time = group_atts["time"]

                self.prob_domain = group_atts["prob_domain"]

                self.domain_size = [
                    self.prob_domain[i] * self.levels[level][self.DX]
                    for i in range(0, len(self.prob_domain))
                ]

                # Moving to ND
                self.full_domain_size = self.domain_size
                for i in range(self.space_dim, self.space_dim + self.space_dim):
                    self.full_domain_size[i] = self.full_domain_size[i] + lev_dx
                    # self.fullDomainSize[3] = self.fullDomainSize[3] + lev_dx

            # Create a box which spans the whole domain
            # Initialise with a box spanning the whole domain, then add data where it exists
            # Important to do it like this for refined levels, where the whole domain isn't covered with data
            size = []
            for i in range(self.space_dim):
                lev_dom_box_dir = np.arange(
                    self.full_domain_size[i] + lev_dx / 2,
                    self.full_domain_size[i + self.space_dim] - lev_dx / 2,
                    lev_dx,
                )
                size.append(lev_dom_box_dir.size)

            blank_data = np.empty(tuple(size))
            blank_data[:] = np.nan

            # Create an empty dataset which spans entire domain, which we will use as a template for loading data into
            coords = {}
            box_size = ()
            for d in range(self.space_dim):
                coords_dir = np.arange(
                    self.prob_domain[d], self.prob_domain[self.space_dim + d] + 1
                )
                coords[self.INDEX_COORDS_NAMES[d]] = coords_dir
                box_size = box_size + (coords_dir.size,)  # append to tuple of sizes

            blank_data = np.empty(box_size)
            ds_dom_box = xr.Dataset({}, coords=coords)

            # Use indexes rather than x, y for now - then convert to x,y later
            # this is to avoid issues with floating point arithmetic when merging datasets
            # (we can end up trying to merge datasets where x coordinates differ by ~ 10^{-10}, creating nonsense)

            # Create empty datasets spanning entire domain for each component
            for comp_name in self.comp_names:
                extended_coords = coords
                extended_coords["level"] = np.array(level)
                dims = self.INDEX_COORDS_NAMES[: self.space_dim]
                # dims = dims[::-1]  # reverse list so we have k, j, i etc
                ds_dom_box[comp_name] = xr.DataArray(
                    blank_data, dims=dims, coords=extended_coords  # dims=['j', 'i'],
                )

            ds_boxes = [ds_dom_box]

            # Get level outlines
            polygons = []
            for box in self.levels[level][self.BOXES]:
                lo_indices, hi_indices = self.get_indices(box)

                # 0.5 because cell centred
                lo_vals = [lev_dx * (0.5 + i) for i in lo_indices]
                hi_vals = [lev_dx * (0.5 + i) for i in hi_indices]

                end_points = [
                    [lo_vals[i] - lev_dx / 2, hi_vals[i] + lev_dx / 2]
                    for i in range(self.space_dim)
                ]

                # For plotting level outlines

                # Construct vertices in n dimensions
                polygon_vertices_auto = list(product(*end_points))
                polygon_vertices_auto = sorted(
                    polygon_vertices_auto,
                    key=lambda x: np.arctan(x[1] / max(abs(x[0]), 0.0001)),
                )

                poly = Polygon(polygon_vertices_auto)
                if poly.is_valid:
                    polygons.append(poly)

            level_outline = gpd.GeoSeries(cascaded_union(polygons))
            self.level_outlines.append(level_outline)

            # Data is sorted by box and by component, so need to know total number of components
            num_comps = 0
            for comp_name in self.data.keys():
                num_comps = num_comps + self.data[comp_name][self.NUM_COMPS]

            # Now get the  data for each field, on each level

            if self.is_plot_file:

                # For plt files, data is sorted by box then by component

                data = level_group["data:datatype=0"]

                # Some other stuff we can get, but don't at the moment:
                # data_offsets = level_group['data:offsets=0']
                # data_atts = level_group['data_attributes']
                # advVel = level_group['advVel:datatype=0']
                # advVel_offsets = level_group['advVel:offsets=0']
                # advVel_atts = level_group['advVel_attributes']

                data_unshaped = data[()]

                offset = 0

                for box in self.levels[level][self.BOXES]:
                    lo_indices = [box[i] for i in range(self.space_dim)]
                    hi_indices = [
                        box[i] for i in range(self.space_dim, 2 * self.space_dim)
                    ]

                    n_cells_dir = [
                        hi_indices[d] + 1 - lo_indices[d] for d in range(self.space_dim)
                    ]

                    num_box_cells = np.prod(
                        n_cells_dir
                    )  # effectively nx * ny * nz * ...
                    num_cells = (
                        num_box_cells * num_comps
                    )  # also multiply by number of components

                    # Now split into individual components
                    # data contains all fields on this level, sort into individual fields
                    comp_offset_start = 0

                    coords = self.get_coordinates(lo_indices, hi_indices)

                    # Blank dataset for this box, which each component will be added to
                    ds_box = xr.Dataset({}, coords=coords)

                    for comp_name in self.comp_names:
                        # logging.info('Num cells in a box: ' + str(num_box_cells))
                        comp_offset_finish = comp_offset_start + num_box_cells

                        indices = [
                            offset + comp_offset_start,
                            offset + comp_offset_finish,
                        ]

                        comp_offset_start = comp_offset_finish

                        ds_box[comp_name] = self.get_box_comp_data(
                            data_unshaped,
                            level,
                            indices,
                            comp_name,
                            n_cells_dir,
                            coords,
                        )

                    # Move onto next box
                    offset = offset + num_cells

                    ds_boxes.append(ds_box)

            else:

                # For chk files, data is sorted by component then by box
                # Loop over components and get data for that component from each box

                box_offset_scalar = 0

                # num_boxes = len(self.levels[level][self.BOXES])
                for box in self.levels[level][self.BOXES]:
                    lo_indices, hi_indices = self.get_indices(box)

                    n_cells_dir = [
                        hi_indices[d] + 1 - lo_indices[d] for d in range(self.space_dim)
                    ]

                    num_box_cells = np.prod(
                        n_cells_dir
                    )  # effectively nx * ny * nz * ...
                    # num_cells = num_box_cells * num_comps  # also multiply by number of components

                    # num_domain_cells = num_box_cells * num_boxes

                    # Now split into individual components
                    # data contains all fields on this level, sort into individual fields
                    # comp_offset_start = 0

                    coords = self.get_coordinates(lo_indices, hi_indices)

                    # Blank dataset for this box, which each component will be added to
                    ds_box = xr.Dataset({}, coords=coords)

                    for comp_name in self.comp_names:
                        component = 0

                        # Need to get data differently if this is a vector
                        is_vector = (
                            comp_name[0] == "x"
                            or comp_name[0] == "y"
                            or comp_name[0] == "z"
                            and sum([comp_name[1:] in x for x in self.comp_names])
                            == self.space_dim
                        )
                        if is_vector:
                            if comp_name[0] == "x":
                                component = 0

                            elif comp_name[0] == "y":
                                component = 1
                            elif comp_name[0] == "z":
                                component = 2

                            # Hardwired to 2D for now
                            num_comps = self.space_dim

                            # This is the data for this component in all boxes
                            data = level_group[comp_name[1:] + ":datatype=0"]
                        else:
                            data = level_group[comp_name + ":datatype=0"]
                            component = 0

                            num_comps = 1

                        data_unshaped = data[()]

                        # logging.info('Num cells in a box: ' + str(num_box_cells))
                        # comp_offset_finish = comp_offset_start + num_box_cells

                        component_offset = 0  # this is just 0 because we only get data for this component

                        # For vectors, we may have an offset?
                        if num_comps > 1:
                            component_offset = component * num_box_cells

                        # start_index = component_offset + box_offset
                        start_index = box_offset_scalar * num_comps + component_offset
                        end_index = start_index + num_box_cells

                        indices = [start_index, end_index]

                        # comp_offset_start = comp_offset_finish

                        ds_box[comp_name] = self.get_box_comp_data(
                            data_unshaped,
                            level,
                            indices,
                            comp_name,
                            n_cells_dir,
                            coords,
                        )

                        # component_offset = component_offset + (num_box_cells*num_comps)

                    # Move onto next box
                    box_offset_scalar = box_offset_scalar + num_box_cells

                    ds_boxes.append(ds_box)

            # ds_level = xr.merge(ds_boxes)

            # ds_level = xr.auto_combine(ds_boxes[1:])

            # Update will replace in place
            first_box = 1
            ds_level = ds_boxes[first_box]
            for b in ds_boxes[first_box + 1 :]:
                ds_level = ds_level.combine_first(b)

            # Create x,y,z, coordinates
            x_y_coords_names = ["x", "y", "z"]

            for d in range(self.space_dim):
                # Factor of 0.5 accounts for cell centering
                ds_level.coords[x_y_coords_names[d]] = (
                    ds_level.coords[self.INDEX_COORDS_NAMES[d]] + 0.5
                ) * lev_dx
            # ds_level.coords['x'] = ds_level.coords['i'] * lev_dx
            # ds_level.coords['y'] = ds_level.coords['j'] * lev_dx

            if zero_x:
                ds_level.coords["x"] = ds_level.coords["x"] - min(ds_level.coords["x"])

            # Swap i,j,k to x,y,z coordinates
            for d in range(self.space_dim):
                ds_level = ds_level.swap_dims(
                    {self.INDEX_COORDS_NAMES[d]: x_y_coords_names[d]}
                )

            # ds_level = ds_level.swap_dims({'i': 'x'})
            # ds_level = ds_level.swap_dims({'j': 'y'})

            # TODO: should level be an attribute or co-ordinate? need to try with actual AMR data
            ds_level.attrs["level"] = level

            ds_levels.append(ds_level)

        self.ds_levels = ds_levels

        h5_file.close()

    def get_coordinates(self, lo, hi):
        coordinates = {}
        for d in range(self.space_dim):
            coords_dir = np.arange(lo[d], hi[d] + 1)
            coordinates[self.INDEX_COORDS_NAMES[d]] = coords_dir

        return coordinates

    def get_box_comp_data(
        self, data_unshaped, level, indices, comp_name, n_cells_dir, coords
    ):

        data_box_comp = data_unshaped[indices[0] : indices[1]]

        if len(data_box_comp) == 0:
            logging.info("ERROR - no data in box")

        # Chombo data is indexed in reverse (i.e. data[k, j, i]), so whilst we have n_cells_dir = [Nx, Ny, Nz],
        # we need to reshape according to [Nz, Ny, Nx] before then transposing to get
        # an array which is indexed as data[i, j, k]
        # reshaped_data = data_box_comp.reshape(tuple(n_cells_dir))
        reshaped_data = data_box_comp.reshape(tuple(n_cells_dir[::-1]))
        reshaped_data = reshaped_data.transpose()

        # I think we only need to transpose in 3D
        # if self.space_dim == 3: #  or self.space_dim == 2
        #     reshaped_data = reshaped_data.transpose()
        reshaped_data = np.array(reshaped_data)

        # Check if scalar or vector
        trimmed_comp_names = [n[1:] for n in self.comp_names]
        field_type = "scalar"
        if comp_name[0] in ("x", "y", "z") and comp_name[1:] in trimmed_comp_names:
            field_type = "vector"

        dim_list = self.INDEX_COORDS_NAMES[: self.space_dim]
        # dim_list = dim_list[::-1]
        extended_coords = coords
        extended_coords["level"] = level

        # It's really unclear when we do and don't need to transpose
        # reshaped_data = reshaped_data.transpose()
        # dim_list = dim_list[::-1]

        if not reshaped_data.shape[0] == len(extended_coords[dim_list[0]]):
            reshaped_data = reshaped_data.transpose()
            # dim_list = dim_list[::-1]

        xarr_component_box = xr.DataArray(
            reshaped_data,
            dims=dim_list,  # ['j', 'i'],
            coords=extended_coords,  # {'i': i_box, 'j': j_box, 'level': level},
            attrs={"field_type": field_type},
        )

        return xarr_component_box

    def get_indices(self, box):
        lo = [box[i] for i in range(self.space_dim)]
        hi = [box[i] for i in range(self.space_dim, 2 * self.space_dim)]
        return lo, hi

    def plot_outlines(self, ax, colors=None):
        """ Plot all level outlines (except level 0)"""

        for level in np.arange(1, len(self.level_outlines)):
            self.plot_outline(ax, level, colors)

    def plot_outline(self, ax, level, colors=None):
        """ Plot level outline for a particular color"""

        # Default colors
        if not colors:
            colors = [[0, 0, 0, 1.0], [1, 0, 0, 1.0], [0, 1, 0, 1.0], [0, 0, 1, 1.0]]

        ec = colors[level][:]

        outline = self.level_outlines[level]

        # Shrink outline slightly

        # outline
        # outline = outline.scale(0.99, 0.99)
        # dx = self.levels[level][self.DX]
        # domain = Polygon([(dx, dx), (1-dx, dx), (1-dx, 1-dx), (dx, 1-dx)])
        # intersect = gpd.sjoin(domain, outline, how="inner", op='intersection')
        # intersect.plot(ax=ax, edgecolor=ec, facecolor=[1,1,1,0], linewidth=2.0)

        outline = outline.scale(0.99, 0.99)
        outline.plot(ax=ax, edgecolor=ec, facecolor=[1, 1, 1, 0], linewidth=3.0)

    @staticmethod
    def get_mesh_grid_n(arr, grow=0):
        x = np.array(arr.coords["x"])
        y = np.array(arr.coords["y"])

        x_min = x[0]
        x_max = x[-1]
        y_min = y[0]
        y_max = y[-1]

        nx = len(x) + grow
        ny = len(y) + grow

        x = np.linspace(x_min, x_max, nx)
        y = np.linspace(y_min, y_max, ny)

        return x, y

    @staticmethod
    def get_mesh_grid_xarray(arr, grow=False):
        x = np.array(arr.coords["x"])
        y = np.array(arr.coords["y"])

        dx = float(x[1] - x[0])
        dy = float(y[1] - y[0])

        if grow:
            x = np.append(x, [float(x[-1]) + dx])
            y = np.append(y, [float(y[-1]) + dy])

            x = x - dx / 2
            y = y - dx / 2

        return x, y

    def get_rotate_dims(self, rotate_dims):
        """ Backward compatibility fix. Originally user had to ask to rotate dimensions to match
        python indexing. We now do this by default. """

        if self.python_index_ordering:
            rotate_dims = not rotate_dims

        return rotate_dims

    def get_mesh_grid(self, level=0, rotate_dims=False, extend_grid=True):

        rotate_dims = self.get_rotate_dims(rotate_dims)

        # dx = self.levels[level][self.DX]

        components = list(self.data.keys())
        # components = [c.decode('UTF-8') for c in components]

        field = self.get_level_data(components[0])

        field_array = np.array(field)
        grid_size = field_array.shape

        x_coords = np.array(field.coords["x"])
        y_coords = np.array(field.coords["y"])

        dx = np.abs(x_coords[1] - x_coords[0])

        if extend_grid:
            extend = dx / 2
        else:
            extend = 0
        y, x = np.mgrid[
            slice(min(x_coords) - extend, max(x_coords) + extend, dx),
            slice(min(y_coords) - extend, max(y_coords) + extend, dx),
        ]

        coord_max = [(grid_size[i] + 1) * dx for i in range(0, self.space_dim)]
        grid_spacing = [coord_max[i] / grid_size[i] for i in range(0, self.space_dim)]
        grids = np.mgrid[
            [slice(0, coord_max[i], grid_spacing[i]) for i in range(0, self.space_dim)]
        ]

        if self.space_dim == 3:
            x = grids[0]
            y = grids[1]
            z = grids[2]

            if rotate_dims:
                x = x.transpose()
                y = y.transpose()
                z = z.transpose()

            z = self.scale_slice_transform(z)
            x = self.scale_slice_transform(x, no_reflect=True)
            y = self.scale_slice_transform(y, no_reflect=True)

            return x, y, z

        else:
            if rotate_dims:
                y_new = x.transpose()
                x_new = y.transpose()

                x = x_new
                y = y_new

            # y = self.scale_slice_transform(y)
            # x = self.scale_slice_transform(x, no_reflect=True)

            return x, y

    # Added for compatibility with ChkFile interface
    def get_data(self, var_name, rotate_dims=False):

        rotate_dims = self.get_rotate_dims(rotate_dims)

        data = self.get_level_data(var_name)

        if data is None:
            return None

        data = np.array(data)

        if rotate_dims:
            data = data.transpose()

        return data

    def get_level_data(self, field, level=0, valid_only=False):

        if len(self.comp_names) == 0:
            logging.info(
                "No data loaded, perhaps you meant to call PltFile.load_data() first? "
            )

        if self.data_load_method == self.YT:
            pass
            # TODO: write this

        if not self.data_loaded:
            logging.info("Data not loaded")
            return

        available_comps = list(self.ds_levels[0].keys())

        if field not in available_comps:
            logging.info("Field: %s not found. The following fields do exist: " % field)
            # logging.info(self.data.keys())
            logging.info(available_comps)
            return

        if self.data_load_method == self.XARRAY:

            # ds_lev = self.ds_amr.sel(level=level)
            # ds_lev = self.ds_levels[level].sel(level=level)
            ds_lev = self.ds_levels[level]

            ld = ds_lev[field]

            # Set covered cells to NaN
            # This is really slow, I'm sure there's a faster way
            if valid_only and level < self.num_levels - 1:
                coarseness = self.levels[level][self.REF_RATIO]
                fine_level = np.array(self.ds_levels[level + 1][field])
                temp = fine_level.reshape(
                    (
                        fine_level.shape[0] // coarseness,
                        coarseness,
                        fine_level.shape[1] // coarseness,
                        coarseness,
                    )
                )
                coarse_fine = np.sum(temp, axis=(1, 3))

                isnan = np.isnan(coarse_fine)
                # ld = ld.where(isnan == True)
                ld = ld.where(isnan)

            # By default, swap to python indexing
            if self.python_index_ordering:
                if self.space_dim == 3:
                    ld = ld.transpose("z", "y", "x")
                elif self.space_dim == 2:
                    ld = ld.transpose("y", "x")

        else:
            ld = self.single_box(field, level)

        ld = self.scale_slice_transform(ld)

        # If this is the x-component of a vector, and we're reflecting, we need to also make the field negative
        if self.reflect:
            if field[0] == "x":
                ld = -ld
            elif field == "streamfunction":
                ld = -ld

        return ld

    def scale_slice_transform(self, data, no_reflect=False):
        """

        :param data:
        :type data: xr.Dataset
        :param no_reflect:
        :type no_reflect: bool
        :return:
        """

        if self.indices:
            data = data[self.indices]

        if self.reflect and not no_reflect:
            # flip will change both the data values and the x coordinate
            data = np.flip(data, 0)

            # reset the x coordinate
            data = data.assign_coords(x=np.flip(data.coords["x"]))

        return data

    def plot_field(self, field):

        self.load_data()

        if self.data_load_method == self.NATIVE:

            cmap = pyplot.get_cmap("PiYG")

            ld = self.get_level_data(field, 0)
            x, y = self.get_mesh_grid()
            img = pyplot.pcolormesh(x, y, ld, cmap=cmap)

            # make a color bar
            pyplot.colorbar(img, cmap=cmap, label="")

            pyplot.xlabel("$x$")
            pyplot.xlabel("$z$")


    def single_box(self, field, level=0):
        ds = self.get_level_data(field, level)
        field_arr = np.array(ds)

        return field_arr

    def set_scale_slice_transform(self, indices, reflect=False):
        """ Describe how to extract data """
        self.indices = indices
        self.reflect = reflect

    def reset_scale_slice_transform(self):
        self.indices = None
        self.reflect = None

