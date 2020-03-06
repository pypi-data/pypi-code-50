# coding: utf-8
###########################################################################
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
#############################################################################

"""contain the AxisProcess
"""

__authors__ = ["C.Nemoz", "H.Payno"]
__license__ = "MIT"
__date__ = "19/03/2019"

from .params import AxisRP
from .mode import AxisMode
from .projectiontype import ProjectionType
from .anglemode import CorAngleMode
from tomwer.core.process.baseprocess import SingleProcess, _input_desc, \
    _output_desc
from tomwer.core.scan.scanbase import TomoBase
from tomwer.core.scan.scanfactory import ScanFactory
from silx.image import tomography
from tomwer.core.progress import Progress
from tomwer.core.log import TomwerLogger
from tomwer.core.utils import logconfig
import numpy
from typing import Union
from scipy.ndimage import shift as img_shift
from tomwer.utils import docstring
from tomwer.core.utils import image
import tomwer.version
from tomwer.core.scan.scanbase import _TomoBaseDock

_logger = TomwerLogger(__name__)

# vertically, work on a window having only a percentage of the frame.
pc_height = 10. / 100.
# horizontally. Global method supposes the COR is more or less in center
# % of the detector:
pc_width = 50. / 100.


def compute_global(radio_1: numpy.ndarray, radio_2: numpy.ndarray,
                   pc_height: float, pc_width: float, flip_radio: bool = True):
    """
    see :ref:`axis global algorithm` for a description of the algorithm

    :param numpy.array radio_1: normalized projection
    :param numpy.array radio_2: normalized projection
    :param bool do_img_scale: if True normalize img2 regarding of img1
    :param float pc_height: percentage of the frame to take vertically into
                            account.
    :param float pc_width: percentage of the frame to take horizontally into
                           account.
    :return: value of the axis position (center of rotation). None if failed.
    :rtype: Union[float, None] value in [-img_width/2, img_width/2]
    """
    shape_projection = radio_2.shape
    beam_size = int(shape_projection[0] * pc_height)
    intercorr = numpy.empty([beam_size, shape_projection[1]])
    det_center = int(shape_projection[1] / 2)
    middle = int(shape_projection[0] / 2)

    im2_ymin = int(middle - beam_size / 2)
    im2_ymax = int(middle + beam_size / 2)
    im2_xmin = int(shape_projection[1] * (1. - pc_width) / 2)
    im2_xmax = shape_projection[1] - im2_xmin

    # set to 0 the non-wanted part of im2
    radio_2[:, 0:im2_xmin] = 0
    radio_2[:, im2_xmax:] = 0

    # flip the radio for the calculation
    if flip_radio:
        radio_2 = numpy.fliplr(radio_2)

    progress = Progress(name='compute cor (using global)')
    cor_position = None
    progress.setMaxAdvancement(im2_ymax-im2_ymin)
    for jj in range(1):
        nhit = 0
        max_pos = 0
        histo = numpy.zeros(shape_projection[1])

        for ii in range(im2_ymin, im2_ymax):
            vec1 = radio_1[ii, :]
            vec2 = radio_2[ii, :]
            intercorr[ii - im2_ymin, :] = numpy.correlate(vec1, vec2, mode='same')
            corr = intercorr[ii - im2_ymin, :]
            corr_argmax = corr.argmax()
            # in the line, search the set of 5 pixels where stdev is maximale
            max_pos += corr_argmax
            nhit += 1
            histo[corr_argmax-im2_xmin] += 1
            progress.increaseAdvancement(i=1)

        # histo contains a statistics of pixels candidates for COR
        # so select the best one
        hmax = histo.argmax()

        def compute_barycenter(hmax, histo):
            """compute barycenter of COR, COR-1 and COR+1"""

            if hmax == 0:
                cor_0 = (hmax) * histo[hmax]
                cor_1 = (hmax + 1) * histo[hmax + 1]
                bary = (cor_0 + cor_1) / (histo[hmax] + histo[hmax+1])
            elif hmax == len(histo) - 1:
                cor_m_1 = (hmax - 1) * histo[hmax - 1]
                cor_0 = (hmax) * histo[hmax]
                bary = (cor_m_1 + cor_0) / (histo[hmax-1] + histo[hmax])
            else:
                cor_m_1 = (hmax - 1) * histo[hmax - 1]
                cor_0 = (hmax) * histo[hmax]
                cor_1 = (hmax + 1) * histo[hmax + 1]
                bary = (cor_m_1 + cor_0 + cor_1) / (histo[hmax - 1] + histo[hmax] + histo[hmax + 1])
            return bary

        corh = compute_barycenter(hmax=hmax, histo=histo)
        corh += im2_xmin
        cor_position = (corh - det_center) / 2.

    return cor_position


