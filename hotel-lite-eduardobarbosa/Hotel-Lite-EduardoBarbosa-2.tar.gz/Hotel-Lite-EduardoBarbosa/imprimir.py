# coding=utf-8
"""
En esta clase se realizará la tarea de imprimir la factura de la reserva
"""
import os
import traceback
import datetime

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

import variables


def basico():
    """
    Creación básica del documento pdf, en esta función se creará el pdf y se le añadirá la base de la factura: número
    de teléfono, nombre de la empresa etc
    @return:
    """
    try:
        global bill
        bill = canvas.Canvas('factura.pdf', pagesize=A4)
        text1 = 'Esperamos que vuelva pronto'
        text2 = 'CIF:00000000A '
        bill.drawImage('./resources/logohotel.png', 475, 670, width=64, height=64)
        bill.setFont('Helvetica-Bold', size=16)
        bill.drawString(250, 800, 'HOTEL LITE')
        bill.setFont('Times-Italic', size=10)
        bill.drawString(240, 785, text1)
        bill.drawString(260, 765, text2)
        bill.line(50, 660, 540, 660)
        textpie = 'Hotel Lite, CIF = 00000000A Tlfo = 986000000 mail = info@hotellite.com'
        bill.setFont('Times-Italic', size=8)
        bill.drawString(170, 20, textpie)
        bill.line(50, 30, 540, 30)
    except Exception:
        traceback.print_exc()


def factura():  # llamar a datosfactura
    """
    Función encargada de añadir todos los datos de la factura, nombre del cliente, dni, servicios etc.
    @return:
    """
    try:
        basico()
        bill.setTitle('Factura Hotel Lite')
        bill.setFont('Helvetica-Bold', size=8)
        text3 = 'Código de la reserva: ' + str(variables.codigo_reserva)
        bill.drawString(50, 735, text3)
        bill.setFont('Helvetica', size=8)
        bill.setFont('Helvetica-Bold', size=8)
        text4 = 'Fecha Factura: ' + datetime.datetime.now().strftime("%d/%m/%Y")
        bill.drawString(300, 735, text4)
        bill.setFont('Helvetica', size=8)
        bill.setFont('Helvetica-Bold', size=8)
        text5 = 'DNI CLIENTE: ' + variables.labels_facturacion[4].get_text()
        bill.drawString(50, 710, text5)
        bill.setFont('Helvetica', size=8)
        bill.setFont('Helvetica-Bold', size=8)
        text6 = 'Nº de Habitación: ' + variables.labels_facturacion[8].get_text()
        bill.drawString(300, 710, text6)
        bill.setFont('Helvetica', size=8)
        bill.setFont('Helvetica-Bold', size=8)
        text7 = 'APELLIDOS: ' + variables.labels_facturacion[5].get_text()
        bill.drawString(50, 680, text7)
        bill.setFont('Helvetica', size=9)
        bill.setFont('Helvetica-Bold', size=8)
        text8 = 'NOMBRE: ' + variables.labels_facturacion[6].get_text()
        bill.drawString(300, 680, text8)

        bill.setFont('Helvetica-Bold', size=9)
        valores_eje_x = (100, 230, 310, 420)
        eje_y = 615
        campos = ("CONCEPTO", "UNIDADES", "PRECIO/UNIDAD", "TOTAL(€)")
        concepto = str(variables.labels_facturacion[0].get_text()).splitlines()
        unidades = str(variables.labels_facturacion[1].get_text()).splitlines()
        precio = str(variables.labels_facturacion[2].get_text()).splitlines()
        total = str(variables.labels_facturacion[3].get_text()).splitlines()

        for i in range(4):
            bill.drawString(valores_eje_x[i], 630, campos[i])

        for i in range(len(concepto)):
            if concepto[i] is not '':
                bill.drawString(valores_eje_x[0], eje_y, concepto[i])
                bill.drawString(valores_eje_x[1], eje_y, unidades[i])
                bill.drawString(valores_eje_x[2], eje_y, precio[i])
                bill.drawString(valores_eje_x[3], eje_y, total[i])
            eje_y = eje_y - 7

        eje_y = 75
        bill.line(50, eje_y, 540, eje_y)

        total_sin_iva = 0
        for i in range(len(total)):
            if total[i] is not '':
                total_sin_iva = total_sin_iva + float(total[i])

        bill.setFont('Helvetica-Bold', size=10)
        bill.drawString(350, eje_y - 16, "TOTAL SIN IVA:             " + str(total_sin_iva) + '€')
        bill.drawString(350, eje_y - 26, "TOTAL CON IVA(10%):  " + str(round(total_sin_iva * 1.1, 2)) + '€')

        bill.showPage()
        bill.save()
        directorio = os.getcwd()
        os.system('/usr/bin/xdg-open "' + directorio + '/factura.pdf"')
    except Exception:
        traceback.print_exc()
