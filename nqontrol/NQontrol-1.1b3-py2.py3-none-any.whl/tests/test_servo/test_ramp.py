import logging as log
import unittest
from time import sleep

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


class TestServoRamp(TestServoTemplate):
    def test_rampWithWrongParameters(self):
        with self.assertRaises(ValueError):
            self.s.enableRamp(amplitude=-0.1)
        with self.assertRaises(ValueError):
            self.s.enableRamp(amplitude=10.1)

    @unittest.skip("Ramp sometimes does not work with real device.")
    def test_ramp(self):
        settings.SAMPLING_RATE = settings.RAMP_DATA_POINTS

        # what happens if stepsize is still None
        _ = self.s.rampFrequency

        self.s.enableRamp(5, 5, enableFifo=False)
        self.s.enableFifo()
        self.assertEqual(self.s._ramp["amplitude"], 5)
        self.assertEqual(self.s._adw.Get_Par(settings.PAR_RCR), 1282)
        self.assertEqual(self.s._adw.Get_FPar(settings.FPAR_RAMPAMP), 0.5)
        self.s.realtimePlot()
        settings.SAMPLING_RATE = 200e3
        sleep(0.1)
        self.s.stopRealtimePlot()

        settings.SAMPLING_RATE = settings.RAMP_DATA_POINTS
        self.s.enableRamp(255, 10)
        self.assertEqual(self.s._ramp["amplitude"], 10)
        self.assertTrue(self.s.rampEnabled)
        self.assertEqual(self.s._adw.Get_Par(settings.PAR_RCR), 65282)
        self.assertEqual(self.s._adw.Get_FPar(settings.FPAR_RAMPAMP), 1.0)
        settings.SAMPLING_RATE = 200e3
        self.s.realtimePlot()
        sleep(0.1)
        self.s.stopRealtimePlot()

        self.sd.removeServo(5)
        self.assertIsNone(self.sd._servos[4])
        self.s.disableRamp()
        for s in self.sd._servos:
            if s is not None:
                self.assertFalse(s.rampEnabled)

        self.s.enableRamp(1, 2)
        self.assertTrue(self.s.fifoEnabled)
        self.assertEqual(self.s._fifo["maxlen"], self.s._fifo["maxlen"])
        self.s.disableRamp()

        # function accepts empty parameter list
        self.s.enableRamp()

    def test_convertFrequencyBack(self):
        for n in range(1, 255):
            self.s.enableFifo(n)
            f = self.s.rampFrequency
            self.s.rampFrequency = f
            self.assertEqual(self.s.fifoStepsize, n)

    def test_calculateRefreshTime(self):
        self.s._fifo["stepsize"] = settings.SAMPLING_RATE
        self.s._fifo["maxlen"] = 1000
        self.s._calculateRefreshTime()
        self.assertAlmostEqual(self.s.realtime["refreshTime"], 500)

        self.s._fifo["stepsize"] = 1
        self.s._calculateRefreshTime()
        self.assertAlmostEqual(self.s.realtime["refreshTime"], self.s._MIN_REFRESH_TIME)

    def test_rampAmplitude(self):
        self.s.rampAmplitude = 5.6
        self.assertEqual(self.s.rampAmplitude, 5.6)
        self.s.enableRamp()
        self.s.rampAmplitude = 8.6
        self.assertEqual(self.s.rampAmplitude, 8.6)
        with self.assertRaises(UserInputError):
            self.s.rampAmplitude = 10.1
        with self.assertRaises(UserInputError):
            self.s.rampAmplitude = -0.1

    def test_rampFrequency(self):
        self.s.rampFrequency = 47.5
        self.assertAlmostEqual(self.s.rampFrequency, 47.5, places=0)
        self.s.enableRamp()
        self.s.rampFrequency = 22

    def test_rampFrequencyMax(self):
        settings.SAMPLING_RATE = 200000
        self.assertAlmostEqual(self.s.rampFrequencyMax, 389, places=0)

    def test_rampFrequencyMin(self):
        settings.SAMPLING_RATE = 200000
        self.assertAlmostEqual(self.s.rampFrequencyMin, 1.5, places=0)

    def test_fastRamp(self):
        plot_sleep_time = 0.1
        self.s.enableRamp(255, 0.1)
        self.s.realtimePlot()
        sleep(plot_sleep_time)
        self.s.stopRealtimePlot()
        self.s.disableRamp()
