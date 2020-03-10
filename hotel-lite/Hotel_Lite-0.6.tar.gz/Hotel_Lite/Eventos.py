# -*- coding: utf-8 -*-
"""Este modulo contiene las funciones que responden a los diferentes eventos generados durante la ejecucion.

Este modulo contiene las siguientes funciones:
    *salir
        -Cierra la ventana principal

    *on_venPrincipal_destroy
        - Cierra la ventana principal ante un evento destroy

    *on_btn_alta_clicked
        - Responde al click del boton de alta de cliente

    *on_btn_baja_clicked
        - Responde al click del boton de baja de cliente

    *on_treeclientes_cursor_changed
        - Responde a la seleccion de una entrada en la lista de clientes

    *on_btn_modif_cli_clicked
        - Responde al click del boton de modificar cliente

    *on_btn_fecha_clicked
        - Responde al click del boton de calendario en el formulario de cliente

    *on_calendar_day_selected_double_click
        - Responde al doble click en el calendario del formulario de cliente

    *on_btn_AltaHabitacion_clicked
        - Responde al click en el boton alta de habitacion

    *on_btn_BajaHabitacion_clicked
        - Responde al click del boton baja de habitacion

    *on_treeHabitaciones_cursor_changed
        - Responde a la seleccion de una entrada en el treeview de habitaciones

    *on_btn_modif_hab_clicked
        - Responde al click en el boton de modificar habitacion

    *on_btn_salir_tool_clicked
        - Responde al click en el boton salir de la toolbar

    *on_btn_cli_tool_clicked
        - Responde al click en el boton cliente de la toolbar

    *on_btn_reservas_tool_clicked
        - Responde al click en el boton reservas de la toolbar

    *on_btn_camas_tool_clicked
        - Responde al click en el boton habitaciones de la toolbar

    *on_btn_service_tool_clicked
        - Responde al click en el boton servicio de la toolbar

    *on_btn_cal_tool_clicked
        - Responde al click en el boton calculadora de la toolbar

    *on_btn_limpiar_tool_clicked
        - Responde al click en el boton limpiar entrada de la toolbar

    *on_menu_bar_salir_activate
        - Responde al click en el boton salir del menu

    *on_btn_menu_acerca_activate
        - Responde al click en el boton acerca de del menu

    *on_bk_activate
        - Responde al click en el boton de copia de seguridad del menu

    *on_bk_salir_clicked
        - Responde al click en el boton de salir del dialogo de copia de seguridad

    *on_btnSalirAcerca_clicked
        - Responde al click en el boton de salir del dialogo de acerca de

    *on_btn_do_backup_clicked
        - Responde al click en el boton de hacer copia de seguridad del dialogo de copia de seguridad

    *on_mainnote_switch_page
        - Responde al cambio de formulario del notebook principal

    *on_entr_dnires_changed
        - Responde al cambio del texto de dni del formulario de clientes

    *on_btn_fechckin_clicked
        - Responde al click en el boton cambio de fecha de check-in

    *on_btn_fechcheckout_clicked
        - Responde al click en el boton cambio de fecha de check-out

    *on_calendar_checkin_day_selected_double_click
        - Responde al doble click en el calendario de check-in

    *on_calendar_checkout_day_selected_double_click
        - Responde al doble click en el calendario de check-out

    *on_btn_AltaReserva_clicked
        - Responde al click en el boton alta de reserva

    *on_btn_BajaReserva_clicked
        - Responde al click en el boton baja de reserva

    *on_treeReservas_cursor_changed
        - Responde a la seleccion en una entrada en el treeview de reservas

    *on_btn_modif_res_clicked
        - Responde al click en el boton modificacion de reserva

    *on_btn_error_aceptar_clicked
        - Responde al click en el boton aceptar del dialogo de error

    *on_btn_imprimir_fact_clicked
        - Responde al click en el boton de imprimir factura

    *on_acep_del_res_clicked
        - Responde al click en el boton de aceptar en el dialogo de confirmacion de check-out

    *on_del_res_cancel_clicked
        - Responde al click en el boton de cancelar en el dialogo de confirmacion de check-out

    *on_menu_bar_importar_activate
        - Responde al click en el boton de importar en el menu

    *on_btn_import_1_clicked
        - Responde al click en el boton importar del dialogo de importación

    *on_import_salir_clicked
        - Responde al click en el boton salir del dialogo de importación.

    *on_menu_bar_exportar_activate
        - Responde al click en el boton de importar de la barra de menu

    *on_btn_altaservicio_clicked
        - Responde al click del boton de alta de servicio

    *on_btn_bajaservicio_clicked
        - Responde al click del boton baja de servicio

    *on_treeServicios_cursor_changed
        - Responde al click en una entrada del treeview de servicios

"""

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from Hotel_Lite import FuncionesCompresion, FuncionesServicios, FuncionesHab, FuncionesCli, FuncionesImportExport, \
    Conexion, FuncionesIm, FuncionesRes
