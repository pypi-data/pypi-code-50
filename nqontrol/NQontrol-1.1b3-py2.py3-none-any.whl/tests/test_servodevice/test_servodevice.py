import os
import unittest
from tempfile import TemporaryDirectory
from time import sleep

from openqlab import io

from nqontrol import Servo, ServoDevice
from nqontrol.general import settings


class TestServoDeviceTemplate(unittest.TestCase):
    def setUp(self):
        settings.NUMBER_OF_SERVOS = 8
        settings.NUMBER_OF_MONITORS = 8
        self.sd = ServoDevice(settings.DEVICE_NUM)


class TestBasics(TestServoDeviceTemplate):
    def test_reboot(self):
        self.sd.reboot()

    def test_add_remove_servo(self):
        sd = ServoDevice(0)
        sd._servos = [None] * settings.NUMBER_OF_SERVOS
        with self.assertRaises(IndexError):
            sd.addServo(0)
        with self.assertRaises(IndexError):
            sd.addServo(9)
        sd.addServo(4)
        self.assertIsInstance(sd._servos[3], Servo)
        with self.assertRaises(IndexError):
            sd.addServo(4)
        sd.removeServo(4)
        self.assertIsNone(sd._servos[3])

    def test_list_servos(self):
        sd = ServoDevice(settings.DEVICE_NUM)
        output = f"""ServoDevice {settings.DEVICE_NUM}
  Servo 1: Servo 1
  Servo 2: Servo 2
  Servo 3: Cavity
  Servo 4: Queen
  Servo 5: Servo 5
  Servo 6: Servo 6
  Servo 7: Servo 7
  Servo 8: Servo 8
"""
        sd.servo(3).name = "Cavity"
        sd.servo(4).name = "Queen"
        self.assertEqual(sd._list_servos_str(), output)
        # now just printout
        self.sd.list_servos()

    def test_get_servo(self):
        for i in range(1, 9):
            self.assertEqual(self.sd.servo(i).channel, i)
        with self.assertRaises(IndexError):
            self.sd.servo(0)
        with self.assertRaises(IndexError):
            self.sd.servo(-1)
        with self.assertRaises(IndexError):
            self.sd.servo(9)

    def test_device_no_not_zero(self):
        _ = ServoDevice(1)  # should not connect

    def test_workload_timestamp(self):
        self.assertEqual(self.sd.workload, 42)
        self.assertGreaterEqual(self.sd.timestamp, 0)

    def test_device_no_none(self):
        settings.CREATE_SETTINGS_BACKUP = False
        with self.assertRaises(Exception):
            _ = ServoDevice(None)
        sd = ServoDevice(0)
        sd.servo(1).offset = 3
        sd.saveDeviceToJson("testDeviceNo")
        sd = ServoDevice(None, readFromFile="testDeviceNo.json")
        if os.path.exists("testDeviceNo.json"):
            os.remove("testDeviceNo.json")

    def test_ramp_enabled(self):
        self.sd.servo(2).enableRamp()
        self.assertEqual(self.sd.rampEnabled, 2)
        self.sd.servo(2).disableRamp()
        self.assertEqual(self.sd.rampEnabled, 0)


