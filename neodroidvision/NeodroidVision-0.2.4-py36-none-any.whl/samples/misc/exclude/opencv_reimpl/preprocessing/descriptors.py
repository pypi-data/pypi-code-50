#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Christian Heider Nielsen'
__doc__ = r'''

           Created on 06/03/2020
           '''

def breif():

  import numpy as np
  import cv2
  from matplotlib import pyplot as plt

  img = cv2.imread('simple.jpg',0)

  # Initiate STAR detector
  star = cv2.FastFeatureDetector("STAR")

  # Initiate BRIEF extractor
  brief = cv2.BOWImgDescriptorExtractor("BRIEF")

  # find the keypoints with STAR
  kp = star.detect(img,None)

  # compute the descriptors with BRIEF
  kp, des = brief.compute(img, kp)

  print(brief.getInt('bytes'))
  print(des.shape)

if __name__ == '__main__':

  breif()
