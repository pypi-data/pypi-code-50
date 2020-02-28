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


import cv2
import numpy as np
import dlib
from collections import OrderedDict
from tobiiglasses.aoi.dnn.model import AOI_DNN_Model
from tobiiglasses.aoi import AOI

FACIAL_LANDMARKS_IDXS = OrderedDict([
        ("mouth", (48, 67)),
        ("right_eyebrow", (17, 21)),
        ("left_eyebrow", (22, 26)),
        ("right_eye", (36, 41)),
        ("left_eye", (42, 47)),
        ("nose", (27, 34)),
        ("jaw", (0, 16))
        ])

FILENAME_SHAPE_PREDICTOR = 'shape_predictor_68_face_landmarks.dat'
FILENAME_FACE_LANDMARKS = 'facial_landmarks_68markup.jpg'
FACE_FEATURES_POINTS = np.array( [[131, 59], [675, 49], [739, 381], [69, 399] ]) #ids = 17, 26, 13, 3

class Face:

    def __init__(self, left, top, right, bottom, face_landmarks):
        self.__left__ = left
        self.__top__ = top
        self.__right__ = right
        self.__bottom__ = bottom
        self.__landmarks__ = face_landmarks

        self.__mouth__ = face_landmarks['mouth']
        self.__right_eyebrow__ = face_landmarks['right_eyebrow']
        self.__left_eyebrow__ = face_landmarks['left_eyebrow']
        self.__right_eye__ = face_landmarks['right_eye']
        self.__left_eye__ = face_landmarks['left_eye']
        self.__nose__ = face_landmarks['nose']
        self.__jaw__ = face_landmarks['jaw']

    @property
    def top(self):
        return self.__top__

    @property
    def right(self):
        return self.__right__

    @property
    def left(self):
        return self.__left__

    @property
    def bottom(self):
        return self.__bottom__

    @property
    def landmarks(self):
        return self.__landmarks__

    @property
    def mouth(self):
        return self.__mouth__

    @property
    def right_eyebrow(self):
        return self.__right_eyebrow__

    @property
    def left_eyebrow(self):
        return self.__left_eyebrow__

    @property
    def right_eye(self):
        return self.__right_eye__

    @property
    def left_eye(self):
        return self.__left_eye__

    @property
    def jaw(self):
        return self.__jaw__

    @property
    def nose(self):
        return self.__nose__


class FaceLandmarksDetector:

    def __init__(self, filename_shape_predictor):
        self.__detector__ = dlib.get_frontal_face_detector()
        self.__predictor__ = dlib.shape_predictor(filename_shape_predictor)

    def getFaces(self, opencvMat):
        gray = cv2.cvtColor(opencvMat, cv2.COLOR_BGR2GRAY)
        faces = self.__detector__(gray)
        Faces = []
        for face in faces:
            landmarks = self.__predictor__(gray, face)
            FACE_LANDMARKS_XY = {}
            for (name, (i, j)) in FACIAL_LANDMARKS_IDXS.items():
                FACE_LANDMARKS_XY[name] = []
                for k in range(i, j):
                    x = landmarks.part(k).x
                    y = landmarks.part(k).y
                    FACE_LANDMARKS_XY[name].append((x,y))
            Faces.append( Face(face.left(), face.top(), face.right(), face.bottom(), FACE_LANDMARKS_XY) )
        return Faces


class AOI_Face_Model(AOI):

    def __init__(self):
        img_face = cv2.imread(FILENAME_FACE_LANDMARKS)
        super().__init__('face', img_face, FACE_FEATURES_POINTS)
        self.__detector__ = FaceLandmarksDetector(FILENAME_SHAPE_PREDICTOR)
        self.__current_faces__ = None

    def apply(self, opencvMat, ts, gaze_x, gaze_y):
    #def apply(self, aoi_id, ts, gaze_x, gaze_y, detected_features_points):
        faces = self.__detector__.getFaces(opencvMat)
        aoi_id = 'face_'
        i = 0
        for face in faces:
            i+=1
            aoi_id += str(i)
            #cv2.rectangle(opencvMat, (face.left, face.top), (face.right, face.bottom), (0, 0, 255), 2)
            #cv2.polylines(opencvMat, [triangle], True, (0,255,0), thickness=3)
            #rpnts = np.append(rpnts, np.array([[x, y]]), axis=0)
            #cv2.polylines(img, [rpnts], False, (255, 0, 0))
            detected_features_points = np.array([[face.landmarks['right_eyebrow'][0][0], face.landmarks['right_eyebrow'][0][1]],
                                                 [face.landmarks['left_eyebrow'][4][0], face.landmarks['left_eyebrow'][4][1]],
                                                 [face.landmarks['jaw'][13][0], face.landmarks['left_eyebrow'][13][1]],
                                                 [face.landmarks['jaw'][3][0], face.landmarks['left_eyebrow'][3][1]]
                                                ])
            aoi_points = super().apply(aoi_id, ts, gaze_x, gaze_y, detected_features_points)
            cv2.polylines(frame, [aoi_points], False, (0, 255, 0))
            for name in face.landmarks.keys():
                for p in face.landmarks[name]:
                    cv2.circle(opencvMat, (p[0], p[1]), 2, (0, 0, 255), -1)
                #cv2.putText(frame, name, (face.landmarks[name][0][0], face.landmarks[name][0][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)


    def show(self):
        for face in faces:
            cv2.rectangle(opencvMat, (face.left, face.top), (face.right, face.bottom), (0, 0, 255), 2)
            for name in face.landmarks.keys():
                for p in face.landmarks[name]:
                    cv2.circle(opencvMat, (p[0], p[1]), 2, (0, 0, 255), -1)
                cv2.putText(frame, name, (face.landmarks[name][0][0], face.landmarks[name][0][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
