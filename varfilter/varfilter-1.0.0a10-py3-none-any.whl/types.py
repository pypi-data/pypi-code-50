#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Definiciones de tipos básicos habituales.

Definición de clases para Db,Query y Datos usuarios.

Funciones de conversión a int,bool,float

"""

__author__ = "Esteban Barón"
__copyright__ = "Copyright 2020, Esteban Barón ,EBP"
__license__ = "MIT"
__email__ = "esteban@gominet.net"
__status__ = "Alpha"
__version__ = "1.0.0a10"


class UserAuthInfo:
    def __init__(self, uname, upass):
        self._data = {'user': uname,
                      'pass': upass}

    def getName(self):
        return self._data.get('user')

    def getPass(self):
        return self._data.get('pass')


class DbInfo:
    def __init__(self, uinfo, dbname, host, port):
        self._data = {'uinfo': uinfo,
                      'dbname': dbname,
                      'host': host,
                      'port': port}

    def getUinfo(self):
        return self._data.get('uinfo')

    def getDbname(self):
        return self._data.get('dbname')

    def getHost(self):
        return self._data.get('host')

    def getPort(self):
        return self._data.get('port')


class SQLQuery:
    def __init__(self, query, params):
        self._query = query
        self._params = params

    def getQuery(self):
        return self._query

    def getParams(self):
        return self._params


if __name__ == "__main__":
    print("Este fichero pertenece a un módulo, "
          "no es operativo como aplicación independiente.")
