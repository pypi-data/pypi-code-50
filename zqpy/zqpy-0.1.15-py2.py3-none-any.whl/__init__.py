print(" Init zqpy core By ZhouQing")

import os, sys
sys.path.append(os.path.dirname(__file__))

from LogService import LogServiceClass
from FileService import FileServiceClass
from HttpService import HttpServiceClass
from RegexService import RegexServiceClass
from ThreadService import ThreadServiceClass
from TimeService import TimeServiceClass
from VideoDownloadService import VideoDownloadServiceClass
from LocallizeService import LocallizeServiceClass

from WaitExecutService import WaitExecutServiceClass
from QrCodeService import QrCodeServiceClass
from ToolsService import ToolsServiceClass

from MailService import MailServiceClass


def vGetLogTag():
    return "BasePyClass"

def vLocallizePath():
    return None

Log = LogServiceClass(tag=vGetLogTag())
LogD = Log.LogD
LogW = Log.LogW
LogE = Log.LogE
FileService = FileServiceClass()
HttpService = HttpServiceClass()
RegexService = RegexServiceClass()
ThreadService = ThreadServiceClass()
TimeService = TimeServiceClass()
VideoDownloadService = VideoDownloadServiceClass()
LocalizeService = LocallizeServiceClass(path=(vLocallizePath() or None))
WaitExecutService = WaitExecutServiceClass()
QrCodeService = QrCodeServiceClass()
ToolsService = ToolsServiceClass()
MailService = MailServiceClass()
########################################通用方法##########################################
def GetLocalize(key):
    return LocalizeService.Get(key)

############################################子类可重写##########################################