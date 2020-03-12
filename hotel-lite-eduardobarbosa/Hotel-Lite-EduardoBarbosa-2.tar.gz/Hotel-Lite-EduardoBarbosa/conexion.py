# coding=utf-8
"""
En está clase se tendrá los métodos necesarios para abrir(crear en el caso de que sea necesario) / cerrar la base de
datos.
"""

import sqlite3
import traceback


class Conexion:

    @staticmethod
    def abrir_bd():
        """
        Método es el encargado de crear la conexión con la base de datos e inicializar las variables de conexión y
        cursor que serán necesarias para realizar consultas, inserciones etc.
        @return:
        """
        try:
            global bd, conexion, cursor
            bd = 'hotellite.sqlite'  # Variable que almacena la base de datos
            conexion = sqlite3.connect(bd)  # Nos conectamos a la base de datos
            cursor = conexion.cursor()  # La variable cursor que hará las operaciones
            print('Conexión con la base de datos realizada correctamente')
        except Exception as e:
            traceback.print_exc()

    @staticmethod
    def cerrar_bd():
        """
        Método es el encargado de cerrar la conexión con la base de datos, para cuando se finalice la aplicación y
        cuando se vayan a hacer los backups.
        @return:
        """
        try:
            cursor.close()
            conexion.close()
            print('Base de datos cerrada correctamente')
        except Exception as e:
            traceback.print_exc()
