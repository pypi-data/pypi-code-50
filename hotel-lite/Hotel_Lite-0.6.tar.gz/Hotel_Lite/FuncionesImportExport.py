# -*- coding: utf-8 -*-

"""Modulo encargado de la importacion/exportacion de datos

Este modulo contiene las siguientes funciones:
    *importar
        - Importa un fichero excel a la base de datos
            + :param file: Archivo excel
    *exportar
        - Exporta los datos de clientes a un fichero excel

"""

from Hotel_Lite import FuncionesCli, Conexion
import xlrd, xlwt
from datetime import datetime


def importar(file):
    doc = xlrd.open_workbook(file)
    clientes = doc.sheet_by_index(0)

    for i in range(1, clientes.nrows):
        row = clientes.row_values(i)

        row[3] = (xlrd.xldate.xldate_as_datetime(row[3], doc.datemode)).strftime("%d/%m/%Y")

        Conexion.abrirDB()

        try:
            Conexion.cur.execute("insert into Clientes (dni,apel,nome,data) values (?,?,?,?)", row)
        except:
            Conexion.cur.execute("delete from Clientes where dni=?", (row[0],))
            Conexion.cur.execute("insert into Clientes (dni,apel,nome,data) values (?,?,?,?)", row)

        Conexion.conex.commit()

        FuncionesCli.listarcli()

        Conexion.cerrarbbdd()


def exportar():
    fecha = datetime.now().strftime("%d-%m-%Y")

    wbook = xlwt.Workbook()

    ws = wbook.add_sheet('Clientes', cell_overwrite_ok=True)
    ws.write(0, 0, 'DNI')
    ws.write(0, 1, 'Apellidos')
    ws.write(0, 2, 'Nombre')
    ws.write(0, 3, 'Fecha Ingreso')

    listcli = FuncionesCli.listado()

    for i in range(len(listcli)):
        for j in range(1, len(listcli[i])):
            ws.write(i + 1, j - 1, listcli[i][j])

    wbook.save(fecha + "_export.xls")
