# -*- coding: utf-8 -*-

"""Modulo encargado de la exportación a PDF

Este modulo contiene las siguientes funciones:
    *basico
        - Crea un formulario base
            +:return bill: Datos del formulario

    *factura
        - Crea una factura

    *impFactura
        - Crea la factura con los datos requeridos
            + :param bill: Datos de la factura

"""
from reportlab.platypus import PageBreak

from Hotel_Lite import Variables, FuncionesGenericas
import os
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def basico(nombre):
    try:

        fecha = datetime.now().strftime("%d/%m/%Y")

        bill = canvas.Canvas(nombre, pagesize=A4)
        text = "Bienvenido a nuestro hotel"
        textcif = "Cif: 00000000a"
        textpie = "Hotel Lite CIF: 00000000a tlf: 986000000 e-mail: info@hotellite.com"
        bill.drawImage('./img/hotel-128x128.png', 460, 735, width=64, height=64)
        bill.setFont('Courier', size=15)
        bill.drawString(233, 770, 'HOTEL LITE')
        bill.setFont('Courier', size=11)
        bill.drawString(50, 730, textcif)
        bill.drawString(190, 750, text)
        bill.drawString(460, 710, fecha)
        bill.line(50, 700, 525, 700)

        bill.line(50, 40, 525, 40)
        bill.drawString(70, 20, textpie)

        return bill

    except:
        print("Error en basico")


def factura():
    try:

        exist = True

        for i in Variables.varsfact:
            if i.get_text() == "":
                exist = False
                break

        if exist:

            bill = basico("factura.pdf")

            impFactura(bill)

            dir = os.getcwd()
            os.system('/usr/bin/xdg-open ' + dir + "/factura.pdf")

        else:
            FuncionesGenericas.showError("No hay suficientes datos para imprimir la factura")

    except:
        print("Error en factura")