class TestJson(TestServoDeviceTemplate):
    def test_saveJson(self):
        settings.CREATE_SETTINGS_BACKUP = False
        self.sd.servo(3).inputSensitivity = 1
        self.sd.servo(3).offset = 3.75
        self.sd.servo(8).offset = 8.8882
        self.sd.enableMonitor(3, 3, "output")
        monitors = self.sd.monitors.copy()
        self.sd.saveDeviceToJson("servos.json")
        self.sd.servo(3).offset = 1.2
        self.sd.servo(8).offset = 4.9
        self.sd.enableMonitor(3, 3, "input")
        self.assertEqual(self.sd.servo(3)._state["offset"], 1.2)
        self.sd.loadDeviceFromJson("servos.json")
        self.assertEqual(self.sd.servo(3)._state["offset"], 3.75)
        self.assertEqual(self.sd.servo(3).inputSensitivity, 1)
        self.assertEqual(self.sd.servo(8)._state["offset"], 8.8882)
        self.assertEqual(self.sd.monitors[3 - 1]["card"], "output")
        self.assertEqual(self.sd.monitors, monitors)

        self.sd.deviceNumber = 94
        self.sd.saveDeviceToJson("servos.json")
        sd2 = ServoDevice(settings.DEVICE_NUM, readFromFile="servos.json")
        self.assertEqual(sd2.deviceNumber, settings.DEVICE_NUM)

        self.assertEqual(
            sd2.servo(8)._state["offset"], self.sd.servo(8)._state["offset"]
        )
        if os.path.exists("servos.json"):
            os.remove("servos.json")

    def test_saving_and_loading_with_plant(self):
        settings.CREATE_SETTINGS_BACKUP = False
        tests_dir = os.path.dirname(os.path.abspath(__file__))
        self.sd.servoDesign.integrator(400)
        dc = io.read(f"{tests_dir}/../support_files/fra.csv")
        self.sd.servoDesign.plant = dc
        servoDesign_str = self.sd.servoDesign.__str__()
        plant = self.sd.servoDesign.plant.copy()
        self.sd.saveDeviceToJson("sd.json")
        self.assertEqual(len(plant), len(self.sd.servoDesign.plant))
        self.sd._servoDesign = None
        self.sd.loadDeviceFromJson("sd.json")
        self.assertEqual(servoDesign_str, self.sd.servoDesign.__str__())
        if os.path.exists("sd.json"):
            os.remove("sd.json")

    def test_backupSettingsFile(self):
        with TemporaryDirectory() as tmpdir:
            savefile = "{}/sd.json".format(tmpdir)
            self.assertEqual(len(os.listdir(tmpdir)), 0)
            settings.CREATE_SETTINGS_BACKUP = False
            # First saving
            self.sd.saveDeviceToJson(savefile)
            # manual backup
            self.sd._backupSettingsFile(savefile)
            self.assertEqual(len(os.listdir(tmpdir)), 2)
            # Backup should not be created
            self.sd.saveDeviceToJson(savefile)
            self.assertEqual(len(os.listdir(tmpdir)), 2)
            # Now it should be created
            settings.CREATE_SETTINGS_BACKUP = True
            assert settings.CREATE_SETTINGS_BACKUP
            sleep(1)
            self.sd.saveDeviceToJson(savefile)
            self.assertEqual(len(os.listdir(tmpdir)), 3)

            # Test it will not overwrite an existing backup file
            settings.BACKUP_SUBSTRING = "will_fail"
            self.sd.saveDeviceToJson(savefile)
            with self.assertRaises((IOError, OSError)):
                self.sd.saveDeviceToJson(savefile)
            self.sd._backupSettingsFile(
                "demokratieverständnis"
            )  # should not do anything

    def test_add_new_servo_with_saved_settings(self):
        settings.CREATE_SETTINGS_BACKUP = False
        savepath = "testing.json"
        sd = ServoDevice(settings.DEVICE_NUM)
        for i in [1, 3]:
            self.assertIsInstance(sd.servo(i), Servo)
        sd.saveDeviceToJson(savepath)
        # Add Servos
        sd = ServoDevice(settings.DEVICE_NUM, readFromFile=savepath)
        for i in range(1, 5):
            self.assertIsInstance(sd.servo(i), Servo)
        if os.path.exists(savepath):
            os.remove(savepath)

    def test_save_load_with_servo_variation(self):
        settings.CREATE_SETTINGS_BACKUP = False
        # first, start with low number of servos
        settings.NUMBER_OF_SERVOS = 3
        settings.NUMBER_OF_MONITORS = 4
        dev = ServoDevice(deviceNumber=settings.DEVICE_NUM)
        SERVO = dev.servo
        # add some settings
        SERVO(3).name = "test123"
        SERVO(3).offset = -1
        SERVO(3).gain = 0.04
        dev.enableMonitor(4, 3, "aux")
        # save it
        dev.saveDeviceToJson(filename="testsomesaving123")
        # now increase number of servos
        settings.NUMBER_OF_SERVOS = 5
        settings.NUMBER_OF_MONITORS = 6
        dev = ServoDevice(
            deviceNumber=settings.DEVICE_NUM, readFromFile="testsomesaving123.json"
        )
        SERVO = dev.servo
        # check that everything is still there
        self.assertEqual(SERVO(3).name, "test123")
        self.assertAlmostEqual(SERVO(3).offset, -1, places=3)
        self.assertEqual(SERVO(3).gain, 0.04)
        self.assertEqual(dev.monitors[3]["servo"], 3)
        # make sure new servos exist in default state
        self.assertEqual(SERVO(5).name, "Servo 5")
        self.assertAlmostEqual(SERVO(5).offset, 0, places=3)
        # set some new values and save them
        SERVO(5).name = "delete me"
        SERVO(5).offset = 4
        dev.enableMonitor(6, 5, "input")
        dev.saveDeviceToJson(filename="testsomesaving123")  # overwrite
        dev.saveDeviceToJson(filename="testmoresaving234")  # new save
        # now reduce number of servos again and create new device
        settings.NUMBER_OF_SERVOS = 3
        settings.NUMBER_OF_MONITORS = 4
        dev = ServoDevice(
            deviceNumber=settings.DEVICE_NUM, readFromFile="testmoresaving234.json"
        )
        self.assertEqual(SERVO(3).name, "test123")
        self.assertAlmostEqual(SERVO(3).offset, -1, places=3)
        self.assertEqual(SERVO(3).gain, 0.04)
        self.assertEqual(dev.monitors[3]["servo"], 3)
        # make sure servos previously set are not loaded
        with self.assertRaises(IndexError):
            SERVO(5).offset = 1
        with self.assertRaises(IndexError):
            SERVO(5).name = "I should not be here"
        # same stuff just for the overwritten save
        settings.NUMBER_OF_SERVOS = 3
        settings.NUMBER_OF_MONITORS = 4
        dev = ServoDevice(
            deviceNumber=settings.DEVICE_NUM, readFromFile="testsomesaving123.json"
        )
        self.assertEqual(SERVO(3).name, "test123")
        self.assertAlmostEqual(SERVO(3).offset, -1, places=3)
        self.assertEqual(SERVO(3).gain, 0.04)
        self.assertEqual(dev.monitors[3]["servo"], 3)
        # make sure servos previously set are not loaded
        with self.assertRaises(IndexError):
            SERVO(5).offset = 1
        with self.assertRaises(IndexError):
            SERVO(5).name = "I should not be here"

        if os.path.exists("testsomesaving123.json"):
            os.remove("testsomesaving123.json")
        if os.path.exists("testmoresaving234.json"):
            os.remove("testmoresaving234.json")
        # ensure this does not interfere with other tests by resetting settings changes
        settings.NUMBER_OF_SERVOS = 8
        settings.NUMBER_OF_MONITORS = 8

    def test_monitors_save_load(self):
        settings.CREATE_SETTINGS_BACKUP = False
        sd = ServoDevice(0)
        sd.enableMonitor(1, 1, "input")
        sd.enableMonitor(1, 2, "ttl")
        sd.enableMonitor(3, 1, "aux")
        old = sd.monitors
        sd.saveDeviceToJson("monitortest")
        sd = ServoDevice(0, readFromFile="monitortest.json")
        self.assertEqual(sd.monitors, old)
        if os.path.exists("monitortest.json"):
            os.remove("monitortest.json")


