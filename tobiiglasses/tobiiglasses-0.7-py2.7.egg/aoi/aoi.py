#   Copyright (C) 2019  Davide De Tommaso
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>

import numpy as np
import cv2
import matplotlib.path as mplPath

class AOI:

    def __init__(self, label, snapshot_cvMat, features_points):
        self.__label__ = label
        self.__snapshot__ = snapshot_cvMat
        self.__aoi_regions__ = {}
        self.__aoi_hits__ = {}
        self.__features_points__ = features_points

    def apply(self, aoi_id, ts, gaze_x, gaze_y, detected_features_points):
        if not aoi_id in self.__aoi_regions__.keys():
            self.__aoi_regions__[aoi_id] = {}
            self.__aoi_hits__[aoi_id] = {}

        H, status = cv2.findHomography(self.__features_points__, detected_features_points)
        rows, cols, ch = self.__snapshot__.shape
        bounding_box_src = np.array([[0,0,1], [0, cols,1], [rows, cols,1], [rows, 0,1]])
        bounding_box_dst = H.dot(bounding_box_src.T)
        bounding_box_dst = np.array([[bounding_box_dst[0,0], bounding_box_dst[1,0]/bounding_box_dst[2,0]],
                                     [bounding_box_dst[0,1], bounding_box_dst[1,1]/bounding_box_dst[2,1]],
                                     [bounding_box_dst[0,2], bounding_box_dst[1,2]/bounding_box_dst[2,2]],
                                     [bounding_box_dst[0,3], bounding_box_dst[1,3]/bounding_box_dst[2,3]] ])

        self.__aoi_regions__[aoi_id][ts] = bounding_box_dst

        if self.contains(ts, aoi_id, gaze_x, gaze_y):
            p = [gaze_x, gaze_y, 1]
            q = H.dot(p)
            q /= q[2]
            self.__aoi_hits__[aoi_id][ts] = [[q[0], q[1]]]

        return self.getAOIRegions(ts, aoi_id)

    def contains(self, ts, aoi_id, gaze_x, gaze_y):
        res = mplPath.Path(self.__aoi_regions__[aoi_id][ts]).contains_point((gaze_x, gaze_y))
        return res

    def getAOIRegions(self, ts, aoi_id):
        return self.__aoi_regions__[aoi_id][ts]

"""
img_src = cv2.imread('book1.jpg')
pts_src = np.array([[210, 180], [329, 251], [261, 332],[140, 248]]) #detected object points
#im_dst = cv2.imread('book2.jpg')
pts_dst = np.array([[135, 164], [320, 180], [322, 313], [117, 297]]) #features points

a = AOI('book', img_src, pts_dst)
a.apply('book1', 0, 93, 299, pts_src)
"""
