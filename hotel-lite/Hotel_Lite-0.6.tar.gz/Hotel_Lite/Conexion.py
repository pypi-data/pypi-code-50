# -*- coding: utf-8 -*-
"""Este modulo permite administrar las cnexiones a la base de datos SQLite.
    Este modulo contiene las siguientes funciones:
    *abrirDB
        - Abre una conexion contra la db

    *cerrarbbdd
        - Cierra una conexion contra la db
"""

import sqlite3
from Hotel_Lite import Variables


def abrirDB():
        try:

            global bbdd, conex, cur

            bbdd = 'empresa.sqlite'
            conex = sqlite3.connect(bbdd) #La abrimos
            cur = conex.cursor() #La variable cursor
            Variables.bdabierta = True

        except sqlite3.OperationalError as e:
            print("Ha ocurrido un error durante la conexion: ", e)

def cerrarbbdd():
        try:

            if Variables.bdabierta:
                Variables.bdabierta = False
                cur.close()
                conex.close()

        except sqlite3.OperationalError as e:
            print("Ha ocurrido un error al cerrar la conexion", e)