class TestMonitors(TestServoDeviceTemplate):
    def test_adwin_monitors(self):
        sd = ServoDevice(0)
        sd.enableMonitor(1, 2, "aux")
        self.assertEqual(sd._monitors[0], {"servo": 2, "card": "aux"})
        sd.enableMonitor(3, 5, "ttl")
        self.assertEqual(sd._monitors[2], {"servo": 5, "card": "ttl"})
        sd.disableMonitor(1)
        self.assertIsNone(sd._monitors[0])
        with self.assertRaises(IndexError):
            sd.enableMonitor(12, 2, "aux")
        with self.assertRaises(IndexError):
            sd.disableMonitor(12)
        with self.assertRaises(ValueError):
            sd.enableMonitor(2, None, "input")
        with self.assertRaises(IndexError):
            sd.enableMonitor(2, 10, "output")
        with self.assertRaises(ValueError):
            sd.enableMonitor(2, 2, None)

    def test_monitors(self):
        self.sd.monitors = [None] * settings.NUMBER_OF_MONITORS


class TestAutolock(TestServoDeviceTemplate):
    def test_lcr_gcr(self):
        settings.NUMBER_OF_SERVOS = 3
        sd = ServoDevice(0)
        self.assertEqual(sd._lockControlRegister(), 0)
        sd.servo(1).lockSearch = 1
        sd.servo(1).relock = 1
        self.assertEqual(sd._lockControlRegister(), 5)
        self.assertEqual(
            sd._greaterControlRegister(), 7
        )  # for 3 channels, defaults to 0b111
        settings.NUMBER_OF_SERVOS = 8
