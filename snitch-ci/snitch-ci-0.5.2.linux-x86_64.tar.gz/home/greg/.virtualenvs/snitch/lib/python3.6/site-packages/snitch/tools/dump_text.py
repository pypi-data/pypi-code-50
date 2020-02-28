#!/usr/bin/python3
"""
Takes a PNG image as parameter and prints the OCR result to the standard output.
"""

import os
import sys

from PIL import Image
import cv2
import pytesseract

SCALE_FACTOR = 2
INTERPOLATION = cv2.INTER_LINEAR
THRESHOLD_METHOD = cv2.THRESH_TOZERO | cv2.THRESH_OTSU


def ocr(filename, autosave=True):
    i = Image.open(filename)
    text = pytesseract.image_to_string(i)

    if autosave:
        with open(os.path.splitext(filename)[0] + '.txt', 'w') as f:
            f.write(text)

    return text


def main():
    if len(sys.argv) < 2:
        print("Missing required parameter")
        sys.exit(1)

    image = sys.argv[1]
    name, ext = os.path.splitext(image)
    processed_image = name + '.processed' + ext

    if not os.path.isfile(image):
        print("File doesn’t exist")
        sys.exit(1)

    # pre processing
    img = cv2.imread(image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_upscale = cv2.resize(img, None, fx=SCALE_FACTOR, fy=SCALE_FACTOR, interpolation=INTERPOLATION)
    img_upscale_thresh = cv2.threshold(img_upscale, 0, 255, THRESHOLD_METHOD)[1]
    cv2.imwrite(processed_image, img_upscale_thresh)

    # actual OCR
    ocr(image)
    print(ocr(processed_image))


if __name__ == '__main__':
    main()
