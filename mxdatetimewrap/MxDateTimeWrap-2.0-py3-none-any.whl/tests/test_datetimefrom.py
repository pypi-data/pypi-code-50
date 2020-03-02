import unittest
import datetime

from mx.DateTime import DateTimeFrom, DateTime


class DateTimeTests(unittest.TestCase):
    comp_d = DateTime(2014, 11, 10)
    comp_dt = DateTime(2014, 11, 10, 18, 30)

    def testIS(self):
        tc = DateTimeFrom('10.11.2014')
        self.assertEqual(tc, self.comp_d)
        tc = DateTimeFrom('10.11.2014 18:30')
        self.assertEqual(tc, self.comp_dt)
        tc = DateTimeFrom('10.11.2014 18:30:00')
        self.assertEqual(tc, self.comp_dt)

    def testISO(self):
        tc = DateTimeFrom('2014-11-10')
        self.assertEqual(tc, self.comp_d)
        tc = DateTimeFrom('2014-11-10 18:30')
        self.assertEqual(tc, self.comp_dt)
        tc = DateTimeFrom('2014-11-10 18:30:00')
        self.assertEqual(tc, self.comp_dt)

    def testUS(self):
        tc = DateTimeFrom('11/10/2014')
        self.assertEqual(tc, self.comp_d)
        tc = DateTimeFrom('11/10/2014 06:30 PM')
        self.assertEqual(tc, self.comp_dt)
        tc = DateTimeFrom('11/10/2014 06:30:00 PM')
        self.assertEqual(tc, self.comp_dt)

    def testTime(self):
        tc = DateTimeFrom(DateTime(2014, 1, 2, 18, 30, 20).time)
        self.assertEqual(tc.hour, 18)
        self.assertEqual(tc.minute, 30)
        self.assertEqual(tc.second, 20)
        tc = DateTimeFrom(23*60*60+59*60)
        self.assertEqual(tc.year, 1970)
        self.assertEqual(tc.hour, 23)
        self.assertEqual(tc.minute, 59)
        self.assertEqual(tc.second, 0)

    def testDate(self):
        tc = DateTimeFrom(DateTime(2014, 1, 2, 18, 30, 20).date)
        self.assertEqual(tc.year, 2014)
        self.assertEqual(tc.month, 1)
        self.assertEqual(tc.day, 2)

    def testCreateFromDateTime(self):
        d = datetime.datetime(2015, 1, 1)
        dmx = DateTimeFrom(d)
        self.assertEqual(d, dmx)
        dmx = DateTimeFrom(dmx)
        self.assertEqual(d, dmx)
        dmx2 = DateTimeFrom(d.date())
        self.assertEqual(dmx, dmx2)

    def testCreateFromArgs(self):
        d1 = DateTime(2015, 1, 1)
        d2 = DateTimeFrom(2015, 1, 1)
        self.assertEqual(d1, d2)
        d2 = DateTimeFrom(year=2015, day=1, month=1)
        self.assertEqual(d1, d2)

    def testCreateFromSecond(self):
        d1 = DateTime(1970, 1, 1, 0, 0, 1)
        d2 = DateTimeFrom(1)
        self.assertEqual(d1, d2)
        d1 = DateTime(1970, 1, 1, 0, 0, 59)
        d2 = DateTimeFrom(59)
        self.assertEqual(d1, d2)

    def testArgsAndKwargs(self):
        with self.assertRaises(TypeError):
            DateTimeFrom(2014, 1, 1, day=1)

    def testUnknownString(self):
        with self.assertRaises(ValueError):
            DateTimeFrom('2015-2-29')

    def testCreateWithTime(self):
        d1 = DateTimeFrom(datetime.time(7, 0))
        d2 = DateTime(1, 1, 1, 7)
        self.assertEqual(d1, d2)
