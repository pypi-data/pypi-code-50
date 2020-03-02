import unittest

import datetime
import copy

from mx.DateTime import DateTime, Feasts


class DateTimeTests(unittest.TestCase):
    def testEasterSunday(self):
        s = Feasts.EasterSunday(2015)
        exp = DateTime(2015, 4, 5)
        self.assertEqual(s, exp)
        s = Feasts.EasterSunday(2014)
        exp = DateTime(2014, 4, 20)
        self.assertEqual(s, exp)

    def testCarnivalMonday(self):
        s = Feasts.CarnivalMonday(2015)
        exp = DateTime(2015, 2, 16)
        self.assertEqual(s, exp)
        s = Feasts.CarnivalMonday(2014)
        exp = DateTime(2014, 3, 3)
        self.assertEqual(s, exp)

    def testMardiGras(self):
        s = Feasts.MardiGras(2015)
        exp = DateTime(2015, 2, 17)
        self.assertEqual(s, exp)
        s = Feasts.MardiGras(2014)
        exp = DateTime(2014, 3, 4)
        self.assertEqual(s, exp)

    def testAshWednesday(self):
        s = Feasts.AshWednesday(2015)
        exp = DateTime(2015, 2, 18)
        self.assertEqual(s, exp)
        s = Feasts.AshWednesday(2014)
        exp = DateTime(2014, 3, 5)
        self.assertEqual(s, exp)

    def testPalmSunday(self):
        s = Feasts.PalmSunday(2015)
        exp = DateTime(2015, 3, 29)
        self.assertEqual(s, exp)
        s = Feasts.PalmSunday(2014)
        exp = DateTime(2014, 4, 13)
        self.assertEqual(s, exp)

    def testEasterFriday(self):
        s = Feasts.EasterFriday(2015)
        exp = DateTime(2015, 4, 3)
        self.assertEqual(s, exp)
        s = Feasts.EasterFriday(2014)
        exp = DateTime(2014, 4, 18)
        self.assertEqual(s, exp)

    def testEasterMonday(self):
        s = Feasts.EasterMonday(2015)
        exp = DateTime(2015, 4, 6)
        self.assertEqual(s, exp)
        s = Feasts.EasterMonday(2014)
        exp = DateTime(2014, 4, 21)
        self.assertEqual(s, exp)

    def testAscension(self):
        s = Feasts.Ascension(2015)
        exp = DateTime(2015, 5, 14)
        self.assertEqual(s, exp)
        s = Feasts.Ascension(2014)
        exp = DateTime(2014, 5, 29)
        self.assertEqual(s, exp)

    def testPentecost(self):
        s = Feasts.Pentecost(2015)
        exp = DateTime(2015, 5, 24)
        self.assertEqual(s, exp)
        s = Feasts.Pentecost(2014)
        exp = DateTime(2014, 6, 8)
        self.assertEqual(s, exp)

    def testWhitMonday(self):
        s = Feasts.WhitMonday(2015)
        exp = DateTime(2015, 5, 25)
        self.assertEqual(s, exp)
        s = Feasts.WhitMonday(2014)
        exp = DateTime(2014, 6, 9)
        self.assertEqual(s, exp)

    def testTrinitySunday(self):
        s = Feasts.TrinitySunday(2015)
        exp = DateTime(2015, 5, 31)
        self.assertEqual(s, exp)
        s = Feasts.TrinitySunday(2014)
        exp = DateTime(2014, 6, 15)
        self.assertEqual(s, exp)

    def testCorpusChristi(self):
        s = Feasts.CorpusChristi(2015)
        exp = DateTime(2015, 6, 4)
        self.assertEqual(s, exp)
        s = Feasts.CorpusChristi(2014)
        exp = DateTime(2014, 6, 19)
        self.assertEqual(s, exp)
