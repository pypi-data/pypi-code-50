# coding=utf-8
"""
Aquí vendrán todas las funciones que afectan a la gestión de los servicios
"""
import sqlite3
import traceback

import conexion
import variables


def insertar_servicios(servicio):
    """
    Función encargada de insertar un servicio adicional a una reserva específica.
    @param servicio: todos los datos del servicio más el código de la reserva
    @return:
    """
    try:
        conexion.cursor.execute(
            'INSERT INTO servicios_adicionales(servicio, codigo_reserva, precio) VALUES(?,?,?)', servicio)
        conexion.conexion.commit()
    except sqlite3.OperationalError:
        traceback.print_exc()


def cargar_servicios_reserva(list_servicios):
    """
    Función encargada de obtener los servicios adicionales de una determinada reserva.
    @param list_servicios: lista de servicios.
    @return: lista con todos los servicios adicionales de la reserva seleccionada.
    """
    try:
        conexion.cursor.execute(
            'SELECT * FROM servicios_adicionales WHERE codigo_reserva = ?',
            (variables.codigo_reserva,))
        servicios = conexion.cursor.fetchall()
        conexion.conexion.commit()
        list_servicios.clear()
        for registro in servicios:
            list_servicios.append(registro)
        return servicios
    except sqlite3.OperationalError:
        traceback.print_exc()


def borrar_servicio(codigo):
    """
    Función encargada de borrar un servicio seleccionado.
    @param codigo: código del servicio adicional seleccionado.
    @return:
    """
    try:
        conexion.cursor.execute('DELETE FROM servicios_adicionales WHERE codigo_servicio = ?', (codigo,))
        conexion.conexion.commit()
    except sqlite3.OperationalError:
        traceback.print_exc()
        conexion.conexion.rollback()