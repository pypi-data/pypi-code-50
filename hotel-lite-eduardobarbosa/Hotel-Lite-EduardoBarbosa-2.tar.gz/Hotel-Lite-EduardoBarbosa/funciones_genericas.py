# coding=utf-8
"""
Esta clase contendrá todas las consultas a la base de datos que puedan ser génericas.
"""
import threading
import time
import traceback
import zipfile
import sqlite3
import re

from datetime import datetime

import conexion
import variables


def consulta_listado(tabla):
    """
    Función encargada de devolver todos los registros de la tabla deseada de la base de datos.
    @param tabla: nombre de la tabla de la cual se desea obtener todos los registros.
    @return: lista con todos los registros.
    """
    try:
        conexion.cursor.execute('SELECT * FROM ' + tabla)
        listado = conexion.cursor.fetchall()
        conexion.conexion.commit()
        return listado
    except Exception:
        traceback.print_exc()


def control_habitaciones():
    """
    Método para controlar las habitaciones, con este método se busca actualizar el estado de libre de la habitación
    automaticamente sin necesidad de que el usuario tenga que modificar manualmente la habitación.
    Esto será hecho con un hilo daemon que se estará ejecutandose en segundo plano durante la ejecución del programa.
    @return:
    """
    variables.timer = threading.Timer(0.5, control_habitaciones)
    variables.timer.daemon = True
    variables.timer.start()
    fecha_hoy = time.strftime('%H:%M:%S')
    fecha_control = '20:08:00'
    if str(fecha_control) == str(fecha_hoy):
        actualizar_habitaciones()


def actualizar_habitaciones():
    """
    Método para actualizar el estado de la habitación.
    @status: Work in Progress.
    @return:
    """
    print('Habitaciones actualizadas.')


def cerrar_timer():
    """
    Finalizar la ejecución del hilo daemon encargado de la actualización automática del estado de las habitaciones.
    @return:
    """
    variables.timer.join(0)


def backup():
    """
    Función encargada de realizar una copia de seguridad de la base de datos, para ello primero cierra la conexión de la
    base de datos, acto seguido creará la copia de seguridad en la carpeta del proyecto. Después la copia de seguridad
    será guardada donde el usuario desee.
    @return: el nombre del backup
    """
    try:
        conexion.Conexion().cerrar_bd()

        backup_archivo = str(datetime.now().strftime("%m-%d-%Y %H:%M:%S")) + ' - hotel_lite.zip'
        copia = zipfile.ZipFile(backup_archivo, 'w')
        copia.write('hotellite.sqlite', compress_type=zipfile.ZIP_DEFLATED)
        copia.close()

        conexion.Conexion().abrir_bd()
        return backup_archivo
    except Exception:
        traceback.print_exc()


def cargar_precios_servicios():
    """
    Método encargado de cargar todos lo precios de los servicios básicos (comida, desayuno y parking), para después
    ponerlos en los entries para la modificación del precio.
    @return:
    """
    try:
        conexion.cursor.execute('SELECT precio FROM servicios_basicos')
        lista_precios = conexion.cursor.fetchall()
        precios = re.findall('\d+\.\d+|\d+', str(lista_precios))
        variables.precios[0].set_text(precios[0])
        variables.precios[1].set_text(precios[1])
        variables.precios[2].set_text(precios[2])
        conexion.conexion.commit()
    except sqlite3.OperationalError:
        traceback.print_exc()
        conexion.conexion.rollback()


def actualizar_precios_servicios():
    """
    Método encargado de actualizar todos los precios de los servicios básicos del Hotel.
    @return:
    """
    try:
        conexion.cursor.execute('UPDATE servicios_basicos SET precio = ? WHERE servicio = "Comida"',
                                (variables.precios[0].get_text(),))
        conexion.cursor.execute('UPDATE servicios_basicos SET precio = ? WHERE servicio = "Desayuno"',
                                (variables.precios[1].get_text(),))
        conexion.cursor.execute('UPDATE servicios_basicos SET precio = ? WHERE servicio = "Parking"',
                                (variables.precios[2].get_text(),))
        conexion.conexion.commit()
    except sqlite3.OperationalError:
        traceback.print_exc()
        conexion.conexion.rollback()


def lista_precios_servicios():
    """
    Función encargada de devolver todos los precios de los servicios básicos, para añadirlos en la factura
    @return: Lista con los precios de los servicios básicos.
    """
    try:
        conexion.cursor.execute('SELECT precio FROM servicios_basicos')
        lista_precios = conexion.cursor.fetchall()
        conexion.conexion.commit()
        return re.findall('\d+\.\d+|\d+', str(lista_precios))
    except sqlite3.OperationalError:
        traceback.print_exc()
        conexion.conexion.rollback()
