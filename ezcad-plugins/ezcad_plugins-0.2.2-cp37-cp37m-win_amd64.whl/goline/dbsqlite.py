# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import copy
import sqlite3
from datetime import datetime
from ezcad.utils.dbsqlite import native_scalar
from ezcad.utils.logger import logger
from gopoint.dbsqlite import DBSQLite as DataBase
from .utils import LINE_STYLE


class DBSQLite(DataBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def create_tables(self):
        DataBase.create_tables(self)
        self.ct_line_style()
        self.ct_line_connection()

    def ct_line_style(self):
        logger.info('Creating table line_style (if not exists)')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS line_style
            (object_name TEXT PRIMARY KEY, width INTEGER,
            colorR INTEGER, colorG INTEGER, colorB INTEGER, colorA INTEGER)
            ''')

    def ct_line_connection(self):
        logger.info('Creating table line_connection (if not exists)')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS line_connection
            (object_name TEXT, chunkID INTEGER, arr ARRAY,
            PRIMARY KEY (object_name, chunkID))
            ''')

    def save_lsty(self, object_name, line_style):
        logger.info('Saving line style')
        width = line_style['width']
        r, g, b = line_style['color'][:3]
        alpha = line_style['opacity']
        width = int(native_scalar(width))
        r = int(native_scalar(r))
        g = int(native_scalar(g))
        b = int(native_scalar(b))
        alpha = int(native_scalar(alpha))
        try:  # insert for new object, update for existing object
            values = (object_name, width, r, g, b, alpha)
            self.cursor.execute("INSERT INTO line_style VALUES \
                (?,?,?,?,?,?)", values)
        except sqlite3.IntegrityError:
            values = (width, r, g, b, alpha, object_name)
            self.cursor.execute("UPDATE line_style SET width = ?, \
                colorR = ?, colorG = ?, colorB = ?, colorA = ? \
                WHERE object_name = ?", values)

    def save_lcon(self, object_name, vertexes, to_project=False,
                  to_object=False):
        if to_project:
            self.save_lcon_to_project(object_name, vertexes)
        if to_object:
            self.save_lcon_to_object(object_name, vertexes)

    def save_lcon_to_project(self, object_name, vertexes):
        if vertexes['conLMT'] < vertexes['conLST']:
            logger.info("Skip saving line connection")
            return
        logger.info('Saving line connection')
        self.remove_lcon(object_name)
        vertexConnect = vertexes['connect']
        values = DBSQLite.__split_array(object_name, vertexConnect)
        self.cursor.executemany("INSERT INTO line_connection VALUES \
            (?,?,?)", values)
        vertexes['conLST'] = datetime.now()

    def save_lcon_to_object(self, object_name, vertexes):
        logger.info('Saving line connection')
        self.remove_lcon(object_name)
        vertexConnect = vertexes['connect']
        values = DBSQLite.__split_array(object_name, vertexConnect)
        self.cursor.executemany("INSERT INTO line_connection VALUES \
            (?,?,?)", values)

    def load_lcon(self, object_name):
        logger.info('Loading line connection')
        values = (object_name,)  # key to find
        self.cursor.execute("SELECT chunkID, arr FROM line_connection \
            WHERE object_name = ?", values)
        connect = DBSQLite.__cat_array(self.cursor)
        return connect

    def load_lsty(self, object_name):
        logger.info('Loading line style')
        values = (object_name,)  # key to find
        self.cursor.execute("SELECT * FROM line_style WHERE \
            object_name = ?", values)
        (name, width, r, g, b, alpha) = self.cursor.fetchone()
        line_style = copy.deepcopy(LINE_STYLE)
        line_style['width'] = width
        line_style['color'] = (r, g, b, alpha)
        line_style['opacity'] = alpha
        return line_style

    def remove_lsty(self, object_name):
        values = (object_name,)
        self.cursor.execute("DELETE FROM line_style WHERE \
            object_name = ?", values)

    def remove_lcon(self, object_name):
        values = (object_name,)
        self.cursor.execute("DELETE from line_connection \
            WHERE object_name = ?", values)

    def remove_tables(self, object_name):
        logger.info('Removing from DB: {}'.format(object_name))
        DataBase.remove_tables(object_name)
        self.remove_lsty(object_name)
        self.remove_lcon(object_name)
