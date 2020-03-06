# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2017 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ###########################################################################*/

__authors__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "04/03/2019"


def _assert_param_instance(param, valid_instances):
    """check the parameter value, can be an instance of valid_instance or
    an iterable of valid_instance"""
    if isinstance(param, valid_instances):
        return
    else:
        try:
            for unique_param in param:
                if not isinstance(unique_param, valid_instances):
                    assert isinstance(unique_param, valid_instances)
        except:
            raise ValueError('%s has an invalid type' % param)


def _assert_cast_to_boolean(value):
    """

    :param value: value we want to cast to a boolean
    """
    try:
        bool(int(value))
    except:
        raise ValueError('%s cannot be cast to boolean' % value)


def _assert_cast_to_int(value):
    try:
        int(value)
    except:
        raise ValueError('%s cannot be cast to int' % value)

