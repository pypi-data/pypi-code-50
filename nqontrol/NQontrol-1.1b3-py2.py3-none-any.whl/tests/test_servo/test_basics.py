import logging as log
import unittest
from math import pow
from multiprocessing import Process
from time import sleep

from ADwin import ADwinError
from openqlab.analysis import ServoDesign

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


class TestServoBasics(TestServoTemplate):
    def test_channel(self):
        serv = Servo(2, MockADwin(0))
        self.assertEqual(2, serv.channel)

    @unittest.skipIf(
        settings.DEVICE_NUM != 0, "This test does not work with the real device"
    )
    def test_triggerReload(self):
        print(self.s._adw.reset_trigger)
        self.s._adw.reset_trigger = False
        print(self.s._adw.reset_trigger)
        with self.assertRaises(DeviceError):
            self.s._triggerReload()

    def test_checkNumberAndChannel(self):
        self.assertEqual(self.s._channel, self.testchannel)

    def test_inputGain(self):
        self.assertEqual(self.s._adw.Get_Par(settings.PAR_SENSITIVITY), 0)

        self.s.inputSensitivity = 2
        self.sd.servo(8).inputSensitivity = 3
        self.assertEqual(self.s._adw.Get_Par(settings.PAR_SENSITIVITY), 49160)

        self.s.auxSensitivity = 3
        self.assertEqual(self.s._adw.Get_Par(settings.PAR_SENSITIVITY), 835592)
        self.sd.servo(7).auxSensitivity = 2
        self.assertEqual(self.s._adw.Get_Par(settings.PAR_SENSITIVITY), 537706504)

    def test_runtime(self):
        self.s.enableFifo(1)
        self.s.enableRamp(1, 1)
        for i in range(1, 9):
            self.sd.enableMonitor(i, i, card="input")
            self.sd.servo(i).offset = 3
            self.sd.servo(i).auxSw = True
            self.sd.servo(i).filters = [[7] * 5] * 5
        sleep(0.1)
        self.assertLess(self.s._adw.Get_Par(settings.PAR_TIMEDIFF), 4500)
        self.assertGreater(self.s._adw.Get_Par(settings.PAR_TIMEDIFF), 2500)

    def test_sampling_rate(self):
        CPU_CLK = 1e9
        self.assertAlmostEqual(
            self.s._adw.Get_Processdelay(1), CPU_CLK / settings.SAMPLING_RATE
        )

    def test_inputSensitivityException(self):
        with self.assertRaises(ValueError):
            self.s.inputSensitivity = -1
        with self.assertRaises(ValueError):
            self.s.inputSensitivity = 4

    def test_auxSensitivityException(self):
        with self.assertRaises(ValueError):
            self.s.auxSensitivity = -1
        with self.assertRaises(ValueError):
            self.s.auxSensitivity = 4

    def test_offsetGain(self):
        self.s.offset = 9.4
        self.s.gain = 1.5
        self.assertEqual(
            self.s._adw.GetData_Double(settings.DATA_OFFSETGAIN, self.testchannel, 1)[
                :
            ],
            [1.5],
        )
        self.assertAlmostEqual(
            self.s._adw.GetData_Double(
                settings.DATA_OFFSETGAIN, self.testchannel + 8, 1
            )[0],
            30801.92,
        )

        self.s.gain = 1.0
        self.s.inputSensitivity = 3
        self.assertEqual(
            self.s._adw.GetData_Double(settings.DATA_OFFSETGAIN, self.testchannel, 1)[
                :
            ],
            [0.125],
        )
        self.assertEqual(self.s.gain, 1)
        self.s.offset = 1
        self.assertEqual(
            self.s._adw.GetData_Double(
                settings.DATA_OFFSETGAIN, self.testchannel + 8, 1
            )[:],
            [26214.4],
        )

    def test_offsetLimits(self):
        for mode in range(4):
            limit = round(10 / pow(2, mode), 2)
            self.s.inputSensitivity = mode
            self.s.offset = limit
            self.assertAlmostEqual(self.s.offset, limit, places=3)
            self.s.offset = limit + 0.1
            self.assertAlmostEqual(self.s.offset, limit, places=3)
            # set offset before sensitivity
            self.s.inputSensitivity = 0
            self.s.offset = 20
            self.s.inputSensitivity = mode
            self.assertAlmostEqual(self.s.offset, limit, places=3)

    def test_break_adwin_with_multiprocessing(self):
        processes = []
        for n in range(10):
            p = Process(target=self.workload_loop, args=(n,))
            processes.append(p)
        for p in processes:
            p.start()
        for p in processes:
            p.join()

    def workload_loop(self, N):
        for _ in range(10):
            _ = self.sd.workload
            _ = self.sd.timestamp
            self.s.filters = [[1] * 5] * 5

    def test_check_control_switch_updates(self):
        self.sd.reboot()
        self.assertFalse(self.s.inputSw)
        self.assertFalse(self.s.outputSw)
        self.assertFalse(self.s.offsetSw)
        # self.assertFalse(self.s.snapSw)
        self.assertFalse(self.s.auxSw)
        self.s.inputSw = True
        self.s.outputSw = True
        self.s.offsetSw = True
        # self.s.snapSw = True
        self.s.auxSw = True
        self.s._state["inputSw"] = False
        self.assertTrue(self.s.inputSw)
        self.s._state["outputSw"] = False
        self.assertTrue(self.s.outputSw)
        self.s._state["offsetSw"] = False
        self.assertTrue(self.s.offsetSw)
        # self.s._state['snapSw'] = False
        # self.assertTrue(self.s.snapSw)
        self.s._state["auxSw"] = False
        self.assertTrue(self.s.auxSw)

    def test_send_state_after_reboot(self):
        sleep(0.1)
        time_ = self.sd.timestamp
        self.assertEqual(
            self.s._adw.GetData_Double(settings.DATA_OFFSETGAIN, self.testchannel, 1)[
                :
            ],
            [1.0],
        )
        self.s.gain = 1.5
        self.assertEqual(
            self.s._adw.GetData_Double(settings.DATA_OFFSETGAIN, self.testchannel, 1)[
                :
            ],
            [1.5],
        )
        self.sd.reboot()
        self.assertEqual(
            self.s._adw.GetData_Double(settings.DATA_OFFSETGAIN, self.testchannel, 1)[
                :
            ],
            [1.5],
        )
        self.assertLessEqual(self.sd.timestamp, time_)

    def test_check_input_offset(self):
        self.s = self.sd.servo(8)
        self.s.enableFifo(1)
        self.s._waitForBufferFilling()
        data = self.s._readoutNewData(self.s._fifo["maxlen"])
        self.assertAlmostEqual(data["aux"].mean(), 0, places=1)
        self.assertAlmostEqual(data["input"].mean(), 0, places=1)


