# coding: utf-8 
# !/usr/bin/python
"""
@File       :   load_data_to_figure.py
@Author     :   jiaming
@Modify Time:   2020/3/9 15:05    
@Contact    :   https://blog.csdn.net/weixin_39541632
@Version    :   1.0
@Desciption :   填充二维码
"""
import os
from PIL import Image

from cqrcode.app.static_data import dataPath

data_list_left = []
data_list_right = []

BOX = -1
VERSION = -1


def load_data_left(data='', figure=None):
    """
    向模板中（左侧）写入数据
    :return:
    """
    if data == '':
        print('数据为空，错误！')
        return False
    index = 0
    # figure = Image.open(filePath)
    figure = figure.convert('RGBA')
    for j in data:
        x, y = data_list_left[index]
        if j == '1':
            for k in range(0, BOX, 1):
                for z in range(0, BOX, 1):
                    figure.putpixel((x + k, y + z), (0, 0, 0))
        elif j == '0':
            for k in range(0, BOX, 1):
                for z in range(0, BOX, 1):
                    figure.putpixel((x + k, y + z), (255, 255, 255))
        index += 1
    fileName = "左侧填充结果.png"
    figure.save(dataPath + fileName, "png")
    return dataPath + fileName


def load_data_right(data='', filePath=''):
    """
    向模板中（右侧）写入数据
    :return:
    """
    if data == '':
        print('数据为空，错误！')
        return False
    index = 0
    figure = Image.open(filePath)
    figure = figure.convert('RGBA')
    for z in data:
        x, y = data_list_right[index]
        if z == '1':
            for i in range(0, BOX, 1):
                for j in range(0, BOX, 1):
                    figure.putpixel((x + i, y + j), (0, 0, 0))
        elif z == '0':
            for i in range(0, BOX, 1):
                for j in range(0, BOX, 1):
                    figure.putpixel((x + i, y + j), (255, 255, 255))
        index += 1
    fileName = str(VERSION)+"填充结果.png"
    os.remove(filePath)
    return figure, dataPath + fileName


def load_data(figure=None, data='', version=-1, box=-1, data_left=-1,
              data_right=-1):
    """

    :param data:
    :param box:
    :param data_left:
    :param data_right:
    :return:
    """
    print('data 长度: ', len(data))
    print('data_left 长度: ', len(data_left))
    print('data_right 长度: ', len(data_right))
    global BOX, data_list_left, data_list_right, VERSION
    BOX = box
    data_list_left = data_left
    data_list_right = data_right
    VERSION = version

    if data == '':
        print('数据为空，不合法！')
        return False

    print('平面二维码左侧数据的比特流: ', data)
    print('左侧写入中...')
    left_filePath = load_data_left(data, figure)
    print('平面二维码右侧数据的比特流: ', data)
    print('右侧写入中...')
    result_figure, result_filePath = load_data_right(data, left_filePath)

    # result_figure.save(result_filePath)
    return result_figure, result_filePath