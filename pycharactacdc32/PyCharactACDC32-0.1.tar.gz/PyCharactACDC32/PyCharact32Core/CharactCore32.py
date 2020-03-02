# -*- coding: utf-8 -*-
"""
Created on Tue Jul 03 10:11:14 2018

@author: user
"""
import sys
import ctypes
import PyGFETdb.DataStructures as PyData
import PyDAQmx as Daq
from ctypes import byref, c_int32
import numpy as np
from scipy import signal
import neo
import quantities as pq
import PyqtTools.DaqInterface as DaqInt

"""This example is a PyDAQmx version of the ContAcq_IntClk.c example
It illustrates the use of callback functions

This example demonstrates how to acquire a continuous amount of
data using the DAQ device's internal clock. It incrementally stores the data
in a Python list.
"""

aiChannels = {'Ch01': 'ai8',
              'Ch11': 'ai12',
              'Ch03': 'ai9',
              'Ch09': 'ai15',
              'Ch05': 'ai10',
              'Ch15': 'ai14',
              'Ch07': 'ai11',
              'Ch13': 'ai13',
              'Ch02': 'ai0',
              'Ch12': 'ai4',
              'Ch04': 'ai1',
              'Ch10': 'ai7',
              'Ch06': 'ai2',
              'Ch16': 'ai6',
              'Ch08': 'ai3',
              'Ch14': 'ai5',
              'Ch27': 'ai27',
              'Ch17': 'ai29',
              'Ch25': 'ai26',
              'Ch19': 'ai30',
              'Ch31': 'ai25',
              'Ch21': 'ai31',
              'Ch29': 'ai24',
              'Ch23': 'ai28',
              'Ch28': 'ai19',
              'Ch18': 'ai21',
              'Ch26': 'ai18',
              'Ch20': 'ai22',
              'Ch32': 'ai17',
              'Ch22': 'ai23',
              'Ch30': 'ai16',
              'Ch24': 'ai20'}

DOChannels = ['port0/line0:9', ]


