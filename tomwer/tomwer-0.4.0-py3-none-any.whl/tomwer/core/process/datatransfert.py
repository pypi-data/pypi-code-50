# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2017 European Synchrotron Radiation Facility
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
# ###########################################################################*/

__authors__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "05/07/2017"


import os
import shutil

from tomwer.core.process.baseprocess import SingleProcess, _input_desc, \
    _output_desc
from tomwer.core.scan.scanfactory import ScanFactory
from tomwer.core.settings import get_lbsram_path, get_dest_path
from tomwer.core.signal import Signal
from tomwer.core.utils import logconfig, rebaseParFile
from tomwer.core.log import TomwerLogger
from tomwer.core.scan.scanbase import TomoBase

logger = TomwerLogger(__name__)

try:
    from tomwer.synctools.rsyncmanager import RSyncManager
except ImportError:
    logger.warning('rsyncmanager not available')
    has_rsync = False
else:
    has_rsync = True


class FolderTransfert(SingleProcess):
    """Manage the copy of scan.

    .. warning : the destination directory is find out from the file system
                 if /lbsramxxx exists for example...
                 In the case we couldn't found the output directory then we
                 will ask for the user to set it.
    """

    inputs = [_input_desc(name='data', type=TomoBase, handler='process',
                          doc='scan path'), ]
    outputs = [_output_desc(name='data', type=TomoBase, doc='scan path')]

    scanready = Signal(TomoBase)

    def __init__(self):
        SingleProcess.__init__(self)
        self.turn_off_print = False
        self._destDir = None
        """
        output directory if forced. By default based by the env variable
        'TARGET_OUTPUT_FOLDER' if exists, else set to '/data/visitor'
         """
        self._copying = False
        self._block = False

    def setProperties(self, properties):
        # No properties stored for now
        if 'dest_dir' in properties:
            self.setDestDir(properties['dest_dir'])

    def _getDefaultOutputDir(self):
        """Return the default output dir based on the computer setup
        """
        if 'TARGET_OUTPUT_FOLDER' in os.environ:
            return os.environ['TARGET_OUTPUT_FOLDER']

        if os.path.isdir('/data/visitor'):
            return '/data/visitor'

        return ''

    def process(self, scan, move=False, force=True, noRsync=False):
        """Launch the process process

        :param scan: the path to the file we want to move/process
        :type scan: :class:`.TomoBase`
        :param move: if True, directly move the files. Otherwise copy the files
        :param force: if True then force the copy even if the file/folder already
            exists
        :param bool noRSync: True if we wan't do sue shutil instead of rsync.
        """
        if scan is None:
            return

        _scan = scan
        if type(_scan) is dict:
            _scan = ScanFactory.create_scan_object_frm_dict(scan)

        assert isinstance(_scan, TomoBase)
        assert move in (True, False)
        if not os.path.isdir(_scan.path):
            logger.warning('scan path given is not a directory (%s).' % _scan.path)
            return

        logger.info('synchronisation with scanPath')
        outputdir = self.getDestinationDir(_scan.path)
        if outputdir is None:
            return

        self._pretransfertOperations(_scan.path, outputdir)
        # as we are in the workflow we want this function to be bloking.
        # so we will not used a thread for folder synchronization
        # for now rsync is not delaing with force option
        if not has_rsync or noRsync is True or RSyncManager().canUseRSync() is False:
            logger.info("Can't use rsync, copying files")
            try:
                if move is True:
                    self._moveFiles(scanPath=_scan.path,
                                    outputdir=os.path.dirname(outputdir),
                                    force=force)
                else:
                    self._copyFiles(scanPath=_scan.path,
                                    outputdir=outputdir,
                                    force=force)
            except shutil.Error as e:
                raise e
            else:
                self.__noticeTransfertSuccess(_scan.path, outputdir)
        else:
            source = _scan.path
            if not source.endswith(os.path.sep):
                source = source + os.path.sep
            target = outputdir

            if not target.endswith(os.path.sep):
                target = target + os.path.sep

            self._signalCopying(scanID=source, outputdir=target)

            RSyncManager().syncFolder(source=source,
                                      target=target,
                                      block=self._block,
                                      delete=True,
                                      handler=self.__noticeTransfertSuccess,
                                      setAllRights=True)

        self.register_output(key='data', value=outputdir)

        if self._return_dict:
            return _scan.to_dict()
        else:
            return _scan


    def _pretransfertOperations(self, scanfolder, outputdir):
        """Operation to be run before making the transfert of the scan"""
        self._updateParFiles(scanfolder, outputdir)

    def _updateParFiles(self, scanfolder, outputdir):
        """Update all path contained in the .par files to fit the new outpudir
        """
        for _file in os.listdir(scanfolder):
            if _file.lower().endswith('.par'):
                rebaseParFile(os.path.join(scanfolder, _file),
                              oldfolder=scanfolder, newfolder=outputdir)

    def __noticeTransfertSuccess(self, scanPath, outputdir):
        self._signalCopySucceed()
        logger.processEnded('transfert succeed',
                            extra={logconfig.DOC_TITLE: self._scheme_title,
                                   logconfig.FROM: scanPath,
                                   logconfig.TO: outputdir})
        self.signalTransfertOk(outputdir)

    def signalTransfertOk(self, scanID):
        if scanID is None:
            return
        assert isinstance(scanID, str)
        # here we create a new scan since the path changed (from transfert)
        scan = ScanFactory.create_scan_object(scan_path=scanID)
        self.scanready.emit(scan.path)

    def _copyFiles(self, scanPath, outputdir, force):
        """Copying files and removing them"""
        assert type(scanPath) is str
        assert type(outputdir) is str
        assert(os.path.isdir(scanPath))
        if force is False:
            assert(os.path.isdir(outputdir))
        # create the destination dir
        if not os.path.isdir(outputdir):
            def createDirAndTopDir(_dir):
                if not os.path.isdir(os.path.dirname(_dir)):
                    createDirAndTopDir(os.path.dirname(_dir))
                os.mkdir(_dir)
            createDirAndTopDir(outputdir)
        # we can't copy directly the top folder because he is already existing
        for f in os.listdir(scanPath):
            file = os.path.join(scanPath, f)
            fileDest = os.path.join(outputdir, f)
            if force is True:
                if os.path.isdir(fileDest):
                    shutil.rmtree(fileDest)
                if os.path.isfile(fileDest):
                    os.remove(fileDest)
            if os.path.exists(fileDest):
                raise FileExistsError(fileDest, 'already exists')
            if os.path.isdir(file):
                shutil.copytree(src=file, dst=fileDest)
            else:
                shutil.copy2(src=file, dst=fileDest)

        info = 'Removing directory at %s' % scanPath
        logger.info(info)
        shutil.rmtree(scanPath)
        info = 'sucessfuly removed file at %s !!!' % scanPath
        logger.info(info)

    def _moveFiles(self, scanPath, outputdir, force):
        """Function simply moving files"""
        assert(os.path.isdir(scanPath))
        if force is False:
            assert(os.path.isdir(outputdir))

        logger.debug('synchronisation with scanPath',
                     extra={logconfig.DOC_TITLE: self._scheme_title})

        target = os.path.join(outputdir, os.path.basename(scanPath))
        if force is True and os.path.isdir(target):
            shutil.rmtree(target)
        shutil.move(scanPath, outputdir)

    def _requestFolder(self):
        out = None
        while(out is None):
            out = input('please give the output directory : \n')
            if not os.path.isdir(out):
                warning = 'given path ' + out
                warning += ' is not a directory, please give a valid directory'
                logger.warning(warning)
                out = None
        return out

    def _getOutputDirSpec(self):
        return None

    def _getOutputDirLBS(self, scanPath):
        if scanPath.startswith(get_lbsram_path()):
            return scanPath.replace(get_lbsram_path(), get_dest_path(), 1)
        else:
            return None

    def getDestinationDir(self, scanPath):
        """Return the destination directory. The destination directory is the
        root directory"""
        if self._destDir is not None:
            return os.path.join(self._destDir, os.path.basename(scanPath))

        # try to get outputdir from spec
        scanIDPath = os.path.abspath(scanPath)

        outputdir = self._getOutputDirSpec() or self._getOutputDirLBS(scanIDPath)
        if outputdir is None:
            outputdir = self._requestFolder()

        return outputdir

    def setDestDir(self, dist):
        """Force the outpudir to dist.

        :param str dist: path to the folder. If None remove force behavior
        """
        self._destDir = dist
        if self._destDir is not None and os.path.isdir(self._destDir):
            logger.warning('Given path %s is not a directory' % self._destDir)

    # some function to print the output in the terminal #

    def _signalCopying(self, scanID, outputdir):
        self._copying = True
        if self.turn_off_print is False:
            print('######################################')
            print('###')
            print('###')
            print('### copying files ', scanID, " to ", outputdir)
            print('### ...')

        info = 'start moving folder from %s to %s' % (scanID, outputdir)
        logger.info(info,
                    extra={logconfig.DOC_TITLE: self._scheme_title})

    def _signalCopyFailed(self):
        self._copying = False
        if self.turn_off_print is False:
            print('###')
            print('### copy failed')
            print('###')
            print('######################################')

    def _signalCopySucceed(self):
        self._copying = False
        if self.turn_off_print is False:
            print('###')
            print('### copy succeeded')
            print('###')
            print('######################################')

    def isCopying(self):
        """

        :return: True if the folder transfert is actually doing a copy
        """
        return self._copying

    def setForceSync(self, b):
        """

        :param bool b: if True then folderTransfert will wait until transfert
            is done to be released. Otherwise will launch a 'free' thread wich
            will notice transfert end later.
        """
        self._block = b

    def getOutput(self, scan):
        """
        
        :param scan: 
        :return: 
        """
        return os.path.join(self.getDestinationDir(scan), os.path.basename(scan))
