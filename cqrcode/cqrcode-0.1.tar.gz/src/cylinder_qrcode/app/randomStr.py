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

"""
import random
import re
from random import Random

number_of_bits_in_character_count = 11  # 字符数据的 bit 值, 两个字符合起来由 11 bit表示
Alphanumeric = '0010'   # 编码样式前缀 —— 字符编码
# 对应关系表
Alphanumeric_mode_table = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 17,
    'I': 18,
    'J': 19,
    'K': 20,
    'L': 21,
    'M': 22,
    'N': 23,
    'O': 24,
    'P': 25,
    'Q': 26,
    'R': 27,
    'S': 28,
    'T': 29,
    'U': 30,
    'V': 31,
    'W': 32,
    'X': 33,
    'Y': 34,
    'Z': 35,
    ' ': 36,
    '$': 37,
    '%': 38,
    '*': 39,
    '+': 40,
    '-': 41,
    '.': 42,
    '/': 43,
    ':': 44,
}
# 数据举例
data64 = "XFSB1wQ2XPKBsVTYdChtz9Gyx4PuYokVvbGX7ai1FYmFHRs2SDIIz39KAiGxkfxL"
data128 = "2rtw17PoD6jt6b1hZJ2HZJS1eWL1n9gXd4GXEa6DgWPQn0ou19YcxsJiTmJJitfr0VeGxbOxMyqncIj7Nw8y7M8woA6pIzQMLqeNWg1lcWsoNuLuCbdzaH2FNWvqsMi8"
data256 = "dMAdeVq2N0S4Htz1hJU5A139n0PeP8URNFEQglTUC4zCZdWpxccC4xGhKWDTR7qVtYl0bN6TlvWPbgFSkqpI1QjM1wEXtFn5I24kMxszm0HAIxvXN7gwkwBGdZ2Joz0uY6WFs9ib6vNwKT20arBeYijwHRrYhfwAjX3Lrc3JEZxpYja4qQp93R7dwfgkLR3cvPop90ryVSdqhQxYFRrhZlpGBaNoXd0HNXI4AjD8NZz3jtOKTIfEGuvpo6qrLGoV"


def data_encode(alpha=data256):
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


def cut_text(text, lenth):
    """
    按照 lenth 的大小分隔 text 字符串
    :param text:
    :param lenth:
    :return: ['123', '456', '12']
    """
    textArr = re.findall('.{' + str(lenth) + '}', text)
    textArr.append(text[(len(textArr) * lenth):])
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


def random_str(randomlength=8):
    """
    返回 randomlength 长度的随机 chars 字符串
    :param randomlength:
    :return:
    """
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return len(str), str


def encode_string(s):
    """
    将字符串编码为比特流
    :param s:
    :return:
    """
    return ''.join([bin(ord(c)).replace('0b', '') for c in s])


def decode_string(s):
    """
    将比特流解码成字符串
    :param s:
    :return:
    """
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])


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
