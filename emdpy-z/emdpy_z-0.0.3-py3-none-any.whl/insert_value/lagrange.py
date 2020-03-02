'''
    拉格朗日插值法
'''

import numpy as np
from sympy.abc import x,y,z


def lagrange(nodes, display=True):
    '''
    拉格朗日插值法
    :param nodes:     插值节点, np.array([[], [], []])
    :param display:
    :return f:        多项式函数
    '''

    # 拉格朗日插值基函数
    base_funcs = []
    for i in range(len(nodes)):
        base_func = 1
        den, num = 1, 1    # 分子  分母
        for j in range(len(nodes)):
            if i != j:
                den = den * (x - nodes[j, 0])
                num = num * (nodes[i, 0] - nodes[j, 0])
                base_func = round(1/num, 6) * den
        base_funcs.append(base_func)

    # 拉格朗日插值函数
    f = 0
    for i in range(len(nodes)):
        f = f + nodes[i, 1] * base_funcs[i]

    if display:
        print('='*25, '拉格朗日插值法', '='*25)
        print('==> 拉格朗日插值基函数')
        counter = 0
        for base_func in base_funcs:
            print('====> L', counter, ':', base_func)
            counter += 1

    # 返回多项式函数
    return f
