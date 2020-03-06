# coding: utf-8
#/*##########################################################################
# Copyright (C) 2016 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
#############################################################################*/


__authors__ = ["H.Payno"]
__license__ = "MIT"
__date__ = "09/08/2018"


import numpy
import os
import logging
import typing

logger = logging.getLogger(__name__)


class ScanBase(object):
    """
    Class representing a scan.
    Contains main functions needed by the processing

    :param str scan: path to the folder containing the scan
    :param str _type: path to the folder containing the scan
    """
    _DICT_TYPE_KEY = 'type'

    _DICT_PATH_KEY = 'path'

    def __init__(self, scan, _type):
        self.path = scan
        self._type = _type

    @property
    def path(self) -> str:
        """
        Union[str,None] - ID of the scan (directory containing projections files)
        """
        return self._path

    @path.setter
    def path(self, path: str) -> None:
        if path is None:
            self._path = path
        else:
            assert type(path) is str
            self._path = os.path.abspath(path)

    @property
    def type(self):
        """
        str - type of the scanBase, can be 'edf' or 'hdf5' for now
        """
        return self._type

    def to_dict(self):
        """convert the TomoBase object to a dictionary"""
        raise NotImplementedError("Base class")

    def load_from_dict(self, _dict):
        raise NotImplementedError("Base class")

    @staticmethod
    def directory_contains_scan(directory, src_pattern, dest_pattern):
        """
        Check if the given directory is holding an acquisition

        :param str directory:
        :return: does the given directory contains any acquisition
        :rtype: bool
        """
        raise NotImplementedError("Base class")

    def is_abort(self, src_pattern, dest_pattern):
        """

        :return: True if the acquisition has been abort
        :rtype: bool
        """
        raise NotImplementedError("Base class")