class ChannelsConfig():

    ChannelIndex = None
    GateChannelIndex = None
    InitSwitch = np.array([0, 1, 0, 0, 0, 0, 0, 0, 0, 0], dtype=np.uint8)

    ChNamesList = None
    # ReadAnalog class with all channels
    Inputs = None
    InitConfig = None

    # Events list
    DCDataDoneEvent = None
    DCDataEveryNEvent = None
    ACDataDoneEvent = None
    ACDataEveryNEvent = None
    GateDataDoneEvent = None
    GateDataEveryNEvent = None

    def DelInputs(self):
        self.Inputs.ClearTask()

    def InitInputs(self, Channels, GateChannel=None):
        print('init inputs')
        if self.Inputs is not None:
            self.DelInputs()

        InChans = []

        self.ChNamesList = sorted(Channels)
        self.ChannelIndex = {}
        index = 0
        for ch in sorted(Channels):
            InChans.append(aiChannels[ch])
            self.ChannelIndex[ch] = (index)

            if ch == 'Ch27' and GateChannel:
                print('Gate/Ch27')
                self.GateChannelIndex = {'Gate': (index)}
            index += 1

        if not self.GateChannelIndex and GateChannel:
            print('GateChannel')
            self.GateChannelIndex = {'Gate': (index)}
            InChans.append('ai27')

        print('Channels configurtation')
        print('Gate', self.GateChannelIndex)
        print('Channels ', len(self.ChNamesList))
        print('ai list ->', InChans)
        for ch in sorted(Channels):
            print(ch, ' DC -> ', aiChannels[ch], self.ChannelIndex[ch])

        self.Inputs = DaqInt.ReadAnalog(InChans=InChans)
        # events linking
        self.Inputs.EveryNEvent = self.EveryNEventCallBack
        self.Inputs.DoneEvent = self.DoneEventCallBack

    def __init__(self, Channels, GateChannel=None,
                 ChVg='ao2', ChVs='ao1', ChVds='ao0', ChVsig='ao3'):

        print('init')
        self.InitConfig = {}
        self.InitConfig['Channels'] = Channels
        if GateChannel is True:
            self.InitConfig['GateChannel'] = GateChannel
        else:
            GateChannel = None
            self.InitConfig['GateChannel'] = GateChannel

        self.InitInputs(Channels=Channels,
                        GateChannel=GateChannel)

        # Output Analog Channels
        self.VsOut = DaqInt.WriteAnalog((ChVs,))
        self.VdsOut = DaqInt.WriteAnalog((ChVds,))
        self.VgOut = DaqInt.WriteAnalog((ChVg,))
        self.Vsig = DaqInt.WriteAnalog((ChVsig,))

        # Output Digital Channels
        self.SwitchOut = DaqInt.WriteDigital(Channels=DOChannels)
        self.SetDigitalSignal(Signal=self.InitSwitch)

    def SetBias(self, Vds, Vgs):
        print('ChannelsConfig SetBias Vgs ->', Vgs, 'Vds ->', Vds)
        self.VdsOut.SetVal(Vds)
        self.VsOut.SetVal(-Vgs)
        self.BiasVd = Vds-Vgs
        self.Vgs = Vgs
        self.Vds = Vds

    def SetSignal(self, Signal, nSamps):
        if not self.VgOut:
            self.VgOut = DaqInt.WriteAnalog(('ao2',))
        self.VgOut.DisableStartTrig()
        self.VgOut.SetSignal(Signal=Signal,
                             nSamps=nSamps)

    def SetContSignal(self, Signal, nSamps):
        if not self.VgOut:
            self.VgOut = DaqInt.WriteAnalog(('ao2',))
        self.VgOut.DisableStartTrig()
        self.VgOut.SetContSignal(Signal=Signal,
                                 nSamps=nSamps)

    def SetDigitalSignal(self, Signal):
        if not self.SwitchOut:
            self.SwitchOut = DaqInt.WriteDigital(Channels=DOChannels)
        self.SwitchOut.SetDigitalSignal(Signal)

    def _SortChannels(self, data, SortDict):
        print('SortChannels')
        (samps, inch) = data.shape
        sData = np.zeros((samps, len(SortDict)))
        for chn, inds in SortDict.items():
            if chn == 'Gate':
                sData[:, 0] = data[:, inds]
            else:
                sData[:, inds] = data[:, inds]
        return sData

    def EveryNEventCallBack(self, Data):
        print('EveryNEventCallBack')
        _DCDataEveryNEvent = self.DCDataEveryNEvent
        _GateDataEveryNEvent = self.GateDataEveryNEvent
        _ACDataEveryNEvent = self.ACDataEveryNEvent

        if _GateDataEveryNEvent:
            _GateDataEveryNEvent(self._SortChannels(Data,
                                                    self.GateChannelIndex))
        if _DCDataEveryNEvent:
            _DCDataEveryNEvent(self._SortChannels(Data,
                                                  self.ChannelIndex))
        if _ACDataEveryNEvent:
            _ACDataEveryNEvent(self._SortChannels(Data,
                                                  self.ChannelIndex))

    def DoneEventCallBack(self, Data):
        print('DoneEventCallBack')
        if self.VgOut:
            self.VgOut.StopTask()

        _DCDataDoneEvent = self.DCDataDoneEvent
        _GateDataDoneEvent = self.GateDataDoneEvent
        _ACDataDoneEvent = self.ACDataDoneEvent

        if _GateDataDoneEvent:
            _GateDataDoneEvent(self._SortChannels(Data,
                                                  self.GateChannelIndex))
        if _DCDataDoneEvent:
            _DCDataDoneEvent(self._SortChannels(Data,
                                                self.ChannelIndex))
        if _ACDataDoneEvent:
            _ACDataDoneEvent(self._SortChannels(Data,
                                                self.ChannelIndex))

    def ReadChannelsData(self, Fs=1000, nSamps=10000, EverySamps=1000):
        self.Inputs.ReadData(Fs=Fs,
                             nSamps=nSamps,
                             EverySamps=EverySamps)

    def __del__(self):
        print('Delete class')
        if self.VgOut:
            self.VgOut.ClearTask()
        self.VdsOut.ClearTask()
        self.VsOut.ClearTask()
        self.Inputs.ClearTask()
#        del(self.VgOut)
#        del(self.VdsOut)
#        del(self.VsOut)
#        del(self.Inputs)

###############################################################################
#####
###############################################################################


