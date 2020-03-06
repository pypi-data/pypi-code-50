#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Christian Heider Nielsen'
__doc__ = r'''

           Created on 06/03/2020
           '''

import cv2
import numpy


def a(original_image,kernel_size=(10, 10)):
  gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
  kernel = numpy.ones(kernel_size, numpy.uint8)
  opening = cv2.morphologyEx(gray_image, cv2.MORPH_OPEN, kernel)
  closing = cv2.morphologyEx(opening,cv2.MORPH_CLOSE,kernel)
  return closing


def gradient():
  # organizing imports
  import cv2
  import numpy as np

  # return video from the first webcam on your computer.
  screenRead = cv2.VideoCapture(0)

  # loop runs if capturing has been initialized.
  while(1):
    # reads frames from a camera
    _, image = screenRead.read()

    # Converts to HSV color space, OCV reads colors as BGR
    # frame is converted to hsv
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # defining the range of masking
    blue1 = np.array([110, 50, 50])
    blue2 = np.array([130, 255, 255])

    # initializing the mask to be
    # convoluted over input image
    mask = cv2.inRange(hsv, blue1, blue2)

    # passing the bitwise_and over
    # each pixel convoluted
    res = cv2.bitwise_and(image, image, mask = mask)

    # defining the kernel i.e. Structuring element
    kernel = np.ones((5, 5), np.uint8)

    # defining the gradient function
    # over the image and structuring element
    gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)

    # The mask and closing operation
    # is shown in the window
    cv2.imshow('Gradient', gradient)

    # Wait for 'a' key to stop the program
    if cv2.waitKey(1) & 0xFF == ord('a'):
      break

  # De-allocate any associated memory usage
  cv2.destroyAllWindows()

  # Close the window / Release webcam
  screenRead.release()

if __name__ == '__main__':
    a()
