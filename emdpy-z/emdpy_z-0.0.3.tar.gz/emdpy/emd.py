'''
    经验模式分解 (Empirical Mode Decomposition, EMD)
'''

import time

import numpy as np
from scipy.interpolate import splrep, splev

from emdpy.insert_value.cubic_spline import cubic_spline, get_xy_cubic


def find_local_points(x, y):
    '''
    寻找局部极值点, 返回极值点的 (x, y) 坐标点
    :param x:              输入序列 x 轴坐标, numpy.ndarray,  shape=(n, )
    :param y:              输入序列 y 轴坐标, numpy.ndarray,  shape=(n, )
    :return down_points:   极小值点, numpy.ndarray,  shape=(n, 2),  (x, y)
    :return up_points:     极大值点, numpy.ndarray,  shape=(n, 2),  (x, y)
    '''
    
    down_loc_p, up_loc_p = list(), list()
    find_low, find_up = False, False
    for i in range(len(y)):
        if i != len(y)-1:
            if i == 0:
                if y[i] > y[i + 1]:
                    find_low = True
                elif y[i] < y[i + 1]:
                    find_up = True

            if find_low:
                if y[i] < y[i + 1]:
                    down_loc_p.append([x[i], y[i]])
                    find_low, find_up = False, True
                    continue
            if find_up:
                if y[i] > y[i + 1]:
                    up_loc_p.append([x[i], y[i]])
                    find_up, find_low = False, True
                    continue
                    
    return np.array(down_loc_p, dtype=float), np.array(up_loc_p, dtype=float)


def find_zp_num(y):
    '''
    序列过零点个数
    :param y:             输入序列 y 轴坐标, numpy.ndarray,  shape=(n, )
    :return zero_nums:    过零点个数
    '''

    zero_nums = 0
    for i in range(len(y)):
        if i != len(y) - 1:
            if y[i] > 0 and y[i + 1] < 0:
                zero_nums += 1
            elif y[i] < 0 and y[i + 1] > 0:
                zero_nums += 1
            elif y[i] == 0.0:
                zero_nums += 1
            elif y[i] > -1e-10 and y[i] < 1e-8:
                # 解决 计算机浮点 问题
                zero_nums += 1
        else:
            if y[i] == 0.0:
                zero_nums += 1
            elif y[i] > -1e-10 and y[i] < 1e-8:
                # 解决 计算机浮点 问题
                zero_nums += 1

    return zero_nums


def get_xy(poly, nodes, ps):

    in_x = np.linspace(nodes[0, 0], nodes[-1, 0], ps)
    out_y = splev(in_x, poly)

    return in_x, out_y
    


def envelope(x, y, loc_p, mode=None, v1=None, vn=None, solver=None, ps=None):
    '''
    上/下包络线， 返回 (x, y) 坐标点
    :param x:              输入序列 x 轴坐标, numpy.ndarray,  shape=(n, )
    :param y:              输入序列 y 轴坐标, numpy.ndarray,  shape=(n, )
    :param loc_p:          局部极值点, numpy.ndarray,  shape=(n, 2),  (x, y)
    :param mode:           三次样条插值方式
    :param v1:
    :param vn:
    :param solver:         求解线性方程组方法
    :param ps:             包络线 x 轴相邻坐标间距
    :return axis_x:        包络线 x 轴坐标
    :return axis_y         包络线 y 轴坐标
    '''

    # 加上序列起始端点
    nodes = np.zeros((len(loc_p)+2, 2), dtype=float)  
    # 序列开始端点/结束端点
    nodes[0, :] = np.array([x[0], y[0]], dtype=float)          
    nodes[-1, :] = np.array([x[-1], y[-1]], dtype=float)       
    if nodes.shape[0] > 2:
        nodes[1:-1, :] = loc_p
    # ----------------------- 三次样条插值 -----------------------  
    a, b, c, d = cubic_spline(nodes, mode=mode, v1=v1, vn=vn, solver=solver)
    axis_x, axis_y = get_xy_cubic(a, b, c, d, nodes, ps)

    # scipy.interpolate.splrep
    # x, y = nodes[:,0], nodes[:,1]
    # poly = splrep(x, y)
    # axis_x, axis_y = get_xy(poly, nodes, ps=ps)

    return axis_x, axis_y


