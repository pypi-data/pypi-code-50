# coding=utf-8
"""
Aquí vendrán todas las funciones que afectan a la gestión de las habitaciones
"""
import sqlite3
import traceback

import conexion
import funciones_genericas
import variables


def cargar_habitaciones(list_habitaciones):
    """
    Función encargada de cargar el tree view de habitaciones con los datos de la tabla de la base de datos.
    @param list_habitaciones: lista de las habitaciones
    @return:
    """
    try:
        variables.listado = funciones_genericas.consulta_listado('habitaciones')
        list_habitaciones.clear()
        for registro in variables.listado:
            list_habitaciones.append(registro)
    except Exception:
        traceback.print_exc()


def lista_numero_habitaciones_combo():
    """
    Función encargada de cargar el combobox con los números de las habitaciones que hay registradas en la base de datos.
    @return:
    """
    try:
        conexion.cursor.execute('SELECT numero FROM habitaciones')
        listado = conexion.cursor.fetchall()
        variables.list_combo_habitaciones.clear()
        for fila in listado:
            variables.list_combo_habitaciones.append(fila)
        conexion.conexion.commit()
    except sqlite3.OperationalError:
        traceback.print_exc()
        conexion.conexion.rollback()


def lista_numero_habitaciones():
    """
    Función encargada de retornar una lista con los números de las habitaciones que hay registradas.
    @return:
    """
    try:
        conexion.cursor.execute('SELECT numero FROM habitaciones')
        listado = conexion.cursor.fetchall()
        return listado
        conexion.conexion.commit()
    except sqlite3.OperationalError:
        traceback.print_exc()
        conexion.conexion.rollback()


def insertar_habitacion(habitacion):
    """
    Función encargada de insertar un registro de habitación en la base de datos.
    @param habitacion: contiene todos los datos necesarios para insertar una habitación.
    @return:
    """
    try:
        conexion.cursor.execute('INSERT INTO habitaciones(numero, tipo, precio, libre) VALUES(?,?,?,?)', habitacion)
        conexion.conexion.commit()
    except sqlite3.OperationalError:
        traceback.print_exc()
        conexion.conexion.rollback()


def borrar_habitacion(numero_habitacion):
    """
    Función encargada de eliminar una habitacióin de la base de datos.
    @param numero_habitacion: número de la habitación que se desea eliminar.
    @return:
    """
    try:
        conexion.cursor.execute('DELETE FROM habitaciones WHERE numero = ?', (numero_habitacion,))
        conexion.conexion.commit()
    except sqlite3.OperationalError as e:
        traceback.print_exc()
        conexion.conex.rollback()


def actualizar_habitacion(habitacion_actualizada, numero_habitacion):
    """
    Función encargada de actualizar los datos de una habitación.
    @param habitacion_actualizada: datos de la habitación actualizada.
    @param numero_habitacion: número de la habitación la cual se deasea actualiazar.
    @return:
    """
    try:
        conexion.cursor.execute('UPDATE habitaciones SET tipo = ?, precio = ?, libre = ? WHERE numero = ?',
                                (habitacion_actualizada[0], habitacion_actualizada[1], habitacion_actualizada[2],
                                 numero_habitacion))
        conexion.conexion.commit()
    except sqlite3.OperationalError:
        traceback.print_exc()
        conexion.conexion.rollback()


def cambiar_estado_habitacion(libre, numero_habitacion_reservada):
    """
    Función encargada de actualizar el estado de la habitación que está libre a ocupada cuando se realiza una reserva
    sobre esta habitación o cuando esa habitación deja de estar ocupada a libre.
    @param libre: estado actual de la habitación.
    @param numero_habitacion_reservada: número de la habitación afectada
    @return:
    """
    try:
        conexion.cursor.execute('UPDATE habitaciones SET libre = ? WHERE numero = ?',
                                (libre[0], numero_habitacion_reservada))
        conexion.conexion.commit()
    except sqlite3.OperationalError:
        traceback.print_exc()
        conexion.conexion.rollback()
