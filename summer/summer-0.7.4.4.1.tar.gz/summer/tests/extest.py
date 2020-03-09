# Copyright (C) 2009-2020 Martin Slouf <martinslouf@users.sourceforge.net>
#
# This file is a part of Summer.
#
# Summer is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

import unittest
import summer


class FooException(summer.ApplicationException):
    def __init__(self, message: str = None, **kwargs):
        super().__init__(message, **kwargs)


class Foo(object):

    def __init__(self):
        self.a = 1
        self.b = [1, 2]

    def __str__(self):
        return f"{self.__class__.__name__} {{a={self.a}, b={self.b}}}"


class ExTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_str(self):
        ex = summer.ApplicationException("message", a="hello", b=1, c=Foo())
        tmp = str(ex)
        self.assertTrue(tmp.startswith("ApplicationException -- message -- a = hello, b = 1"))

        ex = FooException("message", a="hello", b=1, c=Foo())
        tmp = str(ex)
        self.assertTrue(tmp.startswith("FooException -- message -- a = hello, b = 1"))

        ex = FooException()
        tmp = str(ex)
        self.assertEqual(tmp, "FooException")

        ex = FooException("Hello World!")
        tmp = str(ex)
        self.assertEqual(tmp, "FooException -- Hello World!")


if __name__ == "__main__":
    unittest.main()