class FFTConfig():
    Freqs = None
    Fs = None
    nFFT = None
    Finds = None
    AcqSequential = False


class FFTTestSignal():

    FsH = 2e6
    FsL = 1000
    FMinLow = 1  # Lowest freq to acquire in 1 time
    FThres = 10  # For two times adq split freq

    FFTconfs = [FFTConfig(), ]

    Fsweep = None
    FFTAmps = None

    BodeDuration = [None, None]
    Vpp = [None, None]
    AddnFFT = 2
    nAvg = 2
    Arms = 1e-3
    EventFFTDebug = None

    def __init__(self, FreqMin, FreqMax, nFreqs, Arms, nAvg):

        self.nAvg = nAvg
        self.Arms = Arms

        if FreqMax > self.FsH/2:
            FreqMax = self.FsH/2 - 1

        if FreqMax <= self.FThres:
            FreqMax = self.FThres + 1

        fsweep = np.logspace(np.log10(FreqMin), np.log10(FreqMax), nFreqs)
        if np.any(fsweep < self.FMinLow) and nFreqs > 1:  # TODO Check this
            self.FFTconfs.append(FFTConfig())

            self.FFTconfs[0].nFFT = int(2**((np.around(np.log2(self.FsH/self.FThres))+1)+self.AddnFFT))
            self.FFTconfs[1].nFFT = int(2**((np.around(np.log2(self.FsL/FreqMin))+1)+self.AddnFFT))
            self.FFTconfs[0].Fs = self.FsH
            self.FFTconfs[1].Fs = self.FsL

            # LowFrequencies
            FreqsL, indsL = self.CalcCoherentSweepFreqs(FreqMin=FreqMin,
                                                        FreqMax=np.max(fsweep[np.where(self.FThres>fsweep)]),
                                                        nFreqs=np.sum(fsweep < self.FThres),
                                                        Fs=self.FFTconfs[1].Fs,
                                                        nFFT=self.FFTconfs[1].nFFT)

            # HighFrequencies
            FreqsH, indsH = self.CalcCoherentSweepFreqs(FreqMin=np.min(fsweep[np.where(fsweep>self.FThres)]),
                                                        FreqMax=FreqMax,
                                                        nFreqs=np.sum(self.FThres < fsweep),
                                                        Fs=self.FFTconfs[0].Fs,
                                                        nFFT=self.FFTconfs[0].nFFT)
            self.FFTconfs[0].Finds = indsH
            self.FFTconfs[0].Freqs = FreqsH

            self.FFTconfs[1].Finds = indsL
            self.FFTconfs[1].Freqs = FreqsL

            self.Fsweep = np.hstack((self.FFTconfs[1].Freqs,
                                     self.FFTconfs[0].Freqs))

            self.FFTconfs[0].AcqSequential = True

            self.BodeDuration = [self.FFTconfs[0].nFFT*(1/float(self.FFTconfs[0].Fs))*self.nAvg,
                                 self.FFTconfs[1].nFFT*(1/float(self.FFTconfs[1].Fs))*self.nAvg]

        else:
            if len(self.FFTconfs) > 1:
                del(self.FFTconfs[1])
            self.FFTconfs[0].nFFT = int(2**((np.around(np.log2(self.FsH/FreqMin))+1)+self.AddnFFT))
            self.FFTconfs[0].Fs = self.FsH

            FreqsH, indsH = self.CalcCoherentSweepFreqs(FreqMin=FreqMin,
                                                        FreqMax=FreqMax,
                                                        nFreqs=nFreqs,
                                                        Fs=self.FFTconfs[0].Fs,
                                                        nFFT=self.FFTconfs[0].nFFT)
            self.FFTconfs[0].Finds = indsH
            self.FFTconfs[0].Freqs = FreqsH

            self.Fsweep = self.FFTconfs[0].Freqs
            self.FFTconfs[0].AcqSequential = True
            self.BodeDuration = [self.FFTconfs[0].nFFT*(1/float(self.FFTconfs[0].Fs))*self.nAvg, None]

    def CalcCoherentSweepFreqs(self, FreqMin, FreqMax, nFreqs, Fs, nFFT):
        nmin = (FreqMin*(nFFT))/Fs
        nmax = (FreqMax*(nFFT))/Fs
        freqs = np.round(
                np.logspace(np.log10(nmin), np.log10(nmax), nFreqs), 0)
        Freqs = (float(Fs)/(nFFT))*np.unique(freqs)

        # Calc Indexes
        freqs = np.fft.rfftfreq(nFFT, 1/float(Fs))