class TomoBase(ScanBase):
    """
    Class representing a tomography acquisition
    """

    _DICT_TOMO_RP_KEY = "ftseries_recons_params"

    _DICT_LAMINO_RP_KEY = "lamino_recons_params"

    _DICT_AXIS_KEYS = "axis_recons_params"

    def __init__(self, scan, _type):
        ScanBase.__init__(self, scan, _type)
        self._flats = []
        self._darks = []
        self._projections = []
        # TODO: this is the edf approach, should be changed for h5
        self._reconstructions = []
        self._ftseries_params = None
        """ft parameters"""
        # TODO: this information can be used on ftseries to know if this is
        # the first time we are running a reconstruction or not
        self._lamino_params = None
        """Set of reconstructions parameters for laminography"""
        self._axis_params = None
        """Axis parameters"""
        self._process_file = None
        """file storing processes applied on the scan, with their configuration
        and result"""
        self._cache_proj_urls = None
        """cache for the projection urls"""
        self._cache_radio_axis = {}
        """cache for the radio axis. Key is tuple (mode, nearest), value is
        (url1, url2)"""

    @property
    def flats(self):
        """list of flats files"""
        return self._flats

    @flats.setter
    def flats(self, flats):
        self._flats = flats

    @property
    def darks(self):
        """list of darks files"""
        return self._darks

    @darks.setter
    def darks(self, darks):
        self._darks = darks

    @property
    def projections(self):
        """list of projections files"""
        return self._projections

    @projections.setter
    def projections(self, projections):
        self._projections = projections

    @property
    def reconstructions(self):
        """list of reconstruction files"""
        return self._reconstructions

    @reconstructions.setter
    def reconstructions(self, reconstructions):
        self._reconstructions = reconstructions

    @property
    def ftseries_recons_params(self):
        return self._ftseries_params

    @ftseries_recons_params.setter
    def ftseries_recons_params(self, recons_params):
        self._ftseries_params = recons_params

    @property
    def lamino_recons_params(self):
        return self._lamino_params

    @lamino_recons_params.setter
    def lamino_recons_params(self, recons_params):
        self._lamino_params = recons_params

    @property
    def axis_params(self):
        return self._axis_params

    @axis_params.setter
    def axis_params(self, parameters):
        self._axis_params = parameters

    # TODO: change name. Should be generalized to return Dataurl
    def getReconstructedFilesFromParFile(self, with_index):
        raise NotImplementedError('Base class')

    def get_scan_range(self):
        raise NotImplementedError('')

    def getProjectionsUrl(self, use_cache: bool = True) -> dict:
        """
        Return all projections as a dictionary with angle as key and
        DataUrl as value

        :param bool use_cache: if this function has already been called then
                               the result is in cache. If no modification
                               have been bring to the scan the value didn't
                               change

        :return: one DataUrl instance for each projections
        :rtype: dict
        """
        raise NotImplementedError('Base class')

    def getRadiosForAxisCalc(self, mode, nearest: bool = True,
                             use_cache: bool = True) -> tuple:
        """
        Return the radios for axis calculation and the requested mode.

        :param: angles we want to use for COR calculation. Can be 0-180,
                 90-180 or manual. If manual will return the 'most' appropriate
        :type: CorAngleMode
        :param nearest: if True then, pick the closest angle from the requested
                        one. If False, return (None, None) if the the angles
                        does not exists.
        :type: bool
        :return: couple of `opposite` radios that can be used for axis
                 calculation.
        :rtype: tuple(AxisResource, AxisResource)
        """
        if not use_cache:
            del self._cache_radio_axis[(mode, nearest)]

        def compute():
            from ..process.reconstruction.axis.params import AxisResource  # avoid cyclic import
            from ..process.reconstruction.axis.anglemode import CorAngleMode

            _mode = CorAngleMode.from_value(mode)
            if self.path is None:
                return None, None
            radios_with_angle = self.getProjectionsUrl()
            if _mode is CorAngleMode.use_0_180:
                couples = ((0, 180),)
            elif _mode is CorAngleMode.use_90_270:
                couples = ((90, 270),)
            else:
                couples = ((0, 180), (90, 270))

            for couple in couples:
                if(couple[0] in radios_with_angle.keys()
                        and couple[1] in radios_with_angle.keys()):
                    radio_0 = AxisResource(radios_with_angle[couple[0]])
                    radio_1 = AxisResource(radios_with_angle[couple[1]])
                    return radio_0, radio_1

            def find_nearest(angles, angle):
                if len(angles) is 0:
                    return None
                angles = numpy.asarray(angles)
                dist = numpy.abs(angles - angle)
                idx = dist.argmin()
                if isinstance(idx, numpy.ndarray):
                    idx = idx[0]
                return angles[idx]

            if nearest is True:
                angles = []
                # filter str value (0(1)...)
                [angles.append(value) for value in radios_with_angle.keys()
                 if numpy.issubdtype(type(value), numpy.number)]
                nearest_c1 = find_nearest(angles=angles, angle=couples[0][0])
                nearest_c2 = find_nearest(angles=angles, angle=couples[0][1])
                if nearest_c1 is not None and nearest_c2 is not None:
                    radio_0 = AxisResource(radios_with_angle[nearest_c1])
                    radio_1 = AxisResource(radios_with_angle[nearest_c2])
                    return radio_0, radio_1
            return None, None

        if (mode, nearest) not in self._cache_radio_axis:
            radio_0, radio_1 = compute()
            self._cache_radio_axis[(mode, nearest)] = (radio_0, radio_1)
        return self._cache_radio_axis[(mode, nearest)]

    def getFlat(self, index=None):
        """Return the flat file of given index"""
        raise NotImplementedError('Base class')

    def _get_scheme(self):
        """

        :return: scheme to read url
        :rtype: str
        """
        raise NotImplementedError('Base class')

    def getDark(self):
        raise NotImplementedError('Base class')

    def flatFieldCorrection(self, data):
        """Apply flat field correction on the given data

        :param numpy.ndarray data: the data to apply correction on
        :return: corrected data
        :rtype: numpy.ndarray
        """
        raise NotImplementedError('Base class')

    def getReconsParamList(self):
        """

        :return: reconstruction parameters
        :rtype: ReconsParamList
        """
        raise NotImplementedError('Base class')

    @property
    def process_file(self) -> str:
        """

        :return: file used to store the processes launch by tomwer
        """
        return self._process_file

    def to_dict(self):
        res = {}
        res[self._DICT_TYPE_KEY] = self.type
        res[self._DICT_PATH_KEY] = self.path
        # res[self._JSON_TOMO_RP_KEY] = self.ftseries_recons_params
        # ftseries reconstruction parameters
        if self.ftseries_recons_params:
            res[self._DICT_TOMO_RP_KEY] = self.ftseries_recons_params.to_dict()
        else:
            res[self._DICT_TOMO_RP_KEY] = None
        # axis reconstruction parameters
        if self.axis_params is None:
            res[self._DICT_AXIS_KEYS] = None
        else:
            res[self._DICT_AXIS_KEYS] = self.axis_params.to_dict()

        # lamino reconstruction parameters
        res[self._DICT_LAMINO_RP_KEY] = self.lamino_recons_params
        return res

    to_dict.__doc__ = ScanBase.to_dict.__doc__

    def equal(self, other):
        """

        :param :class:`.ScanBase` other: instance to compare with 
        :return: True if instance are equivalent
        :note: we cannot use the __eq__ function because this object need to be
               pickable
        """
        return (
            isinstance(other, self.__class__) or isinstance(self, other.__class__) and
            self.type == other.type and
            self.ftseries_recons_params == other.ftseries_recons_params and
            self.lamino_recons_params == other.lamino_recons_params and
            self.path == other.path
        )

    def getProjectionsUrl(self, use_cache:bool = True):
        """
        Return the 'extra' radios of a scan which are used to see if the scan
        moved during the acquisition. If no extra radio are found, return the
        dictionary of all radios.

        :return dict: angles as keys, radios as value.
        """
        raise NotImplementedError('Base class')

    @staticmethod
    def map_urls_on_scan_range(urls, n_projection, scan_range):
        """
        map given urls to an angle regarding scan_range and number of projection.
        We take the hypothesis that 'extra projection' are taken regarding the
        'id19' policy:
         * If the acquisition has a scan range of 360 then:
            * if 4 extra projection, the angles are (270, 180, 90, 0)
            * if 5 extra projection, the angles are (360, 270, 180, 90, 0)
         * If the acquisition has a scan range of 180 then:
            * if 2 extra projections: the angles are (90, 0)
            * if 3 extra projections: the angles are (180, 90, 0)

        :warning: each url should contain only one radio.

        :param urls: ordered list with all the urls. First url should be
                     the first radio acquire, last url should match the last
                     radio acquire.
        :type: list
        :param n_projection: number of projection for the sample.
        :type: int
        :param scan_range: acquisition range (usually 180 or 360)
        :type: float
        :return: angle in degree as key and url as value
        :rtype: dict
        """
        assert n_projection is not None
        res = {}

        # deal with the 'standard' acquisitions
        for proj_i in range(n_projection):
            if n_projection == 1:
                angle = 0.0
            else:
                angle = proj_i * scan_range / (n_projection -1)
            if proj_i < len(urls):
                res[angle] = urls[proj_i]
                # TODO: better to have them from the header ?!!
                # haven't found the information in here.

        if len(urls) > n_projection:
            # deal with extra images (used to check if the sampled as moved for
            # example)
            extraImgs = urls[n_projection:]
            if len(extraImgs) in (4, 5):
                if scan_range < 360:
                    logger.warning('incoherent data information to retrieve'
                                   'scan extra images angle')
                elif len(extraImgs) == 4:
                    res['270(1)'] = extraImgs[0]
                    res['180(1)'] = extraImgs[1]
                    res['90(1)'] = extraImgs[2]
                    res['0(1)'] = extraImgs[3]
                else:
                    res['360(1)'] = extraImgs[0]
                    res['270(1)'] = extraImgs[1]
                    res['180(1)'] = extraImgs[2]
                    res['90(1)'] = extraImgs[3]
                    res['0(1)'] = extraImgs[4]
            elif len(extraImgs) in (2, 3):
                if scan_range > 180:
                    logger.warning('incoherent data information to retrieve'
                                   'scan extra images angle')
                elif len(extraImgs) is 3:
                    res['180(1)'] = extraImgs[0]
                    res['90(1)'] = extraImgs[1]
                    res['0(1)'] = extraImgs[2]
                else:
                    res['90(1)'] = extraImgs[0]
                    res['0(1)'] = extraImgs[1]
            else:
                logger.warning('incoherent data information to retrieve scan'
                               'extra images angle')
                for i_extra, extra in enumerate(extraImgs):
                    res['? (' + str(i_extra) + ')'] = extra
        return res

    def get_ff_interval(self):
        """

        :param clear_cache: if true then recompute the cache containing
                            the acquisition information
        :type: bool
        :return: number of radio between each reference / flat field
        :rtype: int
        """
        raise NotImplementedError('Base class')

    def get_tomo_n(self):
        """

        :return: None if unable to get the information, else the number of
                 radio made during the acquisition at unique angle
        :rtype: Union[None,int]
        """
        raise NotImplementedError('Base class')

    def get_dim_1(self):
        """

        :return: image width. None if unable to retrieve the information.
        :rtype: Union[None,int]
        """
        raise NotImplementedError('Base class')

    def get_dim_2(self):
        """

        :return: image height. None if unable to retrieve the information.
        :rtype: Union[None,int]
        """
        raise NotImplementedError('Base class')

    def get_pixel_size(self):
        """

        :return: pixel size. Consider as a square. None if unable to retrieve
                 the information.
        :rtype: Union[None,float]
        """
        raise NotImplementedError('Base class')

    def get_sinogram(self, line, progress=None):
        """
        extract the sinogram from the radios / projections

        :param line: which sinogram we want
        :type: int
        :return: sinogram from the radio lines
        :rtype: numpy.array
        """
        raise NotImplementedError('Base class')


class _TomoBaseDock(object):
    """
    Internal class to make difference between a simple TomoBase output and
    an output for a different processing (like scanvalidator.UpdateReconsParam)
    """
    def __init__(self, tomo_instance):
        self.__instance = tomo_instance

    @property
    def instance(self):
        return self.__instance