def get_pending_imf(x, y, mode=None, v1=None, vn=None, solver=None, ps=None):
    '''
    待定 IMF 分量
    :param x:         输入序列 x 轴坐标, numpy.ndarray,  shape=(n, )
    :param y:         输入序列 y 轴坐标, numpy.ndarray,  shape=(n, )
    :param mode:      三次样条插值方式
    :param v1:
    :param vn:
    :param solver:    求解线性方程组方法
    :param ps:        包络线 x 轴相邻坐标间距
    :return p_imf_x:  待定 IMF x 轴坐标
    :return p_imf_y:  待定 IMF y 轴坐标
    '''

    # 输入序列 极值点
    down_loc_p, up_loc_p = find_local_points(x, y)  
    # 上包络线                  
    up_env_x, up_env_y = envelope(x, y, up_loc_p,
                                  mode=mode, v1=v1, vn=vn, solver=solver,
                                  ps=ps) 
    # 下包络线                                         
    down_env_x, down_env_y = envelope(x, y, down_loc_p, 
                                      mode=mode, v1=v1, vn=vn, solver=solver,
                                      ps=ps)    
    # 均值包络线
    mean_x, mean_y = up_env_x, (up_env_y + down_env_y) / 2                 
    # 待定 IMF
    p_imf_x, p_imf_y = up_env_x, (y - mean_y)

    return p_imf_x, p_imf_y


def get_imf_c0(imf_x, imf_y):
    '''
    IMF 约束条件一: IMF 的零点个数与局部极值个数最多相差一个
    :param imf_x:       IMF分量 x 轴坐标
    :param imf_y:       IMF分量 y 轴坐标
    :return imf_c0:     True or False
    '''

    imf_c0 = False
    # IMF 零点个数
    zero_nums = find_zp_num(imf_y)                             
    # IMF 局部极值点
    down_loc_p, up_loc_p = find_local_points(imf_x, imf_y)     
    local_nums = down_loc_p.shape[0] + up_loc_p.shape[0]       # IMF 局部极值点个数

    if np.abs(zero_nums - local_nums) == 0 or np.abs(zero_nums - local_nums) == 1:
        imf_c0 = True
    return imf_c0


def get_imf_c1(imf_x, imf_y,
               mode=None, v1=None, vn=None, solver=None,
               ps=None, c1_error_range=None):
    '''
    IMF 约束条件二: IMF 的上包络线(由局部极大值经过三次样条插值生成)和下包络线(局部极小值)镜面对称
    :param imf_x:         IMF x 轴坐标
    :param imf_y:         IMF y 轴坐标
    :param mode:          三次样条插值方式
    :param v1:
    :param vn:
    :param solver:        解线性方程组方法
    :param ps:            包络线 x 轴相邻坐标间距
    :return imf_c1:       True or False
    '''

    imf_c1 = False
    # IMF 局部极值点
    down_loc_p, up_loc_p = find_local_points(imf_x, imf_y)     
    # IMF 上包络线
    imf_up_env_x, imf_up_env_y = envelope(imf_x, imf_y, up_loc_p,
                                          mode=mode, v1=v1, vn=vn, solver=solver,
                                          ps=ps) 
    # IMF 下包络线
    imf_down_env_x, imf_down_env_y = envelope(imf_x, imf_y, down_loc_p,
                                              mode=mode, v1=v1, vn=vn, solver=solver,
                                              ps=ps)                                     
    
    sum = 0
    for i in range(imf_up_env_y.shape[0]):
        sum = sum + (imf_up_env_y[i]+imf_down_env_y[i])

    if sum>c1_error_range[0] and sum<c1_error_range[1]:
        imf_c1 = True
    return imf_c1


def print_info(info_dict):

    cubic_way = ['自然三次样条插值', '曲率-调准三次样条插值', '夹子三次样条插值', 
                 '末端抛物线三次样条插值', '非节点三次样条插值']

    solver_way = ['高斯消元法', '列主消元法', 'LU 分解法', 'numpy 内置函数']

    print('=' * 25, '经验模式分解 (Empirical Mode Decomposition, EMD)', '=' * 25)
    print('-' * 99)
    print('*', '可选三次样条插值方式:', cubic_way)
    print('*', '可选解线性方程组方式:', solver_way)
    print('-' * 99)
    print('#', '三次样条插值方式:', cubic_way[info_dict['mode']])
    print('#', '解线性方程组方式:', solver_way[info_dict['solver']])
    print('#', 'EMD停止准则-单次迭代次数:', info_dict['max_iter_num'])
    print('#', 'c1 约束误差范围:', info_dict['c1_error_range'])
    print('=' * 99)


