# -*- coding: utf-8 -*-
import os, unittest
from datetime import datetime
from shutil import copyfile

from chappie.utils.date_finder import find_dates


class DateFinderTest(unittest.TestCase):
    def setUp(self):
        """To be executed before each test."""
        self.string_of_dates = [
            (u"# entries are due by enero 4th, 2017 at 8:00pm - ok", 1),
            (u"# 09, 2017 - ok", 9),
            (u"# Ejercicio comprendido entre el 01 de Enero y el 31 de Enero 2017 - ok", 1),
            (u"# Ejercicio comprendido entre el 01 de Enero y el 28 de Febrero 2017 - ok", 2),
            (u"# Ejercicio comprendido entre el 01 de Enero y el 31 de Marzo 2017 - ok", 3),
            (u"# Ejercicio comprendido entre el 01 de Enero y el 30 de Abril 2017 - ok", 4),
            (u"# ACUMULADO AL 30 DE ABRIL 2017 - ok", 4),
            (u"# ACUMULADO AL 31 DE AGOSTO  DE 2017 - ok", 8),
            (u"# ACUMUADO  AL 31 DE MARZO DE 2017 - ok", 3),
            (u"# ACUMULADO AL 31 DE ENERO DE 2017 - ok", 1),
            (u"# ACUMULADO AL 28 FEBRERO 2017 - ok", 2),
            (u"# ACUMULADO AL 31 DE JULIO DE 2017 - ok", 7),
            (u"# ACUMULADO AL 31 DE MAYO DE 2017 - ok", 5),
            (u"# ACUMULADO AL 30 DE SEPTIEMBRE DE 2017 - ok", 9),
            (u"Junio/2017 - ok", 6),
            (u"Abril/2017 - ok", 4),
            (u"Agosto/2017 - ok", 8),
            (u"ACUMULADO AL 31 DE JULIO DE 2017 - ok", 7),
            (u"EJERCICIO DE ENERO A ABRIL DEL 2017 - ok", 4),
            (u"EJERCICIO DE ENERO A DICIEMBRE DEL 2016 - ok", 12),
            (u"EJERCICIO DE ENERO A FEBRERO DEL 2017 - ok", 2),
            (u"EJERCICIO DE ENERO A JUNIO DEL 2017 - ok", 6),
            (u"DE ENERO A SEPTIEMBRE DE 2017 - ok", 9),
            (u"BALANCE_20170623174628 - ok", 6),
            (u"2017/3 - ok", 3),
            (u"BALANCE_20170824144418 - ok", 8),
            (u"""COMPAÑIA MINERA  SALI HOCHSCHILD S.A.
            R U T  N 90.853.000-4 false positive
            EXTRACCION DE COBRE, ARRIENDO DE MINAS		     B A L A N C E       T R I B U T A R I O					I V   NIVEL
            ROMAN DIAZ N 205, DEPTO. 301 false positive
            PROVIDENCIA		ACUMUADO  AL 31 DE MARZO DE 2017 ok
            SANTIAGO""", 3),
            (u"""ADMETRICKS SPA
            76.192.113-4  false positive
            BALANCE GENERAL
            Ejercicio comprendido entre el 01 de Enero y el 31 de Marzo 2017	ok		""", 3)
        ]

    def test_date_search(self):
        """check valid dates are returned for a bunch of test strings"""
        for item in self.string_of_dates:
            matches = find_dates(item[0],source=True, index=True, strict=False, base_date=None)
            for match in matches:
                pass
            # last item
            if match:
                period = match[0]
                self.assertIsInstance(period, datetime)
                self.assertEqual(period.month, item[1])