def impFactura(bill):
    bill.drawString(50, 660, 'DNI:')
    bill.drawString(50, 640, 'Nombre:')
    bill.drawString(350, 660, 'Codigo Reserva:')
    bill.drawString(350, 640, 'Habitacion:')
    bill.line(50, 620, 525, 620)
    bill.drawString(50, 610, 'CONCEPTO')
    bill.drawString(150, 610, 'UNIDADES')
    bill.drawString(250, 610, 'Precio Unitario')
    bill.drawString(450, 610, 'TOTAL')
    bill.line(50, 605, 525, 605)

    bill.drawString(160, 660, Variables.varsfact[0].get_text())
    bill.drawString(160, 640, Variables.varsfact[1].get_text())
    bill.drawString(510, 660, Variables.varsfact[2].get_text())
    bill.drawString(510, 640, Variables.varsfact[3].get_text())
    bill.drawString(50, 710, "Factura nº: " + Variables.varsfact[2].get_text())

    facturabasey = 590

    facturabasex = 50

    facturatotal = 0

    facturatotaliva = 0

    for registro in Variables.listfact:
        # Concepto

        bill.drawString(facturabasex, facturabasey, registro[0])

        # Unidades
        bill.drawString(facturabasex + 100, facturabasey, registro[1])

        # Precio unitario

        bill.drawString(facturabasex + 200, facturabasey, registro[2] + '€')

        # Total

        bill.drawString(facturabasex + 400, facturabasey, registro[3] + '€')
        facturatotal += float(registro[3])
        iva = calcularIva(registro[0])

        facturatotaliva += round(float(registro[3]) + ((float(registro[3]) / 100) * iva), 2)
        facturabasey -= 20

        if facturabasey < 150:
            bill.showPage()

            fecha = datetime.now().strftime("%d/%m/%Y")

            text = "Bienvenido a nuestro hotel"
            textcif = "Cif: 00000000a"
            textpie = "Hotel Lite CIF: 00000000a tlf: 986000000 e-mail: info@hotellite.com"
            bill.drawImage('./img/hotel-128x128.png', 460, 735, width=64, height=64)
            bill.setFont('Courier', size=15)
            bill.drawString(233, 770, 'HOTEL LITE')
            bill.setFont('Courier', size=11)
            bill.drawString(50, 730, textcif)
            bill.drawString(190, 750, text)
            bill.drawString(460, 710, fecha)
            bill.line(50, 700, 525, 700)
            bill.line(50, 40, 525, 40)
            bill.drawString(70, 20, textpie)
            bill.drawString(50, 660, 'DNI:')
            bill.drawString(50, 640, 'Nombre:')
            bill.drawString(350, 660, 'Codigo Reserva:')
            bill.drawString(350, 640, 'Habitacion:')
            bill.line(50, 620, 525, 620)
            bill.drawString(50, 610, 'CONCEPTO')
            bill.drawString(150, 610, 'UNIDADES')
            bill.drawString(250, 610, 'Precio Unitario')
            bill.drawString(450, 610, 'TOTAL')
            bill.line(50, 605, 525, 605)

            bill.drawString(160, 660, Variables.varsfact[0].get_text())
            bill.drawString(160, 640, Variables.varsfact[1].get_text())
            bill.drawString(510, 660, Variables.varsfact[2].get_text())
            bill.drawString(510, 640, Variables.varsfact[3].get_text())
            bill.drawString(50, 710, "Factura nº: " + Variables.varsfact[2].get_text())

            facturabasey = 590

    bill.line(50, 140, 525, 140)
    bill.drawString(facturabasex + 352, 120, "Total: ")
    bill.drawString(facturabasex + 400, 120, str(round(facturatotal, 2)) + '€')

    bill.drawString(facturabasex + 365, 95, "IVA: ")
    bill.drawString(facturabasex + 400, 95, str(round(facturatotaliva - facturatotal, 2)) + '€')

    bill.drawString(facturabasex + 300, 70, "Total con IVA: ")
    bill.drawString(facturabasex + 400, 70, str(round(facturatotaliva, 2)) + '€')

    bill.save()
    bill.showPage()


def calcularIva(registro):
    if registro == "Desayuno" or registro == "Comida" or registro == "Noches":
        iva = 10
    else:
        iva = 21

    return iva


def listadoCli():
    list = basico("clientes.pdf")

    list.drawString(70, 610, 'DNI')
    list.drawString(180, 610, 'Apelidos')
    list.drawString(310, 610, 'Nome')
    list.drawString(460, 610, 'Fecha')

    basey = 590

    basex = 60

    for registro in Variables.listado:

        # DNI
        list.drawString(basex, basey, FuncionesGenericas.censuraDNI(registro[1]))

        # Apelidos
        list.drawString(basex + 80, basey, registro[2])

        # Nome

        list.drawString(basex + 220, basey, registro[3])

        # Data

        list.drawString(basex + 360, basey, registro[4])

        basey -= 20

        if basey < 70:
            list.showPage()

            fecha = datetime.now().strftime("%d/%m/%Y")

            text = "Bienvenido a nuestro hotel"
            textcif = "Cif: 00000000a"
            textpie = "Hotel Lite CIF: 00000000a tlf: 986000000 e-mail: info@hotellite.com"
            list.drawImage('./img/hotel-128x128.png', 460, 735, width=64, height=64)
            list.setFont('Courier', size=15)
            list.drawString(233, 770, 'HOTEL LITE')
            list.setFont('Courier', size=11)
            list.drawString(50, 730, textcif)
            list.drawString(190, 750, text)
            list.drawString(460, 710, fecha)
            list.line(50, 700, 525, 700)

            list.line(50, 40, 525, 40)
            list.drawString(70, 20, textpie)
            basey = 590

    list.showPage()
    list.save()

    dir = os.getcwd()
    os.system('/usr/bin/xdg-open ' + dir + "/clientes.pdf")
