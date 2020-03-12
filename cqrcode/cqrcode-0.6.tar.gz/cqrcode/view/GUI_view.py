# coding: utf-8
# !/usr/bin/python
"""
@File       :   GUI_view.py
@Author     :   jiaming
@Modify Time:   2020/1/16 18:54
@Contact    :   https://blog.csdn.net/weixin_39541632
@Version    :   1.0
@Desciption :   None
"""
import os
from PIL import Image
import matplotlib.pyplot as plt


rawPath = os.path.abspath(__file__)
dataPath = rawPath[:rawPath.find('view')] + 'static\\'


def window(file0Path='', file1Path='', file2Path=''):
    """

    :param time:
    :return:
    """
    titles = [file0Path, file1Path, file2Path, ""]
    print(titles)
    length = len([i for i in titles if i != ''])
    try:
        for i in range(length):
            plt.subplot(2, 2, i + 1)
            plt.imshow(Image.open(titles[i]))
            if i == 0:
                plt.title("oridinary QRcode")
            elif i == 1:
                plt.title("ac QRcode %s (not expanding)" % file1Path[
                    file1Path.rfind('\\'):][1])
            elif i == 2:
                plt.title("")
            # plt.xticks([])
            # plt.yticks([])
    except (FileExistsError, FileNotFoundError):
        print('文件不存在！')
        return None
    else:
        FILE_NAME = r'\overall_'
        FILE = dataPath + FILE_NAME + ".png"
        plt.savefig(FILE, dpi=1000, bbox_inchs='tight')
        plt.show()


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    window()
