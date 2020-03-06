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
"""
This module provides global definitions and functions to manage dark and flat fields
especially for tomo experiments and workflows
"""

__authors__ = ["C. Nemoz", "H.Payno"]
__license__ = "MIT"
__date__ = "06/09/2017"

import functools
import os
import re
from glob import glob

import fabio
import numpy
from queue import Queue

from tomwer.core import settings
from tomwer.core import utils
from tomwer.core.process.baseprocess import SingleProcess, _input_desc, \
    _output_desc
from tomwer.core.signal import Signal
from tomwer.core.utils import getDARK_N
from tomwer.web.client import OWClient
from tomwer.core.log import TomwerLogger
from tomwer.core.scan.scanbase import TomoBase
from . import params as dkrf_reconsparams
from tomwer.core.process.reconstruction.ftseries.params import ReconsParams
from tomwer.core.scan.scanfactory import ScanFactory

logger = TomwerLogger(__name__)

try:
    from tomwer.synctools.rsyncmanager import RSyncManager
    has_rsync = False
except ImportError:
    logger.warning('rsyncmanager not available')
    has_rsync = True


class DarkRefs(SingleProcess, Queue):
    """Compute median/mean dark and ref from originals (dark and ref files)
    """

    inputs = [_input_desc(name='data', type=TomoBase, handler='process',
                          doc='scan path'), ]

    outputs = [_output_desc(name='data', type=TomoBase, doc='scan path'), ]

    WHAT_REF = 'refs'
    WHAT_DARK = 'dark'

    VALID_WHAT = (WHAT_REF, WHAT_DARK)
    """Tuple of valid option for What"""

    info_suffix = '.info'

    sigScanReady = Signal(TomoBase)

    sigUpdated = Signal()
    """Emitted when updated when reconstruction parameters are changed"""

    def __init__(self, reconsparams=None, file_ext='.edf'):
        """

        :param str file_ext:
        :param reconsparams: reconstruction parameters
        :type reconsparams: Union[None, ReconsParams, DKRFRP]
        """
        assert type(file_ext) is str
        SingleProcess.__init__(self, )
        Queue.__init__(self)
        self._recons_params = None
        assert reconsparams is None or isinstance(reconsparams, (ReconsParams, dkrf_reconsparams.DKRFRP))

        _recons_params = reconsparams
        if _recons_params is None:
            _recons_params = dkrf_reconsparams.DKRFRP()
        self.set_recons_params(recons_params=_recons_params)

        self._forceSync = False
        if hasattr(self._recons_params, 'sigChanged'):
            self._recons_params.sigChanged.connect(self._updateReconsParam)

        assert isinstance(self._recons_params, dkrf_reconsparams.DKRFRP)
        self._file_ext = file_ext

        self._updateReconsParam()

        self.worker = self._createThread()

    def set_recons_params(self, recons_params):
        if isinstance(recons_params, ReconsParams):
            self._recons_params = recons_params.dkrf
        elif isinstance(recons_params, dkrf_reconsparams.DKRFRP):
            self._recons_params = recons_params
        else:
            raise TypeError('recons_params should be an instance of '
                            'ReconsParams or DKRFRP')

    def _createThread(self):
        return DarkRefsWorker()

    def _updateReconsParam(self):
        self.sigUpdated.emit()

    def disconnect(self):
        if hasattr(self._recons_params, 'sigChanged'):
            self._recons_params.sigChanged.disconnect(self._updateReconsParam)

    def connect(self):
        if hasattr(self._recons_params, 'sigChanged'):
            self._recons_params.sigChanged.connect(self._updateReconsParam)

    def setPatternRecons(self, pattern):
        self._patternReconsFile = pattern

    def _signalScanReady(self, scan):
        assert isinstance(scan, TomoBase)
        self.sigScanReady.emit(scan)
        self.execNext()

    def process(self, scan):
        if scan is None:
            return

        if type(scan) is str:
            assert os.path.exists(scan)
            _scan = ScanFactory.create_scan_object(scan_path=scan)
        elif isinstance(scan, TomoBase):
            _scan = scan
        elif isinstance(scan, dict):
            _scan = ScanFactory.create_scan_object_frm_dict(scan)
        else:
            raise TypeError('scan should be an instance of TomoBase or path to '
                            'scan dircetory')
        # copy the current parameters to the scan ftseries_recons_params
        if _scan.ftseries_recons_params is None:
            _scan.ftseries_recons_params = self._instanciateReconsParams()
        assert isinstance(self._recons_params, dkrf_reconsparams.DKRFRP)
        assert isinstance(_scan.ftseries_recons_params, ReconsParams)
        assert self._recons_params is not None

        _scan.ftseries_recons_params.copy(self._recons_params)

        # TODO: now we can only pass the scan as it contains `ftseries_recons_params`
        assert _scan.ftseries_recons_params.dkrf is not None
        Queue.put(self, (_scan, _scan.ftseries_recons_params.dkrf))

        if self.canExecNext():
            self.execNext()

        if self._return_dict:
            return _scan.to_dict()
        else:
            return _scan

    def _instanciateReconsParams(self):
        return ReconsParams(empty=True)

    def execNext(self):
        """Launch the next reconstruction if any
        """
        # try catch is needed because a signal can still be emitted event if the
        # QObject has been destroyed.
        try:
            if super(DarkRefs, self).empty():
                return
        except Exception as error:
            logger.warning(error)
        else:
            scan, params = Queue.get(self)

            self._initWorker(scan=scan, params=params, file_ext=self._file_ext)

            self._launchWorker()
            # TODO: should be in scanready. ok for now since only used with
            # synchronization

            self.register_output(key='data', value=scan.path)

    def _launchWorker(self):
        if hasattr(self.worker, 'isRunning'):
            callback = functools.partial(self._signalScanReady,
                                         self.worker.directory)
            self.worker.finished.connect(callback)
            self.worker.start()
            if self._forceSync is True:
                self.worker.wait()
        else:
            self.worker.process()

    def _initWorker(self, scan, params, file_ext):
        assert isinstance(scan, TomoBase)
        assert type(file_ext) is str
        self.worker.init(scan=scan, params=params, file_ext=file_ext)

    def canExecNext(self):
        """
        Can we launch an ftserie reconstruction.
        Reconstruction can't be runned in parallel

        :return: True if no reconstruction is actually running
        """
        if hasattr(self.worker, 'isRunning'):
            return not self.worker.isRunning()
        else:
            return True

    def setForceSync(self, b):
        self._forceSync = True
        self.worker._forceSync = True

    @staticmethod
    def getRefHSTFiles(directory, prefix, file_ext='.edf'):
        """

        :return: the list of existing refs files in the directory according to
                 the file pattern.
        """
        res = []
        if os.path.isdir(directory) is False:
            logger.error(directory + ' is not a directory. Cannot extract '
                                     'RefHST files')
            return res

        for file in os.listdir(directory):
            if file.startswith(prefix) and file.endswith(
                    file_ext):
                res.append(os.path.join(directory, file))
                assert os.path.isfile(res[-1])
        return res

    @staticmethod
    def getDarkHSTFiles(directory, prefix, file_ext='.edf'):
        """

        :return: the list of existing refs files in the directory according to
                 the file pattern.
         """
        res = []
        if os.path.isdir(directory) is False:
            logger.error(directory + ' is not a directory. Cannot extract '
                                     'DarkHST files')
            return res
        for file in os.listdir(directory):
            _prefix = prefix
            if prefix.endswith(file_ext):
                _prefix = prefix.rstrip(file_ext)
            if file.startswith(_prefix) and file.endswith(file_ext):
                _file = file.lstrip(_prefix).rstrip(file_ext)
                if _file == '' or _file.isnumeric() is True:
                    res.append(os.path.join(directory, file))
                    assert os.path.isfile(res[-1])
        return res

    @staticmethod
    def getDarkPatternTooltip():
        return 'define the pattern to find, using the python `re` library.\n' \
               'For example: \n' \
               '   - `.*conti_dark.*` to filter files containing `conti_dark` sentence\n' \
               '   - `darkend[0-9]{3,4}` to filter files named `darkend` followed by three or four digit characters (and having the .edf extension)'

    @staticmethod
    def getRefPatternTooltip():
        return 'define the pattern to find, using the python `re` library.\n' \
               'For example: \n' \
               '   - `.*conti_ref.*` for files containing `conti_dark` sentence\n' \
               '   - `ref*.*[0-9]{3,4}_[0-9]{3,4}` to filter files named `ref` followed by any character and ending by X_Y where X and Y are groups of three or four digit characters.'

    @staticmethod
    def properties_help():
        return """
        - refs: 'None', 'Median', 'Average' \n
        - dark: 'None', 'Median', 'Average' \n
        """

    def setProperties(self, properties):
        # No properties stored for now
        if 'dark' in properties:
            self._recons_params.dark_calc_method = properties['dark']
        if 'refs' in properties:
            self._recons_params.ref_calc_method = properties['refs']