#        freqs = [np.round(x, 7) for x in freq]
#        Freqs = [np.round(x, 7) for x in Freqs]
#        freqs = np.array(freqs)
#        Freqs = np.array(Freqs)
        Inds = np.where(np.in1d(freqs, Freqs))[0]

        return Freqs, Inds

    def GenSignal(self, Ind=0, Delay=0):

        FFTconf = self.FFTconfs[Ind]

        Ts = 1/float(FFTconf.Fs)
        Ps = FFTconf.nFFT * self.nAvg * Ts

        Amp = self.Arms*np.sqrt(2)
        t = np.arange(0, Ps, Ts) + Delay
        out = np.zeros(t.size)
        for f in np.nditer(FFTconf.Freqs):
            s = Amp*np.sin(f*2*np.pi*(t))
            out = out + s

        self.FFTAmps = (2*np.fft.rfft(
                out, FFTconf.nFFT)/FFTconf.nFFT)[FFTconf.Finds]
        self.Vpp[Ind] = np.max(out) + np.abs(np.min(out))
#        self.FFTconfs[Ind].Vpp = np.max(out) + np.abs(np.min(out))

        out[-1] = 0

        return out, t

    def CalcFFT(self, Data, Ind):
        FFTconf = self.FFTconfs[Ind]

        a = Data.reshape((self.nAvg, FFTconf.nFFT))
        acc = np.zeros(((FFTconf.nFFT//2)+1))
        for w in a:
            acc = acc + (2 * np.fft.rfft(w, FFTconf.nFFT) / FFTconf.nFFT)

        Out = (acc/self.nAvg)[FFTconf.Finds]

        if self.EventFFTDebug is not None:
            self.EventFFTDebug(acc/self.nAvg)

        return Out

###############################################################################
#####
###############################################################################


class FFTBodeAnalysis():

    BodeRh = None
    BodeRhardware = 150e3
    BodeSignal = None
    RemoveDC = None

#    AdqDelay = 0
    AdqDelay = -5.8e-7

    def SetBodeConfig(self, FreqMin=0.1, FreqMax=15000, nFreqs=10, Arms=10e-3,
                      nAvg=1, BodeRh=False, BodeOut=False, RemoveDC=False):
        print('FFTBodeAnalysis SetBodeConfig')

        self.BodeSignal = FFTTestSignal(FreqMin=FreqMin,
                                        FreqMax=FreqMax,
                                        nFreqs=nFreqs,
                                        Arms=Arms,
                                        nAvg=nAvg)

        self.BodeRh = BodeRh
        self.BodeOut = BodeOut
        self.RemoveDC = RemoveDC

    def SetContSig(self, FreqMin=0.1, FreqMax=15000, nFreqs=10, Arms=10e-3):
        print('FFTBodeAnalysis SetContSig')
        self.ContSig = FFTTestSignal(FreqMin=FreqMin,
                                     FreqMax=FreqMax,
                                     nFreqs=nFreqs,
                                     Arms=Arms,
                                     nAvg=1)
        self.ContSig.FMinLow = None
        self.ContSig.FsH = 1000
        self.ContSig.__init__(FreqMin=FreqMin,
                              FreqMax=FreqMax,
                              nFreqs=nFreqs,
                              Arms=Arms,
                              nAvg=1)

    def CalcBode(self, Data, Ind, IVGainAC, ChIndexes):
        print('CalcBode')
        if self.BodeRh or self.BodeOut:
            x = Data
        else:
            x = Data / IVGainAC

        if self.RemoveDC:
            print('RemoveDC')
            for chk, chi, in sorted(ChIndexes.items()):
                Data[:, chi] = Data[:, chi] - np.mean(Data[:, chi])

        FFTconf = self.BodeSignal.FFTconfs[Ind]

        (samps, inch) = x.shape
        Gm = np.ones((len(FFTconf.Finds),
                      inch))*np.complex(np.nan)

        for chk, chi, in sorted(ChIndexes.items()):
            Out = self.BodeSignal.CalcFFT(Data=x[:, chi],
                                          Ind=Ind)

#            Delay = self.AdqDelay*chi[0]  ## TODO check this time finer
            self.BodeSignal.GenSignal(Ind=Ind, Delay=self.AdqDelay)

            if self.BodeRh:
                Iin = -self.BodeSignal.FFTAmps/self.BodeRhardware
                gm = Out/Iin
                Gm[:, chi] = gm
            else:
                Gm[:, chi] = Out/self.BodeSignal.FFTAmps

        return Gm

###############################################################################
#####
###############################################################################


class DataProcess(ChannelsConfig, FFTBodeAnalysis):
    # PSD Config
    PSDnFFT = 2**17
    PSDFs = 30e3
    PSDnAvg = 5

    # Variables list
    DCFs = 1000
    DCnSamps = 1000
    IVGainDC = 10e3
    IVGainAC = 1e6
    IVGainGate = 2e6
    DevCondition = 5e-8
    PSDDuration = None
    GenTestSig = None
    ContSig = None
    OldConfig = None
    GmH = None
    Gm = None
    iConf = 0
    SeqIndex = 0

    # Events list
    EventBiasDone = None
    EventBiasAttempt = None
    EventBodeDone = None
    EventPSDDone = None
    EventAcDataAcq = None
    EventSetBodeLabel = None

    def ClearEventsCallBacks(self):
        self.DCDataDoneEvent = None
        self.DCDataEveryNEvent = None
        self.ACDataDoneEvent = None
        self.ACDataEveryNEvent = None
        self.GateDataDoneEvent = None
        self.GateDataEveryNEvent = None

    # DC
    ####
    def GetBiasCurrent(self, Vds, Vgs):
        print('DataProcess GetBiasCurrent')
        self.ClearEventsCallBacks()
        self.SetDigitalSignal(Signal=self.InitSwitch)
        self.SetBias(Vds, Vgs)
        self.DCDataDoneEvent = self.CalcBiasData

        self.ReadChannelsData(Fs=self.DCFs,
                              nSamps=self.DCnSamps,
                              EverySamps=self.DCnSamps)

    def GetGateCurrent(self):
        print('DataProcess GetGateCurrent')
        self.ClearEventsCallBacks()
        self.SetDigitalSignal(Signal=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0,
                                               0], dtype=np.uint8))
        self.GateDataDoneEvent = self.CalcGateData

        self.ReadChannelsData(Fs=self.DCFs,
                              nSamps=self.DCnSamps,
                              EverySamps=self.DCnSamps)

    def GetContinuousCurrent(self, Fs, Refresh, RecDC, GenTestSig):
        print('DataProcess GetContinuousCurrent')
        self.ClearEventsCallBacks()
        if RecDC is True:
            self.SetDigitalSignal(Signal=self.InitSwitch)
            self.DCDataEveryNEvent = self.CalcDcContData
        else:
            self.SetDigitalSignal(Signal=np.array([1, 1, 1, 1, 1,
                                                   1, 1, 1, 1, 1],
                                                  dtype=np.uint8))
            self.ACDataEveryNEvent = self.CalcAcContData

#        if self.GateChannelIndex is not None:
#            self.GateDataEveryNEvent = self.CalcGateContData

        if GenTestSig:
            print('CreateSignal')
            self.GenTestSig = GenTestSig
            print('DataProcess SetContSignal')
            signal, _ = self.ContSig.GenSignal()
            self.SetContSignal(Signal=signal,
                               nSamps=signal.size)
        self.Inputs.ReadContData(Fs=Fs,
                                 EverySamps=Fs*Refresh)

    def CalcBiasData(self, Data):
        print('DataProcess CalcBiasData')

        data = Data
        r, c = data.shape
        x = np.arange(0, r)
        mm, oo = np.polyfit(x, data, 1)
        Dev = np.abs(np.mean(mm))
        print('DataProcess Attempt ', Dev)
        if self.EventBiasAttempt:
            Ids = (data-self.BiasVd)/self.IVGainDC
            if not self.EventBiasAttempt(Ids,
                                         x*(1/np.float32(self.Inputs.Fs)),
                                         Dev):
                return  # Cancel execution

        if (Dev < self.DevCondition):
            Ids = (oo-self.BiasVd)/self.IVGainDC

            if self.EventBiasDone:
                self.EventBiasDone(Ids)
            return

        # try next attempt
        self.ReadChannelsData(Fs=self.DCFs,
                              nSamps=self.DCnSamps,
                              EverySamps=self.DCnSamps)

    def CalcGateData(self, Data):
        print('DataProcess CalcGateData')
        print(Data.shape)
        data = Data[1:, :]
        r, c = data.shape
        x = np.arange(0, r)
        mm, oo = np.polyfit(x, data, 1)
#        Dev = np.abs(np.mean(mm))
#        if (Dev < self.DevCondition):
#            if np.abs(mm) < self.DevCondition:
#                print 'Gate slope ', mm
#            else:
#                print 'WARNING !!! Gate slope ', mm
        Igs = oo/self.IVGainGate

        if self.EventGateDone:
            self.EventGateDone(Igs)
        return

    # AC
    ####
    def GetSeqBode(self, SeqConf):
        print('DataProcess GetSeqBode')
        FFTconf = self.BodeSignal.FFTconfs[self.iConf]

        if SeqConf:
            print('InitInptuns', SeqConf)
            self.InitInputs(**SeqConf)

        signal, _ = self.BodeSignal.GenSignal(Ind=self.iConf)
        self.SetContSignal(Signal=signal, nSamps=signal.size)

        if self.EventSetBodeLabel:
            self.EventSetBodeLabel(Vpp=self.BodeSignal.Vpp)

        print('Acquire Bode data for ',
              self.BodeSignal.BodeDuration[self.iConf], ' Seconds')

        self.ReadChannelsData(Fs=FFTconf.Fs,
                              nSamps=FFTconf.nFFT*self.BodeSignal.nAvg,
                              EverySamps=FFTconf.nFFT)

    def NextChannelAcq(self):
        print('DataProcess NextChannelAcq')
        FFTconf = self.BodeSignal.FFTconfs[self.iConf]

        SeqConf = self.InitConfig.copy()

#        if self.InitConfig['GateChannel'] is not None:
#            SeqConf['GateChannel'] = None

        if FFTconf.AcqSequential is True:

            if self.SeqIndex <= len(self.InitConfig['Channels']) - 1:
                Channel = [sorted(self.InitConfig['Channels'])[self.SeqIndex], ]
                SeqConf['Channels'] = Channel
                self.SeqIndex += 1

            else:
                self.SeqIndex = 0
                if len(self.BodeSignal.FFTconfs) > 1 and self.iConf == 0:
                    self.iConf += 1
                else:
                    self.iConf = 0
                    if self.OldConfig:
                        self.InitInputs(**self.OldConfig)

                    if self.EventBodeDone:
                        self.EventBodeDone(self.Gm, self.BodeSignal.Fsweep)
                    return

        else:
            self.iConf = 0
            if self.OldConfig:
                self.InitInputs(**self.OldConfig)

            if self.EventBodeDone:
                self.EventBodeDone(self.Gm, self.BodeSignal.Fsweep)
            return

        self.GetSeqBode(SeqConf)

    def GetBode(self):
        self.SetDigitalSignal(Signal=np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                              dtype=np.uint8))
        self.OldConfig = self.InitConfig.copy()
        self.ClearEventsCallBacks()
        self.ACDataDoneEvent = self.CalcBodeData
        self.ACDataEveryNEvent = self.EventDataAcq

        ##
        if len(self.BodeSignal.FFTconfs) > 1:
            self.GmH = np.ones((len(self.BodeSignal.FFTconfs[0].Freqs),
                                len(self.ChannelIndex.items())))*np.complex(np.nan)

        self.Gm = np.ones((len(self.BodeSignal.Fsweep),
                           len(self.ChannelIndex.items())))*np.complex(np.nan)
        ##
        self.NextChannelAcq()

    def CalcBodeData(self, Data):
        print('DataProcess CalcBodeData_Data')

        FFTconf = self.BodeSignal.FFTconfs[self.iConf]

        if FFTconf.AcqSequential is True:
            GmSeq = self.CalcBode(Data=Data,
                                  Ind=self.iConf,
                                  IVGainAC=self.IVGainAC,
                                  ChIndexes=self.ChannelIndex)

            if len(self.BodeSignal.FFTconfs) > 1:
                self.GmH[:, self.SeqIndex - 1] = GmSeq[:, 0]
            else:
                self.Gm[:, self.SeqIndex - 1] = GmSeq[:, 0]

            self.NextChannelAcq()

            return

        else:
            GmL = self.CalcBode(Data=Data,
                                Ind=self.iConf,
                                IVGainAC=self.IVGainAC,
                                ChIndexes=self.ChannelIndex)

            self.Gm = np.vstack((GmL, self.GmH))

        self.NextChannelAcq()

    def GetPSD(self):
        self.ClearEventsCallBacks()
        self.SetDigitalSignal(Signal=np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                              dtype=np.uint8))
        self.ACDataEveryNEvent = self.EventDataAcq
        if not self.PSDDuration:
            self.PSDDuration = self.PSDnFFT*self.PSDnAvg*(1/self.PSDFs)
        print('DataProcess Acquire PSD data for ', self.PSDDuration, 'seconds')
        self.ACDataDoneEvent = self.CalcPSDData
        self.ReadChannelsData(Fs=self.PSDFs,
                              nSamps=self.PSDnFFT*self.PSDnAvg,
                              EverySamps=self.PSDnFFT)

    def CalcPSDData(self, Data):
        print(self.IVGainAC, 'CalcPSDData')
        data = Data/self.IVGainAC

        ff, psd = signal.welch(x=data,
                               fs=self.PSDFs,
                               window='hanning',
                               nperseg=self.PSDnFFT,
                               scaling='density', axis=0)
        if self.EventPSDDone:
            self.EventPSDDone(psd, ff, data)

    def EventDataAcq(self, Data):
        print('DataProcess EventAcDataAcq')
        r, c = Data.shape
        x = np.arange(0, r)
        if self.EventAcDataAcq:

            self.EventAcDataAcq(Data/self.IVGainAC,
                                x*(1/np.float32(self.Inputs.Fs)))


