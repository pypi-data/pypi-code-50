from __future__ import absolute_import
from __future__ import division

import tensorflow as tf

from .layers import avg_pool2d
from .layers import batch_norm
from .layers import conv2d
from .layers import convbn
from .layers import convbnrelu as conv
from .layers import sconv2d
from .layers import sconvbn
from .layers import sconvbnrelu as sconv
from .layers import fc
from .layers import max_pool2d
from .layers import l2

from .ops import *
from .utils import pad_info
from .utils import set_args
from .utils import var_scope


def __args0__(is_training):
    return [([avg_pool2d, max_pool2d], {'scope': 'pool'}),
            ([batch_norm], {'scale': True, 'is_training': is_training,
                            'decay': 0.99, 'epsilon': 1e-3, 'scope': 'bn'}),
            ([conv2d], {'padding': 'SAME', 'activation_fn': None,
                        'weights_regularizer': l2(4e-5), 'scope': 'conv'}),
            ([fc], {'activation_fn': None, 'weights_regularizer': l2(4e-5),
                    'scope': 'fc'}),
            ([sconv2d], {'padding': 'SAME', 'activation_fn': None,
                         'weights_regularizer': l2(4e-5),
                         'biases_initializer': None,
                         'scope': 'sconv'})]


def __args__(is_training):
    return [([avg_pool2d, max_pool2d], {'scope': 'pool'}),
            ([batch_norm], {'scale': True, 'is_training': is_training,
                            'decay': 0.99, 'epsilon': 1e-3, 'scope': 'bn'}),
            ([conv2d], {'padding': 'SAME', 'activation_fn': None,
                        'biases_initializer': None, 'scope': 'conv'}),
            ([fc], {'activation_fn': None, 'scope': 'fc'}),
            ([sconv2d], {'padding': 'SAME', 'activation_fn': None,
                         'biases_initializer': None,
                         'scope': 'sconv'})]


def tnet(x, stack_fn, is_training, classes, stem,
         scope=None, reuse=None):
    x = pad(x, pad_info(7), name='conv1/pad')
    x = conv(x, 64, 7, stride=2, padding='VALID', scope='conv1')
    x = pad(x, pad_info(3), name='pool1/pad')
    x = max_pool2d(x, 3, stride=2, padding='VALID', scope='pool1')
    x = stack_fn(x)
    if stem: return x
    x = reduce_mean(x, [1, 2], name='avgpool')
    x = fc(x, classes, scope='logits')
    x = softmax(x, name='probs')
    return x


def tnet2(x, widths, heights, is_training, classes, stem,
          scope=None, reuse=None):
    x = pad(x, pad_info(3), name='conv0/pad')
    x = conv(x, 32, 3, stride=2, padding='VALID', scope='conv0')
    x = conv(x, 64, 3, scope='conv1')
    x = stack(x, widths[0], heights[0], scope='conv2')
    x = stack(x, widths[1], heights[1], scope='conv3')
    x = stack(x, widths[2], heights[2], scope='conv4')
    x = stack(x, widths[3], heights[3], scope='conv5')
    if stem: return x
    x = reduce_mean(x, [1, 2], name='avgpool')
    x = fc(x, classes, scope='logits')
    x = softmax(x, name='probs')
    return x


def tnet4(x, widths, heights, is_training, classes, stem,
          scope=None, reuse=None):
    x = pad(x, pad_info(3), name='conv1/pad')
    x = conv(x, 64, 3, stride=2, padding='VALID', scope='conv1')
    x = stack(x, widths[0], heights[0], scope='conv2')
    x = stack(x, widths[1], heights[1], scope='conv3')
    p2 = blockpool(x, widths[1], 4, 3, scope='conv3pool')
    x = stack(x, widths[2], heights[2], scope='conv4')
    p1 = blockpool(x, widths[2], 2, 3, scope='conv4pool')
    x = stack(x, widths[3], heights[3], scope='conv5')
    x = concat([x, p1, p2], axis=3, name='concat')
    if stem: return x
    x = reduce_mean(x, [1, 2], name='avgpool')
    x = fc(x, classes, scope='logits')
    x = softmax(x, name='probs')
    return x