def emd(x, y, mode=0, v1=None, vn=None, solver=3,
        ps=None, max_iter_num=1500, c1_error_range=(-0.05, 0.05),
        ):
    '''

    :param x:               输入序列 x 轴坐标, numpy.ndarray, x.shape=(n,)
    :param y:               输入序列 y 轴坐标, numpy.ndarray, x.shape=(n,)
    :param mode:            三次样条插值方式, defaule=1, 自然三次样条插值
    :param v1:
    :param vn:
    :param solver:          解线性方程组方式, default=0, 高斯消元法
    :param ps:              x 轴相邻两点间的距离, ps = len(x)
    :param max_iter_num:
    :param c1_error_range:
    :return:
    '''

    # 输出相关信息
    info_dict = {'mode':mode, 'solver':solver,
                 'max_iter_num':max_iter_num, 'c1_error_range':c1_error_range}
    print_info(info_dict)
    # ================================================================================
    # 保证原始输入序列 x, y 不变
    in_x, in_y = np.array([a for a in x]), np.array([a for a in y])
    # ================================================================================
    st_time = time.clock()                                 # 开始计时
    imfs, res= list(), None                                # 存储 IMF 分量, 残差分量
    imf_x, imf_y = None, None
    # EMD 分解
    print('==> EMD 分解过程')
    imf_num = 0                                            # IMF 序号
    while True:
        imf_num += 1                                       
        print('====> IMF ', imf_num)
        # 输入序列 是否 满足 IMF 约束， 若满足，直接结束; 若不满足，则进行 EMD 分解
        # IMF 约束
        x_c0 = get_imf_c0(in_x, in_y)
        x_c1 = get_imf_c1(in_x, in_y,
                          mode=mode, v1=v1, vn=vn, solver=solver,
                          ps=ps, c1_error_range=c1_error_range)
        if x_c0 and x_c1:
            imfs.append([in_x, in_y]) 
            res = np.array([0, 0])
            print('======> 原始输入序列满足 IMF 条件，无残差分量...')
            break
        # ------------------------------------------------------------
        iter_num = 0                             # 输入序列经过 iter_num 次迭代得到 IMF
        imf_c0, imf_c1 = False, False
        _x, _y = np.array([a for a in in_x]), np.array([a for a in in_y])
        while not (imf_c0 and imf_c1):
            # 待定 IMF 
            p_imf_x, p_imf_y = get_pending_imf(_x, _y, mode=mode,
                                               v1=v1, vn=vn, solver=solver,
                                               ps=ps)                          
            # IMF 约束
            imf_c0 = get_imf_c0(p_imf_x, p_imf_y)
            imf_c1 = get_imf_c1(p_imf_x, p_imf_y,
                                mode=mode, v1=v1, vn=vn, solver=solver,
                                ps=ps, c1_error_range=c1_error_range)

            iter_num += 1                       # 迭代次数 +1
            if not (imf_c0 and imf_c1):
                # 若待定 IMF 不满足条件, 则以该 IMF 作为 输入序列
                _x, _y = p_imf_x, p_imf_y
            else:
                imf_x, imf_y = p_imf_x, p_imf_y
                break
            # --------------- 终止条件 ---------------
            if iter_num == max_iter_num:
                if not (imf_c0 and imf_c1):
                    print('======>', imf_num, '达到最大迭代次数，不满足IMF条件...')
                    break
                else:
                    print('======>', imf_num, '达到最大迭代次数，满足IMF条件...')
                    break
        # ------------------------------------------------------------
        if imf_c0 and imf_c1:
            print('======> IMF', imf_num, ' ' * 5, '经过', iter_num, '次迭代...')
            # 保存 IMF
            imfs.append([imf_x, imf_y])
            # 原始输入序列 - IMF, x 轴坐标不变
            in_x, in_y = imf_x, in_y - imf_y
            # --------------- 终止条件 ---------------
            if iter_num == max_iter_num:
                print('======> 满足终止条件...')
                res = np.array([0, 0])
                break
        else:
            # 残差分量
            res = np.array([in_x, in_y])
            break
    # ================================================================================
    end_time = time.clock()                                # 结束计时
    print('=' * 99)
    print('====> 程序运行时间:', ' ' * 5, round(end_time-st_time, 2), '秒')
    print('====> EMD 分解统计:', ' ' * 5, 'IMF分量:', len(imfs), '个')
    # ================================================================================
    # 返回值
    return np.array(imfs), np.array(res)
