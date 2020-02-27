#!/usr/bin/env python
# ******************************************************************************
# Copyright 2019 Brainchip Holdings Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ******************************************************************************

# -*- coding: utf-8 -*-
from __future__ import absolute_import
import tensorflow.keras.backend as K
import tensorflow as tf


class BaseWeightQuantizer:
    """The base class for all Quantizers.

    The relationship between raw weights and quantized weights is:
    (1) W = Wq * scale_factor
    This class provides methods that return quantized weights and their
    associated scale factor.

    """

    def __init__(self, bitwidth):
        """Creates a Weights quantizer for the specified bitwidth.

        Args:
            bitwidth (integer): the quantizer bitwidth defining the number of
                quantized values.

        """
        self.bitwidth_ = bitwidth

    def quantize(self, w):
        """Quantizes the specified weights Tensor.

        Args:
            w (:obj:`tensorflow.Tensor`): the weights Tensor to quantize.

        Returns:
            :obj:`tensorflow.Tensor`: a Tensor of quantized weights.

        """
        return w

    def scale_factor(self, w):
        """Evaluates the scale factor for the specified weights Tensor.

        Args:
          w (:obj:`tensorflow.Tensor`): the weights Tensor to quantize.

        Returns:
          :obj:`tensorflow.Tensor`: a Tensor containing a single scalar value.

        """
        return tf.constant(1.0)

    @property
    def bitwidth(self):
        return self.bitwidth_


class WeightQuantizer(BaseWeightQuantizer):
    """A uniform quantizer.

    Quantize the specified weights into 2^k-1 values, k representing the
    bitwidth.
    The relationship between raw weights and quantized weights is:
    (1) W = Wq * scale_factor

    All values below or above a specified multiple of the weights standard
    deviation are automatically assigned to the min (resp max) value.

    """
    def __init__(self, threshold=3, bitwidth=4):
        """Creates a Weights quantizer for the specified bitwidth.

        Args:
            threshold (integer): the standard deviation multiplier used to exclude
                outliers.
            bitwidth (integer): the quantizer bitwidth defining the number of
                quantized values.

        """
        # Having a cast guarantees a check when the parameters are not numbers
        # (e.g.: None)
        self.threshold_ = float(threshold)
        self.bitwidth_ = int(bitwidth)
        self.kmax_ = (2.**(self.bitwidth_ - 1) - 1)

    def sigma_scaled_(self, w):
        return K.std(w) * self.threshold_

    def bit_range_(self):
        return self.kmax_

    def scale_factor(self, w):
        return self.kmax_ / self.sigma_scaled_(w)

    def quantize(self, w):
        kmax_ = self.kmax_
        delta = self.scale_factor(w)
        out_w = K.clip(round_through(w * delta), -kmax_, kmax_) / delta
        return out_w

class WeightFloat(BaseWeightQuantizer):
    """This quantizer actually does not perform any quantization, and it might
    be used for training.

    """
    def __init__(self, bitwidth = 0):
        super().__init__(bitwidth=bitwidth)


def round_through(x):
    """Element-wise rounding to the closest integer with full gradient propagation.
    A trick from [Sergey Ioffe](http://stackoverflow.com/a/36480182).

    """
    rounded = K.round(x)
    return x + K.stop_gradient(rounded - x)


def ceil_through(x):
    """Element-wise ceiling operation (to the closest greater integer) with
    full gradient propagation.

    """
    ceiling_value = tf.math.ceil(x)
    return x + K.stop_gradient(ceiling_value - x)