###############################################################################
#####
###############################################################################


class Charact(DataProcess):
    # Sweep points
    SwVdsVals = None
    SwVdsInd = None
    SwVgsVals = None
    SwVgsInd = None
    DevACVals = None

    # Status vars
    CharactRunning = False
    RunningConfig = False
    GateChannel = None

    # events list
    EventCharSweepDone = None
    EventCharBiasDone = None
    EventCharBiasAttempt = None
    EventCharAcDataAcq = None
    EventFFTDone = None

    # Neo Record
    ContRecord = None

    def InitSweep(self, VdsVals, VgsVals, PSD=False, Bode=False):
        print('Charact InitSweep')
        self.SwVgsVals = VgsVals
        self.SwVdsVals = VdsVals
        self.Bode = Bode
        self.PSD = PSD
        self.SwVgsInd = 0
        self.SwVdsInd = 0

        self.EventBiasAttempt = self.BiasAttemptCallBack
        self.EventBiasDone = self.BiasDoneCallBack
        self.EventGateDone = self.GateDoneCallBack
        if self.Bode:
            self.EventBodeDone = self.BodeDoneCallBack
            self.BodeSignal.EventFFTDebug = self.EventFFT  # TODO implement if condition
        if self.PSD:
            self.EventPSDDone = self.PSDDoneCallBack
        self.EventAcDataAcq = self.AcAcqCallBack

        self.CharactRunning = True

        # Init Dictionaries
        self.InitDictionaries()
        self.ApplyBiasPoint()

    def InitDictionaries(self):
        # DC dictionaries
        if self.GateChannelIndex is None:
            Gate = False
        else:
            print('Gate Dict True')
            Gate = True

        self.DevACVals = None

        self.DevDCVals = PyData.InitDCRecord(nVds=self.SwVdsVals,
                                             nVgs=self.SwVgsVals,
                                             ChNames=self.ChNamesList,
                                             Gate=Gate)
        # AC dictionaries
        if self.Bode or self.PSD:
            if self.PSD:
                Fpsd = np.fft.rfftfreq(self.PSDnFFT, 1/self.PSDFs)
            else:
                Fpsd = np.array([])

            if self.Bode:
                print('Bode dict')
                nFgm = self.BodeSignal.Fsweep
            else:
                nFgm = np.array([])

            self.DevACVals = PyData.InitACRecord(nVds=self.SwVdsVals,
                                                 nVgs=self.SwVgsVals,
                                                 nFgm=nFgm,
                                                 nFpsd=Fpsd,
                                                 ChNames=self.ChNamesList)

    def ApplyNextBias(self):
        print('Charact ApplyNextBias')
        if self.SwVdsInd < len(self.SwVdsVals)-1:
            self.SwVdsInd += 1
        else:
            self.SwVdsInd = 0
            if self.SwVgsInd < len(self.SwVgsVals)-1:
                self.SwVgsInd += 1
            else:
                self.SwVgsInd = 0

                if self.EventCharSweepDone:
                    self.EventCharSweepDone(self.DevDCVals, self.DevACVals)
                return

        if self.CharactRunning:
            self.ApplyBiasPoint()
        else:
            self.StopCharac()

    def ApplyBiasPoint(self):
        self.GetBiasCurrent(Vds=self.SwVdsVals[self.SwVdsInd],
                            Vgs=self.SwVgsVals[self.SwVgsInd])

    def BiasAttemptCallBack(self, Ids, time, Dev):
        if self.EventCharBiasAttempt:
            self.EventCharBiasAttempt(Ids, time, Dev)

        return self.CharactRunning

    def AcAcqCallBack(self, Ids, time):
        if self.EventCharAcDataAcq:
            self.EventCharAcDataAcq(Ids, time)
        else:
            self.StopCharac()
