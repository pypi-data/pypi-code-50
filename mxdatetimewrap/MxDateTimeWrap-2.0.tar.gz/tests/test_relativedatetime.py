# -*- coding: utf-8 -*-
import unittest

from mx.DateTime import RelativeDateTime, DateTime, RelativeDateTimeFrom


class DateTimeTests(unittest.TestCase):
    # 15.6.2014 18:30:30
    t = DateTime(2014, 6, 15, 18, 30, 30)
    # 31.1.2014 18:30:30
    t2 = DateTime(2014, 1, 31, 18, 30, 30)
    # 29.2.2012 18:30:30 - leap year
    t3 = DateTime(2012, 2, 29, 18, 30, 30)

    def testSetDay(self):
        r = RelativeDateTime(day=1)
        res = self.t + r
        expected = DateTime(2014, 6, 1, 18, 30, 30)
        self.assertEqual(res, expected)
        r = RelativeDateTime(day=31)
        expected = DateTime(2014, 7, 1, 18, 30, 30)
        self.assertEqual(self.t + r, expected)

    def testSetMonth(self):
        r = RelativeDateTime(month=3)
        res = self.t + r
        expected = DateTime(2014, 3, 15, 18, 30, 30)
        self.assertEqual(res, expected)

        r = RelativeDateTime(month=2)
        res = self.t2 + r
        # HAHA þið sáuð þetta ekki fyrir! Vei!
        expected = DateTime(2014, 3, 3, 18, 30, 30)
        self.assertEqual(res, expected)

    def testSetYear(self):
        r = RelativeDateTime(year=1988)
        res = self.t + r
        expected = DateTime(1988, 6, 15, 18, 30, 30)
        self.assertEqual(res, expected)

        r = RelativeDateTime(year=2014)
        res = self.t3 + r
        # Þið áttuð ekki séns....
        expected = DateTime(2014, 3, 1, 18, 30, 30)
        self.assertEqual(res, expected)

    def testSetHour(self):
        r = RelativeDateTime(hour=11)
        res = self.t + r
        expected = DateTime(2014, 6, 15, 11, 30, 30)
        self.assertEqual(res, expected)

    def testSetMinute(self):
        r = RelativeDateTime(minute=11)
        res = self.t + r
        expected = DateTime(2014, 6, 15, 18, 11, 30)
        self.assertEqual(res, expected)

    def testSetSecond(self):
        r = RelativeDateTime(second=11)
        res = self.t + r
        expected = DateTime(2014, 6, 15, 18, 30, 11)
        self.assertEqual(res, expected)

    def testGetEndTime(self):
        r = RelativeDateTime(hour=23, minute=59, second=59)
        res = self.t + r
        expected = DateTime(2014, 6, 15, 23, 59, 59)
        self.assertEqual(res, expected)

        r = RelativeDateTime(hour=23, minute=59)
        res = self.t + r
        expected = DateTime(2014, 6, 15, 23, 59, 30)
        self.assertEqual(res, expected)

    def testOverlap(self):
        r = RelativeDateTime(day=40)
        res = self.t + r
        expected = DateTime(2014, 7, 10, 18, 30, 30)
        self.assertEqual(res, expected)

    def testSetFubar1(self):
        r = RelativeDateTime(day=-15)
        res = self.t + r
        # Telur niður frá 30 (30 dagar í júní)
        expected = DateTime(2014, 6, 16, 18, 30, 30)
        self.assertEqual(res, expected)

    def testSetFubar2(self):
        r = RelativeDateTime(day=-20)
        res = self.t + r
        # Telur niður frá 30 (30 dagar í júní)
        expected = DateTime(2014, 6, 11, 18, 30, 30)
        self.assertEqual(res, expected)

    def testSetFubar3(self):
        r = RelativeDateTime(month=-2)
        res = self.t + r
        # 1 væri janúar 2014, -2 er þá auðvitað október 2013 (0 er des)
        expected = DateTime(2013, 10, 15, 18, 30, 30)
        self.assertEqual(res, expected)

    def testSetFubar4(self):
        r = RelativeDateTime(month=0)
        res = self.t + r
        # 1 væri janúar 2014, 0 er þá eðlilega desember 2013
        expected = DateTime(2013, 12, 15, 18, 30, 30)
        self.assertEqual(res, expected)

    def testSetFubar5(self):
        r = RelativeDateTime(day=0)
        res = self.t + r
        # Svipað og að ofan...
        expected = DateTime(2014, 5, 31, 18, 30, 30)
        self.assertEqual(res, expected)

    def testAddYears(self):
        r = RelativeDateTime(years=1)
        res = self.t + r
        expected = DateTime(2015, 6, 15, 18, 30, 30)
        self.assertEqual(res, expected)

        r = RelativeDateTime(years=-1)
        res = self.t + r
        expected = DateTime(2013, 6, 15, 18, 30, 30)
        self.assertEqual(res, expected)

    def testAddMonths(self):
        r = RelativeDateTime(months=1)
        res = self.t + r
        expected = DateTime(2014, 7, 15, 18, 30, 30)
        self.assertEqual(res, expected)

        r = RelativeDateTime(months=-1)
        res = self.t + r
        expected = DateTime(2014, 5, 15, 18, 30, 30)
        self.assertEqual(res, expected)

        r = RelativeDateTime(months=12)
        res = self.t + r
        expected = DateTime(2015, 6, 15, 18, 30, 30)
        self.assertEqual(res, expected)

    def testAddDays(self):
        r = RelativeDateTime(days=1)
        res = self.t + r
        expected = DateTime(2014, 6, 16, 18, 30, 30)
        self.assertEqual(res, expected)

        r = RelativeDateTime(days=-1)
        res = self.t + r
        expected = DateTime(2014, 6, 14, 18, 30, 30)
        self.assertEqual(res, expected)

        r = RelativeDateTime(days=30)
        res = self.t + r
        expected = DateTime(2014, 7, 15, 18, 30, 30)
        self.assertEqual(res, expected)

    def testAddHours(self):
        r = RelativeDateTime(hours=1)
        res = self.t + r
        expected = DateTime(2014, 6, 15, 19, 30, 30)
        self.assertEqual(res, expected)

        r = RelativeDateTime(hours=-1)
        res = self.t + r
        expected = DateTime(2014, 6, 15, 17, 30, 30)
        self.assertEqual(res, expected)

        r = RelativeDateTime(hours=23)
        res = self.t + r
        expected = DateTime(2014, 6, 16, 17, 30, 30)
        self.assertEqual(res, expected)

    def testAddMinutes(self):
        r = RelativeDateTime(minutes=1)
        res = self.t + r
        expected = DateTime(2014, 6, 15, 18, 31, 30)
        self.assertEqual(res, expected)

        r = RelativeDateTime(minutes=-1)
        res = self.t + r
        expected = DateTime(2014, 6, 15, 18, 29, 30)
        self.assertEqual(res, expected)

        r = RelativeDateTime(minutes=59)
        res = self.t + r
        expected = DateTime(2014, 6, 15, 19, 29, 30)
        self.assertEqual(res, expected)

    def testAddSeconds(self):
        r = RelativeDateTime(seconds=1)
        res = self.t + r
        expected = DateTime(2014, 6, 15, 18, 30, 31)
        self.assertEqual(res, expected)

        r = RelativeDateTime(seconds=-1)
        res = self.t + r
        expected = DateTime(2014, 6, 15, 18, 30, 29)
        self.assertEqual(res, expected)

        r = RelativeDateTime(seconds=59)
        res = self.t + r
        expected = DateTime(2014, 6, 15, 18, 31, 29)
        self.assertEqual(res, expected)

    def testAddTimeToDate(self):
        tc = DateTime(2014, 10, 26, 0, 0)
        r = RelativeDateTimeFrom('08:00')
        res = tc + r
        self.assertEqual(res.year, 2014)
        self.assertEqual(res.month, 10)
        self.assertEqual(res.day, 26)
        self.assertEqual(res.hour, 8)
        self.assertEqual(res.minute, 0)
        self.assertEqual(res.second, 0)

    def testAddYearToLeap(self):
        tc = DateTime(1988, 2, 29)
        r = RelativeDateTime(years=1)
        expected = DateTime(1989, 3, 1)
        self.assertEqual(tc + r, expected)

    def testAddWithSub(self):
        tc = DateTime(2014, 10, 26, 0, 0)
        r = RelativeDateTimeFrom('-08:30')
        res = tc + r
        self.assertEqual(res.year, 2014)
        self.assertEqual(res.month, 10)
        self.assertEqual(res.day, 26)
        self.assertEqual(res.hour, 8)
        self.assertEqual(res.minute, 30)
        self.assertEqual(res.second, 0)

    def testAddWithAdd(self):
        tc = DateTime(2014, 10, 26, 0, 0)
        r = RelativeDateTimeFrom('08:30')
        res = tc + r
        self.assertEqual(res.year, 2014)
        self.assertEqual(res.month, 10)
        self.assertEqual(res.day, 26)
        self.assertEqual(res.hour, 8)
        self.assertEqual(res.minute, 30)
        self.assertEqual(res.second, 0)

    def testMutation(self):
        tc = DateTime(2014, 10, 26, 0, 0)
        r = RelativeDateTimeFrom('08:00')
        res = tc + r
        self.assertFalse(res is tc)

    def testAddRels(self):
        r = RelativeDateTime(years=1, days=1, seconds=5, minute=3)
        r2 = RelativeDateTime(years=1, months=1, minutes=4, seconds=1)
        res = r + r2
        # No mutation
        self.assertFalse(r is res)
        self.assertFalse(r2 is res)
        self.assertEqual(res.years, 2)
        self.assertEqual(res.months, 1)
        self.assertEqual(res.days, 1)
        self.assertEqual(res.minutes, 4)
        self.assertEqual(res.seconds, 6)
        self.assertEqual(res.minute, 3)
        with self.assertRaises(TypeError):
            r + 3
        with self.assertRaises(TypeError):
            r + '3'

    def testRelativeDateTimeFrom(self):
        with self.assertRaises(TypeError):
            RelativeDateTimeFrom(1, 2, 3, manoman=3)

        r = RelativeDateTimeFrom(hour=23, minute=59, second=59)
        res = self.t + r
        expected = DateTime(2014, 6, 15, 23, 59, 59)
        self.assertEqual(res, expected)

        r = RelativeDateTimeFrom(1, 0, 0)
        res = self.t + r
        expected = DateTime(2015, 6, 15, 18, 30, 30)
        self.assertEqual(res, expected)

    def testPlusMinusSame(self):
        r = RelativeDateTimeFrom('00:01')
        r2 = RelativeDateTimeFrom('-00:01')
        self.assertEqual(r, r2)