def tnet6(x, widths, heights, is_training, classes, stem,
          scope=None, reuse=None):
    x = pad(x, pad_info(3), name='conv1/pad')
    x = conv(x, 64, 3, stride=2, padding='VALID', scope='conv1')
    x = stack(x, widths[0], heights[0], scope='conv2')
    x = stack(x, widths[1], heights[1], scope='conv3')
    x = stack(x, widths[2], heights[2], scope='conv4')
    p = pad(x, pad_info(3), name='conv4pool/pad')
    p = max_pool2d(p, 3, 2, padding='VALID', scope='conv4pool/pool')
    x = stack(x, widths[3], heights[3], scope='conv5')
    x = concat([x, p], axis=3, name='concat')
    if stem: return x
    x = reduce_mean(x, [1, 2], name='avgpool')
    x = fc(x, classes, scope='logits')
    x = softmax(x, name='probs')
    return x


def tnet7(x, widths, heights, is_training, classes, stem,
          scope=None, reuse=None):
    x = pad(x, pad_info(3), name='conv1/pad')
    x = conv(x, 32, 3, stride=2, padding='VALID', scope='conv1')
    x = conv(x, 64, 3, scope='conv2')
    x = stack7(x, widths[0], heights[0], scope='conv3')
    x = stack7(x, widths[1], heights[1], scope='conv4')
    x = stack7(x, widths[2], heights[2], scope='conv5')
    x = stack7(x, widths[3], heights[3], scope='conv6')
    if stem: return x
    x = reduce_mean(x, [1, 2], name='avgpool')
    x = fc(x, classes, scope='logits')
    x = softmax(x, name='probs')
    return x