#        return self.CharactRunning

    def BiasDoneCallBack(self, Ids):
        for chn, inds in self.ChannelIndex.items():
            self.DevDCVals[chn]['Ids'][self.SwVgsInd,
                                       self.SwVdsInd] = Ids[inds]

        if self.EventCharBiasDone:
            self.EventCharBiasDone(self.DevDCVals)

        # Measure AC Data
        if self.CharactRunning:
            # Measure Gate Data
            if self.InitConfig['GateChannel'] is True:
                self.GetGateCurrent()

            elif self.PSD:
                self.GetPSD()
            elif self.Bode:
                self.GetBode()
            else:
                self.ApplyNextBias()

    def GateDoneCallBack(self, Igs):
        print('Charact GateDoneCallBack')
        for chn, inds in self.GateChannelIndex.items():
            self.DevDCVals['Gate']['Ig'][self.SwVgsInd, self.SwVdsInd] = Igs

        if self.EventCharBiasDone:
            self.EventCharBiasDone(self.DevDCVals)

        # Measure AC Data
        if self.CharactRunning:
            if self.PSD:
                self.GetPSD()
            elif self.Bode:
                self.GetBode()
            else:
                self.ApplyNextBias()

    def BodeDoneCallBack(self, Gm, SigFreqs):
        print('Charact BodeDoneCallBack')
        for chn, inds in self.ChannelIndex.items():
            self.DevACVals[chn]['gm']['Vd{}'.format(self.SwVdsInd)][
                    self.SwVgsInd] = Gm[:, inds]
            self.DevACVals[chn]['Fgm'] = SigFreqs

        if self.EventCharACDone:
            self.EventCharACDone(self.DevACVals)

        self.ApplyNextBias()

    def PSDDoneCallBack(self, psd, ff, data):
        for chn, inds in self.ChannelIndex.items():
            self.DevACVals[chn]['PSD']['Vd{}'.format(self.SwVdsInd)][
                    self.SwVgsInd] = psd[:, inds]
            self.DevACVals[chn]['Fpsd'] = ff
        if self.EventCharACDone:
            self.EventCharACDone(self.DevACVals)

        if self.CharactRunning:
            if self.Bode:
                self.GetBode()
            else:
                self.ApplyNextBias()
        else:
            self.StopCharac()

    def EventFFT(self, FFT):
        if self.EventFFTDone:
            self.EventFFTDone(FFT)

    def StopCharac(self):
        print('STOP')
        self.CharactRunning = False
#        self.Inputs.ClearTask()
        # if self.ContRecord:
        #     self.Inputs.StopContData()
        #     if self.GenTestSig:
        #         self.VgOut.StopTask()
        #         self.VgOut = None
