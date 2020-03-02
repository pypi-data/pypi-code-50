#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:25:45 2019

@author: aguimera
"""

from PyQt5 import Qt
import pyqtgraph.parametertree.parameterTypes as pTypes
import numpy as np
#import PyCharact16Core.Charact16Core as CoreMod
#import PyqtTools.FileModule as FileMod


ChannelsConfig = ({'title': 'Channels Config',
                   'name': 'ChsConfig',
                   'type': 'group',
                    'children': (
                                 {'tittle': 'Configuration',
                                  'name': 'Configuration',
                                  'type': 'list',
                                  'values': ['Both',
                                             'AC',
                                             'DC', ], },
                                {'title': 'Gain DC',
                                 'name': 'DCGain',
                                 'type': 'float',
                                 'value': 10e3,
                                 'siPrefix': True, },
                                {'title': 'Gain AC',
                                 'name': 'ACGain',
                                 'type': 'float',
                                 'value': 1e6,
                                 'siPrefix': True, },
                                {'title': 'GateChannel',
                                 'name': 'GateChannel',
                                 'type': 'list',
                                 'values': ['',
                                            'Ch01',
                                            'Ch02',
                                            'Ch03',
                                            'Ch04',
                                            'Ch05',
                                            'Ch06',
                                            'Ch07',
                                            'Ch08',
                                            'Ch09',
                                            'Ch10',
                                            'Ch11',
                                            'Ch12',
                                            'Ch13',
                                            'Ch14',
                                            'Ch15',
                                            'Ch16',
                                            ]
                                 },
                                {'tittle': 'Channels',
                                 'name': 'Channels',
                                 'type': 'group',
                                 'children': ({'name': 'Ch01',
                                               'tip': 'Ch01',
                                               'type': 'bool',
                                               'value': False},
                                              {'name': 'Ch02',
                                               'tip': 'Ch02',
                                               'type': 'bool',
                                               'value': False},
                                              {'name': 'Ch03',
                                               'tip': 'Ch03',
                                               'type': 'bool',
                                               'value': False},
                                              {'name': 'Ch04',
                                               'tip': 'Ch04',
                                               'type': 'bool',
                                               'value': False},
                                              {'name': 'Ch05',
                                               'tip': 'Ch05',
                                               'type': 'bool',
                                               'value': False},
                                              {'name': 'Ch06',
                                               'tip': 'Ch06',
                                               'type': 'bool',
                                               'value': False},
                                              {'name': 'Ch07',
                                               'tip': 'Ch07',
                                               'type': 'bool',
                                               'value': True},
                                              {'name': 'Ch08',
                                               'tip': 'Ch08',
                                               'type': 'bool',
                                               'value': False},
                                              {'name': 'Ch09',
                                               'tip': 'Ch09',
                                               'type': 'bool',
                                               'value': False},
                                              {'name': 'Ch10',
                                               'tip': 'Ch10',
                                               'type': 'bool',
                                               'value': False},
                                              {'name': 'Ch11',
                                               'tip': 'Ch11',
                                               'type': 'bool',
                                               'value': False},
                                              {'name': 'Ch12',
                                               'tip': 'Ch12',
                                               'type': 'bool',
                                               'value': False},
                                              {'name': 'Ch13',
                                               'tip': 'Ch13',
                                               'type': 'bool',
                                               'value': False},
                                              {'name': 'Ch14',
                                               'tip': 'Ch14',
                                               'type': 'bool',
                                               'value': False},
                                              {'name': 'Ch15',
                                               'tip': 'Ch15',
                                               'type': 'bool',
                                               'value': False},
                                              {'name': 'Ch16',
                                               'tip': 'Ch16',
                                               'type': 'bool',
                                               'value': False}, ), },
                                {'title': 'Cycles',
                                 'name': 'Cycles',
                                 'type': 'group',
                                 'children': ({'name': 'InitCy',
                                               'type': 'int',
                                               'value': 0,
                                               'step': 1,
                                               },
                                              {'name': 'FinalCy',
                                               'type': 'int',
                                               'value': 1,
                                               'step': 1,
                                               },
                                              {'name': 'CurrentCy',
                                               'type': 'int',
                                               'value': 1,
                                               'readonly': True,
                                               }, ), }
                                 ), }, )


###############################################################################


class SampSetParam(pTypes.GroupParameter):
    NewConf = Qt.pyqtSignal()

    Channels = []
    Gate = []

    def __init__(self, **kwargs):
        super(SampSetParam, self).__init__(**kwargs)
        self.addChildren(ChannelsConfig)

        self.ChsConfig = self.param('ChsConfig')

        self.Channels = self.ChsConfig.param('Channels')
        self.GateChannel = self.ChsConfig.param('GateChannel')
        self.Configuration = self.ChsConfig.param('Configuration')
        self.Cycles = self.ChsConfig.param('Cycles')

        self.DCGain = self.ChsConfig.param('DCGain')
        self.ACGain = self.ChsConfig.param('ACGain')

        # Init Settings
        self.on_Channels_Changed()
        self.on_Gain_Changed()
        self.on_Configuration_Changed()

        # Signals
        self.Channels.sigTreeStateChanged.connect(self.on_Channels_Changed)
        self.GateChannel.sigTreeStateChanged.connect(self.on_Channels_Changed)
        self.Configuration.sigTreeStateChanged.connect(self.on_Configuration_Changed)
        self.DCGain.sigValueChanged.connect(self.on_Gain_Changed)
        self.ACGain.sigValueChanged.connect(self.on_Gain_Changed)

    def on_Channels_Changed(self):
        self.Chs = []
        self.Gate = self.GateChannel.value()

        for p in self.Channels.children():
            if p.value() is True:
                if p.value == self.Gate:
                    print('Gate')
                else:
                    self.Chs.append(p.name())
        self.NewConf.emit()

    def on_Gain_Changed(self):
        if self.Chs:
            self.ChsConfig.param('DCGain').value()
            self.ChsConfig.param('ACGain').value()

    def on_Configuration_Changed(self):
        if self.Chs:
            self.Configuration.value()

    def GetChannelsConfigKwargs(self):
        ChanKwargs = {}
        for p in self.ChsConfig.children():
            if p.name() == 'Channels':
                ChanKwargs[p.name()] = self.Chs
            elif p.name() == 'GateChannel':
                ChanKwargs[p.name()] = self.Gate
            else: 
                ChanKwargs[p.name()] = p.value()

        return ChanKwargs

    def GetCycles(self):
        CycleKwargs = {}
        for p in self.Cycles.children():
            CycleKwargs[p.name()] = p.value()
        return CycleKwargs

###############################################################################


#class DataAcquisitionThread(Qt.QThread):
#    NewMuxData = Qt.pyqtSignal()
#
#    def __init__(self, ChannelsConfigKW, SampKw):
#        super(DataAcquisitionThread, self).__init__()
#        self.DaqInterface = CoreMod.ChannelsConfig(**ChannelsConfigKW)
#        self.DaqInterface.DataEveryNEvent = self.NewData
#        self.SampKw = SampKw
#
#    def run(self, *args, **kwargs):
#        self.DaqInterface.StartAcquisition(**self.SampKw)
#        loop = Qt.QEventLoop()
#        loop.exec_()
#
##    def CalcAverage(self, MuxData):
##        return np.mean(MuxData[:, self.AvgIndex:, :], axis=1)
#
##    def NewData(self, aiData, MuxData):
#    def NewData(self, aiData):
##        self.OutData = self.CalcAverage(MuxData)
#        self.aiData = aiData
#        self.NewMuxData.emit()
