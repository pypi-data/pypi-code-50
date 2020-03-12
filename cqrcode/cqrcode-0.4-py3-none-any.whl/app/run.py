# coding: utf-8
# !/usr/bin/python
"""
@File       :   run.py
@Author     :   jiaming
@Modify Time:   2020/2/27 19:49
@Contact    :   https://blog.csdn.net/weixin_39541632
@Version    :   1.0
@Desciption :   None
"""
import os
import time
from PIL import Image
import pretty_errors
import pysnooper

from cylinder_qrcode_project.cqrcode.app.static_data import data64, data128, data256, \
    dataPath, standard_module_table, Alphanumeric_mode_table, capacity_of_each_qrcode
from cylinder_qrcode_project.cqrcode.app.prepare_data import data_decode, data_encode, \
    random_bit
from cylinder_qrcode_project.cqrcode.app.prepare_figure import prepare_moudle, expand_fig
from cylinder_qrcode_project.cqrcode.app.load_data_to_figure import load_data
from cylinder_qrcode_project.cqrcode.app.scan_figure import scan_cylinder_qr_code

# 二维码版本
VERSION = 10
# 二维码尺寸
SIZE = (VERSION - 1) * 4 + 21
# 每个像素由 4*4 个像素点构成
BOX = 4
# 边界距离 单位
BOUNDARY = 4
data_list_left = []
data_list_right = []
standard_line = []


def create_plane_qrcode(data='', moudulefig=None):
    """
    生成平面二维码
    :param data:
    :param filePath:
    :return:
    """
    print('数据编码中...')
    s = data_encode(alpha=data)
    data_string = ''
    for i in range(len(data_list_left) // len(s)):
        data_string += s
    data_string += random_bit(length=len(data_list_left)-len(data_string))
    figure, filePath = load_data(figure=moudulefig, data=data_string,
                                 version=VERSION, box=BOX,
                                 data_left=data_list_left, data_right=data_list_right)
    figure.save(filePath, dpi=(254.0, 254.0))  # 生成图片
    print('===\n柱形二维码构建完毕. %s %s \n' % (figure, filePath))
    return figure, filePath


def check(data, version=None):
    """
    检查数据以及version是否正确
    :param data:
    :param version:
    :return:
    """
    # 检查数据是否正确
    for i in data.upper():
        if i not in Alphanumeric_mode_table:
            return False
    if version is None:
        for k, v in capacity_of_each_qrcode.items():
            if v >= len(data):
                return k
    else:
        # 检查版本
        if version < 0 or version > 10:
            return False

    return True


# @pysnooper.snoop()
def main(data=data64, version=None, box=4, Boundary=4, exps=True, rate=1.250):
    """

    :param data:
    :param version:
    :param box:
    :param Boundary:
    :param exps: False 不进行扩展 True 进行扩展
    :param rate: 二维码编程 / 柱体半径
    :return:
    """
    if check(data, version) is False:
        print("数据或版本出现错误！")
        return False
    elif version is None:
        version = check(data, version)
        print('自适应版本二维码: ', version)
    global VERSION, SIZE, BOUNDARY, BOX
    VERSION = version
    SIZE = (VERSION - 1) * 4 + 21
    BOUNDARY = Boundary
    BOX = box
    # 生成二维码识别模板
    global data_list_left, data_list_right, standard_line
    moudle, moudleFilePath, data_left, data_right, std_line = prepare_moudle(
        version=VERSION, size=SIZE)
    data_list_left = data_left
    data_list_right = data_right
    standard_line = std_line
    # 生成平面二维码
    figure, plane_qecode_filePath = create_plane_qrcode(data=data,
                                                   moudulefig=moudle)
    # 识别平面二维码
    scan_cylinder_qr_code(data_left=data_list_left, data_right=data_list_right,
                          result=data, filePath=plane_qecode_filePath)
    # 进行二维码扩展
    if exps is True and 1.5 >= rate > 0:
        expand_figure, expand_filePath = expand_fig(multiplying_power=rate,
                                        version=VERSION,
                                       filePath=plane_qecode_filePath)
        expand_figure.save(expand_filePath, dpi=(254.0, 254.0))  # 生成图片
        return plane_qecode_filePath, expand_filePath
    else:
        print('扩展失败！')
        return plane_qecode_filePath


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    main()