import pythoncom
from xabase import XASession, XAQuery, XAReal
import xaio
import time

class Session(XASession):
    def __init__(self):
        super().__init__()

    def login(self, ID, PW, CERT, SERVER, PORT):
        connected = self.ConnectServer(SERVER, PORT)
        if connected:
            self.Login(ID, PW, CERT, 0, False)
            while self.OnLogin is None:
                pythoncom.PumpWaitingMessages()
            report = self.OnLogin
            self.OnLoginReset()
        else:
            report = self.last_error
        return report

    @property
    def last_error(self):
        szCode  = self.GetLastError()
        szMsg   = self.GetErrorMessage(szCode)
        return dict(szCode=szCode, szMsg=szMsg)

class Query(XAQuery):
    def __init__(self, trcode):
        super().__init__()
        self.set_profile(trcode)
        self.LoadFromResFile(self.resfile)

    def __call__(self, **kwargs):
        self.input_kwargs = kwargs
        return self.request()

    def set_profile(self, trcode):
        self.trcode     = trcode
        self.resfile    = xaio.get_resfile(trcode)
        self.trname     = xaio.get_trname(trcode)
        self.in_blocks  = xaio.get_input(trcode)
        self.out_blocks = xaio.get_output(trcode)
        self.out_frame  = xaio.get_output_frame(trcode)
        self.is_cts     = xaio.get_is_cts(trcode)
        self.cts_fields = xaio.get_cts_fields(trcode)

    def request(self):
        self._set_field_data()
        self.Request(self.is_cts)
        while self.OnReceiveData is None:
            pythoncom.PumpWaitingMessages()
            time.sleep(0.1)
        self.OnReceiveDataReset()
        self._get_field_data()

        if self.is_cts and self.IsNext:
            return self.request()
        else:
            return self.out_frame


    def _set_field_data(self):
        for in_block in self.in_blocks:
            for arg in in_block["args"]:
                self.SetFieldData(
                    szBlockName = in_block["name"], 
                    szFieldName = arg, 
                    nOccursIndex= in_block["occurs"], 
                    szData      = self.input_kwargs.get(arg))

    def _get_field_data(self):
        for out_block in self.out_blocks:
            for i in range(self.GetBlockCount(szBlockName = out_block["name"])):
                for arg in out_block["args"]:
                    szData = self.GetFieldData(
                        szBlockName = out_block["name"], 
                        szFieldName = arg,
                        nOccursIndex= i)
                    self.out_frame[out_block["name"]][arg].append(szData)

                    if self.is_cts and arg in self.cts_fields:
                        self.input_kwargs[arg] = szData