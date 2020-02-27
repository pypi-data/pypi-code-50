#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import quaternion
import math

from geometry_msgs.msg import TransformStamped

class Transform:
    # self.matrix = None  # matrix de transfo

    # Constructeur
    def __init__(self, mat=None, quat=None, pos=None, ros_msg=None):
        u""" Constructeur depuis une matrice OU un quaternion et une position."""

        # Ensure that only one populate method is selected:
        conditions = [mat is not None, quat is not None and pos is not None, ros_msg is not None]
        if sum(conditions) > 1:
            raise MultipleInputData

        if mat is not None:
            self.matrix = np.copy(mat)

        elif quat is not None and pos is not None:
            self.from_quatpos(quat, pos)

        elif ros_msg is not None:
            self.from_msg(ros_msg)

        else:
            self.matrix = np.identity(4)

    def from_quatpos(self, quat, pos):
        self.matrix = np.identity(4)
        # (w, x, y, z)
        quat = np.asarray(quat)
        npquat = quaternion.quaternion(quat[0], quat[1],
                                       quat[2], quat[3])
        self.matrix[:3, :3] = quaternion.as_rotation_matrix(npquat)
        self.matrix[:3, 3] = pos

    def from_msg(self, msg):
        self.from_quatpos(pos=[
            msg.transform.translation.x,
            msg.transform.translation.y,
            msg.transform.translation.z,
        ], quat=[
            msg.transform.rotation.w,
            msg.transform.rotation.x,
            msg.transform.rotation.y,
            msg.transform.rotation.z,
        ])

    def to_msg(self, child_frame_id, frame_id='map'):
        msg = TransformStamped()
        quaternion = self.quaternion()
        position = self.position()
        msg.header.frame_id = frame_id
        msg.child_frame_id = child_frame_id
        msg.transform.translation.x = position[0]
        msg.transform.translation.y = position[1]
        msg.transform.translation.z = position[2]
        msg.transform.rotation.x = quaternion.x
        msg.transform.rotation.y = quaternion.y
        msg.transform.rotation.z = quaternion.z
        msg.transform.rotation.w = quaternion.w
        return msg

    def __str__(self):
        u"""Affichage de la transformation."""
        return self.matrix.__str__()

    def __repr__(self):
        u"""Représentation interne de la classe."""
        return self.matrix.__repr__()

    def quat_2_mat(self, quat, pos):
        u"""Conversion quaternion vers matrix."""
        self.matrix[:3, :3] = quaternion.as_rotation_matrix(quat)
        self.matrix[:3, 3] = pos

    def inverse(self):
        u"""Inverse de la transformation."""
        return Transform(np.linalg.inv(self.matrix))

    def __invert__(self):
        u"""Inverse de la transformation inplace."""
        return Transform(np.linalg.inv(self.matrix))

    def __sub__(self, other):
        u"""Renvoie la transformation dans self du repère à l'origine de la transformation other."""
        return self.composition(~other)

    def __isub__(self, other):
        u"""Version 'inplace' de sub."""
        self = self.composition(~other)
        return self

    def composition(self, tr):
        u"""Composition de transformations."""
        return Transform(mat=np.dot(self.matrix, tr.matrix))

    def __mul__(self, other):
        u"""Composition de la transformation de other dans self."""
        return self.composition(other)

    def __imul__(self, other):
        u""""Version 'inplace' de mul."""
        self.matrix = self.matrix.dot(other.matrix)
        return self

    def relative_transform(self, other):
        u"""Transformation de self dans le repère other."""
        return ~other.composition(self)

    def projection(self, pt):
        u"""Transformation d'un point."""
        if (len(pt) == 3):
            return self.matrix.dot(pt + [1])
        else:
            return self.matrix.dot(pt)

    def position(self):
        u"""Extraction de la position depuis matrix."""
        return self.matrix[:3, 3]

    def quaternion(self):
        u"""Extraction du quaternion depuis matrix."""
        return quaternion.from_rotation_matrix(self.matrix)
