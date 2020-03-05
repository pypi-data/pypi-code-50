import unittest
import subprocess
import reptimer


class TestTimerMethods(unittest.TestCase):
    def test_timer(self):
        self.assertTrue(reptimer.timer(0))


if __name__ == "__main__":
    unittest.main()
