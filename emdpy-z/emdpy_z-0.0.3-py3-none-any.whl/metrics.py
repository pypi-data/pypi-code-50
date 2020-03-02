'''
    评价指标
'''

import numpy as np


def systhes(imfs, res, is_std=True, mean=None, std=None):
    '''
    合成 IMF分量 和 残差分量
    :param imfs:
    :param res:
    :param is_std:
    :param mean:
    :param std:
    :return:
    '''

    synthesis = 0
    for i in range(imfs.shape[0]):
        synthesis += imfs[i, 1, :]
    synthesis += res[1]
    if is_std:
        synthesis = synthesis * std + mean
    return synthesis


def cal_abs_error(y, imfs, res, is_std=True, mean=None, std=None):

    syn = systhes(imfs, res, is_std=is_std, mean=mean, std=std)
    abs_error = np.abs(syn - y)
    return abs_error.sum()

