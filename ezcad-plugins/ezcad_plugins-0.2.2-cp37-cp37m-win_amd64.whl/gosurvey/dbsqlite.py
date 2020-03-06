# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import sqlite3
from ezcad.utils.dbsqlite import native_scalar
from ezcad.utils.logger import logger
from gopoint.dbsqlite import DBSQLite as DataBase


class DBSQLite(DataBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def create_tables(self):
        self.ct_geometry_type()
        self.ct_survey_geometry()

    def ct_survey_geometry(self):
        logger.info('Creating table survey_geometry (if not exists)')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS survey_geometry
            (object_name TEXT PRIMARY KEY,
            ilnoP1 INTEGER, xlnoP1 INTEGER, crsxP1 REAL, crsyP1 REAL,
            ilnoP2 INTEGER, xlnoP2 INTEGER, crsxP2 REAL, crsyP2 REAL,
            ilnoP3 INTEGER, xlnoP3 INTEGER, crsxP3 REAL, crsyP3 REAL)
            ''')

    def save_sgmt(self, object_name, dict_sgmt):
        logger.info('Saving survey geometry')
        ilnoP1 = int(native_scalar(dict_sgmt['P1_ILNO']))
        xlnoP1 = int(native_scalar(dict_sgmt['P1_XLNO']))
        crsxP1 = float(native_scalar(dict_sgmt['P1_CRSX']))
        crsyP1 = float(native_scalar(dict_sgmt['P1_CRSY']))
        ilnoP2 = int(native_scalar(dict_sgmt['P2_ILNO']))
        xlnoP2 = int(native_scalar(dict_sgmt['P2_XLNO']))
        crsxP2 = float(native_scalar(dict_sgmt['P2_CRSX']))
        crsyP2 = float(native_scalar(dict_sgmt['P2_CRSY']))
        ilnoP3 = int(native_scalar(dict_sgmt['P3_ILNO']))
        xlnoP3 = int(native_scalar(dict_sgmt['P3_XLNO']))
        crsxP3 = float(native_scalar(dict_sgmt['P3_CRSX']))
        crsyP3 = float(native_scalar(dict_sgmt['P3_CRSY']))
        try:  # insert for new object, update for existing object
            values = (object_name,
                      ilnoP1, xlnoP1, crsxP1, crsyP1,
                      ilnoP2, xlnoP2, crsxP2, crsyP2,
                      ilnoP3, xlnoP3, crsxP3, crsyP3)
            self.cursor.execute("INSERT INTO survey_geometry VALUES \
                (?,?,?,?,?,?,?,?,?,?,?,?,?)", values)
        except sqlite3.IntegrityError:
            values = (ilnoP1, xlnoP1, crsxP1, crsyP1,
                      ilnoP2, xlnoP2, crsxP2, crsyP2,
                      ilnoP3, xlnoP3, crsxP3, crsyP3,
                      object_name)
            self.cursor.execute("UPDATE survey_geometry SET \
                ilnoP1 = ?, xlnoP1 = ?, crsxP1 = ?, crsyP1 = ?, \
                ilnoP2 = ?, xlnoP2 = ?, crsxP2 = ?, crsyP2 = ?, \
                ilnoP3 = ?, xlnoP3 = ?, crsxP3 = ?, crsyP3 = ? \
                WHERE object_name = ?", values)

    def load_sgmt(self, object_name):
        logger.info('Loading survey geometry')
        values = (object_name,)  # key to find
        self.cursor.execute("SELECT * FROM survey_geometry WHERE \
            object_name = ?", values)
        (name, ilnoP1, xlnoP1, crsxP1, crsyP1, ilnoP2, xlnoP2, crsxP2,
            crsyP2, ilnoP3, xlnoP3, crsxP3, crsyP3) = \
            self.cursor.fetchone()
        dict_sgmt = {
            'P1_ILNO': ilnoP1,
            'P1_XLNO': xlnoP1,
            'P1_CRSX': crsxP1,
            'P1_CRSY': crsyP1,
            'P2_ILNO': ilnoP2,
            'P2_XLNO': xlnoP2,
            'P2_CRSX': crsxP2,
            'P2_CRSY': crsyP2,
            'P3_ILNO': ilnoP3,
            'P3_XLNO': xlnoP3,
            'P3_CRSX': crsxP3,
            'P3_CRSY': crsyP3
        }
        return dict_sgmt

    def remove_sgmt(self, object_name):
        values = (object_name,)
        self.cursor.execute("DELETE FROM survey_geometry WHERE \
            object_name = ?", values)

    def remove_tables(self, object_name):
        logger.info('Removing from DB: {}'.format(object_name))
        self.remove_geom(object_name)
        self.remove_sgmt(object_name)
