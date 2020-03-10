# -*- coding: utf-8 -*-

"""Modulo encargado de la compresion de ficheros

Este modulo contiene las siguientes funciones:
    *comprimir
        - Compribe un fichero establecido
            + param rutaf: Directorio del fichero a comprimir

"""

from zipfile import *
from datetime import datetime
import os
from Hotel_Lite import Conexion

'''
Comprimir x archivo ruta como parametro y guardarlo en un directorio
'''

def comprimir(rutaf):

    if (rutaf != None):

        Conexion.cerrarbbdd()
        fecha = datetime.now()
        fichz = ZipFile("/media/TEIS/a13franciscoca/" + str(fecha) + "_backup.zip", "w")
        fichz.write(rutaf,os.path.basename(rutaf) , ZIP_DEFLATED)
        Conexion.abrirDB()
    else:
        print("Falta el fichero de base de datos")