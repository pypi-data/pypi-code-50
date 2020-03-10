# -*- coding: utf-8 -*-

"""Modulo encargado de la gestion de los clientes

Este modulo contiene las siguientes funciones:
    *cargarHabsPik
        - Carga el combobox de habitaciones
    *limpiarEnt
        - Limpia los campos del formulario de reservas.

    *setapeldni
        - Carga el apellido a partir del dni
            + :param dni: DNI

    *insertarres
        - Inserta un registro en la base de datos.
            + param registro: Lista con los datos
            + Excepciones:
                OperationalError -- Si error en la conexion o en la ejecucion de la query

    *listado
        - Obtiene un listado con los reservas.
        - Realiza un select de todos los reservas y genera una lista con los resultados.
            + :return: Listado con las reservas

    *listarres
        - Carga en el treeview de reservas la lista de reservas.

    *selectcli
        - Selecciona retorna el id de un cliente por su DNI.
            + :param dni: dni del cliente
            + :return: id

    *bajares
        - Baja de la reserva.

    *modifres
        - Modifica la reserva

    *altareserva
        - Realiza las comprobaciones y limpia la entrada del formulario reserva durante un alta.

    *cargarres
        - Carga los datos del cliente en el formulario de clientes desde el treeview.

    *valfechas
        - Valida las fechas de reserva ara una habitacion
            + :param fecha1: comienzo del rango
            + :param fecha2: final del rango
            + :param nab: Numero de habitacion

"""

import sqlite3
from datetime import *

from Hotel_Lite import FuncionesServicios, FuncionesHab, Variables, FuncionesGenericas, Conexion, Facturacion


def cargarHabsPik():
    Conexion.cur.execute("select nab from habitaciones")
    listado = Conexion.cur.fetchall()

    Variables.comboxlist.clear()

    for entr in listado:
        Variables.comboxlist.append(entr)


'''
Obtiene un apellido en base a un dni
'''


def setapeldni(dni):
    try:

        Conexion.cur.execute("select apel from clientes where dni=?", (dni,))
        cliapel = Conexion.cur.fetchone()
        Variables.filareservas[1].set_text(cliapel[0])

    except:
        pass


'''
Esta funcion carga el treeview con los datos de la tabla reservas
'''


def listarres():
    try:

        listres = Variables.listreservas

        listreservas = listado()
        listres.clear()
        for registro in listreservas:
            registrofin = []
            registrofin.append(str(registro[0]))
            Conexion.abrirDB()
            Conexion.cur.execute("select apel from clientes where dni=?", (str(registro[0]),))
            cliapel = Conexion.cur.fetchone()

            registrofin.append(str(cliapel[0]))
            registrofin.append(registro[1])
            registrofin.append(str(registro[2]))
            registrofin.append(str(registro[3]))

            d_fchkin = datetime.strptime(registro[2], "%d/%m/%Y")
            d_fchkout = datetime.strptime(registro[3], "%d/%m/%Y")

            dl = d_fchkout - d_fchkin

            registrofin.append(dl.days)

            listres.append(registrofin)

    except:
        FuncionesGenericas.showError("Error en listar reservas")


'''
select para utilizar en las operaciones de datos
'''


def listado():
    try:
        Conexion.cur.execute("select * from reservas where nueva='true'")
        list = Conexion.cur.fetchall()
        Conexion.conex.commit()
        return list
    except sqlite3.OperationalError as e:
        FuncionesGenericas.showError(str("Error: ", e))


'''
Inserta un registro
'''


def insertarres(registro):
    try:

        if registro[0] != "":

            d_fchkin = datetime.strptime(registro[2], "%d/%m/%Y")
            d_fchkout = datetime.strptime(registro[3], "%d/%m/%Y")
            fch_hoy = datetime.now()

            if (d_fchkout - d_fchkin).days > 0:
                if valfechas(registro[2], registro[3], registro[1]):
                    Conexion.cur.execute(
                        "insert into reservas (dnicli, hab, fechcheckin, fechcheckout) values(?,?,?,?)",
                        registro)

                    if fch_hoy >= d_fchkin:
                        Conexion.cur.execute("update habitaciones set ocupada='SI' where nab=?", (registro[1],))

                    Conexion.conex.commit()

                    Facturacion.actfact()

                    limpiarEnt()
                    listarres()
                    FuncionesHab.listarhab(Variables.listlhabitaciones)

                else:
                    FuncionesGenericas.showError("Las fechas coinciden con una reserva ya existente.")

        else:
            FuncionesGenericas.showError("El DNI no es valido.")

    except:
        FuncionesGenericas.showError("Error en la insercion de la reserva")


'''
Limpia la entrada del formulario de reservas
'''


def limpiarEnt():
    fila = Variables.filareservas

    fila[0].set_text("")
    fila[1].set_text("")
    for i in range(3, len(fila)):
        fila[i].set_text("")


'''
Eliminar un registro o pedir confirmacion para hacerlo
'''


