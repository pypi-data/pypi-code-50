import unittest

import datetime
import copy
import sys

from mx.DateTime import DateTime, now, DateTimeType, DateTimeDelta


class DateTimeTests(unittest.TestCase):
    def testDateSet(self):
        tc = DateTime(2004, 12, 13)
        rc = datetime.datetime(2004, 12, 13)
        self.assertTrue(tc.year == rc.year)
        self.assertTrue(tc.month == rc.month)
        self.assertTrue(tc.day == rc.day)

        tc = DateTime(2014, 8, 14)
        rc = datetime.datetime(2014, 8, 14)
        self.assertTrue(tc.year == rc.year)
        self.assertTrue(tc.month == rc.month)
        self.assertTrue(tc.day == rc.day)

    def testDateTimeSet(self):
        tc = DateTime(2011, 2, 28, 16, 44, 39)
        rc = datetime.datetime(2011, 2, 28, 16, 44, 39)
        self.assertTrue(tc.year == rc.year)
        self.assertTrue(tc.month == rc.month)
        self.assertTrue(tc.day == rc.day)
        self.assertTrue(tc.hour == rc.hour)
        self.assertTrue(tc.minute == rc.minute)
        self.assertTrue(tc.second == rc.second)

    def testDTZero(self):
        tc = DateTime(0)
        self.assertTrue(0 <= tc.year <= 1)
        self.assertTrue(tc.month == 1)
        self.assertTrue(tc.day == 1)
        self.assertTrue(tc.hour == 0)
        self.assertTrue(tc.minute == 0)
        self.assertTrue(tc.second == 0.0)

    def testIntegerAdd(self):
        tc = DateTime(2014, 11, 24)
        oc = DateTime(2014, 11, 26)
        self.assertEqual(tc + 2, oc)
        self.assertEqual(tc, oc - 2)
        self.assertTrue(isinstance(oc + 1, DateTimeType))
        self.assertTrue(isinstance(oc - 1, DateTimeType))

    def testSubtract(self):
        tc = DateTime(2014, 11, 24)
        oc = DateTime(2014, 11, 22)
        self.assertEqual(tc - datetime.timedelta(days=2), oc)
        self.assertEqual(tc - oc, DateTimeDelta(2))

        def fu():
            return tc - 'minus'
        self.assertRaises(TypeError, fu)
        # self.assertEqual(tc - 'minus', DateTimeDelta(2))

    def testDateSplit(self):
        tc = DateTime(2015, 2, 15)
        tc_date = tc.date
        self.assertTrue(hasattr(tc_date, 'split'))
        y, m, d = tc_date.split('-')
        self.assertEqual(y, '2015')
        self.assertEqual(m, '02')
        self.assertEqual(d, '15')

    def testCopy(self):
        tc = now()
        oc = copy.deepcopy(tc)
        self.assertEqual(tc, oc)

    def testComparisonSimple(self):
        a = DateTime(2015, 1, 15)
        b = DateTime(2015, 2, 15)
        self.assertLess(a, b)
        self.assertLessEqual(a, b)
        self.assertLessEqual(a, a)
        self.assertGreater(b, a)
        self.assertGreaterEqual(b, a)
        self.assertGreaterEqual(b, b)

    def testComparisonComplex(self):
        a = DateTime(2015, 1, 15)
        self.assertGreaterEqual(a, None)
        self.assertGreaterEqual(a, 0)

        self.assertGreater(a, None)
        self.assertGreater(a, 0)

        self.assertLess(None, a)
        self.assertLess(0, a)
        self.assertLessEqual(None, a)
        self.assertLessEqual(0, a)

        self.assertFalse(a <= None)
        self.assertFalse(None >= a)

        self.assertFalse(a <= a-1)
        self.assertFalse(a-1 >= a)
        self.assertTrue(a >= 1)
        self.assertTrue(1 <= a)
        self.assertFalse(a <= 1)
        self.assertFalse(1 >= a)

        inta = int(a)
        # self.assertGreaterEqual(a, inta)
        # self.assertEqual(a, inta)
        # self.assertLessEqual(a, inta)
        # self.assertLessEqual(a, inta+1)
        self.assertGreaterEqual(int(a), inta)
        self.assertEqual(int(a), inta)
        self.assertLessEqual(int(a), inta)
        self.assertLessEqual(int(a), inta+1)

    def testTuple(self):
        dow = 3
        doy = 1
        expected = (
            2015, 1, 1,
            0, 0, 0,
            dow, doy)
        a = DateTime(2015, 1, 1)
        self.assertEqual(expected, a.tuple()[:-1])

        expected = (
            2015, 1, 1,
            16, 30, 45,
            dow, doy)
        a = DateTime(2015, 1, 1, 16, 30, 45)
        self.assertEqual(expected, a.tuple()[:-1])

        expected = (
            2015, 1, 2,
            16, 30, 45,
            dow+1, doy+1)
        a = DateTime(2015, 1, 2, 16, 30, 45)
        self.assertEqual(expected, a.tuple()[:-1])

    def testDayOfWeek(self):
        d = now()
        self.assertEqual(d.day_of_week, d.weekday())

    def testDaysInMonth(self):
        d = DateTime(2015, 6, 1)
        self.assertEqual(d.days_in_month, 30)
        d = DateTime(2015, 2, 1)
        self.assertEqual(d.days_in_month, 28)
        d = DateTime(1988, 2, 1)
        self.assertEqual(d.days_in_month, 29)

    def testIsoWeek(self):
        d = DateTime(2015, 6, 1)
        self.assertEqual(d.iso_week, (2015, 23, 1))
        d = DateTime(2015, 1, 1)
        self.assertEqual(d.iso_week, (2015, 1, 4))
        d = DateTime(2015, 12, 30)
        self.assertEqual(d.iso_week, (2015, 53, 3))

    def testAbsDays(self):
        d = DateTime(2015, 1, 1, 23, 31, 29)
        if sys.version_info[0] == 3:
            self.assertAlmostEqual(d.absdays, 735599.3751967592)
        else:
            self.assertAlmostEqual(d.absdays, 735598.98019675922)
