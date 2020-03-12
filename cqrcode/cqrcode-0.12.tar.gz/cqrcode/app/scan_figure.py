# coding: utf-8 
# !/usr/bin/python
"""
@File       :   scan_figure.py
@Author     :   jiaming
@Modify Time:   2020/3/9 14:41    
@Contact    :   https://blog.csdn.net/weixin_39541632
@Version    :   1.0
@Desciption :   None
"""
import cv2
import os
import time
import numpy as np
from PIL import Image

from cqrcode.app.prepare_data import data_decode
from cqrcode.app.static_data import dataPath, \
    number_of_bits_in_character_count, coordinate_no_expanding_table

data_list_left = []
data_list_right = []


def scan_left_qrcode(filePath=None, result=''):
    """
    扫描左侧数据
    :param filePath:
    :return:
    """
    print('===\n开始扫描左侧.\n')
    figure = Image.open(filePath)
    img_array = figure.load()
    # 识别左侧区域
    temp = ''
    for i in range(number_of_bits_in_character_count):
        if img_array[data_list_left[4+i][0], data_list_left[4+i][1]]  == (
                255, 255, 255, 255):
            temp += '0'
        elif img_array[data_list_left[4+i][0], data_list_left[4+i][1]]  == (
                0, 0, 0, 255):
            temp += '1'
    print('左侧识别字符个数： ', int(temp, 2))
    if int(temp, 2) % 2 == 0:
        length = int(temp, 2) // 2 * 11
    else:
        length = (int(temp, 2) - 1) // 2 * 11 + 6
    print('左侧识别字符数据 bit 数： ', length)
    temp = ''
    for i in range(length + 4 + 4 + number_of_bits_in_character_count):
        if img_array[data_list_left[i][0], data_list_left[i][1]] == (
                255, 255, 255, 255):
            temp += '0'
        elif img_array[data_list_left[i][0], data_list_left[i][1]] == (
                0, 0, 0, 255):
            temp += '1'
    print('左侧识别字符数据的 bit 流: ', temp)
    return data_decode(temp, result)


def scan_right_qrcode(filePath=None, result=''):
    """
    扫描右侧数据
    :param filePath:
    :return:
    """
    print('===\n开始扫描右侧.\n')
    figure = Image.open(filePath)
    img_array = figure.load()
    # 识别右侧区域
    temp = ''
    for i in range(number_of_bits_in_character_count):
        if img_array[data_list_right[4 + i][0], data_list_right[4 + i][1]] == (
                255, 255, 255, 255):
            temp += '0'
        elif img_array[
            data_list_right[4 + i][0], data_list_right[4 + i][1]] == (
                0, 0, 0, 255):
            temp += '1'
    print('右侧识别字符个数： ', int(temp, 2))
    if int(temp, 2) % 2 == 0:
        length = int(temp, 2) // 2 * 11
    else:
        length = (int(temp, 2) - 1) // 2 * 11 + 6
    print('右侧识别字符数据 bit 数： ', length)
    temp = ''
    for i in range(length + 4 + 4 + number_of_bits_in_character_count):
        if img_array[data_list_right[i][0], data_list_right[i][1]] == (
                255, 255, 255, 255):
            temp += '0'
        elif img_array[data_list_right[i][0], data_list_right[i][1]] == (
                0, 0, 0, 255):
            temp += '1'
    print('右侧识别字符数据的 bit 流: ', temp)
    return data_decode(temp, result)


def scan_cylinder_qr_code(data_left=[], data_right=[],
                          result='', filePath=None, real=False):
    """

    :param data_list_left:
    :param data_list_right:
    :param result:
    :param filePath:
    :return:
    """
    global data_list_left, data_list_right
    #TODO: 默认： BOX=4, BOUNDARY=4
    BOX = 4
    BOUNDARY = 4
    dict_version2size = {}
    if real is True:
        size_table = [((i-1)*4+21)*BOX+2*BOUNDARY*BOX for i in [j for j in
                                                            range(0, 11, 1)]]
        for i in range(0, 11):
            dict_version2size[i] = size_table[i]
        print(dict_version2size)
        # {0: 100, 1: 116, 2: 132, 3: 148, 4: 164, 5: 180, 6: 196, 7: 212, 8: 228, 9: 244, 10: 260}
        img = Image.open(filePath)
        w, h = img.size
        for k, v in dict_version2size.items():
            if v == w:
                version = k
                data_list_left, data_list_right = coordinate_no_expanding_table[version]
                if scan_left_qrcode(filePath, result) or scan_right_qrcode(
                        filePath, result):
                    print('##\n识别完毕\n')
                else:
                    print('##\n识别完毕\n')
                break
        else:
            print('扫描出错！')
    else:
        global data_list_left, data_list_right
        data_list_left = data_left
        data_list_right = data_right
        if scan_left_qrcode(filePath, result) or scan_right_qrcode(filePath, result):
            print('##\n识别成功\n')
        else:
            print('##\n识别失败\n')


def binary_corrode_fig(filePath=dataPath + 'target.png', threshold=200):
    """
    二值化图片
    英文路径！
    :return:
    """
    if os.path.exists(filePath) is False:
        print("文件不存在！")
        return None
    # 二值化
    print('图像二值化...')
    time.sleep(1)
    img = cv2.imread(filePath, 0)
    ret, thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    cv2.imwrite(dataPath + 'binary_figure.jpg', thresh)
    # 腐蚀膨胀
    print('图像腐蚀...')
    time.sleep(1)
    print('图像膨胀...')
    time.sleep(1)
    img = cv2.imread(dataPath + 'binary_figure.jpg', 0)
    kernel = np.ones((4, 4), np.uint8)
    erode = cv2.erode(img, kernel)
    # img = cv2.imread(dataPath+'binary_figure.jpg', 0)
    kernel = np.ones((3, 3), np.uint8)
    new = cv2.dilate(erode, kernel, iterations=1)
    cv2.imwrite(dataPath + 'erode_expanding_figure.jpg', new)
    os.remove(dataPath + 'binary_figure.jpg')
    # 二值化
    print('图像二值化...')
    time.sleep(1)
    img = cv2.imread(dataPath + 'erode_expanding_figure.jpg', 0)
    ret, thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    cv2.imwrite(dataPath + '图像二值化腐蚀膨胀.jpg', thresh)
    os.remove(dataPath + 'erode_expanding_figure.jpg')