def bajares(dni, hab, fechcheckin, conf):
    try:

        fechhoy = datetime.now()
        fechchin = datetime.strptime(fechcheckin, "%d/%m/%Y")

        if fechhoy >= fechchin or conf:
            Conexion.cur.execute("update reservas set nueva='false' where dnicli=? and hab=? and fechcheckin=?",
                                 (dni, hab, fechcheckin,))
            Conexion.cur.execute("update habitaciones set ocupada='NO' where nab=?", (hab,))
            Conexion.conex.commit()

            limpiarEnt()
            FuncionesHab.listarhab(Variables.listlhabitaciones)
            Conexion.abrirDB()
            listarres()
            Conexion.cerrarbbdd()
            Facturacion.limpiarfac()
            FuncionesServicios.limpiarent()
            Variables.listservicios.clear()

        else:
            Variables.diagdialog.connect('delete-event', lambda w, e: w.hide() or True)
            Variables.diagdialog.show()

    except sqlite3.OperationalError as e:
        FuncionesGenericas.showError(str("Error: ", e))
        Conexion.conex.rollback()


'''
Modifica n registro de reservas
'''


def modifres(registro):
    try:
        index = Variables.filareservas[2].get_active()
        model = Variables.filareservas[2].get_model()
        it = model[index]

        Conexion.cur.execute("update reservas set dnicli=?, fechcheckin=?, fechcheckout=? where dnicli=? and hab=?", (
            str(registro[0].get_text()), str(registro[3].get_text()), str(registro[4].get_text()),
            str(registro[0].get_text()), int(it[0]),))
        Conexion.conex.commit()
        listarres()
        Facturacion.actfact()

    except:
        FuncionesGenericas.showError("Ha ocurrido un error mientras se modificaba la reserva.")


'''
Validar las fechas de la reserva con fechas de las reservas actuales.
'''


def valfechas(fecha1, fecha2, nab):
    fecha1_date = datetime.strptime(fecha1, "%d/%m/%Y")
    fecha2_date = datetime.strptime(fecha2, "%d/%m/%Y")
    listfech = listado()
    rtrn = True

    fechocup = [fecha1_date + timedelta(days=d) for d in range((fecha2_date - fecha1_date).days + 1)]

    for l in listfech:
        fecha1_res = datetime.strptime(l[2], "%d/%m/%Y")
        fecha2_res = datetime.strptime(l[3], "%d/%m/%Y")

        if l[1] == nab:

            fechrang = [fecha1_res + timedelta(days=d) for d in range((fecha2_res - fecha1_res).days + 1)]

            for i in range(len(fechocup)):

                if len(fechocup) > 2:

                    if i != 0 and i != len(fechocup):
                        if fechrang[i] in fechocup:
                            rtrn = False
                            break

                    else:
                        if fechrang[i] in fechocup:
                            rtrn = False
                            break

    return rtrn


'''
Alta de reserva
'''


def altareserva():
    index = Variables.filareservas[2].get_active()
    model = Variables.filareservas[2].get_model()
    it = model[index]
    registro = Variables.filareservas[0].get_text(), it[0], Variables.filareservas[3].get_text(), \
               Variables.filareservas[4].get_text()
    insertarres(registro)


'''
Baja de reserva
'''


def bajareserva():
    dni = Variables.filareservas[0].get_text()

    index = Variables.filareservas[2].get_active()
    model = Variables.filareservas[2].get_model()

    checkin = Variables.filareservas[3].get_text()

    if dni != "" and checkin != "" and index != -1:
        it = model[index]
        bajares(dni, it[0], checkin, False)


'''
Cargar reserva en entrada desde seleccion en el treeview
'''


def cargarres():
    model, iter = Variables.treereservas.get_selection().get_selected()
    # Model es el modelo del treeview
    # Inter es el numero que identifica a la fila que hemos marcado

    if iter is not None:

        datares = [model.get_value(iter, 0), model.get_value(iter, 1), model.get_value(iter, 2)]

        Variables.filareservas[0].set_text(datares[0])
        Variables.filareservas[1].set_text(datares[1])

        mcmb = Variables.filareservas[2].get_model()

        for mod in range(len(mcmb)):
            it = mcmb[mod]
            if it[0] == datares[2]:
                Variables.filareservas[2].set_active(mod)

        for num in range(3, len(Variables.filareservas)):
            Variables.filareservas[num].set_text(str(model.get_value(iter, num)))

        Facturacion.actfact()

        Conexion.cur.execute(
            "select codres from reservas where dnicli=? and hab=? and fechcheckin=? and fechcheckout=? and nueva='true'",
            (model.get_value(iter, 0), model.get_value(iter, 2), model.get_value(iter, 3),
             model.get_value(iter, 4),))
        listado = Conexion.cur.fetchone()

        Variables.filaservicios[0].set_text(str(listado[0]))
        FuncionesServicios.listaserv(str(listado[0]))
