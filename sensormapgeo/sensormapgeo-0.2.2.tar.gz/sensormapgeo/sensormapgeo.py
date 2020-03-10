# -*- coding: utf-8 -*-

# sensormapgeo, Transform remote sensing images between sensor and map geometry.
#
# Copyright (C) 2020  Daniel Scheffler (GFZ Potsdam, danschef@gfz-potsdam.de)
#
# This software was developed within the context of the EnMAP project supported
# by the DLR Space Administration with funds of the German Federal Ministry of
# Economic Affairs and Energy (on the basis of a decision by the German Bundestag:
# 50 EE 1529) and contributions from DLR, GFZ and OHB System AG.
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Main module."""

from typing import Any, Union, List, Tuple
import os
import multiprocessing
import sys
import warnings
from tempfile import TemporaryDirectory

import numpy as np
import gdal
from py_tools_ds.geo.projection import EPSG2WKT, WKT2EPSG, proj4_to_WKT
from py_tools_ds.geo.coord_trafo import get_proj4info, proj4_to_dict, transform_coordArray, transform_any_prj
from py_tools_ds.geo.coord_calc import corner_coord_to_minmax, get_corner_coordinates
from py_tools_ds.io.raster.writer import write_numpy_to_image
from py_tools_ds.processing.shell import subcall_with_output

# NOTE: In case of ImportError: dlopen: cannot load any more object with static TLS,
#       one could add 'from pykdtree.kdtree import KDTree' here (before pyresample import)
from pyresample.geometry import AreaDefinition, SwathDefinition
from pyresample.bilinear import resample_bilinear
from pyresample.kd_tree import resample_nearest, resample_gauss, resample_custom


class SensorMapGeometryTransformer(object):
    def __init__(self, lons, lats, resamp_alg='nearest', radius_of_influence=30, **opts):
        # type: (np.ndarray, np.ndarray, str, int, Any) -> None
        """Get an instance of SensorMapGeometryTransformer.

        :param lons:    2D longitude array corresponding to the 2D sensor geometry array
        :param lats:    2D latitude array corresponding to the 2D sensor geometry array

        :Keyword Arguments:  (further documentation here: https://pyresample.readthedocs.io/en/latest/swath.html)
            - resamp_alg:           resampling algorithm ('nearest', 'bilinear', 'gauss', 'custom')
            - radius_of_influence:  <float> Cut off distance in meters (default: 30)
                                    NOTE: keyword is named 'radius' in case of bilinear resampling
            - sigmas:               <list of floats or float> [ONLY 'gauss'] List of sigmas to use for the gauss
                                    weighting of each channel 1 to k, w_k = exp(-dist^2/sigma_k^2). If only one channel
                                    is resampled sigmas is a single float value.
            - neighbours:           <int> [ONLY 'bilinear', 'gauss'] Number of neighbours to consider for each grid
                                    point when searching the closest corner points
            - epsilon:              <float> Allowed uncertainty in meters. Increasing uncertainty reduces execution time
            - weight_funcs:         <list of function objects or function object> [ONLY 'custom'] List of weight
                                    functions f(dist) to use for the weighting of each channel 1 to k. If only one
                                    channel is resampled weight_funcs is a single function object.
            - fill_value:           <int or None> Set undetermined pixels to this value (default: 0).
                                    If fill_value is None a masked array is returned with undetermined pixels masked
            - reduce_data:          <bool> Perform initial coarse reduction of source dataset in order to reduce
                                    execution time
            - nprocs:               <int>, Number of processor cores to be used
            - segments:             <int or None> Number of segments to use when resampling.
                                    If set to None an estimate will be calculated
            - with_uncert:          <bool> [ONLY 'gauss' and 'custom'] Calculate uncertainty estimates
                                    NOTE: resampling function has 3 return values instead of 1: result, stddev, count
        """
        # validation
        if lons.ndim != 2:
            raise ValueError('Expected a 2D longitude array. Received a %dD array.' % lons.ndim)
        if lats.ndim != 2:
            raise ValueError('Expected a 2D latitude array. Received a %dD array.' % lats.ndim)
        if lons.shape != lats.shape:
            raise ValueError((lons.shape, lats.shape), "'lons' and 'lats' are expected to have the same shape.")

        self.resamp_alg = resamp_alg
        self.opts = dict(radius_of_influence=radius_of_influence,
                         sigmas=(radius_of_influence / 2))
        self.opts.update(opts)

        if resamp_alg == 'bilinear':
            del self.opts['radius_of_influence']
            self.opts['radius'] = radius_of_influence

        # NOTE: If pykdtree is built with OpenMP support (default) the number of threads is controlled with the
        #       standard OpenMP environment variable OMP_NUM_THREADS. The nprocs argument has no effect on pykdtree.
        if 'nprocs' in self.opts:
            if self.opts['nprocs'] > 1:
                os.environ['OMP_NUM_THREADS'] = '%d' % opts['nprocs']
            del self.opts['nprocs']

        self.lats = lats
        self.lons = lons
        self.swath_definition = SwathDefinition(lons=lons, lats=lats)
        # use a projection string for local coordinates (https://gis.stackexchange.com/a/300407)
        # -> this is needed for bilinear resampling
        self.swath_definition.proj_str = '+proj=omerc +lat_0=51.6959777875 +lonc=7.0923165808 +alpha=-20.145 ' \
                                         '+gamma=0 +k=1 +x_0=50692.579 +y_0=81723.458 +ellps=WGS84 ' \
                                         '+towgs84=0,0,0,0,0,0,0 +units=m +no_defs'
        self.area_extent_ll = [np.min(lons), np.min(lats), np.max(lons), np.max(lats)]
        self.area_definition = None  # type: AreaDefinition

    def _get_target_extent(self, tgt_epsg):
        if tgt_epsg == 4326:
            tgt_extent = self.area_extent_ll
        else:
            corner_coords_ll = [[self.lons[0, 0], self.lats[0, 0]],  # UL_xy
                                [self.lons[0, -1], self.lats[0, -1]],  # UR_xy
                                [self.lons[-1, 0], self.lats[-1, 0]],  # LL_xy
                                [self.lons[-1, -1], self.lats[-1, -1]],  # LR_xy
                                ]
            corner_coords_tgt_prj = [transform_any_prj(EPSG2WKT(4326), EPSG2WKT(tgt_epsg), x, y)
                                     for x, y in corner_coords_ll]
            corner_coords_tgt_prj_np = np.array(corner_coords_tgt_prj)
            x_coords, y_coords = corner_coords_tgt_prj_np[:, 0], corner_coords_tgt_prj_np[:, 1]
            tgt_extent = [np.min(x_coords), np.min(y_coords), np.max(x_coords), np.max(y_coords)]

        return tgt_extent

    def compute_areadefinition_sensor2map(self, data, tgt_prj, tgt_extent=None, tgt_res=None):
        # type: (np.ndarray, Union[int, str], Tuple[float, float, float, float], Tuple[float, float]) -> AreaDefinition
        """Compute the area_definition to resample a sensor geometry array to map geometry.

        :param data:        numpy array to be warped to sensor or map geometry
        :param tgt_prj:     target projection (WKT or 'epsg:1234' or <EPSG_int>)
        :param tgt_extent:  extent coordinates of output map geometry array (LL_x, LL_y, UR_x, UR_y) in the tgt_prj
                            (automatically computed from the corner positions of the coordinate arrays)
        :param tgt_res:     target X/Y resolution (e.g., (30, 30))
        :return:
        """
        tgt_epsg = WKT2EPSG(proj4_to_WKT(get_proj4info(proj=tgt_prj)))
        tgt_extent = tgt_extent or self._get_target_extent(tgt_epsg)

        def raiseErr_if_empty(gdal_ds):
            if not gdal_ds:
                raise Exception(gdal.GetLastErrorMsg())
            return gdal_ds

        with TemporaryDirectory() as td:
            path_xycoords = os.path.join(td, 'xy_coords.bsq')
            path_xycoords_vrt = os.path.join(td, 'xy_coords.vrt')
            path_data = os.path.join(td, 'data.bsq')
            path_datavrt = os.path.join(td, 'data.vrt')
            path_data_out = os.path.join(td, 'data_out.bsq')

            # write X/Y coordinate array
            if tgt_epsg == 4326:
                xy_coords = np.dstack([self.swath_definition.lons,
                                       self.swath_definition.lats])
                # xy_coords = np.dstack([self.swath_definition.lons[::10, ::10],
                #                        self.swath_definition.lats[::10, ::10]])
            else:
                xy_coords = np.dstack(list(transform_coordArray(EPSG2WKT(4326), EPSG2WKT(tgt_epsg),
                                                                self.swath_definition.lons,
                                                                self.swath_definition.lats)))
            write_numpy_to_image(xy_coords, path_xycoords, 'ENVI')

            # create VRT for X/Y coordinate array
            ds_xy_coords = gdal.Open(path_xycoords)
            drv_vrt = gdal.GetDriverByName("VRT")
            vrt = raiseErr_if_empty(drv_vrt.CreateCopy(path_xycoords_vrt, ds_xy_coords))
            del ds_xy_coords, vrt

            # create VRT for one data band
            mask_band = np.ones((data.shape[:2]), np.int32)
            write_numpy_to_image(mask_band, path_data, 'ENVI')
            ds_data = gdal.Open(path_data)
            vrt = raiseErr_if_empty(drv_vrt.CreateCopy(path_datavrt, ds_data))
            vrt.SetMetadata({"X_DATASET": path_xycoords_vrt,
                             "Y_DATASET": path_xycoords_vrt,
                             "X_BAND": "1",
                             "Y_BAND": "2",
                             "PIXEL_OFFSET": "0",
                             "LINE_OFFSET": "0",
                             "PIXEL_STEP": "1",
                             "LINE_STEP": "1",
                             "SRS": EPSG2WKT(tgt_epsg),
                             }, "GEOLOCATION")
            vrt.FlushCache()
            del ds_data, vrt

            subcall_with_output("gdalwarp '%s' '%s' "
                                '-geoloc '
                                '-t_srs EPSG:%d '
                                '-srcnodata 0 '
                                '-r near '
                                '-of ENVI '
                                '-dstnodata none '
                                '-et 0 '
                                '-overwrite '
                                '-te %s '
                                '%s' % (path_datavrt, path_data_out, tgt_epsg,
                                        ' '.join([str(i) for i in tgt_extent]),
                                        ' -tr %s %s' % tgt_res if tgt_res else '',),
                                v=True)

            # get output X/Y size
            ds_out = raiseErr_if_empty(gdal.Open(path_data_out))

            x_size = ds_out.RasterXSize
            y_size = ds_out.RasterYSize
            out_gt = ds_out.GetGeoTransform()

            # noinspection PyUnusedLocal
            ds_out = None

        # add 1 px buffer around out_extent to avoid cutting the output image
        x_size += 2
        y_size += 2
        out_gt = list(out_gt)
        out_gt[0] -= out_gt[1]
        out_gt[3] += abs(out_gt[5])
        out_gt = tuple(out_gt)
        xmin, xmax, ymin, ymax = corner_coord_to_minmax(get_corner_coordinates(gt=out_gt, cols=x_size, rows=y_size))
        out_extent = xmin, ymin, xmax, ymax

        # get area_definition
        area_definition = AreaDefinition(area_id='',
                                         description='',
                                         proj_id='',
                                         projection=get_proj4info(proj=tgt_prj),
                                         width=x_size,
                                         height=y_size,
                                         area_extent=list(out_extent),
                                         )

        return area_definition

    def _resample(self, data, source_geo_def, target_geo_def):
        # type: (np.ndarray, Union[AreaDefinition, SwathDefinition], Union[AreaDefinition, SwathDefinition]) -> ...
        """Run the resampling algorithm.

        :param data:            numpy array to be warped to sensor or map geometry
        :param source_geo_def:  source geo definition
        :param target_geo_def:  target geo definition
        :return:
        """
        if self.resamp_alg == 'nearest':
            opts = {k: v for k, v in self.opts.items() if k not in ['sigmas']}
            result = resample_nearest(source_geo_def, data, target_geo_def, **opts).astype(data.dtype)

        elif self.resamp_alg == 'bilinear':
            opts = {k: v for k, v in self.opts.items() if k not in ['sigmas']}
            result = resample_bilinear(data, source_geo_def, target_geo_def, **opts).astype(data.dtype)

        elif self.resamp_alg == 'gauss':
            opts = {k: v for k, v in self.opts.items()}

            # ensure that sigmas are provided as list if data is 3-dimensional
            if data.ndim != 2:
                if not isinstance(opts['sigmas'], list):
                    opts['sigmas'] = [opts['sigmas']] * data.ndim
                if not len(opts['sigmas']) == data.ndim:
                    raise ValueError("The 'sigmas' parameter must have the same number of values like data.ndim."
                                     "n_sigmas: %d; data.ndim: %d" % (len(opts['sigmas']), data.ndim))

            result = resample_gauss(source_geo_def, data, target_geo_def, **opts).astype(data.dtype)

        elif self.resamp_alg == 'custom':
            opts = {k: v for k, v in self.opts.items()}
            if 'weight_funcs' not in opts:
                raise ValueError(opts, "Options must contain a 'weight_funcs' item.")
            result = resample_custom(source_geo_def, data, target_geo_def, **opts).astype(data.dtype)

        else:
            raise ValueError(self.resamp_alg)

        return result  # type: np.ndarray

    @staticmethod
    def _get_gt_prj_from_areadefinition(area_definition):
        # type: (AreaDefinition) -> (Tuple[float, float, float, float, float, float], str)
        gt = area_definition.area_extent[0], area_definition.pixel_size_x, 0, \
             area_definition.area_extent[3], 0, -area_definition.pixel_size_y
        prj = proj4_to_WKT(area_definition.proj_str)

        return gt, prj

    def to_map_geometry(self, data, tgt_prj=None, tgt_extent=None, tgt_res=None, area_definition=None):
        # type: (np.ndarray, Union[str, int], Tuple[float, float, float, float], Tuple, AreaDefinition) -> ...
        """Transform the input sensor geometry array into map geometry.

        :param data:            numpy array (representing sensor geometry) to be warped to map geometry
        :param tgt_prj:         target projection (WKT or 'epsg:1234' or <EPSG_int>)
        :param tgt_extent:      extent coordinates of output map geometry array (LL_x, LL_y, UR_x, UR_y) in the tgt_prj
        :param tgt_res:         target X/Y resolution (e.g., (30, 30))
        :param area_definition: an instance of pyresample.geometry.AreaDefinition;
                                OVERRIDES tgt_prj, tgt_extent and tgt_res; saves computation time
        """
        if self.lons.ndim > 2 >= data.ndim:
            raise ValueError(data.ndim, "'data' must at least have %d dimensions because of %d longiture array "
                                        "dimensions." % (self.lons.ndim, self.lons.ndim))

        if data.shape[:2] != self.lons.shape[:2]:
            raise ValueError(data.shape, 'Expected a sensor geometry data array with %d rows and %d columns.'
                             % self.lons.shape[:2])

        # get area_definition
        if area_definition:
            self.area_definition = area_definition
        else:
            if not tgt_prj:
                raise ValueError(tgt_prj, 'Target projection must be given if area_definition is not given.')

            self.area_definition = self.compute_areadefinition_sensor2map(
                data, tgt_prj=tgt_prj, tgt_extent=tgt_extent, tgt_res=tgt_res)

        # resample
        data_mapgeo = self._resample(data, self.swath_definition, self.area_definition)
        out_gt, out_prj = self._get_gt_prj_from_areadefinition(self.area_definition)

        # output validation
        if not data_mapgeo.shape[:2] == (self.area_definition.height, self.area_definition.width):
            raise RuntimeError('The computed map geometry output does not have the expected number of rows/columns. '
                               'Expected: %s; output: %s.'
                               % (str((self.area_definition.height, self.area_definition.width)),
                                  str(data_mapgeo.shape[:2])))
        if data.ndim > 2 and data_mapgeo.ndim == 2:
            raise RuntimeError('The computed map geometry output has only one band instead of the expected %d bands.'
                               % data.shape[2])

        return data_mapgeo, out_gt, out_prj  # type: Tuple[np.ndarray, tuple, str]

    def to_sensor_geometry(self, data, src_prj, src_extent):
        # type: (np.ndarray, Union[str, int], List[float, float, float, float]) -> np.ndarray
        """Transform the input map geometry array into sensor geometry

        :param data:        numpy array (representing map geometry) to be warped to sensor geometry
        :param src_prj:     projection of the input map geometry array (WKT or 'epsg:1234' or <EPSG_int>)
        :param src_extent:  extent coordinates of input map geometry array (LL_x, LL_y, UR_x, UR_y) in the src_prj
        """
        proj4_args = proj4_to_dict(get_proj4info(proj=src_prj))

        # get area_definition
        self.area_definition = AreaDefinition('', '', '', proj4_args, data.shape[1], data.shape[0],
                                              src_extent)

        # resample
        data_sensorgeo = self._resample(data, self.area_definition, self.swath_definition)

        # output validation
        if not data_sensorgeo.shape[:2] == self.lats.shape[:2]:
            raise RuntimeError('The computed sensor geometry output does not have the same X/Y dimension like the '
                               'coordinates array. Coordinates array: %s; output array: %s.'
                               % (self.lats.shape, data_sensorgeo.shape))

        if data.ndim > 2 and data_sensorgeo.ndim == 2:
            raise RuntimeError('The computed sensor geometry output has only one band instead of the expected %d bands.'
                               % data.shape[2])

        return data_sensorgeo


_global_shared_lats = None
_global_shared_lons = None
_global_shared_data = None


def _initializer(lats, lons, data):
    """Declare global variables needed for SensorMapGeometryTransformer3D.to_map_geometry and to_sensor_geometry.

    :param lats:
    :param lons:
    :param data:
    """
    global _global_shared_lats, _global_shared_lons, _global_shared_data
    _global_shared_lats = lats
    _global_shared_lons = lons
    _global_shared_data = data


class SensorMapGeometryTransformer3D(object):
    def __init__(self, lons, lats, resamp_alg='nearest', radius_of_influence=30, mp_alg='auto', **opts):
        # type: (np.ndarray, np.ndarray, str, int, str, Any) -> None
        """Get an instance of SensorMapGeometryTransformer.

        :param lons:    3D longitude array corresponding to the 3D sensor geometry array
        :param lats:    3D latitude array corresponding to the 3D sensor geometry array

        :Keyword Arguments:  (further documentation here: https://pyresample.readthedocs.io/en/latest/swath.html)
            - resamp_alg:           resampling algorithm ('nearest', 'bilinear', 'gauss', 'custom')
            - radius_of_influence:  <float> Cut off distance in meters (default: 30)
                                    NOTE: keyword is named 'radius' in case of bilinear resampling
            - mp_alg                multiprocessing algorithm
                                    'bands': parallelize over bands using multiprocessing lib
                                    'tiles': parallelize over tiles using OpenMP
                                    'auto': automatically choose the algorithm
            - sigmas:               <list of floats or float> [ONLY 'gauss'] List of sigmas to use for the gauss
                                    weighting of each channel 1 to k, w_k = exp(-dist^2/sigma_k^2). If only one channel
                                    is resampled sigmas is a single float value.
            - neighbours:           <int> [ONLY 'bilinear', 'gauss'] Number of neighbours to consider for each grid
                                    point when searching the closest corner points
            - epsilon:              <float> Allowed uncertainty in meters. Increasing uncertainty reduces execution time
            - weight_funcs:         <list of function objects or function object> [ONLY 'custom'] List of weight
                                    functions f(dist) to use for the weighting of each channel 1 to k. If only one
                                    channel is resampled weight_funcs is a single function object.
            - fill_value:           <int or None> Set undetermined pixels to this value (default: 0).
                                    If fill_value is None a masked array is returned with undetermined pixels masked
            - reduce_data:          <bool> Perform initial coarse reduction of source dataset in order to reduce
                                    execution time
            - nprocs:               <int>, Number of processor cores to be used
            - segments:             <int or None> Number of segments to use when resampling.
                                    If set to None an estimate will be calculated
            - with_uncert:          <bool> [ONLY 'gauss' and 'custom'] Calculate uncertainty estimates
                                    NOTE: resampling function has 3 return values instead of 1: result, stddev, count
        """
        # validation
        if lons.ndim != 3:
            raise ValueError('Expected a 3D longitude array. Received a %dD array.' % lons.ndim)
        if lats.ndim != 3:
            raise ValueError('Expected a 3D latitude array. Received a %dD array.' % lats.ndim)
        if lons.shape != lats.shape:
            raise ValueError((lons.shape, lats.shape), "'lons' and 'lats' are expected to have the same shape.")

        self.lats = lats
        self.lons = lons
        self.resamp_alg = resamp_alg
        self.radius_of_influence = radius_of_influence
        self.opts = opts

        # define number of CPUs to use (but avoid sub-multiprocessing)
        #   -> parallelize either over bands or over image tiles
        #      bands: multiprocessing uses multiprocessing.Pool, implemented in to_map_geometry / to_sensor_geometry
        #      tiles: multiprocessing uses OpenMP implemented in pykdtree which is used by pyresample
        self.opts['nprocs'] = opts.get('nprocs', multiprocessing.cpu_count())
        self.mp_alg = ('bands' if self.lons.shape[2] >= opts['nprocs'] else 'tiles') if mp_alg == 'auto' else mp_alg

        # override self.mp_alg if SensorMapGeometryTransformer3D is called by nosetest or unittest
        is_called_by_nose_cmd = 'nosetest' in sys.argv[0]
        if self.opts['nprocs'] > 1 and self.mp_alg == 'bands' and is_called_by_nose_cmd:
            warnings.warn("mp_alg='bands' causes deadlocks if SensorMapGeometryTransformer3D is called within a "
                          "nosetest console call. Using mp_alg='tiles'.")
            self.mp_alg = 'tiles'

    @staticmethod
    def _to_map_geometry_2D(kwargs_dict):
        # type: (dict) -> Tuple[np.ndarray, tuple, str, int]
        assert [var is not None for var in (_global_shared_lons, _global_shared_lats, _global_shared_data)]

        SMGT2D = SensorMapGeometryTransformer(lons=_global_shared_lons[:, :, kwargs_dict['band_idx']],
                                              lats=_global_shared_lats[:, :, kwargs_dict['band_idx']],
                                              resamp_alg=kwargs_dict['resamp_alg'],
                                              radius_of_influence=kwargs_dict['radius_of_influence'],
                                              **kwargs_dict['init_opts'])
        data_mapgeo, out_gt, out_prj = SMGT2D.to_map_geometry(data=_global_shared_data[:, :, kwargs_dict['band_idx']],
                                                              tgt_prj=kwargs_dict['tgt_prj'],
                                                              tgt_extent=kwargs_dict['tgt_extent'],
                                                              tgt_res=kwargs_dict['tgt_res'])

        return data_mapgeo, out_gt, out_prj, kwargs_dict['band_idx']

    def _get_common_target_extent(self, tgt_epsg):
        corner_coords_ll = [[self.lons[0, 0, :].min(), self.lats[0, 0, :].max()],  # common UL_xy
                            [self.lons[0, -1, :].max(), self.lats[0, -1, :].max()],  # common UR_xy
                            [self.lons[-1, 0, :].min(), self.lats[-1, 0, :].min()],  # common LL_xy
                            [self.lons[-1, -1, :].max(), self.lats[-1, -1, :].min()],  # common LR_xy
                            ]
        corner_coords_tgt_prj = [transform_any_prj(EPSG2WKT(4326), EPSG2WKT(tgt_epsg), x, y)
                                 for x, y in corner_coords_ll]
        corner_coords_tgt_prj_np = np.array(corner_coords_tgt_prj)
        x_coords, y_coords = corner_coords_tgt_prj_np[:, 0], corner_coords_tgt_prj_np[:, 1]
        tgt_extent = [np.min(x_coords), np.min(y_coords), np.max(x_coords), np.max(y_coords)]

        return tgt_extent

    def to_map_geometry(self, data, tgt_prj, tgt_extent=None, tgt_res=None):
        # type: (np.ndarray, Union[str, int], Tuple[float, float, float, float], Tuple) -> ...
        """Transform the input sensor geometry array into map geometry.

        :param data:            3D numpy array (representing sensor geometry) to be warped to map geometry
        :param tgt_prj:         target projection (WKT or 'epsg:1234' or <EPSG_int>)
        :param tgt_extent:      extent coordinates of output map geometry array (LL_x, LL_y, UR_x, UR_y) in the tgt_prj
        :param tgt_res:         target X/Y resolution (e.g., (30, 30))
        """
        if data.ndim != 3:
            raise ValueError(data.ndim, "'data' must have 3 dimensions.")

        if data.shape != self.lons.shape:
            raise ValueError(data.shape, 'Expected a sensor geometry data array with %d rows, %d columns and %d bands.'
                             % self.lons.shape)

        # get common target extent
        tgt_epsg = WKT2EPSG(proj4_to_WKT(get_proj4info(proj=tgt_prj)))
        tgt_extent = tgt_extent or self._get_common_target_extent(tgt_epsg)

        init_opts = self.opts.copy()
        if self.mp_alg == 'bands':
            del init_opts['nprocs']  # avoid sub-multiprocessing

        args = [dict(
            resamp_alg=self.resamp_alg,
            radius_of_influence=self.radius_of_influence,
            init_opts=init_opts,
            tgt_prj=tgt_prj,
            tgt_extent=tgt_extent,
            tgt_res=tgt_res,
            band_idx=band
        ) for band in range(data.shape[2])]

        if self.opts['nprocs'] > 1 and self.mp_alg == 'bands':
            with multiprocessing.Pool(self.opts['nprocs'],
                                      initializer=_initializer,
                                      initargs=(self.lats, self.lons, data)) as pool:
                result = pool.map(self._to_map_geometry_2D, args)
        else:
            _initializer(self.lats, self.lons, data)
            result = [self._to_map_geometry_2D(argsdict) for argsdict in args]

        band_inds = list(np.array(result)[:, -1])
        data_mapgeo = np.dstack([result[band_inds.index(i)][0] for i in range(data.shape[2])])
        out_gt = result[0][1]
        out_prj = result[0][2]

        return data_mapgeo, out_gt, out_prj  # type: Tuple[np.ndarray, tuple, str]

    @staticmethod
    def _to_sensor_geometry_2D(kwargs_dict):
        # type: (dict) -> (np.ndarray, int)
        assert [var is not None for var in (_global_shared_lons, _global_shared_lats, _global_shared_data)]

        SMGT2D = SensorMapGeometryTransformer(lons=_global_shared_lons[:, :, kwargs_dict['band_idx']],
                                              lats=_global_shared_lats[:, :, kwargs_dict['band_idx']],
                                              resamp_alg=kwargs_dict['resamp_alg'],
                                              radius_of_influence=kwargs_dict['radius_of_influence'],
                                              **kwargs_dict['init_opts'])
        data_sensorgeo = SMGT2D.to_sensor_geometry(data=_global_shared_data[:, :, kwargs_dict['band_idx']],
                                                   src_prj=kwargs_dict['src_prj'],
                                                   src_extent=kwargs_dict['src_extent'])

        return data_sensorgeo, kwargs_dict['band_idx']

    def to_sensor_geometry(self, data, src_prj, src_extent):
        # type: (np.ndarray, Union[str, int], List[float, float, float, float]) -> np.ndarray
        """Transform the input map geometry array into sensor geometry

        :param data:        3D numpy array (representing map geometry) to be warped to sensor geometry
        :param src_prj:     projection of the input map geometry array (WKT or 'epsg:1234' or <EPSG_int>)
        :param src_extent:  extent coordinates of input map geometry array (LL_x, LL_y, UR_x, UR_y) in the src_prj
        """
        if data.ndim != 3:
            raise ValueError(data.ndim, "'data' must have 3 dimensions.")

        init_opts = self.opts.copy()
        if self.mp_alg == 'bands':
            del init_opts['nprocs']  # avoid sub-multiprocessing

        args = [dict(
            resamp_alg=self.resamp_alg,
            radius_of_influence=self.radius_of_influence,
            init_opts=init_opts,
            src_prj=src_prj,
            src_extent=src_extent,
            band_idx=band
        ) for band in range(data.shape[2])]

        if self.opts['nprocs'] > 1 and self.mp_alg == 'bands':
            with multiprocessing.Pool(self.opts['nprocs'],
                                      initializer=_initializer,
                                      initargs=(self.lats, self.lons, data)) as pool:
                result = pool.map(self._to_sensor_geometry_2D, args)
        else:
            _initializer(self.lats, self.lons, data)
            result = [self._to_sensor_geometry_2D(argsdict) for argsdict in args]

        band_inds = list(np.array(result)[:, -1])
        data_sensorgeo = np.dstack([result[band_inds.index(i)][0] for i in range(data.shape[2])])

        return data_sensorgeo
