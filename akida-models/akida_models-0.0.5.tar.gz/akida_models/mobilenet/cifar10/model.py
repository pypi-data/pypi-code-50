#!/usr/bin/env python
# ******************************************************************************
# Copyright 2020 Brainchip Holdings Ltd.
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
import os

from tensorflow.keras.layers import Input
from tensorflow.keras import Model
from tensorflow.keras.utils import get_file

from ...quantization_blocks import conv_block, separable_conv_block

BASE_WEIGHT_PATH = 'http://data.brainchip.com/models/mobilenet/'

def mobilenet_cifar10(input_shape,
                      classes=10,
                      weights=None,
                      weight_quantization=0,
                      activ_quantization=0,
                      input_weight_quantization=None):
    """Instantiates a MobileNet-like model for the "Cifar-10" example.
    This model is based on the MobileNet architecture, mainly with fewer layers.
    The weights and activations are quantized such that it can be converted into
    an Akida model.
    This architecture is inspired by MobileNet.

    Args:
        input_shape (tuple): input shape tuple of the model
        classes (int): number of classes to classify images into
        weights (str): one of `None` (random initialization), 'cifar10' for
            pretrained weights or the path to the weights file to be loaded.
        weight_quantization (int): sets all weights in the model to have
            a particular quantization bitwidth except for the weights in the
            first layer.

            * '0' implements floating point 32-bit weights
            * '2' through '8' implements n-bit weights where n is from 2-8 bits.
        activ_quantization: sets all activations in the model to have a.
            particular activation quantization bitwidth.

            * '0' implements floating point 32-bit activations.
            * '2' through '8' implements n-bit weights where n is from 2-8 bits.
        input_weight_quantization: sets weight quantization in the first layer.
            Defaults to weight_quantization value.

            * 'None' implements the same bitwidth as the other weights.
            * '0' implements floating point 32-bit weights.
            * '2' through '8' implements n-bit weights where n is from 2-8 bits.

    Returns:
        tf.keras.model: a quantized Keras model for mobileNet/cifar10
    """

    # Overrides input weight quantization if None
    if input_weight_quantization is None:
        input_weight_quantization = weight_quantization

    # Check weights
    if not (weights in {None, 'cifar10'} or os.path.exists(weights)):
        raise ValueError('The `weights` argument should be either '
                         '`None` (random initialization) '
                         'or `cifar10` to load weights over http '
                         'or the path to the weights file to be loaded.')

    # Check if Cifar-10 pretrained weights are compatible with given arguments
    if weights == 'cifar10':
        quant_params = (weight_quantization,
                        activ_quantization,
                        input_weight_quantization)
        if classes != 10:
            raise ValueError("If 'weights' is 'cifar10', classes should be 10")
        if quant_params != (4, 4, 8):
            raise ValueError("If 'weights' is 'cifar10', quantization parameters "
                             "(weight_quantization, activ_quantization, "
                             " input_weight_quantization) must be (4, 4, 8)")
        if input_shape[-1] !=  3:
            raise ValueError("If 'weights' is 'cifar10', channel number"
                             " must be 3")
        if input_shape[0] != 32 or input_shape[1] != 32:
            print("If 'weights' is 'cifar10', weights trained for input (32, 32) "
                  "will be used")

    img_input = Input(shape=input_shape)

    x = conv_block(img_input, filters=128, name='conv_0',
            kernel_size=(3, 3),
            padding='same',
            use_bias=False,
            weight_quantization=input_weight_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters=128, kernel_size=(3,3), name='separable_1',
            padding='same',
            use_bias=False,
            weight_quantization=weight_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters=256, kernel_size=(3,3), name='separable_2',
            padding='same',
            use_bias=False,
            weight_quantization=weight_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters=256, kernel_size=(3,3), name='separable_3',
            padding='same',
            use_bias=False,
            weight_quantization=weight_quantization,
            activ_quantization=activ_quantization,
            pooling='max',
            add_batchnorm=True)

    x = separable_conv_block(x, filters=512, kernel_size=(3,3), name='separable_4',
            padding='same',
            use_bias=False,
            weight_quantization=weight_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters=512, kernel_size=(3,3), name='separable_5',
            padding='same',
            use_bias=False,
            weight_quantization=weight_quantization,
            activ_quantization=activ_quantization,
            pooling='max',
            add_batchnorm=True)

    x = separable_conv_block(x, filters=512, kernel_size=(3,3), name='separable_6',
            padding='same',
            use_bias=False,
            weight_quantization=weight_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters=512, kernel_size=(3,3), name='separable_7',
            padding='same',
            use_bias=False,
            weight_quantization=weight_quantization,
            activ_quantization=activ_quantization,
            pooling='max',
            add_batchnorm=True)

    x = separable_conv_block(x, filters=1024, kernel_size=(3,3), name='separable_8',
            padding='same',
            use_bias=False,
            weight_quantization=weight_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters=1024, kernel_size=(3,3), name='separable_9',
            padding='same',
            use_bias=False,
            weight_quantization=weight_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters=classes, kernel_size=(3,3),
            name='separable_10',
            padding='same',
            use_bias=False,
            weight_quantization=weight_quantization,
            activ_quantization=None,
            pooling='global_avg',
            add_batchnorm=False)

    model = Model(img_input, x, name='mobilenet_cifar10')

    # Load weights
    if weights == 'cifar10':
        model_name = (f'mobilenet_cifar10_wq{weight_quantization}'
                      f'_aq{activ_quantization}.hdf5')
        weights_path = get_file(fname=model_name,
                                origin=BASE_WEIGHT_PATH + model_name,
                                cache_subdir='models')
        model.load_weights(weights_path)
    elif weights is not None:
        model.load_weights(weights)

    return model