class DarkRefsWorker(OWClient):
    """Worker of the Dark refs"""

    TOMO_N = "TOMO_N"

    def __init__(self):
        OWClient.__init__(self, logger)
        self.recons_params = None
        self._forceSync = False
        self.scan = None
        self.directory = None

    def init(self, scan, params, file_ext):
        assert isinstance(scan, TomoBase)
        assert params is not None
        assert isinstance(params, dkrf_reconsparams.DKRFRP)
        assert type(file_ext) is str
        self.scan = scan
        self.directory = self.scan.path
        self.recons_params = params
        self._file_ext = file_ext

    def run(self):
        self.process()

    def process(self):
        if settings.isOnLbsram() and utils.isLowOnMemory(
                settings.get_lbsram_path()) is True:
            mess = 'low memory, do compute dark and flat field mean/median ' \
                   'for %s' % self.scan.path
            logger.processSkipped(mess)
            return

        if not(self.scan and
               os.path.exists(self.scan.path) and
               os.path.isdir(self.scan.path)):
            logger.warning("folder %s is not existing" % self.scan.path)
            return
        whats = (DarkRefs.WHAT_REF, DarkRefs.WHAT_DARK)
        modes = (self.recons_params.ref_calc_method, self.recons_params.dark_calc_method)
        for what, mode in zip(whats, modes):
            self._originalsDark = []
            self._originalsRef = []
            self.compute(directory=self.scan.path, what=what, mode=mode)

    def compute(self, directory, what, mode):
        """Compute the requested what in the given mode for `directory`

        :param str directory: path of the scan
        :param what: what to compute (ref or dark)
        :param mode: how to compute it (median or average...)
        """
        assert type(directory) is str

        def removeFiles():
            """Remove orignals files fitting the what (dark or ref)"""
            if what is DarkRefs.WHAT_DARK:
                # In the case originals has already been found for the median
                # calculation
                if len(self._originalsDark) > 0:
                    files = self._originalsDark
                else:
                    files = getOriginals(DarkRefs.WHAT_DARK)
            elif what is DarkRefs.WHAT_REF:
                if len(self._originalsRef) > 0:
                    files = self._originalsRef
                else:
                    files = getOriginals(DarkRefs.WHAT_REF)
            else:
                logger.error(
                    'the requested what (%s) is not recognized. '
                    'Can\'t remove corresponding file' % what)
                return

            _files = set(files)
            if len(files) > 0:
                if has_rsync:
                    logger.info('ask RSyncManager for removal of %s files in %s' % (what, directory))
                    # for lbsram take into account sync from data watcher
                    if directory.startswith(settings.get_lbsram_path()):
                        for f in files:
                            _files.add(f.replace(settings.get_lbsram_path(),
                                                 settings.get_dest_path(),
                                                 1))
                    RSyncManager().removeSyncFiles(dir=directory,
                                                   files=_files,
                                                   block=self._forceSync)
                else:
                    for _file in _files:
                        try:
                            os.remove(_file)
                        except Exception as e:
                            logger.error(e)

        def getOriginals(what):
            if what is DarkRefs.WHAT_REF:
                try:
                    pattern = re.compile(self.recons_params.ref_pattern)
                except:
                    pattern = None
                    logger.error('Fail to compute regular expresion for %s' % self.recons_params.ref_pattern)
            elif what is DarkRefs.WHAT_DARK:
                re.compile(self.recons_params.dark_pattern)
                try:
                    pattern = re.compile(self.recons_params.dark_pattern)
                except:
                    pattern = None
                    logger.error('Fail to compute regular expresion for %s' % self.recons_params.dark_pattern)

            filelist_fullname = []
            if pattern is None:
                return filelist_fullname
            for file in os.listdir(directory):
                if pattern.match(file) and file.endswith(self._file_ext):
                    if (file.startswith(self.recons_params.ref_prefix) or
                            file.startswith(self.recons_params.dark_prefix)) is False:
                        filelist_fullname.append(os.path.join(directory, file))
            return sorted(filelist_fullname)

        def setup():
            """setup parameter to process the requested what

            :return: True if there is a process to be run, else false
            """
            def getNDigits(_file):
                file_without_scanID = _file.replace(os.path.basename(directory), '', 1)
                return len(re.findall(r'\d+', file_without_scanID))

            def dealWithPCOTomo():
                filesPerSerie = {}
                if self.nfiles % self.nacq is 0:
                    assert self.nacq < self.nfiles
                    self.nseries = self.nfiles // self.nacq
                    self.series = self.fileNameList
                else:
                    logger.warning('Fail to deduce series')
                    return None, None

                linear = getNDigits(self.fileNameList[0]) < 2
                if linear is False:
                    # which digit pattern contains the file number?
                    lastone = True
                    penulti = True
                    for first_files in range(self.nseries - 1):
                        digivec_1 = re.findall(r'\d+', self.fileNameList[
                            first_files])
                        digivec_2 = re.findall(r'\d+', self.fileNameList[
                            first_files + 1])
                        if lastone:
                            lastone = (
                                (int(digivec_2[-1]) - int(digivec_1[-1])) == 0)
                        if penulti:
                            penulti = (
                                (int(digivec_2[-2]) - int(digivec_1[-2])) == 0)

                    linear = not penulti

                if linear is False:
                    digivec_1 = re.findall(r'\d+', self.fileNameList[
                        self.nseries - 1])
                    digivec_2 = re.findall(r'\d+',
                                           self.fileNameList[self.nseries])
                    # confirm there is 1 increment after self.nseries in the uperlast last digit patern
                    if ((int(digivec_2[-2]) - int(digivec_1[-2])) != 1):
                        linear = True

                # series are simple sublists in main filelist
                # self.series = []
                if linear is True:
                    is_there_digits = len(
                        re.findall(r'\d+', self.fileNameList[0])) > 0
                    if is_there_digits:
                        serievec = set(
                            [re.findall(r'\d+', self.fileNameList[0])[-1]])
                    else:
                        serievec = set(['0000'])
                    for i in range(self.nseries):
                        if is_there_digits:
                            serie = re.findall(r'\d+', self.fileNameList[i * self.nacq])[-1]
                            serievec.add(serie)
                            filesPerSerie[serie] = self.fileNameList[i * self.nacq:(i+1)*self.nacq]
                        else:
                            serievec.add('%04d' % i)
                # in the sorted filelist, the serie is incremented, then the acquisition number:
                else:
                    self.series = self.fileNameList[0::self.nseries]
                    serievec = set(
                        [re.findall(r'\d+', self.fileNameList[0])[-1]])
                    for serie in serievec:
                        # serie = re.findall(r'\d+', self.fileNameList[i])[-1]
                        # serievec.add(serie)
                        filesPerSerie[serie] = self.fileNameList[0::self.nseries]
                serievec = list(sorted(serievec))

                if len(serievec) > 2:
                    logger.error('DarkRefs do not deal with multiple scan.'
                                 ' (scan %s)' % directory)
                    return None, None
                assert len(serievec) <= 2
                if len(serievec) > 1:
                    key = serievec[-1]
                    tomoN = self.getInfo(self.TOMO_N)
                    if tomoN is None:
                        logger.error("Fail to found information %s. Can't "
                                     "rename %s" % (self.TOMO_N, key))
                    del serievec[-1]
                    serievec.append(str(tomoN).zfill(4))
                    filesPerSerie[serievec[-1]] = filesPerSerie[key]
                    del filesPerSerie[key]
                    assert len(serievec) is 2
                    assert len(filesPerSerie) is 2

                return serievec, filesPerSerie

            # start setup function
            if mode == dkrf_reconsparams.Method.none:
                return False
            if what == 'dark':
                self.out_prefix = self.recons_params.dark_prefix
                self.info_nacq = 'DARK_N'
            else:
                self.out_prefix = self.recons_params.ref_prefix
                self.info_nacq = 'REF_N'

            # init
            self.nacq = 0
            """Number of acquisition runned"""
            self.files = 0
            """Ref or dark files"""
            self.nframes = 1
            """Number of frame per ref/dark file"""
            self.serievec = ['0000']
            """List of series discover"""
            self.filesPerSerie = {}
            """Dict with key the serie id and values list of files to compute
            for median or mean"""
            self.infofile = ''
            """info file of the acquisition"""

            # sample/prefix and info file
            self.prefix = os.path.basename(directory)
            extensionToTry = (DarkRefs.info_suffix, '0000' + DarkRefs.info_suffix)
            for extension in extensionToTry:
                infoFile = os.path.join(directory, self.prefix + extension)
                if os.path.exists(infoFile):
                    self.infofile = infoFile
                    break

            if self.infofile == '':
                logger.debug('fail to found .info file for %s' % directory)

            """
            Set filelist
            """
            # do the job only if not already done and overwrite not asked
            self.out_files = sorted(
                glob(directory + os.sep + '*.' + self._file_ext))

            self.filelist_fullname = getOriginals(what)
            self.fileNameList = []
            [self.fileNameList.append(os.path.basename(_file)) for _file in self.filelist_fullname]
            self.fileNameList = sorted(self.fileNameList)
            self.nfiles = len(self.filelist_fullname)
            # if nothing to process
            if self.nfiles == 0:
                logger.info('no %s for %s, because no file to compute found' % (what, directory))
                return False

            self.fid = fabio.open(self.filelist_fullname[0])
            self.nframes = self.fid.getNbFrames()
            self.nacq = 0
            # get the info of number of acquisitions
            if self.infofile != '':
                self.nacq = self.getInfo(self.info_nacq)

            if self.nacq == 0:
                self.nacq = self.nfiles

            self.nseries = 1
            if self.nacq > self.nfiles:
                # get ready for accumulation and/or file multiimage?
                self.nseries = self.nfiles
            if self.nacq < self.nfiles and getNDigits(self.fileNameList[0]) < 2:
                self.nFilePerSerie = self.nseries
                self.serievec, self.filesPerSerie = dealWithPCOTomo()
            else:
                self.series = self.fileNameList
                self.serievec = _getSeriesValue(self.fileNameList)
                self.filesPerSerie, self.nFilePerSerie = groupFilesPerSerie(self.filelist_fullname, self.serievec)

            if self.filesPerSerie is not None:
                for serie in self.filesPerSerie:
                    for _file in self.filesPerSerie[serie]:
                        if what == 'dark':
                            self._originalsDark.append(os.path.join(self.directory, _file))
                        elif what == 'ref':
                            self._originalsRef.append(os.path.join(self.directory, _file))

            return self.serievec is not None and self.filesPerSerie is not None

        def _getSeriesValue(fileNames):
            assert (len(fileNames) > 0)
            is_there_digits = len(re.findall(r'\d+', fileNames[0])) > 0
            series = set()
            i = 0
            for fileName in fileNames:
                if is_there_digits:
                    name = fileName.rstrip(self._file_ext)
                    file_index = name.split('_')[-1]
                    rm_not_numeric = re.compile(r'[^\d.]+')
                    file_index = rm_not_numeric.sub('', file_index)
                    series.add(file_index)
                else:
                    series.add('%04d' % i)
                    i += 1
            return list(series)

        def groupFilesPerSerie(files, series):
            def findFileEndingWithSerie(poolFiles, serie):
                res = []
                for _file in poolFiles:
                    _f = _file.rstrip('.edf')
                    if _f.endswith(serie):
                        res.append(_file)
                return res

            def checkSeriesFilesLength(serieFiles):
                length = -1
                for serie in serieFiles:
                    if length == -1:
                        length = len(serieFiles[serie])
                    elif len(serieFiles[serie]) != length:
                        logger.error('Series with inconsistant number of ref files')

            assert len(series) > 0
            if len(series) is 1:
                return {series[0]: files}, len(files)
            assert len(files) > 0

            serieFiles = {}
            unattributedFiles = files.copy()
            for serie in series:
                serieFiles[serie] = findFileEndingWithSerie(unattributedFiles, serie)
                [unattributedFiles.remove(_f) for _f in serieFiles[serie]]

            if len(unattributedFiles) > 0:
                logger.error('Failed to associate %s to any serie' % unattributedFiles)
                return {}, 0

            checkSeriesFilesLength(serieFiles)

            return serieFiles, len(serieFiles[list(serieFiles.keys())[0]])

        def process():
            """process calculation of the what"""
            if mode is dkrf_reconsparams.Method.none:
                return
            shape = fabio.open(self.filelist_fullname[0]).getDims()

            for i in range(len(self.serievec)):
                largeMat = numpy.zeros((self.nframes * self.nFilePerSerie,
                                        shape[1],
                                        shape[0]))

                if what == 'dark' and len(self.serievec) is 1:
                    fileName = self.out_prefix
                    if fileName.endswith(self._file_ext) is False:
                        fileName = fileName + self._file_ext
                else:
                    fileName = self.out_prefix.rstrip(self._file_ext) \
                               + self.serievec[i] + self._file_ext
                fileName = os.path.join(directory, fileName)
                if os.path.isfile(fileName):
                    if ((what == 'refs' and self.recons_params.overwrite_ref is False) or
                            (what == 'dark' and self.recons_params.overwrite_dark is False)):
                        logger.info(
                            'skip creation of %s, already existing' % fileName)
                        continue

                if self.nFilePerSerie == 1:
                    fSerieName = os.path.join(directory, self.series[i])
                    header = {'method': mode.name + ' on 1 image'}
                    header['SRCUR'] = utils.getClosestSRCurrent(scan=directory,
                                                                refFile=fSerieName)
                    if self.nframes == 1:
                        largeMat[0] = fabio.open(fSerieName).data
                    else:
                        handler = fabio.open(fSerieName)
                        dShape = (self.nframes, handler.dim2, handler.dim1)
                        largeMat = numpy.zeros(dShape)
                        for iFrame in range(self.nframes):
                            largeMat[iFrame] = handler.getframe(iFrame).data
                else:
                    header = {'method': mode.name + ' on %d images' % self.nFilePerSerie}
                    header['SRCUR'] = utils.getClosestSRCurrent(scan=directory,
                                                                refFile=self.series[i][0])
                    for j, fName in zip(range(self.nFilePerSerie), self.filesPerSerie[self.serievec[i]]):
                        file_BigMat = fabio.open(fName)
                        if self.nframes > 1:
                            for fr in range(self.nframes):
                                jfr = fr + j * self.nframes
                                largeMat[jfr] = file_BigMat.getframe(
                                    fr).getData()
                        else:
                            largeMat[j] = file_BigMat.data

                if mode == dkrf_reconsparams.Method.median:
                    data = numpy.median(largeMat, axis=0)
                elif mode == dkrf_reconsparams.Method.average:
                    data = numpy.mean(largeMat, axis=0)
                else:
                    assert mode != dkrf_reconsparams.Method.none
                    logger.error(
                        'Unrecognized calculation type request %s' % mode)
                    return
                self.nacq = getDARK_N(directory) or 1
                if what == 'dark' and self.nacq > 1:  # and self.nframes == 1:
                    data = data / self.nacq
                    # add one to add to avoid division by zero
                    # data = data + 1
                file_desc = fabio.edfimage.EdfImage(data=data,
                                                    header=header)
                i += 1
                _ttype = numpy.uint16 if what == 'dark' else numpy.int32
                file_desc.write(fileName, force_type=_ttype)

        if directory is None:
            return
        if setup():
            logger.info('start proccess darks and flat fields for %s' % self.scan.path)
            process()
            logger.info('end proccess darks and flat fields')
        if ((what == 'dark' and self.recons_params.remove_dark is True) or
                (what == 'refs' and self.recons_params.remove_ref is True)):
            removeFiles()

    def getInfo(self, what):
        with open(self.infofile) as file:
            infod = file.readlines()
            for line in infod:
                if what in line:
                    return int(line.split('=')[1])
        # not found:
        return 0

    def getDarkFiles(self, directory):
        """

        :return: the list of existing darks files in the directory according to
                 the file pattern.
         """
        patternDark = re.compile(self.recons_params.dark_pattern)

        res = []
        for file in os.listdir(directory):
            if patternDark.match(file) is not None and file.endswith(
                    self._file_ext):
                res.append(os.path.join(directory, file))
        return res

    def getRefFiles(self, directory):
        """

        :return: the list of existing refs files in the directory according to
                 the file pattern.
         """
        patternRef = re.compile(self.recons_params.ref_pattern)

        res = []
        for file in os.listdir(directory):
            if patternRef.match(file) and file.endswith(self._file_ext):
                res.append(os.path.join(directory, file))
        return res
