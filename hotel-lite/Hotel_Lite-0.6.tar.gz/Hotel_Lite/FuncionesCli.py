# -*- coding: utf-8 -*-
"""Modulo encargado de la gestion de los clientes

Este modulo contiene las siguientes funciones:
    *limpiarEnt
        - Limpia los campos del formulario de clientes.

    *insertarcli
        - Inserta un registro en la base de datos.
            + param registro: Lista con los datos
            + Excepciones:
                OperationalError -- Si error en la conexion o en la ejecucion de la query

    *listado
        - Obtiene un listado con los clientes.
        - Realiza un select de todos los clientes y genera una lista con los resultados.
            + :return: Listado con los clientes

    *listarcli
        - Carga en el treeview de clientes la lista de clientes.

    *selectcli
        - Selecciona retorna el id de un cliente por su DNI.
            + :param dni: dni del cliente
            + :return: id

    *bajacli
        - Baja del cliente pr dni obtenido del campo dni.

    *modificarcliente
        - Modifica el cliente utilizando los campos del formulario de cliente.

    *insertarclimod
        - Actualiza la base de datos con los datos de un cliente modificado.
            +Excepciones:
                Exception -- Excepcion generica

    *altacli
        - Realiza las comprobaciones y limpia la entrada del formulario clientes durante un alta.

    *mostrarcli
        - Carga los datos del cliente en el formulario de clientes desde el treeview.

"""

from Hotel_Lite import Variables, FuncionesGenericas, Conexion, FuncionesRes
import sqlite3

from Hotel_Lite.FuncionesGenericas import validoDNI


def limpiarEnt():
    fila = Variables.filacli

    for i in range(len(fila)):
        fila[i].set_text("")


'''
Inserta un registro
'''


def insertarcli(registro):
    try:
        Conexion.cur.execute("insert into clientes (dni, apel, nome, data) values(?,?,?,?)", registro)
        Conexion.conex.commit()


    except sqlite3.OperationalError as e:
        Conexion.conex.rollback()


'''
select para utilizar en las operaciones de datos
'''


def listado():
    try:

        Conexion.cur.execute("select * from clientes")
        listado = Conexion.cur.fetchall()
        Conexion.conex.commit()

        return listado
    except sqlite3.OperationalError as e:
        print("Error: ", e)


'''
Esta funcion carga el treeview con los datos de la tabla clientes
'''


def listarcli():
    try:
        Variables.listado = listado()
        listclientes = Variables.listlclientes

        listclientes.clear()
        for registro in Variables.listado:
            listclientes.append(registro[1:5])

    except:
        print("Error en treeview")


'''
Seleccionar cliente por dni
'''


def selectcli(dni):
    try:
        Conexion.cur.execute("select id from clientes where dni=?", (dni,))
        res = Conexion.cur.fetchone()
        return str(res[0])
    except sqlite3.OperationalError as e:
        print("Error: ", e)


'''
Baja de cliente por dni
'''


def bajacli():
    try:

        dni = Variables.filacli[1].get_text()
        if dni != "":
            Conexion.cur.execute("delete from clientes where dni=?", (dni,))
            Conexion.conex.commit()

            listarcli()
            limpiarEnt()

    except sqlite3.OperationalError as e:
        print("Error: ", e)
        Conexion.conex.rollback()


'''
Modificacion de cliente
'''


def modificarcliente():
    try:
        cod = Variables.filacli[0].get_text()
        dni = Variables.filacli[1].get_text()
        apel = Variables.filacli[2].get_text()
        nome = Variables.filacli[3].get_text()
        data = Variables.filacli[5].get_text()

        registro = (cod, dni, apel, nome, data)

        if dni != "" and validoDNI(dni):
            insertarclimod(registro)
            listarcli()
            limpiarEnt()
        else:
            FuncionesGenericas.showError("Falto el DNI o no es valido")

    except Exception as e:
        FuncionesGenericas.showError("Error en modificacion", e)


def insertarclimod(registro):
    Conexion.cur.execute("update clientes set dni=?, apel=?, nome=?, data=? where id=?",
                         (registro[1], registro[2], registro[3], registro[4], registro[0],))
    Conexion.conex.commit()


'''
Alta de cliente
'''


def altacli():
    try:

        dni = Variables.filacli[1].get_text()
        apel = Variables.filacli[2].get_text()
        nome = Variables.filacli[3].get_text()
        data = Variables.filacli[5].get_text()
        registro = (dni, apel, nome, data)

        if dni != "" and apel != "":

            if validoDNI(dni):
                Variables.filacli[4].set_text("")
                insertarcli(registro)
                Variables.listlclientes.append(registro)
                Variables.treelclientes.show()
                limpiarEnt()

            else:
                Variables.filacli[4].set_text("X")

    except:
        FuncionesGenericas.showError("Error en altas")


'''
Mostrar en la entrada el cliente seleccionado en el treeview
'''


def mostrarcli():
    try:

        model, iter = Variables.treelclientes.get_selection().get_selected()
        # Model es el modelo del treeview
        # Inter es el numero que identifica a la fila que hemos marcado

        if iter != None:
            datos = [model.get_value(iter, 0), model.get_value(iter, 1), model.get_value(iter, 2),
                     model.get_value(iter, 3)]

            Variables.filacli[0].set_text(selectcli(datos[0]))
            Variables.filacli[1].set_text(datos[0])
            Variables.filacli[2].set_text(datos[1])
            Variables.filacli[3].set_text(datos[2])
            Variables.filacli[5].set_text(datos[3])
            Variables.filareservas[0].set_text(datos[0])
            Conexion.abrirDB()
            FuncionesRes.limpiarEnt()
            FuncionesRes.setapeldni(Variables.filareservas[0].get_text())
            Conexion.cerrarbbdd()

    except:
        FuncionesGenericas.showError("Error en treeclientes")