'''
RelativeDateTime(day=(dagur_vaktar.day)
RelativeDateTime(day=-dagur_vaktar.day)
RelativeDateTime(day=-int(dagur_vaktar.days_in_month)
RelativeDateTime(day=1)
RelativeDateTime(day=1,hour=0,minute=0,second=0)
RelativeDateTime(day=1,hour=1,minute=1,second=1)
RelativeDateTime(day=14)
RelativeDateTime(day=15)
RelativeDateTime(day=16)
RelativeDateTime(day=20)
RelativeDateTime(day=21)
RelativeDateTime(day=21,months=-1)
RelativeDateTime(day=23)
RelativeDateTime(day=24)
RelativeDateTime(day=24,hour=+23,minute=+59,seconds=+29)
RelativeDateTime(day=25)
RelativeDateTime(day=25,hour=+23,minute=+59,seconds=+29)
RelativeDateTime(day=26)
RelativeDateTime(day=27,hour=+23,minute=+59,seconds=+29)
RelativeDateTime(day=28)
RelativeDateTime(day=5,hour=23,minute=59,second=59)
RelativeDateTime(day=6,hour=23,minute=59,second=59)
RelativeDateTime(day=7,hour=23,minute=59,second=59)
RelativeDateTime(day=dagur_vaktar.day)
RelativeDateTime(day=dagur_vaktar.day,hour=+23,minute=+59,seconds=+29)
RelativeDateTime(day=dagur_vaktar.day,hour=+23,minute=+59,seconds=+59)
RelativeDateTime(day=self.upphafsdagur)
RelativeDateTime(days=-(1)
RelativeDateTime(days=-(2)
RelativeDateTime(days=-(3)
RelativeDateTime(days=-(4)
RelativeDateTime(days=-(5)
RelativeDateTime(days=-(6)
RelativeDateTime(days=-(7)
RelativeDateTime(days=-(i+1)
RelativeDateTime(days=-(self.fjoldi_daga_i_rod-1)
RelativeDateTime(days=-0)
RelativeDateTime(days=-1)
RelativeDateTime(days=-1,hour=+23,minute=+59,seconds=+29)
RelativeDateTime(days=-1,hour=00,minute=00,second=00)
RelativeDateTime(days=-1,hour=00,minute=00,second=29)
RelativeDateTime(days=-1,hour=13)
RelativeDateTime(days=-1,hour=23,minute=59,second=0)
RelativeDateTime(days=-1,hour=23,minute=59,second=29)
RelativeDateTime(days=-1,hour=23,minute=59,second=59)
RelativeDateTime(days=-1,hour=h,minute=m,second=0)
RelativeDateTime(days=-10)
RelativeDateTime(days=-11)
RelativeDateTime(days=-12)
RelativeDateTime(days=-13)
RelativeDateTime(days=-13,day=14)
RelativeDateTime(days=-13,hour=00,minute=00,second=29)
RelativeDateTime(days=-14,hour=0,minute=0,seconds=0)
RelativeDateTime(days=-16,day=31)
RelativeDateTime(days=-2)
RelativeDateTime(days=-2,hour=00,minute=00,second=29)
RelativeDateTime(days=-3)
RelativeDateTime(days=-3,hour=00,minute=00,second=29)
RelativeDateTime(days=-4)
RelativeDateTime(days=-4,hour=00,minute=00,second=29)
RelativeDateTime(days=-5)
RelativeDateTime(days=-5,hour=00,minute=00,second=29)
RelativeDateTime(days=-5,hour=23,minute=59,second=29)
RelativeDateTime(days=-6)
RelativeDateTime(days=-6,hour=0,minute=0,second=0)
RelativeDateTime(days=-6,hour=00,minute=00,second=29)
RelativeDateTime(days=-7)
RelativeDateTime(days=-7,hour=00,minute=00,second=29)
RelativeDateTime(days=-8)
RelativeDateTime(days=-9)
RelativeDateTime(days=-i)
RelativeDateTime(days=-self.ve_dagar)
RelativeDateTime(days=0)
RelativeDateTime(days=1)
RelativeDateTime(days=2)
RelativeDateTime(days=3)
RelativeDateTime(hour=+12,minute=+0,seconds=+0)
RelativeDateTime(hour=+13,minute=+0,seconds=+0)
RelativeDateTime(hour=+18,minute=+0,seconds=+0)
RelativeDateTime(hour=+18,minute=+30,seconds=+0)
RelativeDateTime(hour=+23,minute=+29,seconds=+29)
RelativeDateTime(hour=+23,minute=+59,seconds=+29)
RelativeDateTime(hour=+8,minute=+0,seconds=+0)
RelativeDateTime(hour=+8,minute=+30,seconds=+0)
RelativeDateTime(hour=-299,minute=+59,seconds=+29)
RelativeDateTime(hour=0,minute=0,second=0)
RelativeDateTime(hour=0,minute=0,seconds=0,days=-6)
RelativeDateTime(hour=00,minute=00,second=00)
RelativeDateTime(hour=12,minute=0,second=0)
RelativeDateTime(hour=13)
RelativeDateTime(hour=19,minute=0,second=0)
RelativeDateTime(hour=23,minute=59,second=0)
RelativeDateTime(hour=23,minute=59,second=29)
RelativeDateTime(hour=23,minute=59,second=59)
RelativeDateTime(hour=23,minute=59,seconds=29)
RelativeDateTime(hour=24,minute=0,second=0)
RelativeDateTime(hour=8,minute=0,second=0)
RelativeDateTime(hour=8,minute=30,second=0)
RelativeDateTime(hour=self.klst,minute=self.minuta,second=0)
RelativeDateTime(hours=+1)
RelativeDateTime(hours=+2)
RelativeDateTime(hours=+3)
RelativeDateTime(hours=5)
RelativeDateTime(minute=-1)
RelativeDateTime(minute=dest_mins, second=0)
RelativeDateTime(minute=dest_mins,hours = (dest_mins<from_mins)
RelativeDateTime(minute=dest_mins,hours = -1 * (dest_mins>=from_mins)
RelativeDateTime(minutes=+1)
RelativeDateTime(minutes=+210)
RelativeDateTime(minutes=+25)
RelativeDateTime(minutes=+27)
RelativeDateTime(minutes=+5)
RelativeDateTime(minutes=+self.fragangur)
RelativeDateTime(minutes=-1)
RelativeDateTime(minutes=-20)
RelativeDateTime(month=0,day=0,hour=17,minute=0,second=0)
RelativeDateTime(month=0,day=0,hour=18,minute=0,second=0)
RelativeDateTime(month=0,day=0,hour=8,minute=0,second=0)
RelativeDateTime(month=1,day=1)
RelativeDateTime(month=1,day=1,hour=0,minute=0,seconds=0)
RelativeDateTime(month=1,day=4,hour=0,minute=0,second=0)
RelativeDateTime(month=10,day=1)
RelativeDateTime(month=10,day=30,hour=23,minute=59,second=59)
RelativeDateTime(month=12,day=21,hour=0,minute=0,second=0)
RelativeDateTime(month=12,day=21,hour=23,minute=59,second=59)
RelativeDateTime(month=12,day=31,hour=23,minute=59,second=59)
RelativeDateTime(month=3,day=27,hour=0,minute=0,second=0)
RelativeDateTime(month=4,day=1,hour=0,minute=0,second=0)
RelativeDateTime(month=5,day=01,hour=0,minute=0,second=0)
RelativeDateTime(month=5,day=1,hour=0,minute=0,second=0)
RelativeDateTime(month=5,day=15,hour=0,minute=0,second=0)
RelativeDateTime(month=5,day=23,hour=0,minute=0,second=0)
RelativeDateTime(month=5,day=30,hour=0,minute=0,second=0)
RelativeDateTime(month=6,day=1,hour=0,minute=0,second=0)
RelativeDateTime(month=6,day=10,hour=0,minute=0,second=0)
RelativeDateTime(month=6,day=3,hour=23,minute=59,second=59)
RelativeDateTime(month=6,day=8,hour=0,minute=0,second=0)
RelativeDateTime(month=6,day=8,hour=23,minute=59,second=59)
RelativeDateTime(month=8,day=13,hour=23,minute=59,second=59)
RelativeDateTime(month=8,day=14,hour=23,minute=59,second=59)
RelativeDateTime(month=8,day=25,hour=0,minute=0,second=0)
RelativeDateTime(month=8,day=30,hour=23,minute=59,second=59)
RelativeDateTime(month=8,day=31,hour=23,minute=59,second=59)
RelativeDateTime(month=9,day=1,hour=23,minute=59,second=59)
RelativeDateTime(month=9,day=15,hour=23,minute=59,second=29)
RelativeDateTime(month=9,day=15,hour=23,minute=59,second=59)
RelativeDateTime(month=9,day=30,hour=23,minute=59,second=59)
RelativeDateTime(months=+1,day=27,hour=+23,minute=+59,seconds=+29)
RelativeDateTime(months=-1)
RelativeDateTime(months=-1, day=self.upphafsdagur)
RelativeDateTime(months=-1,day=1)
RelativeDateTime(months=-1,day=11)
RelativeDateTime(months=-1,day=15)
RelativeDateTime(months=-1,day=16)
RelativeDateTime(months=-1,day=18)
RelativeDateTime(months=-1,day=20)
RelativeDateTime(months=-1,day=21)
RelativeDateTime(months=-1,day=23)
RelativeDateTime(months=-1,day=24)
RelativeDateTime(months=-1,day=25)
RelativeDateTime(months=-1,day=26)
RelativeDateTime(months=-1,day=27)
RelativeDateTime(months=-1,day=28)
RelativeDateTime(months=-1,day=9)
RelativeDateTime(months=-1,day=fjoldi_daga_i_sidasta_man)
RelativeDateTime(months=-1,day=int(dagur_vaktar.days_in_month)
RelativeDateTime(months=-1,day=naestsidastidagurmanadar)
RelativeDateTime(months=-1,day=self.fyrsti_dagur)
RelativeDateTime(months=-1,day=self.fyrsti_dagur_man)
RelativeDateTime(months=-1,day=self.upphafsdagur)
RelativeDateTime(months=-1,day=self.upphafsdagur,hour=+00,minute=+59,seconds=+29)
RelativeDateTime(months=-1,days=+1,hour=0,minute=0,second=0)
RelativeDateTime(months=-1.0,day=16)
RelativeDateTime(months=-10,day=1)
RelativeDateTime(months=-12)
RelativeDateTime(months=0,day=-dagur_vaktar.days_in_month)
RelativeDateTime(months=0,day=1)
RelativeDateTime(weekday=(mx.DateTime.Monday,0)
RelativeDateTime(weekday=(mx.DateTime.Sunday,0)
RelativeDateTime(weekday=(mx.DateTime.Thursday,0)
RelativeDateTime(weekday=(mx.DateTime.Tuesday,0)
RelativeDateTime(weekday=(mx.DateTime.Wednesday,0)
RelativeDateTime(weeks=-1,hour=23,minute=59,second=29)
RelativeDateTime(weeks=-2,hour=23,minute=59,second=29)
RelativeDateTime(years=-1)
RelativeDateTime(years=-1,month=1,day=1)
RelativeDateTime(years=-1,month=1,day=11)
RelativeDateTime(years=-1,month=12,day=7)
RelativeDateTime(years=-1,month=4,day=28)
RelativeDateTime(years=-1,month=4,day=30)
RelativeDateTime(years=-1,month=5,day=1)
RelativeDateTime(years=-1,month=5,day=16)
RelativeDateTime(years=-1,month=self.upphaf_orlof_man,day=self.upphaf_orlof_dagur)
'''
