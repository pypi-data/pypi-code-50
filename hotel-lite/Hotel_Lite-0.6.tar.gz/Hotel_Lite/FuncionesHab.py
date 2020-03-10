# -*- coding: utf-8 -*-
"""Modulo encargado de la gestion de las habitaciones

Este modulo contiene las siguientes funciones:
    *limpiarEnt
        - Limpia los campos del formulario de habitaciones.

    *insertarhab
        - Inserta un registro en la base de datos.
            + param registro: Lista con los datos
            + Excepciones:
                OperationalError -- Si error en la conexion o en la ejecucion de la query

    *listado
        - Obtiene un listado con las habitaciones.
        - Realiza un select de todos los habitaciones y genera una lista con los resultados.
            + :return: Listado con los clientes

    *listarhab
        - Carga en el treeview de habitaciones la lista de habitaciones.

    *bajanab
        - Baja de la habitacion por el campo numero

    *modifhab
        - Modifica la habitacion utilizando los campos del formulario de habitaciones.

    *controlhab
        - Control de reservas

    *mostrarcli
        - Carga los datos del cliente en el formulario de clientes desde el treeview.

    *cerrartimer
        - Cierra el hilo encargado del control de reservas

    *actualizarhab
        - Actualiza una habitacion

    *cargarenthab
        - Carga datos de la habitacion en la entrada desde el treeview.

"""

import sqlite3, threading
from Hotel_Lite import Variables, FuncionesGenericas, Conexion, FuncionesRes

from datetime import datetime


def limpiarEnt(fila):
    for i in range(3,len(fila)):
        fila[i].set_text("")

    fila[1].set_active(True)

'''
Inserta un registro
'''

def insertarhab(registro):
    try:
        Conexion.cur.execute("insert into habitaciones (nab, tipo, ncamas, npers, precionoc, ocupada) values(?,?,?,?,?,?)", registro)
        Conexion.conex.commit()


    except sqlite3.OperationalError as e:
        print(e)
        Conexion.conex.rollback()

'''
select para utilizar en las operaciones de datos
'''

def listado():
    try:
        Conexion.abrirDB()
        Conexion.cur.execute("select * from habitaciones")
        listado = Conexion.cur.fetchall()
        return listado
    except sqlite3.OperationalError as e:
        print("Error: ", e)

'''
Esta funcion carga el treeview con los datos de la tabla habitaciones
'''
def listarhab(listhabitaciones):

        listhab = listado()
        listhabitaciones.clear()
        for registro in listhab:
            listhabitaciones.append(registro[0:6])

'''
Baja de habitacion por numero
'''

def bajanab(nab):
    try:
        Conexion.abrirDB()
        Conexion.cur.execute("delete from habitaciones where nab=?", (nab,))
        Conexion.conex.commit()
        limpiarEnt(Variables.filahabitacion)
        listarhab(Variables.listlhabitaciones)

    except sqlite3.OperationalError as e:
        print("Error: ", e)
        Conexion.conex.rollback()

    Conexion.cerrarbbdd()

'''
Modificacion de habitacion por registro
'''

def modifhab(registro):

    if Variables.habocupada.get_active():
        ocupada="SI"

    else:
        ocupada="NO"

    Conexion.cur.execute("update habitaciones set nab=?, tipo=?, ncamas=?, npers=?, precionoc=?, ocupada=? where nab=?", (registro[0], registro[1], int(registro[2]), int(registro[3]), float(registro[4]), ocupada , registro[0],))
    Conexion.conex.commit()

'''
Control de reservas
'''

def controlhab():
    Variables.t = threading.Timer(0.5, controlhab)
    Variables.t.daemon = True
    Variables.t.start()
    horahoy = datetime.now().strftime('%H:%M:%S')
    horacontrol = '09:00:00'
    if str(horacontrol) == str(horahoy):
        actualizarhab()

def cerrartimer():
    Variables.t.join(0)


def actualizarhab():

    diahy = datetime.now()

    Conexion.abrirDB()

    Conexion.cur.execute("select fechcheckout from reservas")
    habs = Conexion.cur.fetchall()

    for hab in habs:
        d_fchkout = datetime.strptime(hab[0], '%d/%m/%Y')

        if diahy > d_fchkout:

            Conexion.cur.execute("update habitaciones set ocupada='NO' where ocupada='SI' and nab in (select nab from reservas where fechcheckout=?)", (hab[0],))
            Conexion.cur.execute("delete from reservas where fechcheckout=?", (hab[0],))
            Conexion.conex.commit()

    for nab in Conexion.cur.execute("select hab, fechcheckout from reservas").fetchall():

        if diahy <= datetime.strptime(nab[1], "%d/%m/%Y"):
            Conexion.cur.execute("update habitaciones set ocupada='SI' where nab=?", (hab[0],))

            listarhab(Variables.listlhabitaciones)
            FuncionesRes.listarres()

    Conexion.cerrarbbdd()

def cargarenthab():
    try:
        model, iter = Variables.treehabitaciones.get_selection().get_selected()
        # Model es el modelo del treeview
        # Inter es el numero que identifica a la fila que hemos marcado

        if iter != None:
            nab = str(model.get_value(iter, 0))
            tipo = str(model.get_value(iter, 1))
            ncamas = str(model.get_value(iter, 2))
            npersonas = str(model.get_value(iter, 3))
            pnoche = str(model.get_value(iter, 4))
            stateocupada = str(model.get_value(iter, 5))

            if tipo == "Simple":
                Variables.filahabitacion[0].set_active(True)
            elif tipo == "Double":
                Variables.filahabitacion[1].set_active(True)
            else:
                Variables.filahabitacion[2].set_active(True)

            Variables.filahabitacion[3].set_text(nab)
            Variables.filahabitacion[4].set_text(ncamas)
            Variables.filahabitacion[5].set_text(npersonas)
            Variables.filahabitacion[6].set_text(pnoche)

            if stateocupada == 'SI':
                Variables.habocupada.set_active(True)
            else:
                Variables.habocupada.set_active(False)

    except:
        FuncionesGenericas.showError("Error en en la carga de la lista de clientes")