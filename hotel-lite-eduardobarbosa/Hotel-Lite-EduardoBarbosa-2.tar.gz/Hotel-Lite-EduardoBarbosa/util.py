# coding=utf-8
"""
En esta clase estarán definidos diferentes métodos los cuales serán utilizados a lo largo del programa, como pueden ser
métodos para limpiar las entries, comprobar dni etc.
"""
import traceback

import variables
import funciones_servicios


def validar_dni(dni):
    """
    Función encargada de validar el formato del DNI, longitud, letra/s.
    @param dni: DNI a validar
    @return: true en caso de que sea un dni valido false en caso contrario.
    """
    try:
        # letras del dni, es estandar
        letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
        # tabla letras extranjeroreemplazadas
        letras_extranjero = "XYZ"
        reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
        # números dni
        numeros = "1234567890"

        dni = dni.upper()
        if len(dni) == 9:  # el dni debe tener 9 caracteres
            dig_control = dni[8]
            dni = dni[:8]  # el número que son los 8 primeros
            if dni[0] in letras_extranjero:
                print(dni)
                dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
            return len(dni) == len([n for n in dni if n in numeros]) and letras_dni[int(dni) % 23] == dig_control
        return False
    except Exception as e:
        traceback.print_exc()
        return None


def limpiar_entries(fila):
    """
    Función encargada de limpiar todas las entries y labels de la aplicación
    @param fila: fila la cual se quiere "limpiar" (clientes, habitaciones, reservas, servicios)
    @return:
    """
    if fila == variables.fila_clientes:
        variables.labels_informativos[1].set_text('')
        variables.labels_informativos[0].set_text('')
    elif fila == variables.fila_reservas:
        variables.labels_informativos[3].set_text('')
        variables.labels_informativos[4].set_text('')
        variables.labels_informativos[5].set_text('')
        variables.labels_informativos[7].set_text('')
    for i in range(len(fila)):
        fila[i].set_text('')


def mostrar_servicios_reserva():
    """
    Función utilizada para mostrar los servicios en la previsualización de la factura
    @return:
    """
    concepto = ''
    unidades = ''
    precio = ''
    total = ''
    variables.concepto_adicional = None
    variables.unidades_adicional = None
    variables.precio_adicional = None
    variables.total_adicional = None
    servicios = funciones_servicios.cargar_servicios_reserva(variables.list_servicios)
    # Muestro todos los servicios adicionales
    for registro in servicios:
        concepto = concepto + '\n' + str(registro[1]) + '\n'
        unidades = unidades + '\n1\n'
        precio = precio + '\n' + str(registro[3]) + '\n'
        total = total + '\n' + str(registro[3]) + '\n'
        # Almaceno el valor que tiene la label
    if variables.concepto_basico is not None:
        variables.concepto_adicional = variables.concepto_basico + concepto
        variables.unidades_adicional = variables.unidades_basico + unidades
        variables.precio_adicional = variables.precio_basico + precio
        variables.total_adicional = variables.total_basico + total
    else:
        variables.concepto_adicional = concepto
        variables.unidades_adicional = unidades
        variables.precio_adicional = precio
        variables.total_adicional = total

    if variables.concepto_adicional is not None:
        # Visualizo las diferentes opciones esocogidas por el usuario
        variables.labels_facturacion[0].set_text(variables.concepto_adicional)
        variables.labels_facturacion[1].set_text(variables.unidades_adicional)
        variables.labels_facturacion[2].set_text(variables.precio_adicional)
        variables.labels_facturacion[3].set_text(variables.total_adicional)