class TestServoMonitors(TestServoTemplate):
    def test_monitor(self):
        # assign different channels
        self.sd.enableMonitor(8, self.testchannel, card="input")
        self.sd.enableMonitor(5, self.testchannel, card="aux")
        self.sd.enableMonitor(1, self.testchannel, card="output")
        self.sd.enableMonitor(2, self.testchannel, card="input")
        self.sd.enableMonitor(3, self.testchannel, card="ttl")
        self.assertEqual(self.s._adw.GetData_Long(settings.DATA_MONITORS, 8, 1)[0], 2)
        self.assertEqual(self.s._adw.GetData_Long(settings.DATA_MONITORS, 5, 1)[0], 10)
        self.assertEqual(self.s._adw.GetData_Long(settings.DATA_MONITORS, 1, 1)[0], 22)
        self.assertEqual(self.s._adw.GetData_Long(settings.DATA_MONITORS, 2, 1)[0], 2)
        self.assertEqual(self.s._adw.GetData_Long(settings.DATA_MONITORS, 3, 1)[0], 30)

        # disable monitor
        self.sd.disableMonitor(1)
        self.sd.disableMonitor(8)
        self.assertEqual(self.s._adw.GetData_Long(settings.DATA_MONITORS, 1, 1)[0], 0)
        self.assertEqual(self.s._adw.GetData_Long(settings.DATA_MONITORS, 8, 1)[0], 0)

        # try wrong channels
        with self.assertRaises(IndexError):
            self.sd.enableMonitor(0, self.testchannel, card="input")
        with self.assertRaises(IndexError):
            self.sd.enableMonitor(9, self.testchannel, card="input")
        with self.assertRaises(IndexError):
            self.sd.enableMonitor(-1, self.testchannel, card="input")


