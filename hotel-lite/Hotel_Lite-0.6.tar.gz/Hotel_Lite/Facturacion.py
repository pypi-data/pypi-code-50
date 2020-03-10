# -*- coding: utf-8 -*-

"""Este modulo contiene las funciones que se encargan de operaciones de facturacion.
Este modulo contiene las siguientes funciones:
    *actfact
        -Actualizar la factura

    *addservicios
        -Anade servicios a la factura

    *limpiarfac
        -Limpia la factura

"""

from Hotel_Lite import Variables, Conexion


def actfact():
    model, iter = Variables.treereservas.get_selection().get_selected()
    # Model es el modelo del treeview
    # Inter es el numero que identifica a la fila que hemos marcado

    if iter != None:

        dni = model.get_value(iter, 0)
        nome = model.get_value(iter, 1)
        habitacion = model.get_value(iter, 2)
        dfechcheckin = model.get_value(iter, 3)
        dfechcheckout = model.get_value(iter, 4)
        nnoches = model.get_value(iter, 5)

        Conexion.cur.execute("select nome from clientes where dni=?", (dni,))
        nome += ", " + str(Conexion.cur.fetchone()[0])

        Conexion.cur.execute(
            "select codres from reservas where dnicli=? and hab=? and fechcheckin=? and fechcheckout=? and nueva='true'",
            (dni, habitacion, dfechcheckin, dfechcheckout,))
        codres = str(Conexion.cur.fetchone()[0])

        Conexion.cur.execute("select precionoc from habitaciones where nab=?", (habitacion,))
        precionoc = float(Conexion.cur.fetchone()[0])

        limpiarfac()

        Variables.varsfact[0].set_text(dni)
        Variables.varsfact[1].set_text(nome)
        Variables.varsfact[2].set_text(codres)
        Variables.listfact.append(["Noches", str(nnoches), str(precionoc), str(float(nnoches) * precionoc), ])
        Variables.varsfact[3].set_text(str(habitacion))

        addservicios(codres, float(nnoches) * precionoc)


def addservicios(codres, preciototalhab):
    Conexion.cur.execute(
        "select Servicio, count(Servicio), PrecioUnitario , sum(PrecioUnitario) from servicios where IdReserva=? group by Servicio",
        (codres,))

    listservs = Conexion.cur.fetchall()
    total = preciototalhab
    totaliva = preciototalhab + ((preciototalhab/100)*10)

    for registro in listservs:
        Variables.listfact.append([str(registro[0]), str(registro[1]), str(registro[2]), str(registro[3]), ])
        total += float(registro[3])

        if registro[0] == "Comida" or registro[0] == "Desayuno":
            iva = 10
        else:
            iva = 21

        totaliva += float(registro[3] + ((registro[3]/100)*iva))

    Variables.varsfact[4].set_text(str(total))
    Variables.varsfact[5].set_text(str(totaliva))
    Variables.varsfact[6].set_text(str(round(totaliva - total, 2)))


def limpiarfac():
    for d in range(len(Variables.varsfact)):
        Variables.varsfact[d].set_text("")

    Variables.listfact.clear()
