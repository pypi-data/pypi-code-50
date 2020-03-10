# -*- coding: utf-8 -*-

"""Este modulo contiene funciones utilizadas en diversos puntos de la ejecucion

Este modulo contiene las siguientes funciones:
    *showError
        - Muestra un mensaje de error en un dialogo
            + :param error: Cadena de error

    *validodni
        - Valida el dni establecido
            + :param dni: DNI
            + :return: True si el dni es correcto y False si no

"""

from Hotel_Lite import Variables


def showError(error):
    Variables.lbl_error.set_text(error)
    Variables.ventError.connect('delete-event', lambda w, e: w.hide() or True)
    Variables.ventError.show()


'''
Validar DNI
'''


def validoDNI(dni):
    try:
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"  # letras del dni, es estandar
        dig_ext = "XYZ"  # tabla letras extranjero
        reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}  # letras que identifican extranjero cambiadas por nº
        numeros = "1234567890"
        dni = dni.upper()  # pasa letras a mayúsculas
        if len(dni) == 9:  # el dni debe tener 9 caracteres
            dig_control = dni[8]  # la letra
            dni = dni[:8]  # el número que son los 8 primeros
            if dni[0] in dig_ext:  # comprueba que es extranjero
                dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
            return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control

        # devuelve true si se dan las 2 condiciones y sale del modulo o sino false y sale del modulo
        return False

    except:
        print("Error en la aplicacion")
        return None


def censuraDNI(dni):
    dnicensur = "******"

    dnicensur += dni[6:]

    return dnicensur
