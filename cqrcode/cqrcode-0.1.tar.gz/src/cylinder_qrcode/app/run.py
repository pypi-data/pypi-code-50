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
from app.cylinder_qrcode import data_list_left, data_list_right, \
    encode_left, encode_right, BOX, BOUNDARY, SIZE, expand_figure
from app.randomStr import data64, data128, data_encode, data_decode, \
    random_bit, number_of_bits_in_character_count


rawPath = os.path.abspath(__file__)
dataPath = rawPath[:rawPath.find('app')] + 'static\\'


def create_plane_qrcode(data=''):
    """
    生成平面二维码
    :param data:
    :return:
    """
    print('数据编码中...')
    s = data_encode(data)
    data_string = ''
    for i in range(len(data_list_left) // len(s)):
        data_string += s
    data_string += random_bit(len(data_list_left) - len(data_string))
    # data_string = s
    print('平面二维码左侧数据的比特流: ', data_string)
    print('左侧写入中...')
    fileName = encode_left(data_string)

    time.sleep(2)

    data_string = ''
    for i in range(len(data_list_right) // len(s)):
        data_string += s
    data_string += random_bit(len(data_list_right) - len(data_string))
    # data_string = s
    print('平面二维码右侧数据的比特流: ', data_string)
    print('右侧写入中...')
    file = encode_right(data_string, fileName)
    file[0].save(file[1])

    time.sleep(2)

    print('===\n柱形二维码构建完毕. %s \n' % (file,))
    return file[1]


def scan_left_qrcode(filePath, result=''):
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


def scan_right_qrcode(filePath, result=''):
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


def scan_cylinder_qr_code(filePath=dataPath + 'data.png', result=''):
    """
    扫描识别柱面二维码
    :param filePath:
    :return:
    """
    if scan_left_qrcode(filePath, result) or scan_right_qrcode(filePath, result):
        print('##\n识别成功\n')
    else:
        print('##\n识别失败\n')


# @pysnooper.snoop()
def main():
    data = input('请输入编码数据(仅支持标准字符集):')
    file = create_plane_qrcode(data=data)
    answer = input('未延展二维码生成成功（请在 static/ 目录下查看）\n输入二维码边长与柱体半径比例或者 q 退出:')
    if answer != 'q':
        expand_figure(multiplying_power=float(answer), filePath=file)
        print('延展后二维码生成成功！')
    else:
        scan_cylinder_qr_code(file, result=data)
    # img, file = capture()
    # img.save(file)
    # deal_fig(file, threshold=20)
    # os.remove(file)


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    main()
