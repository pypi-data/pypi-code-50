# coding=utf-8
"""
En este documento están registrados los métodos para importar y exportar un documento de excel con datos de clientes.
"""
import datetime
import traceback

import xlrd
import xlwt

import funciones_clientes
import funciones_genericas
import variables


def importar_xls():
    """
    En este método se importan todos los datos del fichero 'listadoclientes.xlsx'.
    Primero abre el documento para después recorrerlo fila a fila y almacenar los datos en la variable clientes para
    después insertar el cliente en la base de datos.
    @return:
    """
    try:
        # Abrimos el archivo xls con los cliente
        fichero = xlrd.open_workbook("listadoclientes.xlsx")
        clientes = fichero.sheet_by_index(0)
        # Contamos el número de filas que tiene de clientes para el bucle.
        fila_clientes = clientes.nrows

        for i in range(1, fila_clientes):
            dni = clientes.cell(i, 0).value
            apellidos = clientes.cell(i, 1).value
            nombre = clientes.cell(i, 2).value
            fecha = datetime.datetime(*xlrd.xldate_as_tuple(clientes.cell(i, 3).value, fichero.datemode))
            # Cambio el formato de la fecha para obtener dd-mm-yyyy
            cliente = (dni, apellidos, nombre, fecha.strftime("%d/%m/%Y"))

            # Llamo al método para insertar un cliente y actualizar la lista de clientes
            funciones_clientes.insertar_cliente(cliente)
            funciones_clientes.cargar_clientes(variables.list_clientes)
        print('Se han importado correctamente los clientes desde le Excel.')
    except Exception:
        traceback.print_exc()


def exportar_xls():
    """
    En este método se exportarán todos los clientes de la base de datos al documento de excel llamado 'Hotel Lite.xls'.
    Para ello se hará una cosulta en la que se obtenga el listado con todos los clientes y acto seguido se escribiran
    en el documento.
    @return:
    """
    try:
        # Creo los estilos que van a tener las letras en el Excel
        estilo_basico = xlwt.easyxf()
        estilo_personalizado = xlwt.easyxf('font: name DejaVu Sans, colour green, bold on')

        # Creo el fichero y su correspondiente hoja
        fichero = xlwt.Workbook()
        hoja_fichero = fichero.add_sheet('Clientes', True)
        # Creo el encabezado
        hoja_fichero.write(0, 0, 'DNI', estilo_personalizado)
        hoja_fichero.write(0, 1, 'NOMBRE', estilo_personalizado)
        hoja_fichero.write(0, 2, 'APELLIDOS', estilo_personalizado)
        hoja_fichero.write(0, 3, 'FECHA ALTA', estilo_personalizado)

        # Obtengo todos los clientes y los guardo en el Excel
        lista_clientes = funciones_genericas.consulta_listado('clientes')
        j = 1
        for cliente in lista_clientes:
            for i in range(len(cliente)):
                # cliente[0] es el código del cliente y no interesa exportarlo al Excel
                if i is not 0:
                    hoja_fichero.write(j, i - 1, cliente[i], estilo_basico)
            j += 1
        fichero.save('Hotel Lite.xls')
        print('Se ha exportado correctamente')
    except Exception:
        traceback.print_exc()
