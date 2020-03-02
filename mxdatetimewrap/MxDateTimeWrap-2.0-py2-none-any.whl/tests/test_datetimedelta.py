import unittest

from mx.DateTime import DateTimeDelta, DateTime, DateTimeDeltaFrom


class DateTimeTests(unittest.TestCase):
    def testDays(self):
        for t in (-1, 0, 1):
            tc = DateTimeDelta(t)
            self.assertTrue(tc.days == t)

    def testHours(self):
        for t in (-1, 0, 1):
            tc = DateTimeDelta(0, t)
            self.assertTrue(tc.hours == t)

    def testMinutes(self):
        for t in (-1, 0, 1):
            tc = DateTimeDelta(0, 0, t)
            self.assertTrue(tc.minutes == t)

    def testSeconds(self):
        for t in (-1, 0, 1):
            tc = DateTimeDelta(0, 0, 0, t)
            self.assertTrue(tc.seconds == t)

    def testAdd(self):
        base = DateTime(2012, 6, 15, 12, 30, 30)
        for t in (-1, 0, 1):
            for i, kw in enumerate(('day', 'hour', 'minute', 'second')):
                args = [0] * i + [t]
                delta = DateTimeDelta(*args)
                res = getattr(base + delta, kw)
                expected = getattr(base, kw) + t
                self.assertTrue(res == expected)

    def testCompare(self):
        morning = DateTimeDelta(0, 8)
        noon = DateTimeDelta(0, 12)
        afternoon = DateTimeDelta(0, 16)
        minus = DateTimeDelta(0, -8)
        noon_dt = DateTime(2014, 12, 4, 12, 0, 0)
        self.assertTrue(morning < afternoon)
        self.assertTrue(afternoon > morning)
        self.assertTrue(afternoon >= morning)
        self.assertTrue(afternoon >= afternoon)
        self.assertTrue(morning < noon_dt)
        self.assertTrue(noon_dt > morning)
        self.assertTrue(noon_dt > minus)
        self.assertFalse(noon_dt == minus)
        self.assertTrue(afternoon < noon_dt)
        self.assertNotEqual(noon, noon_dt)

    def testStrfTime(self):
        t = DateTimeDelta(5, 23, 59, 30)
        self.assertEqual(
            t.strftime('%d.%m.%Y %H:%M:%S'), '06.01.1900 23:59:30')
        t = DateTimeDelta(hours=7, minutes=30)
        self.assertEqual(
            t.strftime('%H:%M'),
            '07:30'
        )

    def testAddDeltas(self):
        t = DateTimeDelta(5)
        t2 = DateTimeDelta(5)
        self.assertEqual(t, t2)
        res = t + t2
        self.assertEqual(res.days, 10)
        res = t + 5
        self.assertAlmostEqual(res.days, 5.00005787037037)

    def testSubtractDate(self):
        t = DateTimeDelta(5)
        t2 = DateTime(2015, 5, 15)
        with self.assertRaises(TypeError):
            t - t2

    def testCreateWithArgs(self):
        afternoon = DateTimeDelta(0, 16)
        afternoon1 = DateTimeDeltaFrom(0, 16)
        self.assertEqual(afternoon, afternoon1)
