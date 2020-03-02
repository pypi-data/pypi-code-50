'''
    三次样条插值
'''


import numpy as np
import matplotlib.pyplot as plt
from emdpy.eqs.lineqs_direct import gauss_elimination, lu


def cubic_spline(nodes, mode=0, v1=0, vn=0, solver=0):
    '''
    自然三次样条插值 --- 使用端点条件 “自然样条条件”
    :param nodes:    插值节点, np.array([[], [], []])
    :param mode:
        0:  自然三次样条插值
        1:  曲率-调准三次样条插值
        2:  夹子三次样条插值
        3： 末端抛物线三次样条插值
        4:  非节点三次样条插值
    :param v1:       用于 mode=1, 2
    :param vn:       用于 mode=1, 2
    :param solver:   解线性方程组方法
        0:  高斯消元法
        1:  列主消元法
        2:  LU 分解法
        3:  numpy 内置函数
    :return a,b,c,d:   返回 三次多项式组中每个多项式系数, 有 len(nodes)-1 个多项式
    '''

    n = len(nodes)
    # ------------------ dx, dy ------------------
    dx = nodes[1:, 0] - nodes[0:-1, 0]             # numpy.ndarray, n-1
    dy = nodes[1:, 1] - nodes[0:-1, 1]             # numpy.ndarray, n-1
    # ------------------ 端点条件不同，构造的 A 和 B 也不同 ------------------
    A, B = None, None
    if mode == 0:
        # print('='*25, '自然三次样条插值', '='*25)
        # ----------- B -----------
        B = np.zeros((n, 1))
        # for i in range(n):
        #     if i == 0 or i == n-1:
        #         B[i, 0] = 0
        #     else:
        #         B[i, 0] = 3 * ((dy[i]/dx[i]) - (dy[i-1]/dx[i-1]))
        B[1:-1, :] = (3 * ((dy[1:]/dx[1:]) - (dy[0:-1]/dx[0:-1]))).reshape(n-2,1)
        B[0, :], B[-1, :] = 0, 0

        # ----------- A -----------
        A = np.zeros((n, n))
        k = 0
        for i in range(n):
            if i == 0 or i == n-1:
                A[i, i] = 1
            else:
                A[i, i-1] = dx[k]
                A[i, i] = 2 * dx[k] + 2 * dx[k+1]
                A[i, i+1] = dx[k+1]
                k += 1
    elif mode == 1:
        # print('='*25, '曲率-调准三次样条插值', '='*25)
        # B
        B = np.zeros((n, 1))
        for i in range(n):
            if i == 0:
                B[i, 0] = v1
            elif i == n-1:
                B[i, 0] = vn
            else:
                B[i, 0] = 3 * ((dy[i]/dx[i]) - (dy[i-1]/dx[i-1]))
        # A
        A = np.zeros((n, n))
        k = 0
        for i in range(n):
            if i == 0 or i == n-1:
                A[i, i] = 2
            else:
                A[i, i-1] = dx[k]
                A[i, i] = 2 * dx[k] + 2 * dx[k+1]
                A[i, i+1] = dx[k+1]
                k += 1
    elif mode == 2:
        # print('='*25, '夹子三次样条插值', '='*25)
        # B
        B = np.zeros((n, 1))
        for i in range(n):
            if i == 0:
                B[i, 0] = 3 * (dy[0] / (dx[0]-v1))
            elif i == n-1:
                B[i, 0] = 3 * ((vn-dy[-1]) / dx[-1])
            else:
                B[i, 0] = 3 * ((dy[i]/dx[i]) - (dy[i-1]/dx[i-1]))
        # A
        A = np.zeros((n, n))
        k = 0
        for i in range(n):
            if i == 0 :
                A[i, i], A[i, i+1] = 2*dx[0], dx[0]
            elif i == n-1:
                A[i, i-1], A[i, i] = dx[-1], 2*dx[-1]
            else:
                A[i, i-1] = dx[k]
                A[i, i] = 2 * dx[k] + 2 * dx[k+1]
                A[i, i+1] = dx[k+1]
                k += 1
    elif mode == 3:
        # print('='*25, '末端抛物线三次样条插值', '='*25)
        # B
        B = np.zeros((n, 1))
        for i in range(n):
            if i == 0 or i == n-1:
                B[i, 0] = 0
            else:
                B[i, 0] = 3 * ((dy[i]/dx[i]) - (dy[i-1]/dx[i-1]))
        # A
        A = np.zeros((n, n))
        k = 0
        for i in range(n):
            if i == 0:
                A[i, i], A[i, i+1] = 1, -1
            elif i == n-1:
                A[i, i-1], A[i, i] = 1, -1
            else:
                A[i, i-1] = dx[k]
                A[i, i] = 2 * dx[k] + 2 * dx[k+1]
                A[i, i+1] = dx[k+1]
                k += 1
    elif mode == 4:
        # print('='*25, '非节点三次样条插值', '='*25)
        # B
        B = np.zeros((n, 1))
        for i in range(n):
            if i == 0 or i == n-1:
                B[i, 0] = 0
            else:
                B[i, 0] = 3 * ((dy[i]/dx[i]) - (dy[i-1]/dx[i-1]))
        # A
        A = np.zeros((n, n))
        k = 0
        for i in range(n):
            if i == 0 :
                A[i, i], A[i, i+1], A[i, i+2] = dx[1], -dx[0]-dx[1], dx[0]
            elif i == n-1:
                A[i, i-2], A[i, i-1], A[i, i] = dx[-1], -dx[-1]-dx[-2], dx[-2]
            else:
                A[i, i-1] = dx[k]
                A[i, i] = 2 * dx[k] + 2 * dx[k+1]
                A[i, i+1] = dx[k+1]
                k += 1
    else:
        print('error...')
    # ------------------ 系数 c, Ac = B ------------------
    c_ = None
    if solver == 0:
        c_ = gauss_elimination(A, B, display=False, mode='normal')
    elif solver == 1:
        c_ = gauss_elimination(A, B, display=False, mode='col')
    elif solver == 2:
        c_ = lu(A, B, display=False)
    elif solver == 3:
        c_ = np.linalg.solve(A, B)
    else:
        print('error in cubic_spline...')
    c_ = c_.reshape(1, c_.shape[0])
    c = c_[0]                                         # numpy.ndarray, n

    # ------------------ 系数 a ------------------
    a = nodes[:, 1]                                   # numpy.ndarray, n
    # ------------------ 系数 b, d ------------------
    # for i in range(n-1):
    #     d.append((c[i+1]-c[i]) / (3*dx[i]))
    #     b.append((dy[i]/dx[i]) - (dx[i]/3) * (2*c[i]+c[i+1]))
    d = (c[1:]-c[0:-1]) / (3*dx)                      # numpy.ndarray, n-1
    b = (dy/dx) - (dx/3) * (2*c[0:-1]+c[1:])          # numpy.ndarray, n-1

    return a, b, c, d


