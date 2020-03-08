# -*- coding: utf-8 -*-
__all__ = ['Query']

import pythoncom
import win32com.client
from xingapi import res
import time

import pandas as pd

class _XAQueryEvents:
    def __init__(self):
        self.recieved = False
        self.code = None
        self.msg = None

    def reset(self):
        self.recieved = False
        self.code = None
        self.msg = None

    def OnReceiveData(self, szTrCode):
        self.recieved = True

    def OnReceiveMessage(self, systemError, messageCode, message):
        self.code = str(messageCode)
        self.msg = str(message)

class Query:
    label_by_codes = False
    call_next = True
    def __init__(self, trcode):
        self.query = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", _XAQueryEvents)
        if isinstance(trcode, str):
            trcode = getattr(res, trcode)
        self.query.LoadFromResFile(trcode)
        self.trcode_name = trcode.name
        self.blocks = trcode.blocks
        self.inblocks = trcode.inblocks
        self.outblocks = trcode.outblocks

    def __call__(self, **input_kwargs):
        return self.request(**input_kwargs)

    @property
    def data(self):
        output = {}
        for k, v in self.__data.items():
            df = pd.concat(v, ignore_index=True)
            output[k] = df
            if not self.label_by_codes:
                df.columns = map(self.code_to_label, df.columns)
        return output

    def code_to_label(self, code):
        code_dict = {}
        for outblock in self.outblocks.values():
            code_dict.update(outblock.codes)
        label = code_dict[code]
        return label

    def wait(self):
        while not self.query.recieved:
            pythoncom.PumpWaitingMessages()
        self.query.reset()

        TRCountLimit = self.query.GetTRCountLimit(self.trcode_name)
        TRCountPerSec = self.query.GetTRCountPerSec(self.trcode_name)
        TRCountRequest = self.query.GetTRCountRequest(self.trcode_name)
        running_time = time.time() - self._request_start
        log = f'[TRCount: {TRCountRequest}/{TRCountLimit}][Running Time: {running_time:6.2f}s]'
        print(log, end='\r')
        if self.query.GetTRCountRequest(self.trcode_name)==TRCountLimit:
            while (time.time() - self._request_start)<600:
                time.sleep(1)
                time_left = 600 - (time.time() - self._request_start)
                print(f'[{time_left:6.2f}/600s] Waiting for Request Limit Time {self.query.GetTRCountRequest(self.trcode_name)}', end='\r')        
        time.sleep(1/TRCountPerSec)

    def set_input(self, block_name, **kwargs):
        for field_name, data in kwargs.items():
            self.query.SetFieldData(block_name, field_name, 0, data)

    def get_output(self, block_name, call_next=True, *args):
        codes = self.blocks[block_name].codes
        count = self.query.GetBlockCount(block_name) if call_next else 1
        if not args:
            args = tuple(codes.keys())

        data = []
        for i in range(count):
            datum = {}
            for field_name in args:
                datum[field_name] = self.query.GetFieldData(block_name, field_name, i)
            data.append(datum)
        return pd.DataFrame(data)

    def request(self, **input_kwargs):
        self.__data = {outblock_name : [] for outblock_name in self.outblocks.keys()}
        self._request_start = time.time()
        return self._request(**input_kwargs)

    def _request(self, **input_kwargs):
        for inblock_name, inblock in self.inblocks.items():
            kwargs = {x: input_kwargs.get(x) for x in inblock.codes.keys() if input_kwargs.get(x) is not None}
            self.set_input(inblock_name, **kwargs)

        self.query.Request(self.query.IsNext)
        self.wait()
        
        outputs = {}
        for outblock_name in self.outblocks.keys():
            output = self.get_output(outblock_name)
            outputs[outblock_name] = output
            self.__data[outblock_name].append(output)

        if self.call_next and self.query.IsNext:
            for key in self.blocks[self.trcode_name+'OutBlock'].codes.keys():
                for block in outputs.values():
                    occurs_input_kwargs = block.get(key)
                    if occurs_input_kwargs is not None:
                        input_kwargs[key]=occurs_input_kwargs.values[-1]
            try:
                return self._request(**input_kwargs)
            except:
                print('exception occured rather than request')
                return self.data
        else:
            return self.data
