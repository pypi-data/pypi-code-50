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
        DataBase.create_tables(self)
        self.ct_cube_vidx()
        self.ct_cube_vxyz()
        self.ct_cube_secno()

    def ct_cube_vidx(self):
        logger.info('Creating table cube_vidx (if not exists)')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cube_vidx
            (object_name TEXT PRIMARY KEY,
            ilfrst REAL, illast REAL, ilncrt REAL, ilamnt REAL,
            xlfrst REAL, xllast REAL, xlncrt REAL, xlamnt REAL,
            dpfrst REAL, dplast REAL, dpncrt REAL, dpamnt REAL)
            ''')

    def ct_cube_vxyz(self):
        logger.info('Creating table cube_vxyz (if not exists)')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cube_vxyz
            (object_name TEXT PRIMARY KEY,
            orx REAL, ory REAL, orz REAL, dpx REAL, dpy REAL, dpz REAL,
            xlx REAL, xly REAL, xlz REAL, ilx REAL, ily REAL, ilz REAL)
            ''')

    def ct_cube_secno(self):
        logger.info('Creating table cube_secno (if not exists)')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cube_secno
            (object_name TEXT PRIMARY KEY,
            ilno REAL, xlno REAL, dpno REAL)
            ''')

    def save_vidx(self, object_name, dict_vidx):
        logger.info('Saving volume index')
        ilfrst = float(native_scalar(dict_vidx['IL_FRST']))
        illast = float(native_scalar(dict_vidx['IL_LAST']))
        ilncrt = float(native_scalar(dict_vidx['IL_NCRT']))
        ilamnt = float(native_scalar(dict_vidx['IL_AMNT']))
        xlfrst = float(native_scalar(dict_vidx['XL_FRST']))
        xllast = float(native_scalar(dict_vidx['XL_LAST']))
        xlncrt = float(native_scalar(dict_vidx['XL_NCRT']))
        xlamnt = float(native_scalar(dict_vidx['XL_AMNT']))
        dpfrst = float(native_scalar(dict_vidx['DP_FRST']))
        dplast = float(native_scalar(dict_vidx['DP_LAST']))
        dpncrt = float(native_scalar(dict_vidx['DP_NCRT']))
        dpamnt = float(native_scalar(dict_vidx['DP_AMNT']))
        try:  # insert for new object, update for existing object
            values = (object_name,
                      ilfrst, illast, ilncrt, ilamnt,
                      xlfrst, xllast, xlncrt, xlamnt,
                      dpfrst, dplast, dpncrt, dpamnt)
            self.cursor.execute("INSERT INTO cube_vidx VALUES \
                (?,?,?,?,?,?,?,?,?,?,?,?,?)", values)
        except sqlite3.IntegrityError:
            values = (ilfrst, illast, ilncrt, ilamnt,
                      xlfrst, xllast, xlncrt, xlamnt,
                      dpfrst, dplast, dpncrt, dpamnt,
                      object_name)
            self.cursor.execute("UPDATE cube_vidx SET \
                ilfrst = ?, illast = ?, ilncrt = ?, ilamnt = ?, \
                xlfrst = ?, xllast = ?, xlncrt = ?, xlamnt = ?, \
                dpfrst = ?, dplast = ?, dpncrt = ?, dpamnt = ? \
                WHERE object_name = ?", values)

    def save_vxyz(self, object_name, dict_vxyz):
        logger.info('Saving volume xyz')
        orx = float(native_scalar(dict_vxyz['AXIS_ORX']))
        ory = float(native_scalar(dict_vxyz['AXIS_ORY']))
        orz = float(native_scalar(dict_vxyz['AXIS_ORZ']))
        dpx = float(native_scalar(dict_vxyz['AXIS_DPX']))
        dpy = float(native_scalar(dict_vxyz['AXIS_DPY']))
        dpz = float(native_scalar(dict_vxyz['AXIS_DPZ']))
        xlx = float(native_scalar(dict_vxyz['AXIS_XLX']))
        xly = float(native_scalar(dict_vxyz['AXIS_XLY']))
        xlz = float(native_scalar(dict_vxyz['AXIS_XLZ']))
        ilx = float(native_scalar(dict_vxyz['AXIS_ILX']))
        ily = float(native_scalar(dict_vxyz['AXIS_ILY']))
        ilz = float(native_scalar(dict_vxyz['AXIS_ILZ']))
        try:  # insert for new object, update for existing object
            values = (object_name,
                      orx, ory, orz, dpx, dpy, dpz,
                      xlx, xly, xlz, ilx, ily, ilz)
            self.cursor.execute("INSERT INTO cube_vxyz VALUES \
                (?,?,?,?,?,?,?,?,?,?,?,?,?)", values)
        except sqlite3.IntegrityError:
            values = (orx, ory, orz, dpx, dpy, dpz,
                      xlx, xly, xlz, ilx, ily, ilz,
                      object_name)
            self.cursor.execute("UPDATE cube_vxyz SET \
                orx = ?, ory = ?, orz = ?, dpx = ?, dpy = ?, dpz = ?, \
                xlx = ?, xly = ?, xlz = ?, ilx = ?, ily = ?, ilz = ? \
                WHERE object_name = ?", values)

    def save_secno(self, object_name, dictSecno):
        logger.info('Saving volume section number')
        ilno = dictSecno['iline']
        xlno = dictSecno['xline']
        dpno = dictSecno['depth']
        try:
            values = (object_name, ilno, xlno, dpno)
            self.cursor.execute("INSERT INTO cube_secno VALUES \
                (?,?,?,?)", values)
        except sqlite3.IntegrityError:
            values = (ilno, xlno, dpno, object_name)
            self.cursor.execute("UPDATE cube_secno SET \
                ilno = ?, xlno = ?, dpno = ? \
                WHERE object_name = ?", values)

    def load_vidx(self, object_name):
        logger.info('Loading volume index')
        values = (object_name,)  # key to find
        self.cursor.execute("SELECT * FROM cube_vidx WHERE \
            object_name = ?", values)
        (name, ilfrst, illast, ilncrt, ilamnt, xlfrst, xllast, xlncrt,
            xlamnt, dpfrst, dplast, dpncrt, dpamnt) = self.cursor.fetchone()
        dict_vidx = {
            'IL_FRST': ilfrst,
            'IL_LAST': illast,
            'IL_NCRT': ilncrt,
            'IL_AMNT': ilamnt,
            'XL_FRST': xlfrst,
            'XL_LAST': xllast,
            'XL_NCRT': xlncrt,
            'XL_AMNT': xlamnt,
            'DP_FRST': dpfrst,
            'DP_LAST': dplast,
            'DP_NCRT': dpncrt,
            'DP_AMNT': dpamnt
        }
        return dict_vidx

    def load_vxyz(self, object_name):
        logger.info('Loading volume xyz')
        values = (object_name,)  # key to find
        self.cursor.execute("SELECT * FROM cube_vxyz WHERE \
            object_name = ?", values)
        (name, orx, ory, orz, dpx, dpy, dpz,
               xlx, xly, xlz, ilx, ily, ilz) = self.cursor.fetchone()
        dict_vxyz = {
            'AXIS_ORX': orx,
            'AXIS_ORY': ory,
            'AXIS_ORZ': orz,
            'AXIS_DPX': dpx,
            'AXIS_DPY': dpy,
            'AXIS_DPZ': dpz,
            'AXIS_XLX': xlx,
            'AXIS_XLY': xly,
            'AXIS_XLZ': xlz,
            'AXIS_ILX': ilx,
            'AXIS_ILY': ily,
            'AXIS_ILZ': ilz
        }
        return dict_vxyz

    def load_secno(self, object_name):
        logger.info('Loading volume section number')
        values = (object_name,)  # key to find
        self.cursor.execute("SELECT * FROM cube_secno WHERE \
            object_name = ?", values)
        (name, ilno, xlno, dpno) = self.cursor.fetchone()
        dictSecno = {
            'iline': ilno,
            'xline': xlno,
            'depth': dpno
        }
        return dictSecno

    def remove_vidx(self, object_name):
        values = (object_name,)
        self.cursor.execute("DELETE FROM cube_vidx WHERE \
            object_name = ?", values)

    def remove_vxyz(self, object_name):
        values = (object_name,)
        self.cursor.execute("DELETE FROM cube_vxyz WHERE \
            object_name = ?", values)

    def remove_secno(self, object_name):
        values = (object_name,)
        self.cursor.execute("DELETE FROM cube_secno WHERE \
            object_name = ?", values)

    def remove_tables(self, object_name):
        logger.info('Removing from DB: {}'.format(object_name))
        DataBase.remove_tables(object_name)
        self.remove_vidx(object_name)
        self.remove_vxyz(object_name)
        self.remove_secno(object_name)
