# coding: utf-8 
# !/usr/bin/python
"""
@File       :   QRcode.py
@Author     :   jiaming
@Modify Time:   2020/1/13 19:55    
@Contact    :   https://blog.csdn.net/weixin_39541632
@Version    :   1.0
@Desciption :   生成二维码尺寸：Version 10，260x260
"""
import os
import sys
import time
import pretty_errors
import pysnooper
import qrcode
from PIL import Image
from pyzbar import pyzbar
# from app.randomStr import data64, data128, data256


rawPath = os.path.abspath(__file__)
dataPath = rawPath[:rawPath.find('app')] + r'static'


# @pysnooper.snoop()
def load_data():
    """
    读入 static/input.txt 文本内容作为二维码的填充数据
    :return:
    """
    global dataPath
    file = dataPath + r'\_input.txt'
    with open(file, 'r', encoding='utf-8') as f:
        dataString = f.read()
    return dataString


# @pysnooper.snoop()
def create_QRcode():
    """
    创建二维码, 并保存到 static/ 下
    :return: 生成的二维码路径
    """
    print('生成传统二维码')
    # 导入二维码填充数据
    string = load_data()

    # 生成二维码路径以及文件名
    # TIME = time.strftime('_%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    TIME = ''
    FILE_NAME = '\传统二维码'
    FILE = dataPath + FILE_NAME + TIME + ".png"

    # 向二维码中填充数据
    """
    version：值为1~40的整数，控制二维码的大小（最小值是1，是个12×12的矩阵）。 如果想让程序自动确定，将值设置为 None 并使用 fit 参数即可。
    error_correction：控制二维码的错误纠正功能。可取值下列4个常量。
        ERROR_CORRECT_L：大约7%或更少的错误能被纠正。
        ERROR_CORRECT_M（默认）：大约15%或更少的错误能被纠正。
        ROR_CORRECT_H：大约30%或更少的错误能被纠正。
        ERROR_CORRECT_Q:至多能够矫正25%的错误。
    box_size：控制二维码中每个小格子包含的像素数。
    border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4，是相关标准规定的最小值）。
    """
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=4,
    )  # 设置图片格式
    data = string
    qr.add_data(data)
    qr.make(fit=True)
    # 生成二维码
    img = qr.make_image(fill_color='black', back_color='white')
    # img.save(FILE, dpi=(254.0, 254.0))  # 生成图片
    # im = Image.open(FILE)
    # os.remove(FILE)
    # im.save(FILE, dpi=(254.0, 254.0))
    return img, FILE
    # os.remove(QRImagePath)  # 删除图片


# @pysnooper.snoop()
def decode_QRcode(code_img_path):
    """
    :param code_img_path:
    :return: 打印出识别的结果
    """
    decode_data = pyzbar.decode(Image.open(code_img_path), symbols=[
        pyzbar.ZBarSymbol.QRCODE])[0].data.decode('utf-8')
    return decode_data


# @pysnooper.snoop()
def main():
    pass


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    # main()
    path = create_QRcode()
    # print(decode_QRcode(path[0]))
    # print(decode_QRcode("E:\Programmer\PYTHON\graduation_project\static"
    #                "\create_QRcode_2020_01_13_15_04_05.png"))