# -*- coding: utf-8 -*-
# __all__ = ['Real']

import pythoncom
import win32com.client
from xingapi import res
import time

import threading
import queue

class _XARealEvents:
    def __init__(self):
        pass

    def OnReceiveRealData(self, szTrCode):
        codes = self.outblock.codes
        data = {}
        for field_name in codes.keys():
            data[field_name] = self.GetFieldData(self.outblock.name, field_name)
        print(data)
        with open('news.txt', 'w') as f:
            f.write('1')

class Real(threading.Thread):
    def __init__(self, trcode):
        threading.Thread.__init__(self)
        self.setDaemon(True)

        self.real = win32com.client.DispatchWithEvents("XA_DataSet.XAReal", _XARealEvents)
        if isinstance(trcode, str):
            trcode = getattr(res, trcode)
        self.real.LoadFromResFile(trcode)
        self.trcode_name = trcode.name
        self.blocks = trcode.blocks
        self.inblocks = trcode.inblocks
        self.outblocks = trcode.outblocks

        self.real.outblock = trcode.OutBlock
        self.real.inblock = trcode.InBlock

        self.running = True
        self.real.queue = queue.Queue()

    def set_input(self, block_name, **kwargs):
        for field_name, data in kwargs.items():
            self.real.SetFieldData(block_name, field_name, data)

    def advise(self, **input_kwargs):
        self.real.UnadviseRealData()
        self.set_input(self.real.inblock.name, **input_kwargs)
        
        self.real.AdviseRealData()
        return self

    def run(self):
        while self.running:
            pythoncom.PumpWaitingMessages()
            time.sleep(0.1)
