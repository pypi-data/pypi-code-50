# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import copy
import sqlite3
from datetime import datetime
from ezcad.utils.dbsqlite import native_scalar
from ezcad.utils.logger import logger
from gopoint.dbsqlite import DBSQLite as DataBase
from .utils import TEXT_STYLE


class DBSQLite(DataBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def create_tables(self):
        self.ct_geometry_type()
        self.ct_point_vertexes()
        self.ct_text_style()
        self.ct_text_labels()

    def ct_text_style(self):
        logger.info('Creating table text_style (if not exists)')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS text_style
            (object_name TEXT PRIMARY KEY, size INTEGER, angle REAL,
            anchorX REAL, anchorY REAL, scaleX REAL, scaleY REAL,
            colorR INTEGER, colorG INTEGER, colorB INTEGER, colorA INTEGER)
            ''')

    def ct_text_labels(self):
        logger.info('Creating table text_labels (if not exists)')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS text_labels
            (object_name TEXT, chunkID INTEGER, arr ARRAY,
            PRIMARY KEY (object_name, chunkID))
            ''')

    def save_lbl(self, object_name, vertexes, to_project=False,
        to_object=False):
        if to_project:
            self.save_lbl_to_project(object_name, vertexes)
        if to_object:
            self.save_lbl_to_object(object_name, vertexes)

    def save_lbl_to_project(self, object_name, vertexes):
        if vertexes['labelLMT'] < vertexes['labelLST']:
            logger.info("Skip saving label array")
            return
        logger.info('Saving label array')
        self.remove_lbl(object_name)
        labelArray = vertexes['label']
        values = DBSQLite.__split_array(object_name, labelArray)
        self.cursor.executemany("INSERT INTO text_labels VALUES \
            (?,?,?)", values)
        vertexes['labelLST'] = datetime.now()

    def save_lbl_to_object(self, object_name, vertexes):
        logger.info('Saving label array')
        self.remove_lbl(object_name)
        labelArray = vertexes['label']
        values = DBSQLite.__split_array(object_name, labelArray)
        self.cursor.executemany("INSERT INTO text_labels VALUES \
            (?,?,?)", values)

    def save_tsty(self, object_name, text_style):
        logger.info('Saving text style')
        size = text_style['font_size']
        angle = text_style['angle']
        ax, ay = text_style['anchor']
        sx, sy = text_style['scale']
        r, g, b = text_style['color'][:3]
        alpha = text_style['opacity']
        size = float(native_scalar(size))
        angle = float(native_scalar(angle))
        ax = float(native_scalar(ax))
        ay = float(native_scalar(ay))
        sx = float(native_scalar(sx))
        sy = float(native_scalar(sy))
        r = int(native_scalar(r))
        g = int(native_scalar(g))
        b = int(native_scalar(b))
        alpha = int(native_scalar(alpha))
        try:  # insert for new object, update for existing object
            values = (object_name, size, angle, ax, ay, sx, sy, r, g, b, alpha)
            self.cursor.execute("INSERT INTO text_style VALUES \
                (?,?,?,?,?,?,?,?,?,?,?)", values)
        except sqlite3.IntegrityError:
            values = (size, angle, ax, ay, sx, sy, r, g, b, alpha, object_name)
            self.cursor.execute("UPDATE text_style \
                SET size = ?, angle = ?, anchorX = ?, anchorY = ?, \
                scaleX = ?, scaleY = ?, \
                colorR = ?, colorG = ?, colorB = ?, colorA = ? \
                WHERE object_name = ?", values)

    def load_lbl(self, object_name):
        logger.info('Loading labels')
        values = (object_name,)  # key to find
        self.cursor.execute("SELECT chunkID, arr FROM text_labels \
            WHERE object_name = ?", values)
        labels = DBSQLite.__cat_array(self.cursor)
        return labels

    def load_tsty(self, object_name):
        logger.info('Loading text style')
        values = (object_name,)  # key to find
        self.cursor.execute("SELECT * FROM text_style WHERE \
            object_name = ?", values)
        (name, size, angle, ax, ay, sx, sy, r, g, b, alpha) = \
            self.cursor.fetchone()
        text_style = copy.deepcopy(TEXT_STYLE)
        text_style['font_size'] = size
        text_style['angle'] = angle
        text_style['anchor'] = (ax, ay)
        text_style['scale'] = (sx, sy)
        text_style['color'] = (r, g, b, alpha)
        text_style['opacity'] = alpha
        return text_style

    def remove_lbl(self, object_name):
        values = (object_name,)
        self.cursor.execute("DELETE from text_labels \
            WHERE object_name = ?", values)

    def remove_tsty(self, object_name):
        values = (object_name,)
        self.cursor.execute("DELETE FROM text_style WHERE \
            object_name = ?", values)

    def remove_tables(self, object_name):
        logger.info('Removing from DB: {}'.format(object_name))
        self.remove_geom(object_name)
        self.remove_vtx(object_name)
        self.remove_tsty(object_name)
        self.remove_lbl(object_name)
