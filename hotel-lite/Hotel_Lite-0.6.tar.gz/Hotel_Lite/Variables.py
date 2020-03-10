# -*- coding: utf-8 -*-
"""
Módulo variables, almacena variables que necesitamos en otros modulos

    - filacli Almacena los valores del entry de clientes

    - listlclientes Lista de clientes

    - treelclientes Treeview de clientes

    - listado List de clientes

    - ventcalendar Ventana de calendario de fecha de clientes

    - calendar Calendario de la ventana de calendario

    - filahabitacion Almacena los valores del entry de habitaciones

    - listlhabitaciones Lista de habitaciones

    - treehabitaciones Treeview de habitaciones

    - habocupada Boolean de control de habitación ocupada

    - treereservas Treeview de reservas

    - listreservas Lista de reservas

    - filareservas Almacena los valores del entry de reservas

    - comboxlist Combolist de numeros de habitaciones

    - combox Combobox de habitaciones

    - panel GtkNoebook principal

    - vent_calendarcheckin Ventana calendario checkin

    - vent_calendarcheckout Ventana calendario checkout

    - calcheckin Calendario de checkin

    - calcheckout Calendario de checkout

    - ventacerca Ventana de acerca de

    - ventbackup Ventana de backup

    - lbl_error Label con el mensaje de error generico

    - ventError Ventana de error generica

    - t Hilo de comprobación de fechas

    - varsfact Listado de variables relacionas con la factura

    - listfact Listado de datos de la factura

    - treeviewfact Treeview de la factura

    - diagdialog Dialogo de confirmacion de checkout

    - diagimp Dialogo de impresión

    - treeservicios Treeview de servicios

    - listservicios Listado de servicios

    - filaservicios Fila de variables de servicios

    - bdabierta Flag de comprobación de base de datos abierta


"""

#Almacena los valores del entry

filacli = ()

#list cliente almacena los valores a mostrar en el entryview
listlclientes = ()

#treecliente almacena el widget

treelclientes = ()

listado = ()

ventcalendar = None
calendar = None

#Habitaciones
filahabitacion = ()

listlhabitaciones = ()

treehabitaciones = ()

habocupada = None

#Reservas

treereservas = ()

listreservas = ()

filareservas = ()

comboxlist = ()

combox = None

panel = None

vent_calendarcheckin = None

vent_calendarcheckout = None

calcheckin = None

calcheckout = None

#Variables panel

ventacerca = None

ventbackup = None

#Ventana generica de error
lbl_error = None
ventError = None

#Threads
t = None

#Varsfact

varsfact = ()
listfact = ()
treeviewfact = ()


#DialogoCheckout

diagdialog = None


#DialogImportarExcel
diagimp = None

#Servicios

treeservicios = ()

listservicios = ()

filaservicios = ()


#BD abierta
bdabierta = False