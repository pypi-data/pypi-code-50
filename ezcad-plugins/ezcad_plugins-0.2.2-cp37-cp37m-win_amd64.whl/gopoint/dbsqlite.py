# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import copy
import sqlite3
from datetime import datetime
from ezcad.utils.dbsqlite import DBSQLite as DataBase
from ezcad.utils.dbsqlite import native_scalar
from ezcad.utils.logger import logger
from .utils import ATOM_STYLE


class DBSQLite(DataBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def create_tables(self):
        self.ct_geometry_type()
        self.ct_atom_style()
        self.ct_current_property()
        self.ct_point_vertexes()
        self.ct_property_arrays()
        self.ct_properties()
        self.ct_color_gradient_ticks()

    def ct_atom_style(self):
        logger.info('Creating table atom_style (if not exists)')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS atom_style
            (object_name TEXT PRIMARY KEY, symbol TEXT, size INTEGER,
            edge_width INTEGER, coloring INTEGER,
            colorR INTEGER, colorG INTEGER, colorB INTEGER, colorA INTEGER)
            ''')

    def ct_geometry_type(self):
        logger.info('Creating table geometry_type (if not exists)')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS geometry_type
            (object_name TEXT PRIMARY KEY, geometry_type TEXT)
            ''')

    def ct_current_property(self):
        logger.info('Creating table current_property (if not exists)')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS current_property
            (object_name TEXT PRIMARY KEY, current_property TEXT)
            ''')

    def ct_point_vertexes(self):
        logger.info('Creating table point_vertexes (if not exists)')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS point_vertexes
            (object_name TEXT, chunkID INTEGER, arr ARRAY,
            PRIMARY KEY (object_name, chunkID))
            ''')

    def ct_property_arrays(self):
        logger.info('Creating table property_arrays (if not exists)')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS property_arrays
            (object_name TEXT, prop_name TEXT, chunkID INTEGER, arr ARRAY,
            PRIMARY KEY (object_name, prop_name, chunkID))
            ''')

    def ct_properties(self):
        logger.info('Creating table properties (if not exists)')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS properties
            (object_name TEXT, prop_name TEXT,
            clipMin REAL, clipMax REAL, colorGradientMode TEXT,
            PRIMARY KEY (object_name, prop_name))
            ''')

    def ct_color_gradient_ticks(self):
        logger.info('Creating table color_gradient_ticks (if not exists)')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS color_gradient_ticks
            (object_name TEXT, prop_name TEXT, tickv REAL,
            tickr INTEGER, tickg INTEGER, tickb INTEGER, ticka INTEGER,
            PRIMARY KEY (object_name, prop_name, tickv))
            ''')

    def save_geom(self, object_name, geometry_type):
        logger.info('Saving geometry type')
        try:
            values = (object_name, geometry_type)
            self.cursor.execute("INSERT INTO geometry_type VALUES \
                (?,?)", values)
        except sqlite3.IntegrityError:
            values = (geometry_type, object_name)
            self.cursor.execute("UPDATE geometry_type \
                SET geometry_type = ? WHERE object_name = ?", values)

    def save_atom(self, object_name, atom_style):
        logger.info('Saving atom style')
        symbol = atom_style['symbol']
        size = atom_style['size']
        coloring = atom_style['coloring']
        edge_width = atom_style['edge_width']
        r, g, b = atom_style['face_color'][:3]
        alpha = atom_style['opacity']
        size = int(native_scalar(size))
        coloring = int(native_scalar(coloring))
        edge_width = int(native_scalar(edge_width))
        r = int(native_scalar(r))
        g = int(native_scalar(g))
        b = int(native_scalar(b))
        alpha = int(native_scalar(alpha))
        try:  # insert for new object, update for existing object
            values = (object_name, symbol, size, edge_width, coloring,
                      r, g, b, alpha)
            self.cursor.execute("INSERT INTO atom_style VALUES \
                (?,?,?,?,?,?,?,?,?)", values)
        except sqlite3.IntegrityError:
            values = (symbol, size, edge_width, coloring, r, g, b, alpha,
                      object_name)
            self.cursor.execute("UPDATE atom_style SET symbol = ?, \
                size = ?, edge_width = ?, coloring = ?, colorR = ?, \
                colorG = ?,  colorB = ?, colorA = ? \
                WHERE object_name = ?", values)

    def save_cprop(self, object_name, current_property):
        logger.info('Saving current property')
        try:
            values = (object_name, current_property)
            self.cursor.execute("INSERT INTO current_property VALUES \
                (?,?)", values)
        except sqlite3.IntegrityError:
            values = (current_property, object_name)
            self.cursor.execute("UPDATE current_property \
                SET current_property = ? WHERE object_name = ?", values)

    def save_vtx(self, object_name, vertexes, to_project=False,
        to_object=False):
        if to_project:  # accumulative
            self.save_vtx_to_project(object_name, vertexes)
        if to_object:  # granular
            self.save_vtx_to_object(object_name, vertexes)

    def save_vtx_to_project(self, object_name, vertexes):
        if vertexes['xyzLMT'] < vertexes['xyzLST']:
            logger.info('Skip saving vertex array')
            return
        logger.info('Saving vertex array')
        # Delete all vertexes then insert current ones
        self.remove_vtx(object_name)
        vertexArray = vertexes['xyz']
        values = DBSQLite.__split_array(object_name, vertexArray)
        self.cursor.executemany("INSERT INTO point_vertexes VALUES \
            (?,?,?)", values)
        vertexes['xyzLST'] = datetime.now()

    def save_vtx_to_object(self, object_name, vertexes):
        # Force save everything and do not modify time stamps
        logger.info('Saving vertex array')
        # Delete all vertexes then insert current ones
        self.remove_vtx(object_name)
        vertexArray = vertexes['xyz']
        values = DBSQLite.__split_array(object_name, vertexArray)
        self.cursor.executemany("INSERT INTO point_vertexes VALUES \
            (?,?,?)", values)

    def save_props(self, object_name, prop, prop_array_key,
        to_project=False, to_object=False):
        for prop_name in sorted(prop):
            logger.info('Saving property: {}'.format(prop_name))
            self.save_prop_clip(prop, prop_name, object_name)
            self.save_prop_color_gradient(prop, prop_name, object_name)
            if to_project:
                lmt = prop[prop_name]['arrayLMT']
                lst = prop[prop_name]['arrayLST']
                if lmt >= lst:
                    self.save_prop_array(prop, prop_name, prop_array_key,
                        object_name)
                    prop[prop_name]['arrayLST'] = datetime.now()
                else:
                    logger.info("Skip saving property array")
            if to_object:
                self.save_prop_array(prop, prop_name, prop_array_key,
                    object_name)

    def save_prop_array(self, prop, prop_name, prop_array_key, object_name):
        logger.info('Saving property array')
        values = (object_name, prop_name)
        self.cursor.execute("DELETE from property_arrays \
            WHERE object_name = ? AND prop_name = ?", values)
        array = prop[prop_name][prop_array_key]
        values = DBSQLite.__split_array(object_name, array, prop_name)
        self.cursor.executemany("INSERT INTO property_arrays \
            VALUES (?,?,?,?)", values)

    def save_prop_clip(self, prop, prop_name, object_name):
        logger.info('Saving property clip')
        clipMin, clipMax = prop[prop_name]['colorClip']
        clipMin = float(native_scalar(clipMin))
        clipMax = float(native_scalar(clipMax))
        mode = prop[prop_name]['colorGradient']['mode']
        try:
            values = (object_name, prop_name, clipMin, clipMax, mode)
            self.cursor.execute("INSERT INTO properties VALUES \
                (?,?,?,?,?)", values)
        except sqlite3.IntegrityError:
            values = (clipMin, clipMax, mode, object_name, prop_name)
            self.cursor.execute("UPDATE properties SET \
                clipMin = ?, clipMax = ?, colorGradientMode = ? \
                WHERE object_name = ? AND prop_name = ?", values)

    def save_prop_color_gradient(self, prop, prop_name, object_name):
        logger.info('Saving property color gradient')
        values = (object_name, prop_name)
        self.cursor.execute("DELETE from color_gradient_ticks \
            WHERE object_name = ? AND prop_name = ?", values)
        ticks = prop[prop_name]['colorGradient']['ticks']
        for tick in ticks:
            tv = tick[0]
            tr, tg, tb, ta = tick[1]
            tv = float(native_scalar(tv))
            tr = int(native_scalar(tr))
            tg = int(native_scalar(tg))
            tb = int(native_scalar(tb))
            ta = int(native_scalar(ta))
            values = (object_name, prop_name, tv, tr, tg, tb, ta)
            self.cursor.execute("INSERT INTO color_gradient_ticks \
                VALUES (?,?,?,?,?,?, ?)", values)

    def load_geom(self, object_name):
        logger.info('Loading geometry type')
        values = (object_name,)
        self.cursor.execute("SELECT geometry_type FROM geometry_type \
            WHERE object_name = ?", values)
        (geometry_type,) = self.cursor.fetchone()
        return geometry_type

    def load_vtx(self, object_name):
        logger.info('Loading vertexes')
        values = (object_name,)  # key to find
        self.cursor.execute("SELECT chunkID, arr FROM point_vertexes \
            WHERE object_name = ?", values)
        vertexes = DBSQLite.__cat_array(self.cursor)
        return vertexes

    def load_props(self, object_name):
        values = (object_name,)  # key to find
        self.cursor.execute("SELECT * FROM properties WHERE \
            object_name = ?", values)
        props = self.cursor.fetchall()  # a list
        propPacks = []
        for prop in props:
            (name, prop_name, clipMin, clipMax, mode) = prop
            clip = (clipMin, clipMax)
            logger.info('Loading property: {}'.format(prop_name))

            # get the color gradient ticks for this property
            propID = (name, prop_name)
            self.cursor.execute("SELECT * FROM color_gradient_ticks \
                WHERE object_name = ? AND prop_name = ?", propID)
            dbTicks = self.cursor.fetchall()  # a list
            # need sort the ticks? what order in the fetchall?
            # or does order matter?
            ticks = []
            for dbTick in dbTicks:
                (name2, prop_name2, tv, tr, tg, tb, ta) = dbTick
                tick = (tv, (tr, tg, tb, ta))
                ticks.append(tick)
            gradient = {'ticks': ticks, 'mode': mode}

            self.cursor.execute("SELECT chunkID, arr FROM property_arrays \
                WHERE object_name = ? AND prop_name = ?", propID)
            array = DBSQLite.__cat_array(self.cursor)
            propPack = [prop_name, array, clip, gradient]
            propPacks.append(propPack)
        return propPacks

    def load_atom(self, object_name):
        logger.info('Loading atom style')
        values = (object_name,)  # key to find
        self.cursor.execute("SELECT * FROM atom_style WHERE \
            object_name = ?", values)
        (name, symbol, size, edge_width, coloring, r, g, b, alpha) = \
            self.cursor.fetchone()
        atom_style = copy.deepcopy(ATOM_STYLE)
        atom_style['symbol'] = symbol
        atom_style['size'] = size
        atom_style['coloring'] = coloring
        atom_style['edge_width'] = edge_width
        atom_style['face_color'] = (r, g, b, alpha)
        atom_style['opacity'] = alpha
        return atom_style

    def load_cprop(self, object_name):
        logger.info('Loading current property')
        values = (object_name,)  # key to find
        self.cursor.execute("SELECT current_property FROM \
            current_property WHERE object_name = ?", values)
        (prop_name,) = self.cursor.fetchone()
        return prop_name

    def remove_geom(self, object_name):
        values = (object_name,)
        self.cursor.execute("DELETE FROM geometry_type WHERE \
            object_name = ?", values)

    def remove_atom(self, object_name):
        values = (object_name,)
        self.cursor.execute("DELETE FROM atom_style WHERE \
            object_name = ?", values)

    def remove_cprop(self, object_name):
        values = (object_name,)
        self.cursor.execute("DELETE FROM current_property WHERE \
            object_name = ?", values)

    def remove_vtx(self, object_name):
        values = (object_name,)
        self.cursor.execute("DELETE from point_vertexes \
            WHERE object_name = ?", values)

    def remove_props(self, object_name, prop_name=None):
        if prop_name is None:
            values = (object_name,)
            self.cursor.execute("DELETE from property_arrays \
                WHERE object_name = ?", values)
            self.cursor.execute("DELETE from properties \
                WHERE object_name = ?", values)
            self.cursor.execute("DELETE from color_gradient_ticks \
                WHERE object_name = ?", values)
        else:
            values = (object_name, prop_name)
            self.cursor.execute("DELETE from property_arrays \
                WHERE object_name = ? AND prop_name = ?", values)
            self.cursor.execute("DELETE from properties \
                WHERE object_name = ? AND prop_name = ?", values)
            self.cursor.execute("DELETE from color_gradient_ticks \
                WHERE object_name = ? AND prop_name = ?", values)

    def remove_tables(self, object_name):
        logger.info('Removing from DB: {}'.format(object_name))
        self.remove_geom(object_name)
        self.remove_atom(object_name)
        self.remove_cprop(object_name)
        self.remove_vtx(object_name)
        self.remove_props(object_name)
