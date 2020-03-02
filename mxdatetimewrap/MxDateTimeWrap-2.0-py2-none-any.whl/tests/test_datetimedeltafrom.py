import unittest

from mx.DateTime import DateTimeDeltaFrom, DateTime


class DateTimeTests(unittest.TestCase):
    def testInteger(self):
        tc = DateTimeDeltaFrom(45)
        self.assertEqual(tc.hours, 0.0125)
        self.assertEqual(tc.minutes, 0.75)
        self.assertEqual(tc.seconds, 45)

        tc = DateTimeDeltaFrom(30 * 60)
        self.assertEqual(tc.hours, 0.5)
        self.assertEqual(tc.minutes, 30)
        self.assertEqual(tc.seconds, 30 * 60)

        tc = DateTimeDeltaFrom(30 * 60 * 60)
        self.assertEqual(tc.hours, 30)
        self.assertEqual(tc.minutes, 30 * 60)
        self.assertEqual(tc.seconds, 30 * 60 * 60)

    def testString(self):
        tc = DateTimeDeltaFrom("07:54")
        self.assertEqual(tc.hours, 7.9)
        self.assertEqual(tc.minutes, 7 * 60 + 54)

        tc = DateTimeDeltaFrom('08:30:30')
        # self.assertEqual(tc.hours, 8.5)
        self.assertAlmostEqual(
            tc.hours, 8 + 30 / 60.0 + 30 / (60.0 * 60.0)
        )
        self.assertEqual(tc.minutes, 8 * 60 + 30 + 30 / 60.0)
        self.assertEqual(tc.seconds, 8 * 60 * 60 + 30 * 60 + 30)

    def testStringCommas(self):
        tc = DateTimeDeltaFrom('3.25:0')
        self.assertEqual(tc.hours, 3.25)
        self.assertEqual(tc.minutes, 3 * 60 + 15)

        tc = DateTimeDeltaFrom('1.25:45:60')
        self.assertEqual(tc.hours, 2 + 1/60.0)
        self.assertEqual(tc.minutes, 121)
        self.assertEqual(tc.seconds, 121 * 60)

    def testStringNegative(self):
        tc = DateTimeDeltaFrom('-08:00')
        base = DateTime(2014, 11, 24, 16, 30, 0)
        summed = base + tc
        self.assertEqual(summed.hour, 8)
        self.assertEqual(summed.minute, 30)

        tc = DateTimeDeltaFrom('-03:30')
        self.assertEqual(tc.hours, -3.5)
        self.assertEqual(tc.minutes, -(60 * 3 + 30))

    def testKeywords(self):
        tc = DateTimeDeltaFrom(
            hours=3,
            minutes=30,
            seconds=30
        )
        self.assertEqual(tc.hours, 3.5 + 0.5 / 60.0)
        self.assertEqual(tc.minutes, 3 * 60 + 30.5)

    def testFromTime(self):
        tc = DateTimeDeltaFrom(DateTime(2014, 1, 2, 18, 30, 20).time)
        self.assertEqual(tc.hour, 18)
        self.assertEqual(tc.minute, 30)
        self.assertEqual(tc.second, 20)

    def testEmptyString(self):
        tc = DateTimeDeltaFrom('')
        self.assertEqual(tc.hour, 0)
        self.assertEqual(tc.minute, 0)

    def testSubtractReturnsMX(self):
        a = DateTimeDeltaFrom("24:00")
        b = DateTimeDeltaFrom("20:00")
        res = a - b
        self.assertTrue(hasattr(res, 'hours'))
        self.assertEqual(res.hours, 4)
        a = DateTimeDeltaFrom("24:00")
        b = DateTimeDeltaFrom("20:30")
        res = a - b
        self.assertTrue(hasattr(res, 'hours'))
        self.assertEqual(res.hours, 3.5)

    def testMissingArgs(self):
        tc = DateTimeDeltaFrom(':')
        self.assertEqual(tc.hour, 0)
        self.assertEqual(tc.minute, 0)
        self.assertEqual(tc.second, 0)
        tc = DateTimeDeltaFrom(':00')
        self.assertEqual(tc.hour, 0)
        self.assertEqual(tc.minute, 0)
        self.assertEqual(tc.second, 0)
        tc = DateTimeDeltaFrom('00:')
        self.assertEqual(tc.hour, 0)
        self.assertEqual(tc.minute, 0)
        self.assertEqual(tc.second, 0)
