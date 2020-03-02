'''
    线性方程组
    =========================================================================================
    =   直接法：（A为方阵）
    =       1. 高斯消去法/列主元消去法
    =       2. 三角分解法
    =             直接分解法: A = L(DU)   -- Doolittle 分解
    =                         Ax = b --> LUx = b --> 令 Ux = y, 则 Ax = LUx = Ly = b
    =             追赶法:     A = (LD)U   -- crout 分解
    =                         Ax = b --> LDUx = b --> 令 Ux = y, 则 Ax = (LD)Ux = (LD)y = b
    =========================================================================================
'''


import numpy as np


def gauss_elimination(A, b, display=True, mode='normal'):
    '''
    高斯消去法
    :param A:         n 阶系数矩阵 (n, n)
    :param b:         (n, 1)
    :param display:   是否显示矩阵变换信息
    :param mode:      'normal'-高斯消元法   'col'-列主消元法
    :return x:        解向量 - (n, 1)
    '''

    # A 为方阵
    if A.shape[0] == A.shape[1]:
        # 合并A、b为增广矩阵
        amat = np.zeros((A.shape[0],A.shape[1]+1))
        amat[:, 0:A.shape[1]], amat[:, A.shape[1]] = A, b[:,0]
        (row, col) = np.shape(amat)

        if display:
            if mode == 'normal':
                print('=' * 25, '高斯消元法', '=' * 25)
            elif mode == 'col':
                print('=' * 25, '列主消元法', '=' * 25)

        # 消元过程
        for k in range(row-1):                                                  # row-1次消元
            if mode == 'col':
                # 列主消元法
                _max_index = np.abs(amat[:, k]).argmax()
                temp = np.array([0.0] * (col))
                for i in range(col):
                    temp[i] = amat[_max_index, i]
                amat[_max_index, :] = amat[k, :]
                for i in range(col):
                    amat[k, i] = temp[i]
                if display:
                    print(' ====> 第', k+1, '换行：')
                    print(amat)

            m_ik = np.array([0.0]*(row-1-k))                                    # 计算Mik
            if amat[k, k] != 0:
                for c in range(len(m_ik)):
                    m_ik[c] = amat[k+1+c, k] / amat[k, k]                       # 公式
                # 计算消元K次后各元素的值
                for i in range(row-1-k):
                    amat[k+1+i, :] = amat[k+1+i, :] - m_ik[i]*amat[k, :]    # 公式
            else:
                print('==> 主对角线元素为0，不能使用高斯消元法...')
                return 0
            # 输出消元过程
            if display:
                print('==> 第',k+1,'次消元：')
                print(amat)

        # 回代过程 -- 求解向量
        x = np.zeros((row, 1))                                                   # 解向量
        x[row-1, 0] = amat[row-1, col-1] / amat[row-1, col-2]                    # Xn
        for r in range(row-1):
            sum = 0.0
            for c in range(col-2-(row-2-r)):
                sum = sum + amat[row-2-r, (row-2-r)+1+c] * x[(row-2-r)+1+c, 0]

            x[row-2-r, 0] = (amat[row-2-r, col-1] - sum) / amat[row-2-r, row-2-r]

        # 返回解向量
        return x
    else:
        print('==> 矩阵 A 不是n阶矩阵...')
        return 0


def lu(A, b, display=True):
    '''
    :直接三角形分解法 -- 使用的是杜利特尔分解
    :param A:         n 阶系数矩阵 (n, n)
    :param b:
    :param display:   是否显示矩阵变换信息
    :return:          解向量 - (n, 1)
    '''

    m, n = A.shape[0], A.shape[1]
    if m == n:
        # 判断 n-1 阶顺序主子式非零
        no_zero = False
        for i in range(m):
            if i == 0:
                if A[i,i] != 0: no_zero = True
                else: no_zero = False
            else:
                if np.linalg.det(A[0:i, 0:i]) !=0 : no_zero = True
                else: no_zero = False

        if no_zero:
            A = np.array(A, dtype=float)                              # 如果A的所有元素为整数，必须变换A的类型！！！
            # 矩阵LU分解
            L = np.eye(m)                                             # 单位下三角矩阵 L
            for k in range(m-1):
                # 计算Mik
                m_ik = np.array([0.0]*(m-1-k))
                if A[k, k] != 0:
                    for c in range(len(m_ik)):
                        m_ik[c] = A[k+1+c, k] / A[k, k]               # 公式
                        A[k+1+c,:] = A[k+1+c,:] + (-m_ik[c]*A[k,:])
                for i in range(m-1-k):
                    L[i+1+k, k] = m_ik[i]                             # L矩阵

            U = A                                                     # 上三角矩阵 U

            y = np.dot(np.linalg.inv(L), b)    # Ly = b
            x = np.dot(np.linalg.inv(U), y)    # Ux = y

            if display:
                print('='*25, 'LU分解法', '='*25)
                print('==> 矩阵 L (单位下三角矩阵):')
                print(L)
                print('==> 矩阵 U (上三角矩阵);')
                print(U)

            # 返回解向量
            return x
        else:
            print('==> 顺序主子式非零不全为 非零  ...')
    else:
        print('==> 矩阵 A 应为 n阶矩阵...')
        return 0


def purchase(A, b, display=True):
    '''
    :追赶法 -- 使用的是crout分解
    :param A:  系数矩阵
    :param b:
    :return:   返回x、L、D、U
    '''

    m, n = A.shape[0], A.shape[1]
    if m == n:
        # 判断 n-1 阶顺序主子式非零
        no_zero = False
        for i in range(m):
            if i == 0:
                if A[i, i] != 0:
                    no_zero = True
                else:
                    no_zero = False
            else:
                if np.linalg.det(A[0:i, 0:i]) != 0:
                    no_zero = True
                else:
                    no_zero = False
        if no_zero:
            A = np.array(A, dtype=float)
            # 矩阵LU分解
            L = np.eye(m)                                                          # 单位下三角矩阵 L
            for k in range(m-1):
                # 计算Mik
                m_ik = np.array([0.0] * (m-1-k))
                if A[k, k] != 0:
                    for c in range(len(m_ik)):
                        m_ik[c] = A[k+1+c, k] / A[k, k]                             # 公式
                        A[k+1+c, :] = A[k+1+c, :] + (-m_ik[c] * A[k, :])
                for i in range(m-k-1):
                    L[i+1+k, k] = m_ik[i]                                           # L矩阵

            U = A                                                                   # 上三角矩阵 U
            D = np.zeros((m,n))                                                     # 对角矩阵
            for i in range(m):
                if U[i,i] != 0:
                    D[i,i] = U[i,i]
                    U[i,:] = U[i,:] / D[i,i]  # 把U变为单位下三角矩阵

            y = np.dot(np.linalg.inv(np.dot(L,D)), b)     # (LD)y = b
            x = np.dot(np.linalg.inv(U), y)               #  Ux = y

            if display:
                print('=' * 25, '追赶法', '=' * 25)
                print('==> 矩阵 L (单位下三角矩阵):')
                print(L)
                print('==> 矩阵 D (对角矩阵):')
                print(D)
                print('==> 矩阵 U (单位上三角矩阵);')
                print(U)

            # 返回解向量
            return x
        else:
            print('==> 顺序主子式非零不全为 非零  ...')
    else:
        print('==> 矩阵 A 应为 n阶矩阵...')
        return 0

