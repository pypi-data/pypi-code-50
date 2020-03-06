import logging as log
from time import sleep, time

import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame
from scipy.signal import argrelmax, find_peaks

from nqontrol import Servo, ServoDevice
from nqontrol.general import helpers, settings
from nqontrol.general.errors import ConfigurationError, DeviceError, UserInputError
from nqontrol.general.mockAdwin import MockADwin

from .test_servo import TestServoTemplate

log.basicConfig(
    format="%(levelname)s: %(module)s.%(funcName)s: %(message)s", level="INFO"
)

settings.NUMBER_OF_SERVOS = 8
settings.NUMBER_OF_MONITORS = 8


class TestServoPlotting(TestServoTemplate):
    def test_readoutNewData(self):
        self.s.enableFifo(1)
        self.s._waitForBufferFilling()
        data = self.s._readoutNewData(self.s._fifo["maxlen"])
        self.assertEqual(type(data), DataFrame)
        self.assertEqual(len(data), self.s._fifo["maxlen"])
        # Readout 0 data
        data = self.s._readoutNewData(0)
        self.assertEqual(type(data), DataFrame)
        self.assertEqual(len(data), 0)
        self.assertListEqual(list(data.columns), self.s.realtime["ydata"])

        # read more data than available
        b_size = self.s._fifoBufferSize
        data = self.s._readoutNewData(1000000)
        self.assertLessEqual(len(data), b_size + 500)

    def test_prepareContinuousData(self):
        self.s.enableFifo(int(settings.SAMPLING_RATE / 100))
        for i in range(10):
            self.s._prepareContinuousData()
            sleep(0.01)

        self.s.enableFifo(1)
        self.s._waitForBufferFilling()
        self.s._prepareContinuousData()
        dc = self.s._fifoBuffer
        self.assertEqual(len(dc), self.s._fifo["maxlen"])
        self.s._waitForBufferFilling()
        dc = self.s.takeData()
        self.assertTrue(dc.equals(self.s._fifoBuffer))
        self.assertEqual(len(dc), self.s._fifo["maxlen"])
        self.s.enableFifo(int(settings.SAMPLING_RATE))
        i = 0
        while self.s._fifoBufferSize > 10:
            self.s._prepareContinuousData()
            i += 1
            if i > 200:
                assert False, "Can't read fast enough."

    def test_timeForFifoCycles(self):
        self.s._fifo["stepsize"] = 1
        self.assertEqual(self.s._timeForFifoCycles(10), 10 / settings.SAMPLING_RATE)

    def test_waitForBufferFilling(self):
        self.s.enableFifo(10)
        t1 = time()
        self.s._waitForBufferFilling()
        t2 = time()
        t = 10 / settings.SAMPLING_RATE * self.s._fifo["maxlen"]
        self.assertAlmostEqual(t2 - t1, t, places=2)

        self.s.enableFifo(10)
        t1 = time()
        self.s._waitForBufferFilling(refill=False)
        t2 = time()
        t = 10 / settings.SAMPLING_RATE * self.s._fifo["maxlen"]
        self.assertLess(t2 - t1, t)

        self.s.enableFifo(1)
        t1 = time()
        self.s._waitForBufferFilling(n=30005, refill=False)
        t2 = time()
        t = 1 / settings.SAMPLING_RATE * self.s._fifo["maxlen"]
        self.assertLess(t2 - t1, t)

    def test_prepareRampData(self):
        for n in (100, 255, 13):
            log.warning("n = {}".format(n))
            self.s.enableRamp(n, 10 / n)
            self.s._prepareRampData()
            dc = self.s._fifoBuffer

            peaks, _ = find_peaks(dc["output"])
            (minima,) = argrelmax(np.array(dc["output"]))

            if len(peaks) > 1:
                _ = dc.plot()
                dc["output"].iloc[peaks].plot(style="o", ax=_)
                dc["input"].iloc[minima].plot(style="o", ax=_)
                plt.show()
            self.assertLessEqual(len(peaks), 1)

            if len(dc) < self.s._fifo["maxlen"] / 2:
                print(len(dc))
                self.assertEqual(self.s.fifoStepsize, 1)

            # Check 1 / max time = f
            # self.assertGreaterEqual(1 / dc.index[-1], self.s.rampFrequency * .7)

            with self.assertLogs(level="WARNING"):
                self.s._prepareRampData(0)

    def test_prepareRampDataException(self):
        self.s.enableFifo(1)
        self.s._ramp["minimum"] = -5
        self.s._waitForBufferFilling()
        with self.assertLogs(level="WARNING"):
            self.s._prepareRampData(10)

    def test_realtimePlot(self):
        with self.assertLogs(level="WARNING"):
            self.s.stopRealtimePlot()

        plot_sleep_time = 0.3
        self.s.enableFifo(10)
        self.s.realtimePlot(refreshTime=0.06)
        self.s.realtime["ylim"] = (-0.1, 0.2)
        sleep(plot_sleep_time)
        self.s.stopRealtimePlot()

        self.s.enableRamp(10, 0.1)
        self.s.realtimePlot(ydata=["input"])
        self.s.realtime["ylim"] = None
        sleep(plot_sleep_time)
        self.s.realtime["ydata"] = ["aux", "output"]
        self.s.enableRamp(5, 0.05)
        sleep(plot_sleep_time)
        self.s.disableRamp()
        sleep(0.1)
        self.s.stopRealtimePlot()

    def test_tooManyRealtimePlots(self):
        self.s.realtimePlot()
        sleep(0.1)
        with self.assertRaises(UserInputError):
            self.s.realtimePlot()
        self.s.stopRealtimePlot()

    def test_fifo_switching_with_ramp_bug(self):
        s1 = self.sd.servo(3)
        s2 = self.sd.servo(4)
        s1.enableRamp(50, 5)
        s1.takeData()
        s2.enableFifo()
        s2._waitForBufferFilling()
        s2.takeData()
        s1.takeData()

    def test_realtime_fifo(self):
        self.s.realtime["enabled"] = True
        self.assertFalse(self.s.realtimeEnabled)
        self.s.enableFifo()
        self.assertTrue(self.s.realtimeEnabled)
        self.s.disableFifo()
        self.s.disableFifo()

    def test_fifoOutput(self):
        # enable FIFO and test correct Parameters
        stepsize = 100
        self.s.enableFifo(stepsize)
        self.assertEqual(
            2, self.s._adw.Get_Par(settings.PAR_ACTIVE_CHANNEL)
        )  # Test channel
        self.assertEqual(
            stepsize, self.s._adw.Get_Par(settings.PAR_FIFOSTEPSIZE)
        )  # Test stepsize
        self.s.disableFifo()
        self.assertFalse(self.s.fifoEnabled)
        self.s.enableFifo(1)
        self.assertEqual(self.s.fifoStepsize, 1)
        with self.assertRaises(ValueError):
            self.s.enableFifo(0)

    def test_fifoFrequency(self):
        self.s.enableFifo(frequency=30)
        self.assertEqual(
            2, self.s._adw.Get_Par(settings.PAR_ACTIVE_CHANNEL)
        )  # Test channel
        self.assertEqual(round(self.s.rampFrequency), 30)
        self.assertEqual(self.s.fifoStepsize, 10)
