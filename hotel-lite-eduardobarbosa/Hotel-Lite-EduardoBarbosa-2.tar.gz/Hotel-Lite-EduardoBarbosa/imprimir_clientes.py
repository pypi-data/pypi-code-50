import os
import traceback
import datetime

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

import variables


def cabecera():
    try:
        global clientes
        clientes = canvas.Canvas('clientes.pdf', pagesize=A4)
        clientes.setTitle("Clientes registrados")
        clientes.setFont('Helvetica-Bold', size=16)
        clientes.drawString(250, 800, 'HOTEL LITE')
        clientes.setFont('Times-Italic', size=10)
        clientes.drawString(240, 785, 'Clientes registrados en Hotel Lite.')
        clientes.drawString(260, 765, 'Fecha: ' + datetime.datetime.now().strftime("%d/%m/%Y"))
        clientes.line(50, 740, 540, 740)
        clientes.setFont('Times-Italic', size=8)
        clientes.drawString(170, 20, 'Hotel Lite, CIF = 00000000A Tlfo = 986000000 mail = info@hotellite.com')
        clientes.line(50, 30, 540, 30)
    except Exception:
        traceback.print_exc()


def exportar():
    try:
        cabecera()
        clientes.setFont('Helvetica-Bold', size=11)
        valores_eje_x = (100, 220, 360, 500)
        eje_y = 705
        campos = ("DNI", "NOMBRE", "APELLIDOS", "FECHA ALTA")

        for i in range(4):
            clientes.drawCentredString(valores_eje_x[i], 720, campos[i])

        count = 0

        clientes.setFont('Helvetica', size=9)
        for i in variables.listado:
            clientes.drawCentredString(valores_eje_x[0], eje_y, i[1])
            clientes.drawCentredString(valores_eje_x[1], eje_y, i[3])
            clientes.drawCentredString(valores_eje_x[2], eje_y, i[2])
            clientes.drawCentredString(valores_eje_x[3], eje_y, i[4])
            eje_y = eje_y - 15
            count += 1
            if count % 45 is 0:
                clientes.showPage()
                clientes.setFont('Helvetica-Bold', size=16)
                clientes.drawString(250, 800, 'HOTEL LITE')
                clientes.setFont('Times-Italic', size=10)
                clientes.drawString(240, 785, 'Clientes registrados en Hotel Lite.')
                clientes.drawString(260, 765, 'Fecha: ' + datetime.datetime.now().strftime("%d/%m/%Y"))
                clientes.line(50, 740, 540, 740)
                clientes.setFont('Times-Italic', size=8)
                clientes.drawString(170, 20, 'Hotel Lite, CIF = 00000000A Tlfo = 986000000 mail = info@hotellite.com')
                clientes.line(50, 30, 540, 30)
                clientes.setFont('Helvetica-Bold', size=11)
                valores_eje_x = (100, 220, 360, 500)
                eje_y = 705
                campos = ("DNI", "NOMBRE", "APELLIDOS", "FECHA ALTA")

                for j in range(4):
                    clientes.drawCentredString(valores_eje_x[j], 720, campos[j])
                clientes.setFont('Helvetica', size=9)
                count = 0

        clientes.showPage()
        clientes.save()
        directorio = os.getcwd()
        os.system('/usr/bin/xdg-open "' + directorio + '/clientes.pdf"')
    except Exception:
        traceback.print_exc()
