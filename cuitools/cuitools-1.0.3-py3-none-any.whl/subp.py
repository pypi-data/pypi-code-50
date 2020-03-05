import math
import subprocess
import unicodedata


def count_zen(str):
    n = 0
    for c in str:
        wide_chars = "WFA"
        eaw = unicodedata.east_asian_width(c)
        if wide_chars.find(eaw) > -1:
            n += 1
    return n


def width_kana(str):
    all = len(str)  # 全文字数
    zenkaku = count_zen(str)  # 全角文字数
    hankaku = all - zenkaku  # 半角文字数

    return zenkaku * 2 + hankaku


def center_kana(str, size, pad=" "):
    space = size - width_kana(str)
    if space > 0:
        str = pad * int(math.floor(space / 2.0)) + str + pad * int(math.ceil(space / 2.0))
    return str


def get_lines(cmd):
    '''
    :param cmd: str 実行するコマンド.
    :rtype: generator
    :return: 標準出力 (行毎).
    '''
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    while True:
        line = proc.stdout.readline()
        if line:
            yield line

        if not line and proc.poll() is not None:
            break
