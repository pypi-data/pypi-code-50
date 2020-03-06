#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import argparse
from silx.gui import qt
import signal
import functools
from tomwer.gui import icons
from tomwer.gui.utils.splashscreen import getMainSplashScreen
from tomwer.gui.reconstruction.axis import AxisWindow
from tomwer.core.scan.scanfactory import ScanFactory
from tomwer.synctools.axis import QAxisRP
from tomwer.core.process.reconstruction.axis.axis import AxisProcess, NoAxisUrl
from silx.io.url import DataUrl
import logging


logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)


class _AxisProcessGUI(AxisProcess, AxisWindow):
    def __init__(self, scan, axis_params):
        AxisProcess.__init__(self, axis_params=axis_params)
        AxisWindow.__init__(self, axis_params=axis_params)
        self.hideLockButtons()
        self.hideApplyButtons()
        self.setScan(scan=scan)

        # connect Signal / Slot
        callback = functools.partial(self.process, scan)
        self.sigComputationRequested.connect(callback)
        self.setWindowIcon(icons.getQIcon('tomwer'))

    def compute(self, scan, wait=True):
        mess = ' '.join(('start axis calculation with',
                         scan.axis_params.axis_url_1.url.file_path()))
        _logger.info(mess)
        try:
            AxisProcess.compute(self, scan=scan, wait=wait)
        except NoAxisUrl:
            msg = qt.QMessageBox(self)
            msg.setIcon(qt.QMessageBox.Warning)
            text = "Unable to find url to compute the axis, please select them " \
                   "from the `axis input` tab"
            msg.setText(text)
            msg.exec_()
            return None
        else:
            position = scan.axis_params.value
            assert isinstance(position, (float, type(None)))
            frm = 'sinogram' if scan.axis_params.use_sinogram else 'radio'
            AxisWindow.setPosition(self, frm=frm, value=position)
            return position


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--scan-path',
        help='scan path',
        default=None)
    parser.add_argument(
        '--use-sinogram',
        help='use the signoram from radio for computing COR. This only work'
             'with the =scan-path option',
        action="store_true",
        default=False)
    parser.add_argument(
        '--radio1',
        help='first file to be used for computing axis',
        default=None)
    parser.add_argument(
        '--radio2',
        help='second file to be used for computing axis',
        default=None)
    parser.add_argument(
        '--debug',
        dest="debug",
        action="store_true",
        default=False,
        help='Set logging system in debug mode')

    options = parser.parse_args(argv[1:])

    if options.debug:
        logging.root.setLevel(logging.DEBUG)

    global app  # QApplication must be global to avoid seg fault on quit
    app = qt.QApplication.instance() or qt.QApplication([])
    splash = getMainSplashScreen()
    qt.QApplication.setOverrideCursor(qt.Qt.WaitCursor)
    qt.QApplication.processEvents()

    qt.QLocale.setDefault(qt.QLocale.c())
    signal.signal(signal.SIGINT, sigintHandler)
    sys.excepthook = qt.exceptionHandler

    timer = qt.QTimer()
    timer.start(500)
    # Application have to wake up Python interpreter, else SIGINT is not
    # catch
    timer.timeout.connect(lambda: None)

    if options.scan_path is not None:
        options.scan_path = options.scan_path.rstrip(os.path.sep)
        scan = ScanFactory.create_scan_object(scan_path=options.scan_path)
    else:
        scan = ScanFactory.mock_scan()
        if options.file1 is None:
            raise ValueError('At least a file or a scan path should be given')

    # if (scan.get_scan_range() != 360 and
    #         options.use_sinogram is True):
    #     raise ValueError('Unable to use sinogram option for scan range != 360')

    if options.radio1 is not None:
        radio1 = DataUrl(file_path=options.radio1, scheme='fabio')
        scan.axis_params.axis_url_1 = radio1
        if options.radio2 is not None:
            radio2 = DataUrl(file_path=options.radio2, scheme='fabio')
        else:
            radio2 = None
        scan.axis_params.axis_url_2 = radio2

    if options.debug:
        _logger.setLevel(logging.DEBUG)

    axis_params = QAxisRP()
    axis_params.use_sinogram = options.use_sinogram
    if scan.get_dim_2() is not None:
        axis_params.sinogram_line = scan.get_dim_2() // 2

    window = _AxisProcessGUI(scan=scan, axis_params=axis_params)
    window.setWindowTitle('axis')
    window.setWindowIcon(icons.getQIcon('tomwer'))

    splash.finish(window)
    window.show()
    qt.QApplication.restoreOverrideCursor()
    app.exec_()


def getinputinfo():
    return "tomwer axis [scanDir]"


def sigintHandler(*args):
    """Handler for the SIGINT signal."""
    qt.QApplication.quit()


if __name__ == '__main__':
    main(sys.argv)
