# coding: utf-8
# !/usr/bin/python
"""
@File       :   cylinder_qrcode.py
@Author     :   jiaming
@Modify Time:   2020/2/21 15:52
@Contact    :   https://blog.csdn.net/weixin_39541632
@Version    :   1.0
@Desciption :
            准备二维码模板。
            拉伸图片。
"""
import math
from copy import deepcopy
from PIL import Image

from cqrcode.app.static_data import dataPath, standard_module_table

# 二维码版本
VERSION = -1
# 二维码尺寸
SIZE = -1
# 每个像素由 4*4 个像素点构成
BOX = 4
# 边界距离 单位
BOUNDARY = 4

# 标线坐标
standard_line = []
# 写入数据的坐标
data_list_right = []
data_list_left = []


def draw_position_detection_pattern(figure=None, key=-1):
    """
    绘制position detection pattern
    :param img:
    :return:
    """
    coordinates = []
    # 绘制第一个图案
    for i in range(7):
        coordinates.append((BOUNDARY+i, BOUNDARY))
    for i in range(6):
        coordinates.append((BOUNDARY, BOUNDARY+i))
        coordinates.append((BOUNDARY+6, BOUNDARY+i))
    for i in range(7):
        coordinates.append((BOUNDARY+i, BOUNDARY+6))
    for i in range(3):
        for j in range(3):
            coordinates.append((BOUNDARY+2+i, BOUNDARY+2+j))
    # 绘制第二个图案
    column = BOUNDARY + SIZE - 7
    for i in range(7):
        coordinates.append((column + i, BOUNDARY))
    for i in range(6):
        coordinates.append((column, BOUNDARY + i))
        coordinates.append((column + 6, BOUNDARY + i))
    for i in range(7):
        coordinates.append((column + i, BOUNDARY + 6))
    for i in range(3):
        for j in range(3):
            coordinates.append((column + 2 + i, BOUNDARY + 2 + j))

    for value in coordinates:
        i, j = value
        for k in range(0, BOX, 1):
            for z in range(0, BOX, 1):
                figure.putpixel((i * BOX + k, j * BOX + z), (0, 0, 0))
    if key != -1:
        for i in range(BOUNDARY, BOUNDARY+8):
            for j in range(BOUNDARY, BOUNDARY+8):
                for k in range(0, BOX, 1):
                    for z in range(0, BOX, 1):
                        figure.putpixel((i * BOX + k, j * BOX + z), (0, 0,0))
        for i in range(BOUNDARY + SIZE - 8, BOUNDARY + SIZE):
            for j in range(BOUNDARY, BOUNDARY+8):
                for k in range(0, BOX, 1):
                    for z in range(0, BOX, 1):
                        figure.putpixel((i * BOX + k, j * BOX + z), (0, 0,0))
    return figure


def draw_alignment_pattern(figure=None, key=-1):
    """
    绘制 alignment pattern
    :param img:
    :return:
    """
    if VERSION <= 3:
        pass
    elif 3 < VERSION <= 6:
        x = (SIZE+BOUNDARY*2) // 2
        y = (SIZE+BOUNDARY*2) // 2
        for k in range(0, BOX, 1):
            for z in range(0, BOX, 1):
                figure.putpixel((x * BOX + k, y * BOX + z), (0, 0, 0))
        temp_list = []
        for i in range(-2, 2):
            temp_list.append((x + i, y - 2))
        for i in range(-2, 3):
            temp_list.append((x - 2, y + i))
            temp_list.append((x + 2, y + i))
        for i in range(-2, 2):
            temp_list.append((x + i, y + 2))
        for value in temp_list:
            i, j = value
            for k in range(0, BOX, 1):
                for z in range(0, BOX, 1):
                    figure.putpixel((i * BOX + k, j * BOX + z), (0, 0, 0))
        if key != -1:
            for i in range(-2, 3):
                for j in range(-2, 3):
                    for k in range(0, BOX, 1):
                        for z in range(0, BOX, 1):
                            figure.putpixel(((x+i) * BOX + k, (y+j) * BOX + z),
                                            (0, 0, 0))
    elif 6 < VERSION <= 10:
        _, tuple = standard_module_table[VERSION]
        x1, x2, x3 = [i + BOUNDARY for i in tuple]
        # print(x1, x2, x3)
        l = [(x1, x2), (x2, x1), (x2, x3), (x3, x2), (x2, x2)]
        for value in l:
            x, y = value
            for k in range(0, BOX, 1):
                for z in range(0, BOX, 1):
                    figure.putpixel((x * BOX + k, y * BOX + z), (0, 0, 0))
            temp_list = []
            for i in range(-2, 2):
                temp_list.append((x+i, y-2))
            for i in range(-2, 3):
                temp_list.append((x-2, y+i))
                temp_list.append((x+2, y+i))
            for i in range(-2, 2):
                temp_list.append((x+i, y+2))
            for value in temp_list:
                i, j = value
                for k in range(0, BOX, 1):
                    for z in range(0, BOX, 1):
                        figure.putpixel((i * BOX + k, j * BOX + z), (0, 0, 0))
        if key != -1:
            for value in l:
                x, y = value
                for i in range(-2, 3):
                    for j in range(-2, 3):
                        for k in range(0, BOX, 1):
                            for z in range(0, BOX, 1):
                                figure.putpixel(((x+i) * BOX + k, (y+j) * BOX + z),
                                                (0, 0, 0))
    else:
        return False
    return figure


