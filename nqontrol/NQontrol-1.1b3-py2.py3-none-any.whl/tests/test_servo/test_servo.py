import logging as log
import unittest

import matplotlib.pyplot as plt

from nqontrol import Servo, ServoDevice
from nqontrol.general import helpers, settings
from nqontrol.general.errors import ConfigurationError, DeviceError, UserInputError
from nqontrol.general.mockAdwin import MockADwin

log.basicConfig(
    format="%(levelname)s: %(module)s.%(funcName)s: %(message)s", level="INFO"
)

settings.NUMBER_OF_SERVOS = 8
settings.NUMBER_OF_MONITORS = 8


class TestServoTemplate(unittest.TestCase):
    def tearDown(self) -> None:
        figs = list(map(plt.figure, plt.get_fignums()))
        for fig in figs:
            plt.close(fig)

    def setUp(self):
        self.sd = ServoDevice(settings.DEVICE_NUM)
        self.sd.reboot()
        self.testchannel = 2
        self.s = self.sd.servo(self.testchannel)
        import nqontrol

        log.warning("nqontrol path: {}".format(nqontrol.__path__[0]))
        if "site-packages" in nqontrol.__path__[0]:
            raise Exception("Not running the development code!!!")
