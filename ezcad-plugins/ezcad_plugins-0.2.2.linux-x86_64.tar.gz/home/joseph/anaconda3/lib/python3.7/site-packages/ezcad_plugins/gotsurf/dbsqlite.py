# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import copy
import sqlite3
from datetime import datetime
from ezcad.utils.dbsqlite import native_scalar
from ezcad.utils.logger import logger
from gopoint.dbsqlite import DBSQLite as DataBase
from .utils import SURF_STYLE


class DBSQLite(DataBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def create_tables(self):
        DataBase.create_tables(self)
        self.ct_surf_style()
        self.ct_tsurf_connection()

    def ct_surf_style(self):
        logger.info('Creating table surf_style (if not exists)')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS surf_style
            (object_name TEXT PRIMARY KEY, face_pure INTEGER,
            draw_edge INTEGER, draw_face INTEGER,
            fr REAL, fg REAL, fb REAL, fa REAL,
            er REAL, eg REAL, eb REAL, ea REAL)
            ''')

    def ct_tsurf_connection(self):
        logger.info('Creating table tsurf_connection (if not exists)')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tsurf_connection
            (object_name TEXT, chunkID INTEGER, arr ARRAY,
            PRIMARY KEY (object_name, chunkID))
            ''')

    def save_tcon(self, object_name, triangles, to_project=False,
                  to_object=False):
        if to_project:
            self.save_tcon_to_project(object_name, triangles)
        if to_object:
            self.save_tcon_to_object(object_name, triangles)

    def save_tcon_to_project(self, object_name, triangles):
        if triangles['ijkLMT'] < triangles['ijkLST']:
            logger.info('Skip saving tsurface connection')
            return
        logger.info('Saving tsurface connection')
        self.remove_tcon(object_name)
        triArray = triangles['ijk']
        values = DBSQLite.__split_array(object_name, triArray)
        self.cursor.executemany("INSERT INTO tsurf_connection VALUES \
            (?,?,?)", values)
        triangles['ijkLST'] = datetime.now()

    def save_tcon_to_object(self, object_name, triangles):
        logger.info('Saving tsurface connection')
        self.remove_tcon(object_name)
        triArray = triangles['ijk']
        values = DBSQLite.__split_array(object_name, triArray)
        self.cursor.executemany("INSERT INTO tsurf_connection VALUES \
            (?,?,?)", values)

    def save_ssty(self, object_name, options):
        logger.info('Saving surface style')
        fpc = 1 if options['face_pure'] else 0
        draw_edge = 1 if options['draw_edge'] else 0
        draw_face = 1 if options['draw_face'] else 0
        (fr, fg, fb, fa) = options['face_color']
        (er, eg, eb, ea) = options['edge_color']
        fr = float(native_scalar(fr))
        fg = float(native_scalar(fg))
        fb = float(native_scalar(fb))
        fa = float(native_scalar(fa))
        er = float(native_scalar(er))
        eg = float(native_scalar(eg))
        eb = float(native_scalar(eb))
        ea = float(native_scalar(ea))
        try:  # insert for new object, update for existing object
            values = (object_name, fpc, draw_edge, draw_face, fr, fg, fb, fa,
                      er, eg, eb, ea)
            self.cursor.execute("INSERT INTO surf_style VALUES \
                (?,?,?,?,?,?,?,?,?,?,?,?)", values)
        except sqlite3.IntegrityError:
            values = (fpc, draw_edge, draw_face, fr, fg, fb, fa,
                      er, eg, eb, ea, object_name)
            self.cursor.execute("UPDATE surf_style SET face_pure = ?, \
                draw_edge = ?, draw_face = ?, fr = ?, fg = ?, fb = ?, \
                fa = ?, er = ?, eg = ?, eb = ?, ea = ? \
                WHERE object_name = ?", values)

    def load_tcon(self, object_name):
        logger.info('Loading tsurface connection')
        values = (object_name,)  # key to find
        self.cursor.execute("SELECT chunkID, arr FROM tsurf_connection \
            WHERE object_name = ?", values)
        connect = DBSQLite.__cat_array(self.cursor)
        return connect

    def load_ssty(self, object_name):
        logger.info('Loading surface style')
        values = (object_name,)  # key to find
        self.cursor.execute("SELECT * FROM surf_style WHERE \
            object_name = ?", values)
        (name, fpc, draw_edge, draw_face, fr, fg, fb, fa, er, eg, eb, ea) = \
            self.cursor.fetchone()
        surf_style = copy.deepcopy(SURF_STYLE)
        surf_style['face_pure'] = True if fpc else False
        surf_style['draw_edge'] = True if draw_edge else False
        surf_style['draw_face'] = True if draw_face else False
        surf_style['face_color'] = (fr, fg, fb, fa)
        surf_style['edge_color'] = (er, eg, eb, ea)
        return surf_style

    def remove_tcon(self, object_name):
        values = (object_name,)
        self.cursor.execute("DELETE from tsurf_connection \
            WHERE object_name = ?", values)

    def remove_ssty(self, object_name):
        values = (object_name,)
        self.cursor.execute("DELETE FROM surf_style WHERE \
            object_name = ?", values)

    def remove_tables(self, object_name):
        logger.info('Removing from DB: {}'.format(object_name))
        DataBase.remove_tables(object_name)
        self.remove_ssty(object_name)
        self.remove_tcon(object_name)
