import cv2
import numpy as np


def judge_similar_area(img, x1, y1, x2, y2):
    """
    判断区域(x1, y1, x2, y2)是否相似（是否轮廓突变，边界为轮廓突变）
    :param im: 背景图片
    :param x1:  区域起始列
    :param y1:  区域起始行
    :param x2:  区域结束
    :param y2:  区域结束行
    :return:    True:该区域为空白区域, False:该区域非空白区域
    """

    # img = cv2.cvtColor(np.asarray(im), cv2.COLOR_RGBA2BGRA)
    height, width = img.shape[:2]
    if x1 < 0 or y1 < 0 or x2 > width - 1 or y2 > height - 1 or x1 > x2 or y1 > y2:
        # 是否超出im范围
        return False

    crop = img[y1:y2, x1:x2]
    crop = cv2.Canny(crop, 100, 200)  # 检查阈值边缘差距
    contours, _ = cv2.findContours(crop, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        return False
    return True


def spreading_area(img, rect, align, offset, direct):
    """
    对一个区域，向上下移动，找到安全的区域（区域不突变）
    :param rect:
    :param align:
    :param offset: 2
    :param direct: 0 y，1 x
    :return:
    """
    limit = img.shape[direct]
    index_1, index_2 = (0, 2) if direct else (1, 3)
    while True:
        is_similar_area = judge_similar_area(img, *rect)
        if is_similar_area:
            if align == 0:  # 做对齐
                ymax = rect[index_2] + offset
                if ymax > limit - 1:
                    break
                rect[index_2] = ymax
            elif align == 1:
                ymin, ymax = rect[index_1] - offset, rect[index_2] + offset
                if ymin < 0 or ymax > limit - 1:
                    break
                rect[index_1] = ymin
                rect[index_2] = ymax
            else:
                ymin = rect[index_1] - offset
                if ymin < 0:
                    rect[index_1] = ymin
                rect[index_1] = ymin
        else:
            rect[index_1] = max(rect[index_1], 0)
            rect[index_2] = min(rect[index_2], limit - 1)
            break
    return rect


def multi_spreading_area(img, rect, factor_info):
    while True:
        for index, factor in factor_info.items():
            rect[index] += factor * (1 if index >= 2 else -1)
        is_similar_area = judge_similar_area(img, *rect)
        if not is_similar_area:
            break
    return rect
