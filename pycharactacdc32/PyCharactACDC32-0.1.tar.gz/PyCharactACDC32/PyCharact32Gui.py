#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:29:47 2019

@author: aguimera
"""


from __future__ import print_function
from PyQt5 import Qt

from qtpy import QtWidgets
import numpy as np
import os
import sys
import deepdish as dd
import matplotlib.pyplot as plt
from pyqtgraph.parametertree import Parameter, ParameterTree

import PyqtTools.FileModule as FileMod
import PyqtTools.SweepsModule as SweepMod
import PyqtTools.ACModule as BodeMod

import PyGFETdb.PlotDataClass as PyFETpl
import PyCharact32Core.Charact32Thread as CharactMod
import PyCharact32Core.CharactCore32 as CoreMod


###############################################################################
####
###############################################################################


class CharacLivePlot():

    DCPlotVars = ('Ids', 'Rds', 'Gm', 'Ig')
    BodePlotVars = ('GmPh', 'GmMag')
    PSDPlotVars = ('PSD',)
    PlotSwDC = None
    PlotSwAC = None
    DebugFig = None

    def __init__(self, SinglePoint=True, Bode=True, PSD=True, FFT=False):

        self.DebugFig, self.DebugAxs = plt.subplots()
        self.DebugAxs.ticklabel_format(axis='y', style='sci',
                                       scilimits=(-2, 2))
        plt.show()

        if not SinglePoint:
            self.PlotSwDC = PyFETpl.PyFETPlot()
            self.PlotSwDC.AddAxes(self.DCPlotVars)

        if Bode or PSD:
            PVAC = []
            if Bode:
                for var in self.BodePlotVars:
                    PVAC.append(var)
            if PSD:
                for var in self.PSDPlotVars:
                    PVAC.append(var)
            self.PlotSwAC = PyFETpl.PyFETPlot()
            self.PlotSwAC.AddAxes(PVAC)

        if FFT:
            self.FFTFig, self.FFTAxs = plt.subplots()
            self.FFTAxs.ticklabel_format(axis='y', style='sci',
                                         scilimits=(-2, 2))
            plt.show()

    def UpdateTimeViewPlot(self, Ids, Time, Dev):
        while self.DebugAxs.lines:
            self.DebugAxs.lines[0].remove()
        self.DebugAxs.plot(Time, Ids)
        self.DebugAxs.set_ylim(np.min(Ids), np.max(Ids))
        self.DebugAxs.set_xlim(np.min(Time), np.max(Time))
        self.DebugAxs.set_title(str(Dev))
        self.DebugFig.canvas.draw()

    def UpdateTimeAcViewPlot(self, Ids, Time):
        while self.DebugAxs.lines:
            self.DebugAxs.lines[0].remove()
        self.DebugAxs.plot(Time, Ids)
        self.DebugAxs.set_ylim(np.min(Ids), np.max(Ids))
        self.DebugAxs.set_xlim(np.min(Time), np.max(Time))
        self.DebugFig.canvas.draw()

    def UpdateSweepDcPlots(self, Dcdict):
        if self.PlotSwDC:
            self.PlotSwDC.ClearAxes()
            self.PlotSwDC.PlotDataCh(Dcdict)
            self.PlotSwDC.AddLegend()
            self.PlotSwDC.Fig.canvas.draw()

    def UpdateAcPlots(self, Acdict):
        if self.PlotSwAC:
            self.PlotSwAC.ClearAxes()
            self.PlotSwAC.PlotDataCh(Acdict)
            self.PlotSwAC.Fig.canvas.draw()

    def PlotFFT(self, FFT):
        self.FFTAxs.plot(np.abs(FFT))
        self.FFTFig.canvas.draw()

    def __del__(self):
        plt.close('all')


###############################################################################
####
###############################################################################


class MainWindow(Qt.QWidget):
    ''' Main Window '''

    Charac = None
    PlotSweep = None

    def __init__(self):
        super(MainWindow, self).__init__()

        layout = Qt.QVBoxLayout(self)

        self.btnAcq = Qt.QPushButton("Start Acq!")
        layout.addWidget(self.btnAcq)

        self.ChannelsPar = CharactMod.SampSetParam(name='ChannelsConfig')
        self.Parameters = Parameter.create(name='App Parameters',
                                           type='group',
                                           children=(self.ChannelsPar,))

        self.ChannelsPar.NewConf.connect(self.on_NewConf)

        # Sweeps
        self.SweepsParams = SweepMod.SweepsConfig(name='SweepOptions')
        self.Parameters.addChild(self.SweepsParams)

        # Bode
        self.ACParams = BodeMod.ACConfig(name='ACOptions')
        self.Parameters.addChild(self.ACParams)

        self.Parameters.sigTreeStateChanged.connect(self.on_pars_changed)

        self.treepar = ParameterTree()
        self.treepar.setParameters(self.Parameters, showTop=False)
        self.treepar.setWindowTitle('pyqtgraph example: Parameter Tree')

        layout.addWidget(self.treepar)

        self.setGeometry(650, 20, 400, 800)
        self.setWindowTitle('MainWindow')

        self.btnAcq.clicked.connect(self.on_btnStart)

        self.FileParameters = FileMod.SaveFileParameters(QTparent=self,
                                                         name='Record File')
        self.Parameters.addChild(self.FileParameters)

        # Threadings
        self.threadAcq = None
        self.threadSave = None
        self.threadPlotter = None

        self.ConfigParameters = FileMod.SaveSateParameters(QTparent=self, name='Configuration File')
        self.Parameters.addChild(self.ConfigParameters)

    def on_pars_changed(self, param, changes):
        for param, change, data in changes:
            path = self.Parameters.childPath(param)
            if path is not None:
                childName = '.'.join(path)
            else:
                childName = param.name()
        print('  parameter: %s' % childName)
        print('  change:    %s' % change)
        print('  data:      %s' % str(data))
        print('  ----------')

        if childName == 'SweepOptions.SweepsConfig.MaxSlope':
            self.DevCondition = data
            if self.Charac:
                self.Charac.DevCondition = self.DevCondition

    def on_NewConf(self):
        self.Parameters.sigTreeStateChanged.disconnect()
        self.Parameters.sigTreeStateChanged.connect(self.on_pars_changed)

    def on_btnStart(self):
        print('BUTTON')

        if self.Charac is not None:
            print('do nothing')
        else:
            ChannelsKwargs = self.ChannelsPar.GetChannelsConfigKwargs()
            print(ChannelsKwargs)
            if ChannelsKwargs['GateChannel'] == True and 'Ch27' not in ChannelsKwargs['Channels']:
                print('GGGGAATTTEEEE')
                self.ChannelsPar.Channels.param('Ch27').setValue(True)
                ChannelsKwargs = self.ChannelsPar.GetChannelsConfigKwargs()

            # for ch in ChannelsKwargs['Channels']:
                   
            #     if ChannelsKwargs['GateChannel'] == ch:
            #         self.ChannelsPar.Channels.param(ch).setValue(False)
                    # ChannelsKwargs = self.ChannelsPar.GetChannelsConfigKwargs()

            self.Charac = CoreMod.Charact(Channels=ChannelsKwargs['Channels'],
                                          GateChannel=ChannelsKwargs['GateChannel'],)
                                          # Configuration=ChannelsKwargs['Configuration'])

        if self.Charac.CharactRunning:
            print('STOOP')
            self.StopSweep()
        else:
            self.SweepsKwargs = self.SweepsParams.GetSweepsParams()
            self.BodeKwargs = self.ACParams.GetBodeParams()
            self.PSDKwargs, self.CheckPSD = self.ACParams.GetPSDParams()
            self.Rhardware, self.CheckBode = self.ACParams.GetBodeSettings()
            print(self.Rhardware, self.CheckBode)
            print(self.CheckPSD)

            if len(self.SweepsKwargs['VgSweep']) < 2 and len(self.SweepsKwargs['VdSweep']):
                self.SinglePoint = True
            else:
                self.SinglePoint = False

            self.Cycles = self.ChannelsPar.GetCycles()

            # Define events callbacks
            self.Charac.EventCharSweepDone = self.CharSweepDoneCallBack
            self.Charac.EventCharBiasDone = self.CharBiasDoneCallBack
            self.Charac.EventCharBiasAttempt = self.CharBiasAttemptCallBack
            self.Charac.EventCharACDone = self.CharACDoneCallBack
            self.Charac.EventCharAcDataAcq = self.CharAcDataAcq

            self.FileName = self.FileParameters.FilePath()
            print('FileName', self.FileName)
            if self.FileName == '':
                print('No file')
            else:
                if os.path.isfile(self.FileName):
                    print('Remove File')
                    os.remove(self.FileName)

            # Plotting
            if self.PlotSweep:
                del self.PlotSweep
            self.PlotSweep = CharacLivePlot(SinglePoint=self.SinglePoint,
                                            Bode=self.CheckBode,
                                            PSD=self.CheckPSD,
                                            )
            SwVgsVals, SwVdsVals = self.SweepVariables()

            # Cycles
            self.initCy = self.Cycles['InitCy']
            self.finalCy = self.Cycles['FinalCy']
            if self.initCy > self.finalCy:
                print('Set correct Cycles')
                self.finalCy = self.initCy + 1
                self.ChannelsPar.Cycles.param('FinalCy').setValue(self.finalCy)
            self.ChannelsPar.Cycles.param('CurrentCy').setValue(self.initCy)

            # Set Charact Configuration
            self.Charac.IVGainDC = ChannelsKwargs['DCGain']
            self.Charac.IVGainAC = ChannelsKwargs['ACGain']
            self.Charac.DevCondition = self.SweepsKwargs['MaxSlope']

            if self.CheckBode:
                if self.Charac:
                    if self.BodeKwargs['FreqMin'] and self.BodeKwargs['FreqMax'] > 0:
                        self.Charac.SetBodeConfig(FreqMin=self.BodeKwargs['FreqMin'],
                                                  FreqMax=self.BodeKwargs['FreqMax'],
                                                  nFreqs=self.BodeKwargs['nFreqs'],
                                                  Arms=self.BodeKwargs['Arms'],
                                                  nAvg=self.BodeKwargs['nAvg'],
                                                  BodeRh=self.CheckBode,
                                                  )
                                                  
                        self.ACParams.BodeParameters.param('BodeL Duration').setValue(self.Charac.BodeSignal.BodeDuration[0])
                        self.ACParams.BodeParameters.param('BodeH Duration').setValue(self.Charac.BodeSignal.BodeDuration[1])

            if self.CheckPSD:
                if self.Charac:
                    self.SetPSDConfig()
                    self.Charac.PSDDuration = self.ACParams.GetPSDDuration()

            self.Charac.InitSweep(VgsVals=SwVgsVals,
                                  VdsVals=SwVdsVals,
                                  PSD=self.CheckPSD,
                                  Bode=self.CheckBode)

            if self.Charac.CharactRunning:
                self.btnAcq.setText("Stop Gen")
            else:
                print('ERROR')

    def SweepVariables(self):
        SwVgsVals = self.SweepsKwargs['VgSweep']
        SwVdsVals = self.SweepsKwargs['VdSweep']
        return SwVgsVals, SwVdsVals

    def SetPSDConfig(self):
        self.Charac.PSDnFFT = 2**self.PSDKwargs['2**nFFT']
        self.Charac.PSDFs = self.PSDKwargs['Fs']
        self.Charac.PSDnAvg = self.PSDKwargs['PSDnAvg']

    def NextCycle(self):
        if self.initCy < self.finalCy-1:
            self.initCy += 1
            self.ChannelsPar.Cycles.param('CurrentCy').setValue(self.initCy)

            SwVgsVals, SwVdsVals = self.SweepVariables()
            self.Charac.InitSweep(VgsVals=SwVgsVals,
                                  VdsVals=SwVdsVals,
                                  PSD=self.CheckPSD,
                                  Bode=self.CheckBode)
        else:
            if self.Charac.CharactRunning:
                self.initCy = 0
                self.ChannelsPar.Cycles.param('CurrentCy').setValue(self.initCy)
                self.Charac.SetBias(Vds=0, Vgs=0)
                self.StopSweep()

# Events Done
###############################################################################

    def CharSweepDoneCallBack(self, Dcdict, Acdict):
        if self.FileName:
            Filename = self.FileName + "{}-Cy{}.h5".format('', self.initCy)
            if Acdict:
                dd.io.save(Filename, (Dcdict, Acdict), ('zlib', 1))
#                pickle.dump(Acdict, open('SaveDcData.pkl', 'wb'))
            else:
                dd.io.save(Filename, Dcdict, ('zlib', 1))
        self.NextCycle()

    def CharBiasDoneCallBack(self, Dcdict):
        self.PlotSweep.UpdateSweepDcPlots(Dcdict)

#    def CharFFTCallBack(self, FFT):
#        if self.ChckFFT.isChecked():
#            self.PlotSweep.PlotFFT(FFT[1:])

    def CharAcDataAcq(self, Ids, time):
        self.PlotSweep.UpdateTimeAcViewPlot(Ids, time)

    def CharACDoneCallBack(self, Acdict):
        self.PlotSweep.UpdateAcPlots(Acdict)
        if not self.Charac.CharactRunning:
            self.StopSweep()

    def CharBiasAttemptCallBack(self, Ids, Time, Dev):
        self.PlotSweep.UpdateTimeViewPlot(Ids, Time, Dev)
        if not self.Charac.CharactRunning:
            self.StopSweep()

# Stop Events
###############################################################################
    def StopSweep(self):
        print('Stop')
        self.Charac.StopCharac()
        self.Charac.SetBias(Vds=0, Vgs=0)
        self.Charac.SetDigitalSignal(Signal=np.array([0, 0, 0, 0, 0, 0, 0, 0,
                                                      0, 0], dtype=np.uint8))
        self.Charac.__del__()
        self.Charac = None
        self.btnAcq.setText("Start")
#        self.ChckSaveData.setChecked(False)

# Save Data Events
###############################################################################


def main():
    import argparse
    import pkg_resources

    # Add version option
    __version__ = pkg_resources.require("PyqtTools")[0].version
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version',
                        version='%(prog)s {version}'.format(
                            version=__version__))
    parser.parse_args()

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