from Hotel_Lite.FuncionesIm import *


class Eventos:

    '''Cierre de la ventana principal.

    '''

    def salir(self):
        Gtk.main_quit()

    # Eventos generales

    '''
    Cierre de la ventana principal
    '''

    def on_venPrincipal_destroy(self, widget):
        self.salir()

    '''
    Alta de cliente
    '''

    def on_btn_alta_clicked(self, widget):
        Conexion.abrirDB()
        FuncionesCli.altacli()
        Conexion.cerrarbbdd()

    '''
    Baja de cliente
    '''

    def on_btn_baja_clicked(self, widget):
        Conexion.abrirDB()
        FuncionesCli.bajacli()
        Conexion.cerrarbbdd()

    '''
    Seleccion de cliente en treeview
    '''

    def on_treeclientes_cursor_changed(self, widget):
        Conexion.abrirDB()
        FuncionesCli.mostrarcli()
        Conexion.cerrarbbdd()

    '''
    Modificacion de cliente
    '''

    def on_btn_modif_cli_clicked(self, widget):
        Conexion.abrirDB()
        FuncionesCli.modificarcliente()
        Conexion.cerrarbbdd()

    '''
    Fecha cliente
    '''

    def on_btn_fecha_clicked(self, widget):
        try:
            Variables.ventcalendar.connect('delete-event', lambda w, e: w.hide() or True)
            Variables.ventcalendar.show()
        except:
            FuncionesGenericas.showError("Error al abrir calendario")

    def on_calendar_day_selected_double_click(self, widget):
        try:
            agno, mes, dia = Variables.calendar.get_date()
            fecha = '%02d/' % dia + "%02d/" % (mes + 1) + "%s" % agno
            Variables.filacli[5].set_text(fecha)
            Variables.ventcalendar.hide()
        except:
            FuncionesGenericas.showError("Error en seleccionar fecha")

    '''
    Alta habitacion
    '''

    def on_btn_AltaHabitacion_clicked(self, widget):

        try:

            tipohab = ""
            if Variables.filahabitacion[0].get_active():
                tipohab = "Simple"
            elif Variables.filahabitacion[1].get_active():
                tipohab = "Double"
            elif Variables.filahabitacion[2].get_active():
                tipohab = "Family"

            if Variables.habocupada.get_active():
                ocu = 'SI'
            else:
                ocu = 'NO'

            nab = int(Variables.filahabitacion[3].get_text())
            ncamas = int(Variables.filahabitacion[4].get_text())
            npers = int(Variables.filahabitacion[5].get_text())
            pnoche = float(Variables.filahabitacion[6].get_text())
            registro = (nab, tipohab, ncamas, npers, pnoche, ocu)

            if nab != "" and ncamas != "" and npers != "" and pnoche != "":
                Conexion.abrirDB()
                FuncionesHab.listarhab(Variables.listlhabitaciones)
                FuncionesHab.insertarhab(registro)
                Variables.listlhabitaciones.append(registro)
                Variables.treehabitaciones.show()
                FuncionesHab.limpiarEnt(Variables.filahabitacion)
                Conexion.cerrarbbdd()

        except:
            FuncionesGenericas.showError("Error en alta")

    def on_btn_BajaHabitacion_clicked(self, widget):
        try:

            nab = Variables.filahabitacion[3].get_text()
            if nab != "":
                FuncionesHab.bajanab(nab)

        except:
            FuncionesGenericas.showError("Error en baja")

    def on_treeHabitaciones_cursor_changed(self, widget):
        FuncionesHab.cargarenthab()

    def on_btn_modif_hab_clicked(self, widget):
        try:
            Conexion.abrirDB()
            nab = int(Variables.filahabitacion[3].get_text())
            ncamas = int(Variables.filahabitacion[4].get_text())
            npers = int(Variables.filahabitacion[5].get_text())
            pnoche = float(Variables.filahabitacion[6].get_text())

            tipohab = ""
            if Variables.filahabitacion[0].get_active():
                tipohab = "Simple"
            elif Variables.filahabitacion[1].get_active():
                tipohab = "Double"
            elif Variables.filahabitacion[2].get_active():
                tipohab = "Family"

            registro = (nab, tipohab, ncamas, npers, pnoche)

            if nab is not None:
                FuncionesHab.modifhab(registro)
                FuncionesHab.listarhab(Variables.listlhabitaciones)
                FuncionesHab.limpiarEnt(Variables.filahabitacion)
            else:
                FuncionesGenericas.showError("Faltan datos")

        except Exception as e:
            FuncionesGenericas.showError("Error en modificacion")

    # Declaracion de los botones del toolbar

    def on_btn_salir_tool_clicked(self, widget):
        self.salir()

    def on_btn_cli_tool_clicked(self, widget):
        try:
            panelactual = Variables.panel.get_current_page()
            if panelactual != 0:
                Variables.panel.set_current_page(0)

        except:
            FuncionesGenericas.showError("Error en btn_cli")

    def on_btn_reservas_tool_clicked(self, widget):
        try:
            panelactual = Variables.panel.get_current_page()
            if panelactual != 1:
                Variables.panel.set_current_page(1)

        except:
            FuncionesGenericas.showError("Error en btn_cli")

    def on_btn_camas_tool_clicked(self, widget):
        try:
            panelactual = Variables.panel.get_current_page()
            if panelactual != 2:
                Variables.panel.set_current_page(2)

        except:
            FuncionesGenericas.showError("Error en btn_cli")

    def on_btn_service_tool_clicked(self, widget):
        try:
            panelactual = Variables.panel.get_current_page()
            if panelactual != 3:
                Variables.panel.set_current_page(3)

        except:
            FuncionesGenericas.showError("Error en btn_servicio")

    def on_btn_cal_tool_clicked(self, widget):
        os.system("gnome-calculator")

    def on_btn_limpiar_tool_clicked(self, widget):
        FuncionesHab.limpiarEnt(Variables.filahabitacion)
        FuncionesCli.limpiarEnt()
        FuncionesRes.limpiarEnt()

        Variables.filaservicios[0].set_text("")
        FuncionesServicios.limpiarent()

    # Eventos de la barra de menu

    def on_menu_bar_salir_activate(self, widget):
        self.salir()

    def on_btn_menu_acerca_activate(self, widget):
        Variables.ventacerca.connect('delete-event', lambda w, e: w.hide() or True)
        Variables.ventacerca.show()

    def on_bk_activate(self, widget):
        Variables.ventbackup.connect('delete-event', lambda w, e: w.hide() or True)
        Variables.ventbackup.show()

    def on_bk_salir_clicked(self, widget):
        Variables.ventbackup.connect('delete-event', lambda w, e: w.hide() or True)
        Variables.ventbackup.hide()

    def on_btnSalirAcerca_clicked(self, widget):
        Variables.ventacerca.connect('delete-event', lambda w, e: w.hide() or True)
        Variables.ventacerca.hide()

    def on_btn_do_backup_clicked(self, widget):
        FuncionesCompresion.comprimir(Variables.ventbackup.get_filename())
        Variables.ventbackup.connect('delete-event', lambda w, e: w.hide() or True)
        Variables.ventbackup.hide()

    def on_mainnote_switch_page(self, widget, DATA=None, PAGE=None):
        Conexion.abrirDB()
        FuncionesRes.cargarHabsPik()
        Conexion.cerrarbbdd()

    def on_entr_dnires_changed(self, widget):
        FuncionesRes.setapeldni(Variables.filareservas[0].get_text())

    def on_btn_fechckin_clicked(self, widget):
        Variables.vent_calendarcheckin.connect('delete-event', lambda w, e: w.hide() or True)
        Variables.vent_calendarcheckin.show()

    def on_btn_fechcheckout_clicked(self, widget):
        Variables.vent_calendarcheckout.connect('delete-event', lambda w, e: w.hide() or True)
        Variables.vent_calendarcheckout.show()

    def on_calendar_checkin_day_selected_double_click(self, widget):
        agno, mes, dia = Variables.calcheckin.get_date()
        fecha = '%02d/' % dia + "%02d/" % (mes + 1) + "%s" % agno
        Variables.filareservas[3].set_text(fecha)
        Variables.vent_calendarcheckin.hide()

        if Variables.filareservas[4].get_text() != "":
            d_fchkout = datetime.strptime(Variables.filareservas[4].get_text(), "%d/%m/%Y")
            d = d_fchkout - datetime(agno, mes + 1, dia)
            dias = d.days
            if dias > 0:
                Variables.filareservas[5].set_text(str(dias))

    def on_btn_imprimir_tool_clicked(self, widget):
        os.system("system-config-printer")

    def on_calendar_checkout_day_selected_double_click(self, widget):
        agno, mes, dia = Variables.calcheckout.get_date()
        fecha = '%02d/' % dia + "%02d/" % (mes + 1) + "%s" % agno
        Variables.filareservas[4].set_text(fecha)
        Variables.vent_calendarcheckout.hide()

        if Variables.filareservas[3].get_text() != "":

            d_fchkin = datetime.strptime(Variables.filareservas[3].get_text(), "%d/%m/%Y")
            d = datetime(agno, mes + 1, dia) - d_fchkin

            dias = d.days
            if dias > 0:
                Variables.filareservas[5].set_text(str(dias))

    def on_btn_AltaReserva_clicked(self, widget):
        Conexion.abrirDB()
        FuncionesRes.altareserva()
        Conexion.cerrarbbdd()

    def on_btn_BajaReserva_clicked(self, widget):
        Conexion.abrirDB()
        FuncionesRes.bajareserva()
        Conexion.cerrarbbdd()

    def on_treeReservas_cursor_changed(self, widget):
        Conexion.abrirDB()
        FuncionesRes.cargarres()
        Conexion.cerrarbbdd()

    def on_btn_modif_res_clicked(self, widget):
        Conexion.abrirDB()
        FuncionesRes.modifres(Variables.filareservas)
        Conexion.cerrarbbdd()

    # Ventana error
    def on_btn_error_aceptar_clicked(self, widget):
        Variables.ventError.hide()

    # Facturacion

    def on_btn_imprimir_fact_clicked(self, widget):
        factura()

    # Checkout
    def on_acep_del_res_clicked(self, widget):
        dni = Variables.filareservas[0].get_text()

        index = Variables.filareservas[2].get_active()
        model = Variables.filareservas[2].get_model()

        checkin = Variables.filareservas[3].get_text()

        it = model[index]
        Conexion.abrirDB()
        FuncionesRes.bajares(dni, it[0], checkin, True)
        Conexion.cerrarbbdd()

        Variables.diagdialog.connect('delete-event', lambda w, e: w.hide() or True)
        Variables.diagdialog.hide()

    def on_del_res_cancel_clicked(self, widget):
        Variables.diagdialog.connect('delete-event', lambda w, e: w.hide() or True)
        Variables.diagdialog.hide()

    # Importar

    def on_menu_bar_importar_activate(self, widget):
        Variables.diagimp.connect('delete-event', lambda w, e: w.hide() or True)
        Variables.diagimp.show()

    def on_btn_import_1_clicked(self, widget):
        FuncionesImportExport.importar(Variables.diagimp.get_filename())
        Variables.diagimp.connect('delete-event', lambda w, e: w.hide() or True)
        Variables.diagimp.hide()

    def on_import_salir_clicked(self, widget):

        Variables.diagimp.connect('delete-event', lambda w, e: w.hide() or True)
        Variables.diagimp.hide()

    def on_menu_bar_exportar_activate(self, widget):
        Conexion.abrirDB()
        FuncionesImportExport.exportar()
        Conexion.cerrarbbdd()

    def on_menu_list_clientes_activate(self, widget):
        FuncionesIm.listadoCli()

    # Servicios

    def on_btn_altaservicio_clicked(self, widget):
        Conexion.abrirDB()
        FuncionesServicios.altaServicioOrd()
        Conexion.cerrarbbdd()

    def on_btn_bajaservicio_clicked(self, widget):
        Conexion.abrirDB()
        FuncionesServicios.bajaserv()
        Conexion.cerrarbbdd()

    def on_treeServicios_cursor_changed(self, widget):
        FuncionesServicios.entrserv()