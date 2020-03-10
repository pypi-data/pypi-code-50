# -*- coding: utf-8 -*-

"""Modulo encargado de la gestion de los clientes

Este modulo contiene las siguientes funciones:

    *altaServicioOrd
        - Realiza las comprobaciones y limpia la entrada del formulario de servicios durante un alta.

    *listaserv
        - Carga en el treeview de reservas la lista de servicios.

    *listado
        - Obtiene un listado con los servicios.
        - Realiza un select de todos los servicios y genera una lista con los resultados.
            + :return: Listado con los servicios

    *bajaserv
        - Baja del servicio.

    *limpiarEnt
        - Limpia los campos del formulario de servicios.

    *entrserv
        - Carga los datos de servicios en el formulario de servicios desde el treeview.

"""

from Hotel_Lite import Variables, FuncionesGenericas, Conexion, Facturacion


# Alta servicio ordinario

def altaServicioOrd():
    try:

        servicio = ""

        punidad = Variables.filaservicios[4].get_text()

        if Variables.filaservicios[5].get_text() != "":

            servicio = Variables.filaservicios[5].get_text()
            punidad = Variables.filaservicios[6].get_text()

        elif Variables.filaservicios[1].get_active():

            servicio = "Desayuno"

        elif Variables.filaservicios[2].get_active():

            servicio = "Comida"

        elif Variables.filaservicios[3].get_active():

            servicio = "Parking"

        if punidad != "" and Variables.filaservicios[0].get_text() != "":

            if Variables.filaservicios[5].get_text() != "":

                Conexion.cur.execute(
                    "insert into servicios (IdReserva,PrecioUnitario,Servicio) values (?,?,?)",
                    (Variables.filaservicios[0].get_text(), float(punidad), servicio,))
                Conexion.conex.commit()

            else:
                for i in range(int(Variables.filareservas[5].get_text())):
                    Conexion.cur.execute(
                        "insert into servicios (IdReserva,PrecioUnitario,Servicio) values (?,?,?)",
                        (Variables.filaservicios[0].get_text(), float(punidad), servicio,))
                    Conexion.conex.commit()

            listaserv(Variables.filaservicios[0].get_text())

            Facturacion.actfact()
            limpiarent()

        else:
            FuncionesGenericas.showError("Se ha introducido un campo invalido")

    except:
        FuncionesGenericas.showError("Se ha introducido un campo invalido")


'''
Esta funcion carga el treeview con los datos de la tabla servicios
'''


def listaserv(idres):
    try:

        listservs = listado(idres)
        Variables.listservicios.clear()
        for registro in listservs:
            registrofin = [int(registro[0]), str(registro[2]), float(registro[1]), int(registro[3])]

            Variables.listservicios.append(registrofin)

    except:
        FuncionesGenericas.showError("Error al listar los servicios")


'''
select para utilizar en las operaciones de datos
'''


def listado(idres):
    Conexion.cur.execute("select * from servicios where IdReserva=?", (idres,))
    list = Conexion.cur.fetchall()
    Conexion.conex.commit()
    return list


'''
Baja de servicio
'''


def bajaserv():
    try:

        model, iter = Variables.treeservicios.get_selection().get_selected()
        # Model es el modelo del treeview
        # Inter es el numero que identifica a la fila que hemos marcado

        if iter is not None:

            idserv = model.get_value(iter, 3)

            Conexion.cur.execute("delete from servicios where id_servicio=?", (idserv,))
            Conexion.conex.commit()
            listaserv(str(model.get_value(iter, 0)))
            Facturacion.actfact()
            limpiarent()

        else:
            FuncionesGenericas.showError("Selecciona una entrada")

    except:
        FuncionesGenericas.showError("Error en la eliminacion de un servicio")


def entrserv():
    try:
        model, iter = Variables.treeservicios.get_selection().get_selected()
        # Model es el modelo del treeview
        # Inter es el numero que identifica a la fila que hemos marcado

        if iter != None:
            num_reserva = str(model.get_value(iter, 0))
            tipo = str(model.get_value(iter, 1))
            precio_unidad = str(model.get_value(iter, 2))

            if tipo == "Desayuno":
                Variables.filaservicios[1].set_active(True)
                Variables.filaservicios[5].set_text("")
                Variables.filaservicios[6].set_text("")
            elif tipo == "Comida":
                Variables.filaservicios[2].set_active(True)
                Variables.filaservicios[5].set_text("")
                Variables.filaservicios[6].set_text("")
            elif tipo == "Parking":
                Variables.filaservicios[3].set_active(True)
                Variables.filaservicios[5].set_text("")
                Variables.filaservicios[6].set_text("")
            else:
                Variables.filaservicios[5].set_text(tipo)
                Variables.filaservicios[6].set_text(precio_unidad)

            Variables.filaservicios[0].set_text(num_reserva)
            Variables.filaservicios[4].set_text(precio_unidad)

    except:
        FuncionesGenericas.showError("Ha ocurrido un error cargando de la lista de servicios")


def limpiarent():
    for i in range(4, len(Variables.filaservicios)):
        Variables.filaservicios[i].set_text("")