def draw_mask(figure=None):
    """

    :param figure:
    :return:
    """
    temp_list = []
    for i in range(2*BOUNDARY+SIZE):
        for j in range(BOUNDARY):
            temp_list.append((i, j))
            temp_list.append((i, j+SIZE+BOUNDARY))
    for i in range(BOUNDARY):
        for j in range(BOUNDARY, BOUNDARY+SIZE):
            temp_list.append((i, j))
            temp_list.append((i+BOUNDARY+SIZE, j))
    for value in temp_list:
        i, j = value
        for k in range(0, BOX, 1):
            for z in range(0, BOX, 1):
                figure.putpixel((i * BOX + k, j * BOX + z), (0, 0, 0))
    draw_position_detection_pattern(figure, key=1)
    draw_alignment_pattern(figure, key=1)
    return figure


def stand_point(figure=None):
    """
    标定数据点
    :return:
    """
    global data_list_left, data_list_right
    data_list_left = []
    data_list_right = []
    img_array = figure.load()
    for i in range(BOUNDARY, SIZE + BOUNDARY, 1):
        for j in range(BOUNDARY, SIZE + BOUNDARY, 1):
            if img_array[i * BOX, j * BOX] == (255, 255, 255):
                # figure.putpixel((i*BOX, j*BOX), (0, 0, 0)) # 写入单个像素
                if i < (BOUNDARY + SIZE) // 2 + 2:
                    figure.putpixel((i * BOX, j * BOX), (255, 0, 0))
                    data_list_left.append((i * BOX, j * BOX))
                    # for k in range(0, BOX, 1):
                    #     for z in range(0, BOX, 1):
                    #         figure.putpixel((i * BOX + k, j*BOX + z), (255, 255, 0))
    data_list_left = list(reversed(data_list_left))  # 生成左侧编码位需要
    for i in range(BOUNDARY, SIZE + BOUNDARY, 1):
        for j in range(BOUNDARY, SIZE + BOUNDARY, 1):
            if img_array[i * BOX, j * BOX] == (255, 255, 255):
                # figure.putpixel((i*BOX, j*BOX), (0, 0, 0)) # 写入单个像素
                if i > (BOUNDARY + SIZE) // 2 + 2:
                    figure.putpixel((i * BOX, j * BOX), (255, 0, 0))
                    data_list_right.append((i * BOX, j * BOX))
                    # for k in range(0, BOX, 1):
                    #     for z in range(0, BOX, 1):
                    #         figure.putpixel((i * BOX + k, j*BOX + z), (255, 0, 0))
    print('data_list_right: ', list(data_list_right))
    print('data_list_right 长度: ', len(list(data_list_right)))
    print('data_list_left: ', list(data_list_left))
    print('data_list_left 长度: ', len(list(data_list_left)))
    return figure


