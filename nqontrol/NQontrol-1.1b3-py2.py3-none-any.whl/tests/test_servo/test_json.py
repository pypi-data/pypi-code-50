import logging as log
import multiprocessing as mp
import os
from time import sleep

from openqlab import io

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


class TestServoJson(TestServoTemplate):
    def test_saveLoadJson(self):
        # TODO better test
        self.s.enableFifo(3)
        self.s.enableRamp(30, 0.1)
        self.s.realtimePlot()
        sleep(0.1)
        self.s.stopRealtimePlot()
        self.s.servoDesign.integrator(100)
        self.s.servoDesign.notch(500, 4)
        servoDesign_str = self.s.servoDesign.__str__()
        self.s.gain = 20345.190
        self.s.saveJsonToFile("servo.json")
        self.s.gain = 10
        self.assertEqual(self.s._state["gain"], 10)
        self.s.loadSettings("servo.json")
        self.assertEqual(self.s._state["gain"], 20345.190)
        self.assertEqual(self.s.servoDesign.__str__(), servoDesign_str)
        self.sd.removeServo(3)
        self.sd.addServo(3, "servo.json")
        self.assertEqual(self.sd.servo(3)._state["gain"], 20345.190)
        self.assertEqual(self.sd.servo(3)._channel, 3)
        self.assertIsInstance(self.sd.servo(3)._ramp, mp.managers.DictProxy)
        if os.path.exists("servo.json"):
            os.remove("servo.json")

    def test_load_settings(self):
        with self.assertRaises(ValueError):
            self.s.loadSettings(1)

    def test_read_json_from_file(self):
        with self.assertRaises(FileNotFoundError):
            self.s._readJsonFromFile("I hate sand")

    def test_saving_and_loading_with_plant_and_temp_feedback(self):
        tests_dir = os.path.dirname(os.path.abspath(__file__))
        self.s.servoDesign.integrator(400)
        dc = io.read(f"{tests_dir}/../support_files/fra.csv")
        self.s.servoDesign.plant = dc
        self.s.tempFeedbackStart(0.84, (1, 3), voltage_limit=3.6, update_interval=1.3)
        servoDesign_str = self.s.servoDesign.__str__()
        plant = self.s.servoDesign.plant.copy()
        self.s.saveJsonToFile("servo.json")
        self.s.tempFeedbackStop()
        self.assertIsNone(self.s.tempFeedback)
        self.s._tempFeedbackSettings = {}
        self.assertEqual(len(plant), len(self.s.servoDesign.plant))
        self.s.servoDesign = None
        self.s.loadSettings("servo.json")
        self.assertEqual(servoDesign_str, self.s.servoDesign.__str__())
        self.assertEqual(self.s._tempFeedbackSettings["dT"], 0.84)
        self.assertEqual(tuple(self.s._tempFeedbackSettings["mtd"]), (1, 3))
        self.assertEqual(self.s._tempFeedbackSettings["voltage_limit"], 3.6)
        self.assertEqual(self.s._tempFeedbackSettings["update_interval"], 1.3)
        if os.path.exists("servo.json"):
            os.remove("servo.json")

    def test_apply_old_settings(self):
        self.s.outputSw = True
        dic = self.s.getSettingsDict()
        # del dict['_state']['snapSw']
        # self.s.snapSw = True
        self.s.outputSw = False
        self.assertTrue(dic["_state"]["outputSw"])
        self.assertFalse(self.s.outputSw)
        self.s.loadSettings(dic)
        # self.assertTrue(self.s.snapSw)
        self.assertTrue(self.s.outputSw)

    def test_read_settings_from_adwin_before_saving(self):
        sd2 = ServoDevice(settings.DEVICE_NUM)
        s = sd2.servo(2)
        s._adw = self.s._adw

        s.inputSw = True
        s.offset = 0.84
        s.gain = 94.1
        s.inputSensitivity = 3
        s.auxSensitivity = 2
        s.filterStates = [True, False, True, True, False]

        # pre-check if mockAdwin is the same
        self.assertEqual(s._adw, self.s._adw)

        if isinstance(s._adw, MockADwin):
            self.assertListEqual(s._adw._par, self.s._adw._par)

        self.s.filters = [
            [2, 3, 4, 5, 6],
            [2, 3, 4, 5, 6],
            [2, 3, 4, 5, 6],
            [2, 3, 4, 5, 6],
            [2, 3, 4, 5, 6],
        ]
        new_filters = [
            [20, 30, 40, 50, 60],
            [20, 30, 40, 50, 60],
            [20, 30, 40, 50, 60],
            [20, 30, 40, 50, 60],
            [20, 30, 40, 50, 60],
        ]
        s.filters = new_filters

        dic = self.s.getSettingsDict()

        self.assertEqual(dic["_state"]["inputSw"], True)
        self.assertAlmostEqual(dic["_state"]["offset"], 0.84)
        self.assertAlmostEqual(dic["_state"]["gain"], 94.1)
        self.assertEqual(dic["_state"]["inputSensitivity"], 3)
        self.assertEqual(dic["_state"]["auxSensitivity"], 2)
        self.assertEqual(
            list(dic["_state"]["filtersEnabled"]), [True, False, True, True, False]
        )
        self.assertEqual(list(dic["_state"]["filters"]), new_filters)
