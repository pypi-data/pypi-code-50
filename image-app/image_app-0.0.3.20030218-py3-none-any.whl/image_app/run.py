import time
from PIL import Image
import cv2
import numpy as np

rect = list((2032, 370, 2249, 416))
image = Image.open('../example/11123.png')
img = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGBA2BGRA)
start_time = time.time()

# from image_app import area
#
# # print(area.move_single_y_to_safe_area(image, rect, is_up=True))
# # print(area.move_single_y_to_safe_area(image, rect, is_up=False))
# print(area.resize_x_to_largest_area(img, rect, align=1))   #0.1534895896911621

import area_py_s as area_py

# print(area_py.resize_x_to_largest_area(img, rect, align=2))
print(rect, id(rect))
# rect1 = area_py.relarge_area(img, rect, 2, offset=2, direct=1)
# print(rect1, id(rect1))
# print(area_py.relarge_area(img, rect, 0, 2, 1))
# print(area_py.relarge_area(img, rect, 2, 2, 0))
# print(area_py.relarge_area(img, rect, 0, 2, 0))
# print(area_py.relarge_area(img, rect, 2, 2, 1))

area_py.muli_relarge_area(img, rect, factor_info={0: -2, 2: 1})
print(time.time() - start_time)

cv2.rectangle(img, (rect[0], rect[1]), (rect[2], rect[3]), (120, 78, 255), 2)
cv2.imwrite('test.jpg', img)
