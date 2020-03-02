'''
    线性方程组
    =====================================================
    =   迭代法：（A为方阵）
    =       1. 雅可比迭代法
    =       2. 高斯—塞德尔迭代法
    =       3. 逐次超松弛迭代法
    =====================================================
'''


import numpy as np


def jacobi(A, b, x0, epochs=5, display=True):
    '''
    雅可比迭代法
    :param A:       系数矩阵
    :param b:
    :param x0:      初始解
    :param epochs:  迭代次数
    :return:        解向量x
    '''

    x = x0                                                    # 解向量
    A = np.array(A, dtype=float)
    # 判断是否为非奇异矩阵
    if np.linalg.det(A) != 0.0 or np.linalg.det(A) != 0:
        (m, n) = np.shape(A)                                  # 系数矩阵的行数、列数
        D = np.zeros((m, n))                                  # 对角矩阵 D
        for i in range(m):
            D[i, i] = A[i, i]
        M = D                                                 # 分裂矩阵 M
        I = np.eye(m)                                         # 单位矩阵 I
        B = I - np.dot(np.linalg.inv(M), A)                   # 迭代矩阵 B
        # 判断迭代法是否收敛：p(B)<1
        eigvals = np.linalg.eigvals(B)                        # 迭代矩阵 B 的所有特征值
        pB = np.max(np.abs(eigvals))                          # 迭代矩阵 B 的谱半径

        if pB < 1 - 1e-06:                                    # 由于浮点运算存在误差，为了满足条件，减去一个误差
            # 正式进入雅可比迭代法计算
            f = np.dot(np.linalg.inv(M), b)                   # 原象
            for i in range(epochs):
                x = np.dot(B, x) + f

            if display:
                print('='*25, '雅可比迭代法', '='*25)
                print('==> 分裂矩阵 M')
                print(M)
                print('==> 迭代矩阵 B')
                print(B)
                print('==> 迭代矩阵 B 的谱半径')
                print(round(pB, 6))

            # 返回值
            return x
        else:
            print('==> 雅可比迭代法发散，不可以使用...')
    else:
        print('==> 输入矩阵为奇异矩阵...')


def gs(A, b, x0, epochs=5, display=True):
    '''
    高斯—塞德尔迭代法
    :param A:      系数矩阵
    :param b:
    :param x0:     初始解
    :param epochs:  迭代次数
    :return:       解向量x、分裂矩阵M、迭代矩阵B
    '''

    x = x0                                                    # 解向量
    A = np.array(A, dtype=float)
    # 判断是否为非奇异矩阵
    if np.linalg.det(A) != 0.0 or np.linalg.det(A) != 0:
        (m, n) = np.shape(A)                                  # 系数矩阵的行数、列数
        D = np.zeros((m, n))                                  # 对角矩阵 D
        L = np.zeros((m, n))                                  # 下三角矩阵 L -- 元素为相反数
        for i in range(m):
            D[i, i] = A[i, i]
        for i in range(m):
            for j in range(n):
                if i >= j:
                    L[i, j] = -A[i, j]
        M = D - L                                             # 分裂矩阵 M
        I = np.eye((m))                                       # 单位矩阵 I
        B = I - np.dot(np.linalg.inv(M), A)                   # 迭代矩阵 B
        # 判断迭代法是否收敛：p(B)<1
        eigvals = np.linalg.eigvals(B)                        # 迭代矩阵 B 的所有特征值
        pB = np.max(np.abs(eigvals))                          # 迭代矩阵 B 的谱半径
        if pB < 1 - 1e-06:                                    # 由于浮点运算存在误差，为了满足条件，减去一个误差
            # 正式进入高斯—塞德尔迭代法计算
            f = np.dot(np.linalg.inv(M), b)                   # 原象
            for i in range(epochs):
                x = np.dot(B, x) + f

            if display:
                print('='*25, '高斯—塞德尔迭代法', '='*25)
                print('==> 分裂矩阵 M')
                print(M)
                print('==> 迭代矩阵 B')
                print(B)
                print('==> 迭代矩阵 B 的谱半径')
                print(round(pB, 6))

            # 返回值
            return x
        else:
            print('==> 高斯—塞德尔迭代法发散，不可以使用...')
    else:
        print('==> 输入矩阵为奇异矩阵...')


def sor(A, b, x0, epochs=5, w=1.5, display=True):
    '''
    :逐次超松弛迭代法
    :param A:
    :param b:
    :param x0:
    :param epochs:
    :param w:
    :return:
    '''

    x = x0  # 解向量
    A = np.array(A, dtype=float)  #
    # 判断是否为非奇异矩阵
    if np.linalg.det(A) != 0.0 or np.linalg.det(A) != 0:
        (m, n) = np.shape(A)                                   # 系数矩阵的行数、列数
        D = np.zeros((m, n))                                   # 对角矩阵 D
        L = np.zeros((m, n))                                   # 下三角矩阵 L
        for i in range(m):
            D[i, i] = A[i, i]
        for i in range(m):
            for j in range(n):
                if i >= j:
                    L[i, j] = -A[i, j]
        M = (D - w * L) * (1 / w)                              # 分裂矩阵 M
        I = np.eye(m)                                          # 单位矩阵 I
        B = I - np.dot(np.linalg.inv(M), A)                    # 迭代矩阵 B
        # 判断迭代法是否收敛：p(B)<1
        eigvals = np.linalg.eigvals(B)                         # 迭代矩阵 B 的所有特征值
        pB = np.max(np.abs(eigvals))                           # 迭代矩阵 B 的谱半径
        if pB < 1 - 1e-06:  # 由于浮点运算存在误差，为了满足条件，减去一个误差
            # 正式进入逐次超松弛迭代法计算
            f = np.dot(np.linalg.inv(M), b)                    # 原象
            for i in range(epochs):
                x = np.dot(B, x) + f

            if display:
                print('='*25, '逐次超松弛迭代法', '='*25)
                print('==> 分裂矩阵 M')
                print(M)
                print('==> 迭代矩阵 B')
                print(B)
                print('==> 迭代矩阵 B 的谱半径')
                print(round(pB, 6))

            # 返回值
            return x
        else:
            print('==> 高斯—塞德尔迭代法发散，不可以使用...')
    else:
        print('==> 输入矩阵为奇异矩阵...')

