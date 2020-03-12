# coding=utf-8
"""
Aquí vendrán todas las funciones que afectan a la gestión de las reservas, cálculo del número de noches, inserciones,
updates, etc...
"""
import sqlite3
import traceback

from datetime import datetime
import conexion
import funciones_genericas
import variables


def calcular_noches():
    """
    En este método se calcula el número de noches que se va a quedar un cliente, tomando la fecha del entry-box del
    Check-in y del Check-out y haciendo el correspondiente calculo, en caso de estar las fechas bien, mostrará el número
    de noches que pasará el cliente y actualizará el flag a 1.
    En caso de que el usuario haya puesto mal la fecha (Check-out antes del Check-in) lanzará un mensaje de error
    en la GUI actualizará el flag a 0.
    @return:
    """
    dia_in = variables.fila_reservas[2].get_text()
    date_in = datetime.strptime(dia_in, '%d/%m/%Y').date()
    dia_out = variables.fila_reservas[3].get_text()
    date_out = datetime.strptime(dia_out, '%d/%m/%Y').date()
    noches = (date_out - date_in).days
    if noches <= 0:
        variables.labels_informativos[5].set_text('Check-Out debe ser posterior')
        variables.reserva = 0
    else:
        variables.reserva = 1
        variables.labels_informativos[5].set_text(str(noches))


def es_libre(numero_habitacion):
    """
    Comprueba si la habitación seleccionada está libre o no.
    @param numero_habitacion: el número de la habitación seleccionada por el usuario.
    @return: devuelve true en caso de estar libre y false en el caso contrario.
    """
    try:
        conexion.cursor.execute('SELECT libre FROM habitaciones WHERE numero = ?', (numero_habitacion,))
        lista = conexion.cursor.fetchone()
        conexion.conexion.commit()
        if lista[0] == 'SI':
            return True
        else:
            return False
    except sqlite3.OperationalError:
        traceback.print_exc()
        conexion.conex.rollback()


def cargar_reservas(list_reservas):
    """
    Esta función carga el tree view con los datos de la tabla de reservas.
    @param list_reservas: lista de las reservas.
    @return:
    """
    try:
        variables.listado = funciones_genericas.consulta_listado('reservas')
        list_reservas.clear()
        for registro in variables.listado:
            list_reservas.append(registro)
    except Exception:
        traceback.print_exc()


def insertar_reservas(fila):
    """
    Insertar en la base de datos un registro de reservas.
    @param fila: Que contiene todos los datos de la reserva.
    @return:
    """
    try:
        conexion.cursor.execute(
            'INSERT INTO reservas(dni, numero_habitacion, checkin, checkout, noches) VALUES(?,?,?,?,?)', fila)
        conexion.conexion.commit()
    except sqlite3.OperationalError:
        traceback.print_exc()


def borrar_reservas(codigo):
    """
    Borrar de la base de datos un registro de reservas
    @param codigo: el código de la reserva (primary key en la base de datos)
    @return:
    """
    try:
        conexion.cursor.execute('DELETE FROM reservas WHERE codigo_reserva = ?', (codigo,))
        conexion.conexion.commit()
    except sqlite3.OperationalError:
        traceback.print_exc()
        conexion.conexion.rollback()


def actualizar_reservas(reserva_actualizada, codigo_reserva):
    """
    Actualizar de la bbase de datos una reserva.
    @param reserva_actualizada: Los datos actualizados de la reserva.
    @param codigo_reserva: El código de la reserva que se desea actualizar.
    @return:
    """
    try:
        conexion.cursor.execute(
            'UPDATE reservas SET dni = ?, numero_habitacion = ?, checkin = ?, checkout = ?, noches = ? WHERE '
            'codigo_reserva = ?',
            (reserva_actualizada[0], reserva_actualizada[1], reserva_actualizada[2],
             reserva_actualizada[3], reserva_actualizada[4], codigo_reserva))
        conexion.conexion.commit()
    except sqlite3.OperationalError:
        traceback.print_exc()
        conexion.conexion.rollback()


def buscar_cliente_apellido_por_dni(dni):
    """
    Consulta en la que se obtiene el apellido del cliente buscándolo por su DNI.
    @param dni: El DNI del cliente.
    @return: El apellido del cliente.
    """
    try:
        conexion.cursor.execute('SELECT apellidos FROM clientes WHERE dni = ?', (dni,))
        apellidos = conexion.cursor.fetchone()
        conexion.conexion.commit()
        return apellidos
    except sqlite3.OperationalError:
        traceback.print_exc()
        conexion.conexion.rollback()


def buscar_cliente_nombre_por_dni(dni):
    """
    Consulta en la que se obtiene el nombre del cliente buscándolo por su DNI.
    @param dni: El DNI del cliente.
    @return: El nombre del cliente.
    """
    try:
        conexion.cursor.execute('SELECT nombre FROM clientes WHERE dni = ?', (dni,))
        nombre = conexion.cursor.fetchone()
        conexion.conexion.commit()
        return nombre
    except sqlite3.OperationalError:
        traceback.print_exc()
        conexion.conexion.rollback()