def compute_scan_global(scan):
    """
    will compute the axis, using the global method. The calculation will be
    based on the scan object to retrieve the projections to be used and the
    option of the compute global calculation.

    :param `.TomoBase` scan:
    :rtype: Union[float, None]
    """
    assert scan.axis_params is not None
    radio_1, radio_2 = AxisProcess.get_inputs(scan=scan)
    if radio_1 is None or radio_2 is None:
        raise NoAxisUrl('Unable to find projections to global axis calculation')

    _logger.info('compute scan axis from global method for %s with pc_height: '
                 '%f, pc_width: %f' % (scan.path, pc_height, pc_width))

    return compute_global(radio_1=radio_1.copy(), radio_2=radio_2.copy(),
                          pc_height=pc_height, pc_width=pc_width)


def compute_scan_near(scan):
    """
    will compute the near algorithm within the axis_params contains in the scan
    and for the given scan

    :param scan: scan for which we want to compute the center of rotation
    :type: TomoBase
    """
    assert scan.axis_params is not None
    radio_1, radio_2 = AxisProcess.get_inputs(scan=scan)
    if radio_1 is None or radio_2 is None:
        raise NoAxisUrl('Unable to find projections to global axis calculation')

    _logger.info('compute scan axis from near method for %s with near position'
                 ': %f, window size: %s, fine step x: %s, look at stdmax: %s'
                 '' % (scan.path, scan.axis_params.near_position,
                       scan.axis_params.near_wx,
                       scan.axis_params.fine_step_x,
                       scan.axis_params.look_at_stdmax))

    return compute_near(radio_1=radio_1.copy(), radio_2=radio_2.copy(),
                        near_pos=scan.axis_params.near_position,
                        window_size=scan.axis_params.near_wx,
                        fine_step_x=scan.axis_params.fine_step_x,
                        look_at_stdmax=scan.axis_params.look_at_stdmax)


def compute_near(radio_1: numpy.ndarray, radio_2: numpy.ndarray,
                 near_pos: float, window_size: float, fine_step_x: float,
                 look_at_stdmax: bool, flip_radio: bool = True) -> Union[None,float]:
    """
    see :ref:`axis near algorithm` for a description of the algorithm

    :param radio_1: normalized projection
    :type: numpy.array
    :param radio_2: normalized projection to be put in relation with radio 1
    :type: numpy.array
    :param near_pos: position to look around
    :type: float
    :param look_at_stdmax:
    :param wxmin:
    :type: float
    :param wxmax:
    :type: float
    :return: center of rotation value in [-img_width/2, img_width/2]
    :type: float
    """
    mid_width = radio_1.shape[1] // 2
    mid_height = radio_1.shape[0] // 2
    beamheight = int(radio_1.shape[0] * pc_height)
    wxmin = int(radio_1.shape[1] * (1. - pc_width)/2)
    wxmax = radio_1.shape[1] - wxmin
    wymin = int(mid_height - beamheight / 2)
    wymax = int(mid_height + beamheight / 2)

    # This is the distance to shift im2_flipped to make coincidence.
    sh_im0 = int(round(2. * near_pos))
    x_pos_inf = wxmin
    x_pos_sup = wxmax
    if look_at_stdmax is True:
        xpos = get_stdmax_column(radio_1[mid_height,:])
        if xpos <= mid_width:
            x_pos_inf = window_size + 1
            x_pos_sup = 2 * xpos - x_pos_inf
        else:
            x_pos_sup = radio_1.shape[1] - window_size - 1
            x_pos_inf = 2 * xpos - x_pos_sup
        assert x_pos_inf <= x_pos_sup

    # define an integer window to shift im2_flipped around sh_im0
    sh_int_range = sh_im0 + (numpy.arange(2*window_size+1)-window_size)

    # define the number of fine steps in 1 pixel
    n_fine_step_x = int(1./fine_step_x)

    sh_fine_range = fine_step_x * numpy.arange(n_fine_step_x)

    cor_f = sh_im0
    h_minim = 1.e12
    if flip_radio:
        radio2_flipped = numpy.fliplr(radio_2.copy())
    else:
        radio2_flipped = radio_2.copy()

    progress = Progress(name='compute cor (using global)')
    progress.setMaxAdvancement(len(sh_int_range))
    for shint in sh_int_range:
        imout0 = numpy.roll(radio2_flipped, shint, 1)
        for shfine in sh_fine_range:
            imout = img_shift(imout0, (0, shfine), order=1)

            diff = (radio_1 - imout)[wymin:wymax, x_pos_inf:x_pos_sup]
            ampx = diff.max() - diff.min()
            if ampx < h_minim:
                h_minim = ampx
                cor_f = shint + shfine
        progress.increaseAdvancement(i=1)
    return cor_f / 2


