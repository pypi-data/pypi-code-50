#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Christian Heider Nielsen'
__doc__ = r'''

           Created on 06/03/2020
           '''

from pathlib import Path

import numpy
import cv2
from PIL.Image import Image
from matplotlib import pyplot as plt


def main(img1, img2, detector=cv2.ORB()):

  # find the keypoints and descriptors with detector
  kp1, des1 = detector.detectAndCompute(img1, None)
  kp2, des2 = detector.detectAndCompute(img2, None)

  if False:
    # BFMatcher with default params
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    # Apply ratio test
    good = []
    for m, n in matches:
      if m.distance < 0.75 * n.distance:
        good.append([m])

    # cv2.drawMatchesKnn expects list of lists as matches.
    img3 = Image()
    cv2.drawMatchesKnn(img1, kp1, img2, kp2, good,img3,flags=2)

    plt.imshow(img3)
  elif True:
    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)[:10]

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches, flags=2)

    plt.imshow(img3)

  else:
    FLANN_INDEX_KDTREE = 0
    MIN_MATCH_COUNT = 10
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1,des2,k=2)

    # store all the good matches as per Lowe's ratio test.
    good = []
    for m,n in matches:
      if m.distance < 0.7*n.distance:
        good.append(m)
    if len(good)>MIN_MATCH_COUNT:
      src_pts = numpy.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
      dst_pts = numpy.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

      M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
      matchesMask = mask.ravel().tolist()

      h,w = img1.shape
      pts = numpy.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
      dst = cv2.perspectiveTransform(pts,M)

      img2 = cv2.polylines(img2,[numpy.int32(dst)],True,255,3, cv2.LINE_AA)

    else:
      print("Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT))
      matchesMask = None

    draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                       singlePointColor = None,
                       matchesMask = matchesMask, # draw only inliers
                       flags = 2)

    img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)

    plt.imshow(img3, 'gray')



print('fock')
root_path = Path('/home/heider/Projects/Alexandra/Python/vision/samples/misc/exclude/opencv_reimpl'
                 '/matching/')

img1_ = cv2.imread(str(root_path / 'aau-city-2.jpg'), 0)  # queryImage
img2_ = cv2.imread(str(root_path / 'aau-city-1.jpg'), 0)  # trainImage

print('fock')
main(img1_, img2_)
print('fock')
plt.show()
