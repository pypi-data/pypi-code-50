# coding: utf-8
# !/usr/bin/python
"""
@File       :   randomStr.py
@Author     :   jiaming
@Modify Time:   2020/2/14 13:14
@Contact    :   https://blog.csdn.net/weixin_39541632
@Version    :   1.0
@Desciption :   集合了字符编码解码函数调用
                只能对于 Alphanumeric_mode_table 中的字符进行编码
                进行编码以及节码

"""
import re
import random
from cqrcode.app.static_data import number_of_bits_in_character_count, \
    Alphanumeric, Alphanumeric_mode_table


def data_encode(alpha=''):
    """
    对传入原生字符串进行检查并编码为一份标准填充比特流。
    :param alpha: Alphanumeric_mode_table 表中的字符
    :return: 原生字符对应的填充比特流
    """
    alpha = alpha.upper()
    for i in alpha:
        if i not in Alphanumeric_mode_table.keys():
            print('ValueError 不支持字符！')
            return False
    alpha_group = ''
    results = ''  # 保存最终比特流

    # 对于原生字符，两两成组，转换为 11 bit
    for i in range(0, len(alpha) - 1, 2):
        alpha_group += alpha[i] + alpha[i + 1] + ' '
        number = Alphanumeric_mode_table[alpha[i]] * 45 + \
            Alphanumeric_mode_table[alpha[i + 1]]
        bits = ''.join(list(bin(number))[2:])
        # 不够 11 bit， 用 0 补齐。
        if len(bits) < 11:
            bits = '0' * (11 - len(bits)) + bits  # 得到原始数据
        results += bits + ' '

    # 对于落单的字符单独编成 6 bit 数据
    if len(alpha) % 2 != 0:
        alpha_group += alpha[-1]
        number = Alphanumeric_mode_table[alpha[-1]]
        bits = ''.join(list(bin(number))[2:])
        if len(bits) < 6:
            bits = '0' * (6 - len(bits)) + bits  # 得到原始数据
        results += bits + ' '

    number_of_bits = ''.join(list(bin(len(alpha)))[2:])
    if len(number_of_bits) < number_of_bits_in_character_count:
        number_of_bits = '0' * \
            (number_of_bits_in_character_count - len(number_of_bits)) + number_of_bits

    print('消除空格前编码后数据： ', Alphanumeric + ' ' + number_of_bits + ' ' + results +
          '0000')
    data_bits = (Alphanumeric + ' ' + number_of_bits + ' ' + results +
                 '0000').replace(' ', '')
    print('消除空格后编码后数据: ', data_bits)
    return data_bits


def cut_text(text, length):
    """
    按照 lenth 的大小分隔 text 字符串
    :param text:
    :param lenth:
    :return: ['123', '456', '12']
    """
    textArr = re.findall('.{' + str(length) + '}', text)
    textArr.append(text[(len(textArr) * length):])
    return textArr


def get_key(value):
    """
    根据字典的值，返回键
    :param value:
    :return:
    """
    for k, v in Alphanumeric_mode_table.items():
        if v == value:
            return k


def data_decode(data_bits='', result=''):
    """
    数据解码，对于原生字符串编码后的数据进行解码
    :param data_bits: 编码后的比特流
    :param result: 解码的正确结果
    :return:
    """
    # 去除编码模式，因为我们默认为字符编码，占 4 bits —— 1101
    # 我们默认是版本 10，故，两个字符占用 11 bits
    data_bits = data_bits[number_of_bits_in_character_count + 4:-4]  # 取出数据位
    print('原生字符串中数据的编码结果：', data_bits)
    print('数据分段显示： ', cut_text(data_bits, 11))  # ['00111001110',
    # '11100111001', '000010']
    data_list = cut_text(data_bits, 11)
    if data_list[-1] == '':
        data_list = data_list[:-1]
    data = ''
    for i in data_list:
        # 11 bit 的数据解码
        if len(i) == number_of_bits_in_character_count:
            alpha1 = get_key(int(i, 2) // 45)
            alpha2 = get_key(int(i, 2) % 45)
            data += alpha1 + alpha2
            print('*解码数据： ', alpha1 + alpha2)
        # 6 bit 的数据解码
        elif len(i) == 6:
            alpha3 = get_key(int(i, 2) % 45)
            data += alpha3
            print('*解码数据： ', alpha3)
        # 否则出错
        else:
            raise RuntimeError('解码运行出错！', i)
    print('##\n最终识别结果： %s\n' % (data,))
    if data == result.upper():
        # print('解码结果：Successed!')
        return True
    else:
        # print('解码结果 Failed!')
        # print(data)
        return False


def random_bit(length=1459):
    """
    返回 length 长度的比特流
    :param length:
    :return:
    """

    # s = """
    # 上邪！我欲与君相知，长命无绝衰。
    # 山无陵，江水为竭，冬雷震震，夏雨雪，天地合，乃敢与君绝。
    # """
    # return encode_string(s)
    randomNum = ''.join([random.choice(['1', '0']) for i in range(length)])
    return randomNum


if __name__ == "__main__":
    data_encode()