def get_stdmax_column(x: numpy.ndarray) -> float:
    """

    :param x:
    :return: column index of the maximal standard deviation
    """
    kernel_size = 5
    l = len(x)
    r = range(l - kernel_size)
    y = numpy.empty(l - kernel_size)
    for i in r:
        s = numpy.std(x[i:i + kernel_size])
        y[i] = s

    return y.argmax()


def compute_frm_sinogram(scan, line, is_emission, subsampling):
    """
    Compute the center of rotation of the sinogram for the given
    :param scan:
    :param line:
    :param is_emission:
    :return: axis of rotation in [-image_width/2, image_width/2]
    """
    assert type(line) is int
    sinogram = scan.get_sinogram(line=line, subsampling=subsampling)
    if is_emission is True:
        sinogram = sinogram.max() - sinogram
    sinogram[sinogram == numpy.nan] = None
    sinogram[sinogram == numpy.inf] = None
    # make sure minimal value is 1
    sinogram = sinogram + abs(sinogram.min()) + 1
    sinogram = sinogram + 1

    _logger.info('Compute axis from sinogram for %s. With line:%s,'
                 'subsamppling: %s, is emission: %s'
                 '' % (scan.path, line, subsampling, is_emission))

    res = tomography.calc_center_centroid(sino=sinogram.T)
    # move it to tomwer ref [-image_width/2, image_width/2]
    return  res - sinogram.shape[0] // 2


class NoAxisUrl(Exception):
    pass


