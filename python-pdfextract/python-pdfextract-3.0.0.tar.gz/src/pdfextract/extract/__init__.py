from jpype import *
import chardet
import threading

lock = threading.Lock()

ByteArrayInputStream        = JClass('java.io.ByteArrayInputStream')
ByteArrayOutputStream       = JClass('java.io.ByteArrayOutputStream')


class Extractor(object):
    extractor = None
    data      = None

    def __init__(self, **kwargs):
        if 'pdf' in kwargs:
            self.data = kwargs['pdf']
        if "keepBrTags" in kwargs:
            self.keepBrTags = kwargs['keepBrTags']
        else:
            self.keepBrTags = 0
        if "getPermission" in kwargs:
            self.getPermission = kwargs['getPermission']
        else:
            self.getPermission = 0 
        try:
            # make it thread-safe
            if threading.activeCount() > 1:
                if isThreadAttachedToJVM() == False:
                    attachThreadToJVM()
            lock.acquire()

            self.extractor = JClass("pdfextract.PDFExtract")()

        finally:
            lock.release()

    def setData(self,data):
        self.data = data

    def getHTML(self):
        self.reader = ByteArrayInputStream(self.data)
        return str(self.extractor.Extract(self.reader, self.keepBrTags, self.getPermission).toString())
