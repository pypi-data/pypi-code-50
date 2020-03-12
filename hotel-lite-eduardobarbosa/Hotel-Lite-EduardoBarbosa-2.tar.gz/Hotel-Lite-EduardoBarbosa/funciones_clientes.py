# coding=utf-8
"""
Aquí vendrán todas las funciones que afectan a la gestión de los clientes
"""
import sqlite3
import traceback

import conexion
import funciones_genericas
import variables


def cargar_clientes(list_clientes):
    """
    Función encargada de cargar el tree view con los datos de la tabla de clientes de la base de datos
    @param list_clientes: lista de clientes
    @return:
    """
    try:
        variables.listado = funciones_genericas.consulta_listado('clientes')
        list_clientes.clear()
        for registro in variables.listado:
            list_clientes.append(registro[1:5])
    except Exception:
        traceback.print_exc()


def insertar_cliente(cliente):
    """
    Función encargada de insertar en la base de datos un registro de cliente.
    @param cliente: Contiene todos los datos necesarios para insertar un cliente.
    @return:
    """
    try:
        conexion.cursor.execute('INSERT INTO clientes(dni, apellidos, nombre, fecha) VALUES(?,?,?,?)', cliente)
        conexion.conexion.commit()
    except sqlite3.OperationalError:
        traceback.print_exc()


def borrar_cliente(dni):
    """
    Función encargada de borrar un registro de cliente en la base de datos en función a su DNI.
    @param dni: DNI del cliente el cual se desea eliminar de la base de datos.
    @return:
    """
    try:
        conexion.cursor.execute('DELETE FROM clientes WHERE dni = ?', (dni,))
        conexion.conexion.commit()
    except sqlite3.OperationalError:
        traceback.print_exc()
        conexion.conexion.rollback()


def actualizar_cliente(cliente_actualizado, codigo_cliente):
    """
    Función encargada de actualizar los datos de un cliente existente en la base de datos.
    @param cliente_actualizado: Los datos del cliente ya actualizados.
    @param codigo_cliente: Código del cliente a actualizar (primary key en la base de datos)
    @return:
    """
    try:
        conexion.cursor.execute('UPDATE clientes SET dni = ?, apellidos = ?, nombre = ?, fecha = ? WHERE id = ?',
                                (cliente_actualizado[0], cliente_actualizado[1], cliente_actualizado[2],
                                 cliente_actualizado[3], codigo_cliente))
        conexion.conexion.commit()
    except sqlite3.OperationalError:
        traceback.print_exc()
        conexion.conexion.rollback()


def select_cliente(dni):
    """
    Función encargada de obetener el ID del cliente seleccionado en el tree view.
    @param dni: DNI del cliente seleccionado en el tree view.
    @return: id del cliente.
    """
    try:
        conexion.cursor.execute('SELECT id FROM clientes WHERE dni = ?', (dni,))
        cliente = conexion.cursor.fetchone()
        conexion.conexion.commit()
        return cliente
    except sqlite3.OperationalError:
        traceback.print_exc()
        conexion.conexion.rollback()