def poly(a, b, c, d, x, k, nodes):

    # k = 0, ..., n-1
    f_val = a[k] + b[k]*(x-nodes[k, 0]) + c[k]*(x-nodes[k, 0])**2 + d[k]*(x-nodes[k, 0])**3
    return f_val


def get_xy_cubic(a, b, c, d, nodes, ps):
    '''
    获取插值端点内所有点
    :param polys:   三次多项式组
    :param nodes:   插值节点
    :param ps:      x 轴上 点 的个数
    :return:
    '''

    in_x = np.linspace(nodes[0, 0], nodes[-1, 0], ps)
    # x 分组，用于不同的 poly
    x_group = list()
    for i in range(len(nodes)):
        if i != len(nodes)-1:
            temp = []
            for _x in in_x:
                if _x >= nodes[i, 0] and _x<nodes[i+1, 0]:
                    temp.append(_x)
            if i == len(nodes)-2:
                temp.append(in_x[-1])
            x_group.append(np.array(temp, dtype=float))
    # y
    y_group = list()
    for i in range(len(x_group)):
        f_val = poly(a, b, c, d, x_group[i], i, nodes)
        y_group.append(f_val)
    
    return np.concatenate(x_group, axis=0), np.concatenate(y_group, axis=0)


def plot_cubic_spline(_x, _y, nodes):

    # 三次样条曲线
    plt.plot(_x, _y, 'k-')
    # 插值节点
    for i in range(len(nodes)):
        plt.scatter(nodes[i, 0], nodes[i, 1], marker='x')

    plt.xlim(nodes[0, 0], nodes[len(nodes) - 1, 0])
    plt.ylim(_y[_y.argmin()], _y[_y.argmax()])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['curve', 'nodes'])
    plt.show()