@var_scope('tnet20')
@set_args(__args0__)
def TNet20(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    def stack_fn(x):
        x = _stack(x, 64, 2, stride1=1, scope='conv2')
        x = _stack(x, 64, 3, scope='conv3')
        x = _stack(x, 64, 5, scope='conv4')
        x = _stack(x, 64, 2, scope='conv5')
        return x
    return tnet(x, stack_fn, is_training, classes, stem, scope, reuse)


@var_scope('tnet21')
@set_args(__args0__)
def TNet21(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    def stack_fn(x):
        x = _stack(x, 64, 2, stride1=1, scope='conv2')
        x = _stack(x, 64, 3, scope='conv3')
        x = _stack(x, 128, 5, scope='conv4')
        x = _stack(x, 128, 2, scope='conv5')
        return x
    return tnet(x, stack_fn, is_training, classes, stem, scope, reuse)


@var_scope('tnet22')
@set_args(__args0__)
def TNet22(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    def stack_fn(x):
        x = _stack(x, 64, 3, stride1=1, scope='conv2')
        x = _stack(x, 64, 3, scope='conv3')
        x = _stack(x, 64, 3, scope='conv4')
        x = _stack(x, 64, 3, scope='conv5')
        return x
    return tnet(x, stack_fn, is_training, classes, stem, scope, reuse)


@var_scope('tnet23')
@set_args(__args0__)
def TNet23(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    def stack_fn(x):
        x = _stack(x, 64, 3, stride1=1, scope='conv2')
        x = _stack(x, 64, 4, scope='conv3')
        x = _stack(x, 64, 5, scope='conv4')
        x = _stack(x, 64, 6, scope='conv5')
        return x
    return tnet(x, stack_fn, is_training, classes, stem, scope, reuse)


@var_scope('tnet24')
@set_args(__args0__)
def TNet24(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    def stack_fn(x):
        x = _stack(x, 64, 2, stride1=1, scope='conv2')
        x = _stack(x, 64, 3, scope='conv3')
        x = _stack(x, 64, 3, scope='conv4')
        x = _stack(x, 64, 4, scope='conv5')
        return x
    return tnet(x, stack_fn, is_training, classes, stem, scope, reuse)


@var_scope('tnet30')
@set_args(__args__, weights_regularizer=l2(4e-5))
def TNet30(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet2(x, [64, 64, 64, 64], [3, 4, 6, 3],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet31')
@set_args(__args__)
def TNet31(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet2(x, [64, 64, 128, 128], [3, 4, 6, 3],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet32')
@set_args(__args__)
def TNet32(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet2(x, [64, 64, 64, 64], [4, 4, 4, 4],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet33')
@set_args(__args__)
def TNet33(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet2(x, [64, 64, 64, 64], [4, 5, 6, 7],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet34')
@set_args(__args__)
def TNet34(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet2(x, [64, 64, 64, 64], [3, 4, 4, 5],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet35')
@set_args(__args__, weights_regularizer=l2(2e-4))
def TNet35(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet2(x, [64, 64, 128, 256], [3, 4, 6, 3],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet36')
@set_args(__args__, weights_regularizer=l2(4e-5))
def TNet36(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet2(x, [64, 64, 64, 64], [3, 4, 6, 3],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet37')
@set_args(__args__, weights_regularizer=l2(8e-5))
def TNet37(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet2(x, [64, 64, 128, 256], [3, 4, 6, 3],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet38')
@set_args(__args__, weights_regularizer=l2(4e-5))
def TNet38(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet2(x, [64, 64, 64, 64], [2, 3, 7, 4],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet39')
@set_args(__args__, weights_regularizer=l2(2e-4))
def TNet39(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet2(x, [64, 64, 128, 256], [2, 2, 7, 3],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet392')
@set_args(__args__, weights_regularizer=l2(2e-4))
def TNet392(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet2(x, [64, 64, 128, 192], [2, 2, 7, 7],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet40')
@set_args(__args__)
def TNet40(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet4(x, [64, 64, 64, 64], [3, 4, 6, 3],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet41')
@set_args(__args__)
def TNet41(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet4(x, [64, 64, 128, 128], [3, 4, 6, 3],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet42')
@set_args(__args__)
def TNet42(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet4(x, [64, 64, 64, 64], [4, 4, 4, 4],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet43')
@set_args(__args__)
def TNet43(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet4(x, [64, 64, 64, 64], [4, 5, 6, 7],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet44')
@set_args(__args__)
def TNet44(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet4(x, [64, 64, 64, 64], [3, 4, 4, 5],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet45')
@set_args(__args__)
def TNet45(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet4(x, [64, 64, 128, 256], [3, 4, 6, 3],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet50')
@set_args(__args0__)
def TNet50(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    def stack_fn(x):
        x = _stack(x, 64, 2, stride1=1, scope='conv2')
        x = _stack(x, 128, 3, scope='conv3')
        x = _stack(x, 256, 5, scope='conv4')
        x = _stack(x, 512, 2, scope='conv5')
        return x
    return tnet(x, stack_fn, is_training, classes, stem, scope, reuse)


@var_scope('tnet60')
@set_args(__args__)
def TNet60(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet6(x, [64, 64, 64, 64], [3, 4, 6, 3],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet61')
@set_args(__args__)
def TNet61(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet6(x, [64, 64, 128, 128], [3, 4, 6, 3],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet62')
@set_args(__args__)
def TNet62(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet6(x, [64, 64, 64, 64], [4, 4, 4, 4],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet63')
@set_args(__args__)
def TNet63(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet6(x, [64, 64, 64, 64], [4, 5, 6, 7],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet64')
@set_args(__args__)
def TNet64(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet6(x, [64, 64, 64, 64], [3, 4, 4, 5],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet65')
@set_args(__args__)
def TNet65(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet6(x, [64, 64, 128, 256], [3, 4, 6, 3],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet70')
@set_args(__args__)
def TNet70(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet7(x, [128, 128, 128, 128], [3, 4, 6, 5],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet71')
@set_args(__args__)
def TNet71(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet7(x, [128, 128, 256, 256], [3, 4, 6, 5],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet72')
@set_args(__args__)
def TNet72(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet7(x, [128, 128, 128, 128], [4, 4, 5, 5],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet73')
@set_args(__args__)
def TNet73(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet7(x, [128, 128, 128, 128], [4, 5, 6, 7],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet74')
@set_args(__args__)
def TNet74(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet7(x, [64, 64, 64, 64], [3, 5, 5, 6],
                 is_training, classes, stem, scope, reuse)


@var_scope('tnet75')
@set_args(__args__)
def TNet75(x, is_training=False, classes=1000,
           stem=False, scope=None, reuse=None):
    return tnet7(x, [64, 64, 128, 256], [3, 4, 6, 4],
                 is_training, classes, stem, scope, reuse)


@var_scope('stack')
def _stack(x, filters, blocks, stride1=2, scope=None):
    x = _reduction(x, filters, stride1, scope='block1')
    for i in range(blocks):
        x = _normal(x, filters, scope="block%d" % (i + 2))
    return x


@var_scope('normal')
def _normal(x, filters, kernel_size=3, scope=None):
    shortcut = x
    x = conv(x, filters, 1, scope='1')
    #x = conv(x, filters, kernel_size, scope='2')
    x = sconv(x, None, kernel_size, 1, scope='2')
    x = convbn(x, 4 * filters, 1, scope='3')
    return relu(shortcut + x, name='out')


@var_scope('reduction')
def _reduction(x, filters, stride=2, kernel_size=3, scope=None):
    shortcut = x
    x = conv(x, filters, 1, scope='1')
    x = pad(x, pad_info(kernel_size), name='2/pad')
    #x = conv(x, filters, kernel_size, stride=stride,
    #         padding='VALID', scope='2')
    x = sconv(x, None, kernel_size, 1, stride=stride,
              padding='VALID', scope='2')
    x = convbn(x, 4 * filters, 1, scope='3')
    shortcut = pad(shortcut, pad_info(kernel_size), name='0/pad')
    shortcut = avg_pool2d(shortcut, kernel_size, stride,
                          padding='VALID', scope='0/pool')
    shortcut = convbn(shortcut, 4 * filters, 1, scope='0')
    return relu(shortcut + x, name='out')


@var_scope('stack')
def stack(x, filters, blocks, scope=None):
    x = block(x, filters, 2, scope='reduction')
    for i in range(blocks):
        x = block(x, filters, 1, scope="normal%d" % (i + 1))
    return x


@var_scope('blockpool')
def blockpool(x, filters, stride, kernel_size, scope=None):
    x = pad(x, pad_info(kernel_size), name='0/pad')
    x = max_pool2d(x, kernel_size, stride, padding='VALID', scope='0')
    return conv(x, filters, 1, scope='1')


@var_scope('stack7')
def stack7(x, filters, blocks, scope=None):
    x = block7(x, filters, 2, scope='reduction')
    for i in range(blocks):
        x = block7(x, filters, 1, scope="normal%d" % (i + 1))
    return x


@var_scope('pool7')
def pool7(x, filters, stride, kernel_size, scope=None):
    x = pad(x, pad_info(kernel_size), name='0/pad')
    x = max_pool2d(x, kernel_size, stride, padding='VALID', scope='0')
    x = conv(x, filters, 1, scope='1')
    x = sconv(x, None, 1, 1, scope='2')
    return convbn(x, filters, 1, scope='3')


@var_scope('block7')
def block7(x, filters, stride, kernel_size=3, scope=None):
    if stride > 1:
        shortcut = pool7(x, filters, stride, kernel_size, scope='shortcut')
    else:
        shortcut = x
    x = conv(x, filters, 1, scope='1')
    x = pad(x, pad_info(kernel_size), name='2/pad')
    x = sconv(x, None, kernel_size, 1, stride, padding='VALID', scope='2')
    x = convbn(x, filters, 1, scope='3')
    return relu(shortcut + x, name='out')


@var_scope('pool')
def pool(x, filters, stride, kernel_size, scope=None):
    x = pad(x, pad_info(kernel_size), name='0/pad')
    x = max_pool2d(x, kernel_size, stride, padding='VALID', scope='0')
    x = conv(x, filters, 1, scope='1')
    x = sconv2d(x, None, 1, 1, scope='2')
    return convbn(x, 4 * filters, 1, scope='3')


@var_scope('block')
def block(x, filters, stride, kernel_size=3, scope=None):
    if stride > 1:
        shortcut = pool(x, filters, stride, kernel_size, scope='shortcut')
    else:
        shortcut = x
    x = conv(x, filters, 1, scope='1')
    x = pad(x, pad_info(kernel_size), name='2/pad')
    x = sconv2d(x, None, kernel_size, 1, stride, padding='VALID', scope='2')
    x = convbn(x, 4 * filters, 1, scope='3')
    # return add(shortcut, x, name='out')
    # return swish(shortcut + x, name='out')
    return relu(shortcut + x, name='out')