class AxisProcess(SingleProcess):
    """
    Process used to compute the center of rotation of a scan

    :param axis_params: parameters to configure the axis process
    :type: AxisRP
    """
    inputs = [
        _input_desc(name='data', type=TomoBase, handler='process',
                    doc='scan path'),
        _input_desc(name='change recons params', type=_TomoBaseDock,
                    handler='reprocess', doc='recompute axis'),
    ]
    outputs = [_output_desc(name='data', type=TomoBase, doc='scan path')]

    RADIO_CALCULATIONS_METHODS = {
        AxisMode.global_: compute_scan_global,
        AxisMode.near: compute_scan_near,
    }

    def __init__(self, axis_params):
        SingleProcess.__init__(self)
        self._mode_calculation_fct = {}
        """dict with function pointer to call for making the mode calculation.
        Function should have only one 'scan' paramter as input"""

        assert axis_params is None or isinstance(axis_params, AxisRP)
        self._axis_params = axis_params or AxisRP()
        """Axis reconstruction parameters to apply"""
        self._locked = False
        """Boolean used to lock reconstruction parameters edition"""
        self._recons_params_before_lock = None
        """Recons parameters register before locking the position"""

    def set_recons_params(self, recons_params):
        assert isinstance(recons_params, AxisRP)
        self._axis_params = recons_params

    def lock_position_value(self, lock=True):
        """
        lock the position currently computed or defined by the user.
        In this case we will lock the axis as defined 'fixed' with the current
        value

        :param bool lock: if true lock the currently existing position value
        """
        self._locked = lock
        if lock:
            self._recons_params_before_lock = self._axis_params.to_dict()
            if self._axis_params not in (AxisMode.manual, AxisMode.read):
                self._axis_params.mode = AxisMode.manual
        else:
            if self._recons_params_before_lock:
                self._axis_params.load_from_dict(self._recons_params_before_lock)  #noqa

    def process(self, scan):
        """
        Compute the position value then get ready to the next. And call

        .. note:: this simply call `compute`.
                  But this is needed for the AxisProcessThreaded class
        """
        if scan is None:
            return
        _logger.info('start axis calculation for %s' % scan.path)
        cor = error = None
        try:
            scan_res = self.compute(scan=scan)
        except Exception as e:
            scan_res = None
            error = e
        else:
            if isinstance(scan_res, TomoBase):
                cor = scan_res.axis_params.value
            elif scan_res is None:
                if scan.axis_params.value is not None:
                    cor = scan.axis_params.value
            elif isinstance(scan_res, float):
                cor = scan_res
            else:
                assert isinstance(scan_res, dict)
                b_dict = scan_res
                if TomoBase._DICT_AXIS_KEYS in scan_res:
                    b_dict = scan_res['axis_recons_params']
                cor = b_dict['POSITION_VALUE']
        finally:
            self._process_end(scan, cor=cor, error=error)
        return scan_res

    def reprocess(self, scan):
        """
        Reprocess the scan. For now simply call process

        :param scan:
        """
        return self.process(scan=scan)

    def _process_end(self, scan, cor, error=None):
        assert isinstance(scan, TomoBase)
        if scan.process_file is not None:
            self.register_process(
                process_file=scan.process_file,
                results={'center_of_rotation': cor if cor is not None else '-'},
                configuration=self._axis_params.to_dict(),
                process_index=0,
                overwrite=True)

        if error is not None:
            info = ' '.join(('fail to compute axis position for scan',
                             str(scan.path), 'reason is ', str(error)))
        else:
            info = ' '.join(('axis calculation defined for', scan.path, ':',
                             str(scan.axis_params.value)))

        _logger.processEnded(info,
                             extra={
                                logconfig.DOC_TITLE: self._scheme_title,
                                logconfig.SCAN_ID: scan.path})

    @staticmethod
    def get_inputs_urls(scan):
        """Make sure we have valid projections to be used for axis calculation

        :param TomoBase scan: scan to check
        :raise: NoAxisUrl if fails to found
        :return: the two projections to be used for axis calculation
        :rtype: tuple of AxisResource
        """
        if (scan.axis_params and scan.axis_params.axis_url_1
                and scan.axis_params.axis_url_1.url):
            return scan.axis_params.axis_url_1, scan.axis_params.axis_url_2
        else:
            _radio_1, _radio_2 = scan.getRadiosForAxisCalc(mode=CorAngleMode.manual_selection)
        return _radio_1, _radio_2

    @staticmethod
    def get_inputs(scan):
        assert isinstance(scan, TomoBase)
        radio_1, radio_2 = AxisProcess.get_inputs_urls(scan=scan)
        if radio_1 and radio_2:
            mess = ' '.join(('input radios are', radio_1.url.path(), 'and',
                             radio_2.url.path()))
            _logger.info(mess)
            log_ = scan.axis_params.projection_type is ProjectionType.transmission

            # if necessary normalize data
            if radio_1.normalized_data is None:
                radio_1.normalize_data(scan, log_=log_)
            if radio_2.normalized_data is None:
                radio_2.normalize_data(scan, log_=log_)

            if scan.axis_params.paganin_preproc:
                data_1 = radio_1.normalized_data_paganin
                data_2 = radio_2.normalized_data_paganin
            else:
                data_1 = radio_1.normalized_data
                data_2 = radio_2.normalized_data

            if scan.axis_params.scale_img2_to_img1:
                data_2 = image.scale_img2_to_img1(img_1=data_1, img_2=data_2)

            return data_1, data_2
        else:
            _logger.info('fail to find any inputs')
            return None, None

    def compute(self, scan, wait=True):
        """
        Compute the position value for the scan

        :param TomoBase scan:
        :param bool wait: used for threaded process. True if we want to end the
                          computation before releasing hand.
        :return: scan as a TomoBase
        """
        assert scan is not None
        if isinstance(scan, dict):
            _logger.warning('convert scan from a dict')
            _scan = ScanFactory.create_scan_object_frm_dict(scan)
        else:
            _scan = scan
        assert isinstance(_scan, TomoBase)

        # if the scan has no tomo reconstruction parameters yet create them
        if _scan.axis_params is None:
            _scan.axis_params = AxisRP()

        # copy axis recons parameters. We skip the axis_url which are specific
        # to the scan
        _scan.axis_params.copy(self._axis_params, copy_axis_url=False)
        assert scan.axis_params is not None
        return self._process_computation(scan=_scan)

    def scan_ready(self, scan):
        _logger.info(scan, 'processed')

    def _process_computation(self, scan):
        """

        :param TomoBase scan: scan for which we want to compute the axis
                              position.
        :return: scan as a TomoBase or a dict if _return_dict activated
        """
        _logger.info('compute center of rotation for %s' % scan.path)
        try:
            position = self.compute_axis_position(scan)
        except NotImplementedError:
            scan.axis_params.value = None
            raise NotImplementedError('Not implemented')
        except ValueError as e:
            scan_name = scan.path or 'undef scan'
            scan.axis_params.value = None
            raise Exception('Fail to compute axis position for', scan_name,
                            'reason is', e)
        else:
            scan.axis_params.value = position
            self._axis_params.value = position
            scan_name = scan.path or 'undef scan'
            mess = 'Compute axis position (' + str(scan.axis_params.value) + ') for ' + scan_name
            _logger.info(mess)
        if self._return_dict:
            return scan.to_dict()
        else:
            return scan

    def setMode(self, mode, value):
        if mode is AxisMode.manual:
            self._axis_params.cor_position = value
        else:
            raise NotImplementedError('mode not implemented yet')

    def define_calculation_mode(self, mode, fct_pointer):
        """Register the function to call of the given mode

        :param AxisMode mode: the mode to register
        :param fct_pointer: pointer to the function to call
        """
        self._mode_calculation_fct[id] = fct_pointer

    def compute_axis_position(self, scan):
        """

        :param scan: scan for which we compute the center of rotation
        :type: TomoScan
        :return: position of the rotation axis. Use the `.AxisMode` defined
                 by the `.ReconsParams` of the `.AxisProcess`
        :rtype: float or None (if fail to compute the axis position)
        """
        mode = self._axis_params.mode
        use_sinogram = self._axis_params.use_sinogram
        if use_sinogram:
            _logger.info('use sinogram')
            is_emission = (self._axis_params.projection_type == ProjectionType.absorption)
            subsampling = self._axis_params.sinogram_subsampling
            assert type(self._axis_params.sinogram_line) is int
            res = compute_frm_sinogram(scan=scan,
                                       line=self._axis_params.sinogram_line,
                                       is_emission=is_emission,
                                       subsampling=subsampling)
        elif mode in (AxisMode.manual, AxisMode.read):
            # If mode is read or manual the position_value is not computed and
            # we will keep the actual one (should have been defined previously)
            res = self._axis_params.value
        elif mode in self.RADIO_CALCULATIONS_METHODS:
            _logger.info('use radios, mode is %s' % mode.value)
            res = self.RADIO_CALCULATIONS_METHODS[mode](scan)
        else:
            raise NotImplementedError('Method for', mode, 'is not defined')
        return res

    @docstring(SingleProcess.program_name)
    @staticmethod
    def program_name():
        return 'tomwer_axis'

    @docstring(SingleProcess.program_version)
    @staticmethod
    def program_version():
        return tomwer.version.version

    @docstring(SingleProcess.definition)
    @staticmethod
    def definition():
        return 'Compute center of rotation'
