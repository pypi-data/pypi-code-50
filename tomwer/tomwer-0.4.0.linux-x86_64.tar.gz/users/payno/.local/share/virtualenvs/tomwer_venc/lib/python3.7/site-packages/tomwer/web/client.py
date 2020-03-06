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
"""module defining functions and class to communicate a status to the
orange-server.
The orange-server is used to display the advancement of the workflow.
"""

__authors__ = ["H.Payno"]
__license__ = "MIT"
__date__ = "28/04/2017"


try:
    import graypy
    has_graypy = True
except:
    has_graypy = False
from .config import grayport_port, grayport_host
import os
import socket
import logging

_logger = logging.getLogger(__name__)

global _INFO_UNKNOWN_HOST_NAME
_INFO_UNKNOWN_HOST_NAME = False
"""Cache variable to avoid several log about this information"""


class OWClient(object):
    """Orange widget Client can emit information about his advancement
    """

    WORKFLOW_INFO = 'workflow'  # general information about a workflow
    SCAN_INFO = 'scan'  # information focus on a scan

    def __init__(self, loggers):
        assert loggers is not None
        if OWClient._knows_hostname(hostname=grayport_host) is False:
            global _INFO_UNKNOWN_HOST_NAME
            if _INFO_UNKNOWN_HOST_NAME is False:
                _logger.warning('unknow host %s' % grayport_host)
                _INFO_UNKNOWN_HOST_NAME = True
            return
        if type(loggers) not in (list, tuple):
            loggers = (loggers, )
        for logger in loggers:
            if os.environ.get('ORANGE_WEB_LOG', 'True') is 'True':
                try:
                    self.graylogHandler = graypy.GELFHandler(grayport_host, grayport_port)
                except:
                    logger.error('Fail to create GELFHandler. Won\'t report log message')
                else:
                    logger.addHandler(self.graylogHandler)
                    logger.debug('- add graypy handler')
            else:
                info = 'No log will be send to graylog.'
                info += 'ORANGE_WEB_LOG variable is setted to False'
                logger.debug(info)

    @staticmethod
    def _knows_hostname(hostname):
        if hostname is None:
            return False
        try:
            socket.gethostbyname(hostname)
            return True
        except socket.error:
            return False