class TestServoFilters(TestServoTemplate):
    def test_filters(self):
        # default filter state
        filters = [
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
        ]
        filtersEnabled = [False] * 5
        self.assertEqual(list(self.s._state["filters"]), filters)
        self.assertEqual(list(self.s._state["filtersEnabled"]), filtersEnabled)

        # change filters
        filters = [
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 4, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 8, 0],
        ]
        self.s.filters = filters
        self.assertEqual(list(self.s._state["filters"]), filters)
        # Write junk to _filters to check reading
        self.s._filters = [[0.0] * 5] * 5
        self.assertEqual(self.s.filters, filters)
        self.assertEqual(list(self.s._state["filters"]), filters)
        for i in range(3, settings.NUMBER_OF_SERVOS):
            self.assertEqual(list(self.sd.servo(i).filters), self.s._DEFAULT_FILTERS)

    def test_filterExceptions(self):
        with self.assertRaises(IndexError):
            self.s.filters = [
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
            ]
        with self.assertRaises(IndexError):
            self.s.filters = [
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
            ]
        with self.assertRaises(IndexError):
            self.s.filters = [
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
            ]
        with self.assertRaises(IndexError):
            self.s.filters = [
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
            ]

    def test_filterControlRegister(self):
        # change filtersEnabled
        filtersEnabled = [True] * 5
        self.assertEqual(list(self.s._state["filtersEnabled"]), [False] * 5)
        self.s.filterStates = filtersEnabled
        self.assertEqual(list(self.s._state["filtersEnabled"]), filtersEnabled)

        # disable one by one
        filtersEnabled[2] = False
        self.s.filterState(2, False)
        filtersEnabled[4] = False
        self.s.filterState(4, False)
        self.assertEqual(list(self.s._state["filtersEnabled"]), filtersEnabled)

        # enable one by one
        filtersEnabled[2] = True
        self.s.filterState(2, True)
        filtersEnabled[4] = True
        self.s.filterState(4, True)
        self.assertEqual(list(self.s._state["filtersEnabled"]), filtersEnabled)

        # change the other bool states
        self.assertEqual(self.s._state["auxSw"], False)
        self.assertEqual(self.s._state["offsetSw"], False)
        self.assertEqual(self.s._state["outputSw"], False)
        self.assertEqual(self.s._state["inputSw"], False)
        self.s.auxSw = True
        self.s.offsetSw = True
        self.s.outputSw = True
        self.s.inputSw = True
        # read the states from ADwin
        self.s._readFilterControl()
        self.assertEqual(self.s._state["auxSw"], True)
        self.assertEqual(self.s._state["offsetSw"], True)
        self.assertEqual(self.s._state["outputSw"], True)
        self.assertEqual(self.s._state["inputSw"], True)


class TestServoInitialization(TestServoTemplate):
    def test_initWrongServoNumber(self):
        with self.assertRaises(ValueError):
            Servo(settings.NUMBER_OF_SERVOS + 1, MockADwin(0))
        with self.assertRaises(ValueError):
            Servo(0, MockADwin(0))

    def test_init_with_name(self):
        serv = Servo(2, MockADwin(0), name="Lincoln")
        self.assertEqual(serv.name, "Lincoln")

    def test_init_with_filters(self):
        filters = [
            [1, 0.3, 0, 0, 0],
            [1, 0, 0.02, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
        ]
        serv = Servo(2, MockADwin(0), filters=filters)
        self.assertEqual(serv._state["filters"], filters)

    def test_initWrongBufferSize(self):
        buff_size = settings.FIFO_BUFFER_SIZE

        settings.FIFO_BUFFER_SIZE = 2 * settings.FIFO_MAXLEN - 1
        with self.assertRaises(ConfigurationError):
            Servo(1, MockADwin(0))

        settings.FIFO_BUFFER_SIZE = buff_size

    def test_initRaisesError(self):
        with self.assertRaises(ADwinError):
            Servo(1, MockADwin(0, raiseError=True))


class TestServoDesign(TestServoTemplate):
    def test_applyServoDesign(self):
        sDesign = ServoDesign()
        sDesign.integrator(1e3)
        sDesign.notch(2e4, 1)
        sDesign.get(1).enabled = False
        sDesign.lowpass(1e5)
        settings.SAMPLING_RATE = 100000
        self.s.applyServoDesign(sDesign)
        filters = [
            [1.0313938638494844, -0.9999371701207665, 0.0, -0.9390625058174923, 0.0],
            [
                0.6777233810861951,
                -0.41885608448176614,
                0.35544676217239035,
                -0.6180339887498948,
                1.0,
            ],
            [9.869604401089363, -2.0000000000000004, 1.0000000000000004, 2.0, 1.0],
            [1.0, 0, 0, 0, 0],
            [1.0, 0, 0, 0, 0],
        ]
        self.assertEqual(self.s.filters, filters)
        self.assertEqual(self.s.filterStates, [True, False, True, False, False])
        self.s.applyServoDesign()


class TestServoAutooffset(TestServoTemplate):
    @unittest.skip("Feature not finished, yet.")
    def test_offset_autoset(self):
        self.s.inputSensitivity = 3
        self.s.offsetAutoSet()
        self.s.disableFifo()
        self.s.gain = 10
        self.assertAlmostEqual(self.s.offset, 0, places=1)
        self.assertNotEqual(self.s.offset, 0)
        log.warning("offset: {}".format(self.s.offset))
        sleep(0.1)

        self.s.inputSw = True
        self.s.outputSw = True
        self.s.filterState(1, True)
        self.s.enableFifo()
        self.s._waitForBufferFilling()
        df = self.s._readoutNewData(10000)["output"]
        mean_uncorrected = df.mean()
        log.warning(str(df.head()))
        log.warning(f"length of data: {len(df)}")
        self.assertNotEqual(mean_uncorrected, 0)
        self.s.offsetSw = True
        self.s._waitForBufferFilling()
        mean_corrected = self.s._readoutNewData(10000)["output"].mean()
        self.assertNotEqual(mean_corrected, 0)
        self.assertAlmostEqual(mean_corrected, 0, places=1)