def prepare_moudle(version=-1, size=-1):
    """
    准备相应的二维码识别模板
    仅支持version 0~10
    :param version: 二维码版本
    :param size:
    :return: 二维码数据模板,左侧坐标，右侧坐标, 标线坐标
    """
    global VERSION, SIZE
    VERSION = version
    SIZE = size

    number = version

    if VERSION > 10 or VERSION < 0:
        return False
    length_of_qrcode = SIZE * BOX + BOUNDARY * BOX * 2
    img = Image.new('RGB', (length_of_qrcode, length_of_qrcode),
                    (255, 255, 255))
    print('白板生成成功！')
    img.save(dataPath + '_白板.png')  # 不允许注释
    img = draw_position_detection_pattern(img)
    img = draw_alignment_pattern(figure=img)
    moudle = deepcopy(img)
    img.save(dataPath + str(number) + '二维码识别模板.png')
    moudleFilePath = dataPath + str(number) + '二维码识别模板.png'
    print('二维码识别模板生成成功！')
    mask = draw_mask(img)
    print('二维码识别掩码生成成功！')
    mask.save(dataPath + str(number) + '二维码识别掩码.png')
    mask = stand_point(mask)
    mask.save(dataPath + str(number) + '二维码填充效果.png')
    # moudle.show()
    return moudle, moudleFilePath, data_list_left, data_list_right, standard_line


def expand_fig(multiplying_power=1.250, version=-1, filePath=''):
    """
    水平拉伸图片
    1 mm = 10 像素
    1 像素 = 0.1 mm
    :param multiplying_power:
    :return:
    """

    print('进行二维码拓展 %s...' % (str(multiplying_power), ))
    INPUT_IMAGE = Image.open(filePath)
    w1, h1 = INPUT_IMAGE.size
    img_array = INPUT_IMAGE.load()
    if w1 != h1:
        print('扩展图片失败！')
        return None
    # print(w1, h1)  # 260 260
    pixel = w1
    a = -1   # 平面二维码数据点距离中线位置(像素) multiplying_power=1.250 时，a = 115 极限
    l = 350  # 固定值（mm）
    r = 0.1 * h1 / multiplying_power  # 圆柱体半径（mm）
    x = [0.1 * i for i in range(0, pixel // 2, 1)]  # （mm）
    y = []
    for i in x:
        # 将移动的单位换算为像素
        y.append((math.asin(((r + l) / r) * math.sin(math.atan(i / l))
                            ) - math.atan(i / l)) * r * 10 - i * 10)
    y.reverse()
    # print(len(y), '\n', y)

    # 读入空白图片
    OUT_IMAGE = Image.open(dataPath + '_白板.png')
    # 扩展图片尺寸
    OUT_IMAGE = OUT_IMAGE.resize(
        (2 * round(y[0]) + pixel, pixel), Image.ANTIALIAS)
    # print(OUT_IMAGE.SIZE[0], OUT_IMAGE.SIZE[1])  # 284 260
    w2, h2 = OUT_IMAGE.size
    # 向左侧写入数据
    z = 0
    for i in range(0, w1 // 2, 1):
        for j in range(0, h1, 1):
            if img_array[i, j] == (0, 0, 0, 255):
                OUT_IMAGE.putpixel(
                    (i - round(y[z]) + round(y[0]), j), (0, 0, 0))
        z += 1
    z = 0
    # 向右侧写入数据
    for i in range(w1 - 1, w1 // 2, -1):
        for j in range(0, h1, 1):
            if img_array[i, j] == (0, 0, 0, 255):
                OUT_IMAGE.putpixel(
                    (i + round(y[z]) + round(y[0]), j), (0, 0, 0))
        z += 1
    out_img_array = OUT_IMAGE.load()
    # 填补空白
    for i in range(w2):
        for j in range(h2):
            if out_img_array[i, j] == (0, 0, 0) and out_img_array[i + 2, j] == (0, 0, 0):
                OUT_IMAGE.putpixel((i + 1, j), (0, 0, 0))
    filePath = dataPath + str(version) + '扩展图片.png'
    print('扩展二维码成功 %s %s.' % (OUT_IMAGE, filePath))
    return OUT_IMAGE, filePath


if __name__ == "__main__":
    pass
