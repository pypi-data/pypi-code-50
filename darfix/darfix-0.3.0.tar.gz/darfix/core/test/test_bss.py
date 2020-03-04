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


__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "26/11/2019"


import unittest

import numpy

from darfix.core.blindSourceSeparation import BSS
from darfix.test import utils


class TestBSS(unittest.TestCase):

    """Tests for `blind_source_separation.py`."""

    def setUp(self):

        self.dataset = utils.createRandomDataset(dims=(100, 100), nb_dark_files=1, header=True)
        self.bss = BSS(self.dataset.data)

    def test_pca(self):

        components, W = self.bss.PCA(num_components=5)

        shape_frame = len(self.dataset.data[0].flatten())
        self.assertEqual(components.shape, (5, shape_frame))
        self.assertEqual(W.shape, (self.dataset.nframes, 5))

    def test_whiten(self):

        Z, V = self.bss.whiten(num_components=5)

        cov = numpy.cov(Z)
        numpy.testing.assert_almost_equal(cov, numpy.eye(5))

    def test_nnica(self):

        components, W = self.bss.non_negative_ICA(num_components=5)

        shape_frame = len(self.dataset.data[0].flatten())
        self.assertEqual(components.shape, (5, shape_frame))
        self.assertEqual(W.shape, (self.dataset.nframes, 5))

    def test_nmf(self):

        components, W = self.bss.NMF(num_components=5)

        shape_frame = len(self.dataset.data[0].flatten())
        self.assertEqual(components.shape, (5, shape_frame))
        self.assertEqual(W.shape, (self.dataset.nframes, 5))
