# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import copy
import sqlite3
from datetime import datetime
from ezcad.utils.dbsqlite import native_scalar
from ezcad.utils.logger import logger
from gopoint.dbsqlite import DBSQLite as DataBase
from gotsurf.utils import SURF_STYLE


class DBSQLite(DataBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def create_tables(self):
        DataBase.create_tables(self)
        self.ct_surf_style()
        self.ct_gsurf_gridz()
        self.ct_gsurf_index()

    def ct_surf_style(self):
        logger.info('Creating table surf_style (if not exists)')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS surf_style
            (object_name TEXT PRIMARY KEY, face_pure INTEGER,
            draw_edge INTEGER, draw_face INTEGER,
            fr REAL, fg REAL, fb REAL, fa REAL,
            er REAL, eg REAL, eb REAL, ea REAL)
            ''')

    def ct_gsurf_index(self):
        logger.info('Creating table gsurf_index (if not exists)')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS gsurf_index
            (object_name TEXT PRIMARY KEY,
            ilfrst INTEGER, illast INTEGER, ilncrt INTEGER, ilamnt INTEGER,
            xlfrst INTEGER, xllast INTEGER, xlncrt INTEGER, xlamnt INTEGER)
            ''')

    def ct_gsurf_gridz(self):
        logger.info('Creating table gsurf_gridz (if not exists)')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS gsurf_gridz
            (object_name TEXT, chunkID INTEGER, arr ARRAY,
            PRIMARY KEY (object_name, chunkID))
            ''')

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

    def save_sidx(self, object_name, dict_sidx):
        logger.info('Saving gsurface index')
        ilfrst = int(native_scalar(dict_sidx['IL_FRST']))
        illast = int(native_scalar(dict_sidx['IL_LAST']))
        ilncrt = int(native_scalar(dict_sidx['IL_NCRT']))
        ilamnt = int(native_scalar(dict_sidx['IL_AMNT']))
        xlfrst = int(native_scalar(dict_sidx['XL_FRST']))
        xllast = int(native_scalar(dict_sidx['XL_LAST']))
        xlncrt = int(native_scalar(dict_sidx['XL_NCRT']))
        xlamnt = int(native_scalar(dict_sidx['XL_AMNT']))
        try:  # insert for new object, update for existing object
            values = (object_name,
                      ilfrst, illast, ilncrt, ilamnt,
                      xlfrst, xllast, xlncrt, xlamnt)
            self.cursor.execute("INSERT INTO gsurf_index VALUES \
                (?,?,?,?,?,?,?,?,?)", values)
        except sqlite3.IntegrityError:
            values = (ilfrst, illast, ilncrt, ilamnt,
                      xlfrst, xllast, xlncrt, xlamnt,
                      object_name)
            self.cursor.execute("UPDATE gsurf_index SET \
                ilfrst = ?, illast = ?, ilncrt = ?, ilamnt = ?, \
                xlfrst = ?, xllast = ?, xlncrt = ?, xlamnt = ? \
                WHERE object_name = ?", values)

    def save_gridz(self, object_name, gridz, to_project=False, to_object=False):
        if to_project:
            self.save_gridz_to_project(object_name, gridz)
        if to_object:
            self.save_gridz_to_object(object_name, gridz)

    def save_gridz_to_project(self, object_name, gridz):
        if gridz['arrayLMT'] < gridz['arrayLST']:
            logger.info('Skip saving gsurface gridz')
            return
        logger.info('Saving gsurface gridz')
        self.remove_gridz(object_name)
        gridzArray = gridz['array']
        values = DBSQLite.__split_array(object_name, gridzArray)
        self.cursor.executemany("INSERT INTO gsurf_gridz VALUES \
            (?,?,?)", values)
        gridz['arrayLST'] = datetime.now()

    def save_gridz_to_object(self, object_name, gridz):
        logger.info('Saving gsurface gridz')
        self.remove_gridz(object_name)
        gridzArray = gridz['array']
        values = DBSQLite.__split_array(object_name, gridzArray)
        self.cursor.executemany("INSERT INTO gsurf_gridz VALUES \
            (?,?,?)", values)

    def load_gridz(self, object_name):
        logger.info('Loading gsurface griz')
        values = (object_name,)  # key to find
        self.cursor.execute("SELECT chunkID, arr FROM gsurf_gridz \
            WHERE object_name = ?", values)
        arrayGridz = DBSQLite.__cat_array(self.cursor)
        return arrayGridz

    def load_sidx(self, object_name):
        logger.info('Loading gsurface index')
        values = (object_name,)  # key to find
        self.cursor.execute("SELECT * FROM gsurf_index WHERE \
            object_name = ?", values)
        (name, ilfrst, illast, ilncrt, ilamnt, xlfrst, xllast,
            xlncrt, xlamnt) = self.cursor.fetchone()
        dict_sidx = {
            'IL_FRST': ilfrst,
            'IL_LAST': illast,
            'IL_NCRT': ilncrt,
            'IL_AMNT': ilamnt,
            'XL_FRST': xlfrst,
            'XL_LAST': xllast,
            'XL_NCRT': xlncrt,
            'XL_AMNT': xlamnt
        }
        return dict_sidx

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

    def remove_gridz(self, object_name):
        values = (object_name,)
        self.cursor.execute("DELETE FROM gsurf_gridz WHERE \
            object_name = ?", values)

    def remove_sidx(self, object_name):
        values = (object_name,)
        self.cursor.execute("DELETE FROM gsurf_index WHERE \
            object_name = ?", values)

    def remove_ssty(self, object_name):
        values = (object_name,)
        self.cursor.execute("DELETE FROM surf_style WHERE \
            object_name = ?", values)

    def remove_tables(self, object_name):
        logger.info('Removing from DB: {}'.format(object_name))
        DataBase.remove_tables(object_name)
        self.remove_ssty(object_name)
        self.remove_gridz(object_name)
        self.remove_sidx(object_name)
