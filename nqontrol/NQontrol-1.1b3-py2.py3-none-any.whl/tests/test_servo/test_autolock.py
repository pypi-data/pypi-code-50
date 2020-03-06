import logging as log
from time import sleep

import numpy as np

from nqontrol.general import helpers, settings
from nqontrol.general.errors import UserInputError

from .test_servo import TestServoTemplate

log.basicConfig(
    format="%(levelname)s: %(module)s.%(funcName)s: %(message)s", level="INFO"
)

settings.NUMBER_OF_SERVOS = 8
settings.NUMBER_OF_MONITORS = 8


class TestServoAutolock(TestServoTemplate):
    def test_lock_getters_and_setters(self):
        self.s.lockSearch = 0
        with self.assertRaises(TypeError):
            self.s.lockSearch = "Hello there!"
        with self.assertRaises(TypeError):
            self.s.locked = "General Kenobi"
        with self.assertRaises(TypeError):
            self.s.relock = "A surprise to be sure"
        with self.assertRaises(TypeError):
            self.s.lockGreater = "But a welcome one"
        self.assertEqual(0, self.s.lockSearch)
        with self.assertRaises(TypeError):
            self.s.lockThreshold = "wrong type"
        with self.assertRaises(ValueError):
            self.s.lockThreshold = 11
        with self.assertRaises(TypeError):
            self.s.lockSearchRange = "wrong type"
        with self.assertRaises(TypeError):
            self.s.lockSearchRange = -12
        with self.assertRaises(ValueError):
            self.s.lockSearchRange = [1, 2, 3]
        with self.assertRaises(TypeError):
            self.s.lockSearchRange = [1, "something"]
        with self.assertRaises(TypeError):
            self.s.lockSearchRange = ["something", 1]
        with self.assertRaises(ValueError):
            self.s.lockSearchRange = [-12, 3]
        with self.assertRaises(ValueError):
            self.s.lockSearchRange = [1, 14]
        with self.assertRaises(ValueError):
            self.s.lockSearchRange = [5, -3]
        with self.assertRaises(ValueError):
            self.s.lockSearchRange = [-4, -7]
        self.s.lockSearchRange = [0, 3]
        testrange = self.s.lockSearchRange
        self.assertAlmostEqual(testrange[0], 0, places=3)
        self.assertAlmostEqual(testrange[1], 3, places=3)
        self.assertAlmostEqual(self.s.lockSearchMax, 3, places=3)
        self.assertAlmostEqual(self.s.lockSearchMin, 0, places=3)
        self.s.lockThreshold = 7
        self.s.lockGreater = 1
        self.s.lockSearch = 1
        # let's ensure that lock will still be running after changing range
        # also minimum value should be smaller than maximum value
        self.assertTrue(self.s.lockSearch)
        self.s.lockSearchRange = [2, 4]
        self.assertTrue(self.s.lockSearch)
        self.assertAlmostEqual(self.s.lockSearchMin, 2, places=3)
        # mroe weird shennigans that really should not occur in use case
        self.s.relock = 1
        self.assertTrue(self.s.relock)
        self.s.lockThreshold = 10
        self.s.lockGreater = 0
        self.s.lockSearch = 0
        self.s.locked = True
        self.assertTrue(self.s.locked)
        self.s.lockGreater = False
        self.assertFalse(self.s.lockGreater)
        self.s.lockGreater = 1
        self.assertTrue(self.s.lockGreater)

    def test_servo_autolock(self):
        # set everything to off
        self.s.lockSearch = 0
        self.s.locked = 0
        self.assertEqual(self.s.lockSearch, self.s.locked)

        # settings so that lock should always find a lock point
        self.s.lockThreshold = 10
        self.s.lockSearchRange = [-10, 3]
        self.s.relock = 0
        self.s.lockGreater = 0
        log.debug(f"Lock control register   {bin(self.sd._lockControlRegister())}")

        self.s.lockSearch = 1
        sleep(0.1)
        # should have found the lock right away, has to turn off lock mode and turn on locked state
        self.assertTrue(self.s.locked)

        self.assertFalse(self.s.lockSearch)
        self.s.lockGreater = 1
        sleep(0.1)
        self.assertFalse(self.s.locked)

    def test_lock_searches_in_correct_range(self):
        self.s.locked = 0
        self.s.relock = 1
        # we'll start this before, to make sure that resetting the range does not result in the lock iterator being out of bounds!
        # this might happen, for example, if the new range is smalle than the current one and the search is still active
        self.s.lockSearch = 1
        self.s.lockGreater = True
        self.s.lockThreshold = 8
        self.s.lockSearchRange = [3, 5]
        sleep(0.1)
        # let's test this a couple of times
        for _ in range(20):
            self.assertGreater(self.s._lockIter(), 3)
            self.assertLess(self.s._lockIter(), 5)
        self.s.lockSearchRange = [-6, -4]
        sleep(0.1)
        for _ in range(20):
            self.assertGreater(self.s._lockIter(), -6)
            self.assertLess(self.s._lockIter(), -4)

    def test_lock_control_register(self):
        lcr1 = self.sd._lockControlRegister()
        log.debug(f"The old register for debugging: {bin(lcr1)}")
        self.s.lockSearch = 0
        self.s.relock = 0
        self.s.locked = 0
        self.s.lockGreater = 0
        lcr2 = self.sd._lockControlRegister()
        gcr = self.sd._greaterControlRegister()
        log.debug(f"lcr2 lock register for debugging: {bin(lcr2)}")
        bitoffset = (self.s._channel - 1) * 3
        lock = helpers.readBit(lcr2, bitoffset)
        locked = helpers.readBit(lcr2, bitoffset + 1)
        relock = helpers.readBit(lcr2, bitoffset + 2)
        greater = helpers.readBit(gcr, self.s._channel - 1)
        self.assertEqual(lock, 0)
        self.assertEqual(locked, 0)
        self.assertEqual(relock, 0)
        self.assertEqual(greater, 0)
        # now the other way round
        # first, ensure a lock wont be found
        self.s.lockThreshold = 9
        self.s.lockGreater = 1
        self.s.relock = 1
        self.s.lockSearch = 1
        lcr3 = self.sd._lockControlRegister()
        gcr = self.sd._greaterControlRegister()
        log.debug(f"lcr3 lock register for debugging: {bin(lcr3)}")
        lock = helpers.readBit(lcr3, bitoffset)
        locked = helpers.readBit(lcr3, bitoffset + 1)
        relock = helpers.readBit(lcr3, bitoffset + 2)
        greater = helpers.readBit(gcr, self.s._channel - 1)
        self.assertTrue(lock)
        self.assertFalse(locked)
        self.assertTrue(relock)
        self.assertTrue(greater)
        # let's have a lock found
        self.s.lockThreshold = 10
        self.s.lockGreater = 0
        sleep(0.1)
        lcr4 = self.sd._lockControlRegister()
        gcr = self.sd._greaterControlRegister()
        log.warning(
            f"lcr4 lock register for debugging: lcr {bin(lcr4)} gcr {bin(gcr)}, offset {bitoffset}"
        )
        lock = helpers.readBit(lcr4, bitoffset)
        locked = helpers.readBit(lcr4, bitoffset + 1)
        relock = helpers.readBit(lcr4, bitoffset + 2)
        greater = helpers.readBit(gcr, self.s._channel - 1)
        # lock should now be off if testing on a real device
        self.assertFalse(lock)
        self.assertTrue(locked)
        self.assertFalse(greater)
        self.assertTrue(relock)

    def test_lock_disables_input_output(self):
        # start infinite lock process
        self.s.lockThreshold = 10
        self.s.lockGreater = 1
        self.s.lockSearch = 1
        self.assertFalse(self.s.inputSw)
        self.assertFalse(self.s.outputSw)
        self.assertFalse(self.s.auxSw)
        sleep(0.1)
        self.s.lockGreater = 0
        sleep(0.1)
        self.assertTrue(self.s.locked)
        self.assertTrue(self.s.inputSw)
        self.assertTrue(self.s.outputSw)

    def test_lock_search_state(self):
        # enable infinite lock
        self.s.lockThreshold = 10
        self.s.lockGreater = 1
        self.s.lockSearch = 1
        sleep(0.1)
        self.assertTrue(self.s.lockSearch)

    def test_lock_found_state(self):
        self.s.lockThreshold = -8
        self.s.lockGreater = True
        self.s.lockSearch = 1
        sleep(0.1)
        self.assertTrue(self.s.locked)

    def test_lock_relock_starts_search(self):
        # infinite search
        self.s.lockThreshold = 8
        self.s.lockGreater = True
        self.s.locked = False
        self.s.relock = 1
        self.s.lockSearch = 1
        sleep(0.1)
        self.assertTrue(self.s.lockSearch)
        self.s.lockGreater = False
        sleep(0.1)
        self.assertFalse(self.s.lockSearch)
        self.assertTrue(self.s.locked)
        self.assertTrue(self.s.relock)
        self.s.lockGreater = True
        sleep(0.1)
        # this is the relevant part
        self.assertTrue(self.s.lockSearch)
        self.assertFalse(self.s.locked)
        self.assertTrue(self.s.relock)

    def test_lock_output_range(self):
        self.s.gain = 1
        self.s.offset = 0
        # this is to make sure that the output actually remains where it finds the lock and doesnt start correcting from 0 volt again
        # let's set up an infinite search with a small possible area for the output
        self.s.lockSearchRange = [7, 8]
        self.s.lockThreshold = 8  # some arbitrary high value, no correlation with the searchrange (we expect to test with white noise)
        self.s.lockGreater = True
        self.s.relock = 0
        # start search
        self.s.lockSearch = True
        sleep(0.1)
        # we expect it to be in search state
        self.assertTrue(self.s.lockSearch)
        self.assertFalse(self.s.locked)
        self.assertTrue(7 < self.s._lockIter() < 8)
        log.debug(f"iter {self.s._lockIter()}")
        log.debug(f"output {self.s._testLockOutput()}")
        self.assertEqual(
            self.s.filters,
            [
                [1.0, 0.0, 0.0, 0.0, 0.0],
                [1.0, 0.0, 0.0, 0.0, 0.0],
                [1.0, 0.0, 0.0, 0.0, 0.0],
                [1.0, 0.0, 0.0, 0.0, 0.0],
                [1.0, 0.0, 0.0, 0.0, 0.0],
            ],
        )

        # switch to Greater = False, should "find" lock immediately
        self.s.lockGreater = False
        # let's see what happens to the output
        data = self.s.takeData()
        self.assertFalse(self.s.lockSearch)
        self.assertTrue(self.s.locked)
        data = data["output"].to_numpy()
        log.warning(data)
        self.assertTrue(7 < self.s._lockIter() < 8)
        log.debug(f"iter {self.s._lockIter()}")
        log.debug(f"output {self.s._testLockOutput()}")
        # output should roughly stay within the same range as set for the search
        self.assertTrue(np.all((data > 6) & (data < 9)))

    def test_lock_off_state(self):
        self.s.lockThreshold = 8
        self.s.lockGreater = 1
        self.s.lockSearch = 1
        sleep(0.1)
        self.s.lockSearch = 0
        self.assertFalse(self.s.lockSearch)
        self.assertFalse(self.s.locked)

    def test_lock_disables_ramp(self):
        self.s.enableRamp()
        self.s.lockSearch = 1
        sleep(1e-3)
        self.assertFalse(self.s.rampEnabled)
        with self.assertRaises(UserInputError):
            self.s.enableRamp()
        self.s.lockThreshold = 9
        self.s.lockGreater = 0
        self.assertTrue(self.s.locked)
        with self.assertRaises(UserInputError):
            self.s.enableRamp()

    def test_autolock_commandline_usage(self):
        with self.assertRaises(TypeError):
            self.s.autolock("baby yoda")
        with self.assertRaises(TypeError):
            self.s.autolock(relock="luke")
        with self.assertRaises(TypeError):
            self.s.autolock(greater="rey")
        with self.assertRaises(TypeError):
            self.s.autolock(threshold="jar jar")
        with self.assertRaises(TypeError):
            self.s.autolock(searchrange="harrypotter")
        with self.assertRaises(ValueError):
            self.s.autolock(threshold=-12)
        with self.assertRaises(ValueError):
            self.s.autolock(searchrange=[-11, 3])
        with self.assertRaises(ValueError):
            self.s.autolock(searchrange=[3, 15])
        with self.assertRaises(ValueError):
            self.s.autolock(searchrange=[])

        self.assertIn("hello there", self.s.autolock(relock=True, kenobi="hello there"))
        self.assertIn("no effect", self.s.autolock(relcok=False))
        self.assertIn("No options changed", self.s.autolock(election="establishment"))
        self.s.autolock(False)
        self.assertFalse(self.s.lockSearch)

        self.assertNotIn(
            "No options changed.",
            self.s.autolock(
                relock=True, greater=False, searchrange=[2, 4], treshold=-0.4
            ),
        )

        self.assertNotIn("Additional arguments", self.s.autolock(greater=True))

        self.assertIn("threshold", self.s.autolock(threshold=3))
