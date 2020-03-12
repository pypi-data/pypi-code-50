# coding=utf-8
"""
Aquí están registrados todos los handlers del la interfaz gráfica
"""
import os
import shutil
import traceback
import datetime
import webbrowser

import gi
from gi.repository import Gtk

import conexion
import funciones_clientes
import funciones_genericas
import funciones_reservas
import funciones_servicios
import funciones_habitaciones
import imprimir_clientes
import variables
import util
import big_data
import imprimir

gi.require_version('Gtk', '3.0')


class Eventos:

    ####################################################################################################################
    #                                                                                                                  #
    #                                            OTROS EVENTOS                                                         #
    #                                                                                                                  #
    ####################################################################################################################
    @staticmethod
    def salir():
        try:
            conexion.Conexion.cerrar_bd()
            funciones_genericas.cerrar_timer()
            Gtk.main_quit()
        except Exception as e:
            traceback.print_exc()

    @staticmethod
    def on_ventana_principal_destroy(widget):
        try:
            Eventos.salir()
        except Exception as e:
            traceback.print_exc()

    @staticmethod
    def on_calendario_day_selected_double_click(widget):
        try:
            anho, mes, dia = variables.calendario.get_date()
            fecha = "%s/" % dia + "%s/" % (mes + 1) + "%s" % anho
            if variables.semaforo == 1:
                variables.fila_clientes[3].set_text(fecha)
            elif variables.semaforo == 2:
                variables.fila_reservas[2].set_text(fecha)
            elif variables.semaforo == 3:
                variables.fila_reservas[3].set_text(fecha)
                funciones_reservas.calcular_noches()
            else:
                pass
            variables.ventana_calendario.hide()
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_btn_salir_clicked(widget):
        try:
            Eventos.salir()
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_btn_cancelar_clicked(widget):
        try:
            variables.ventana_dialog_salir.connect('delete-event', lambda w, e: w.hide() or True)
            variables.ventana_dialog_salir.hide()
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_btn_cerrar_about_clicked(widget):
        try:
            variables.ventana_about.connect('delete-event', lambda w, e: w.hide() or True)
            variables.ventana_about.hide()
        except Exception:
            traceback.print_exc()

    ####################################################################################################################
    #                                                                                                                  #
    #                                            EVENTOS MENU BAR                                                      #
    #                                                                                                                  #
    ####################################################################################################################

    @staticmethod
    def on_menubar_salir_activate(widget):
        try:
            variables.ventana_dialog_salir.show()
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_exportar_activate(widget):
        try:
            big_data.exportar_xls()
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_importar_activate(widget):
        try:
            big_data.importar_xls()
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_about_activate(widget):
        try:
            variables.ventana_about.show()
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_precios_activate(widget):
        try:
            variables.ventana_precios_servicios.show()
            funciones_genericas.cargar_precios_servicios()
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_clientes_pdf_activate(widget):
        try:
            funciones_clientes.cargar_clientes(variables.list_clientes)
            imprimir_clientes.exportar()
        except:
            traceback.print_exc()

    ####################################################################################################################
    #                                                                                                                  #
    #                                            EVENTOS TOOL BAR                                                      #
    #                                                                                                                  #
    ####################################################################################################################

    @staticmethod
    def on_tool_cliente_clicked(widget):
        try:
            variables.panel_notebook.set_current_page(0)
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_tool_habitaciones_clicked(widget):
        try:
            variables.panel_notebook.set_current_page(1)
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_tool_github_clicked(widget):
        try:
            webbrowser.open("https://github.com/Baaarbz/Hotel-Lite")
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_tool_reservas_clicked(widget):
        try:
            variables.panel_notebook.set_current_page(2)
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_tool_servicios_clicked(widget):
        try:
            variables.panel_notebook.set_current_page(3)
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_tool_calculadora_clicked(widget):
        try:
            os.system('/snap/bin/gnome-calculator')
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_tool_salir_clicked(widget):
        try:
            variables.ventana_dialog_salir.show()
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_tool_refresh_clicked(widget):
        try:
            util.limpiar_entries(variables.fila_reservas)
            util.limpiar_entries(variables.fila_habitaciones)
            util.limpiar_entries(variables.fila_clientes)
            variables.combo_habitaciones.set_active(-1)
            variables.labels_informativos[6].set_text('')
            variables.labels_informativos[2].set_text('')
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_tool_backup_clicked(widget):
        try:
            variables.ventana_backup.show()
            variables.backup_path = funciones_genericas.backup()
            variables.backup_path = str(os.path.abspath(variables.backup_path))
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_tool_imprimir_clicked(widget):
        try:
            imprimir.factura()
        except Exception:
            traceback.print_exc()

    ####################################################################################################################
    #                                                                                                                  #
    #                                            EVENTOS CLIENTES                                                      #
    #                                                                                                                  #
    ####################################################################################################################

    @staticmethod
    def on_btn_alta_cliente_clicked(widget):
        try:
            variables.labels_informativos[2].set_text('')
            dni = variables.fila_clientes[0].get_text()
            apellidos = variables.fila_clientes[1].get_text()
            nombre = variables.fila_clientes[2].get_text()
            fecha = variables.fila_clientes[3].get_text()
            cliente = (dni, apellidos, nombre, fecha)
            if util.validar_dni(dni):
                funciones_clientes.insertar_cliente(cliente)
                funciones_clientes.cargar_clientes(variables.list_clientes)
                util.limpiar_entries(variables.fila_clientes)
            else:
                variables.labels_informativos[0].set_text('Error en el DNI.')
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_btn_baja_cliente_clicked(widget):
        try:
            dni = variables.fila_clientes[0].get_text()
            if dni != '':
                funciones_clientes.borrar_cliente(dni)
                funciones_clientes.cargar_clientes(variables.list_clientes)
                util.limpiar_entries(variables.fila_clientes)
            else:
                print('Falta el DNI del cliente u otro error.')
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_btn_modificar_cliente_clicked(widget):
        try:
            codigo = variables.labels_informativos[1].get_text()
            dni = variables.fila_clientes[0].get_text()
            apellidos = variables.fila_clientes[1].get_text()
            nombre = variables.fila_clientes[2].get_text()
            fecha = variables.fila_clientes[3].get_text()
            cliente_actualizado = (dni, apellidos, nombre, fecha)
            if dni != '':
                funciones_clientes.actualizar_cliente(cliente_actualizado, codigo)
                funciones_clientes.cargar_clientes(variables.list_clientes)
                util.limpiar_entries(variables.fila_clientes)
            else:
                print('Falta el DNI del cliente')
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_btn_calendario_clicked(widget):
        try:
            variables.semaforo = 1
            variables.ventana_calendario.connect('delete-event', lambda w, e: w.hide() or True)
            variables.ventana_calendario.show()
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_tree_clientes_cursor_changed(widget):
        try:
            model, iter_cliente = variables.tree_clientes.get_selection().get_selected()
            # model es el modelo de la tabla de datos
            # iter es el número que identifica a la fila que marcamos
            variables.labels_informativos[0].set_text('')
            util.limpiar_entries(variables.fila_clientes)
            if iter_cliente is not None:
                dni = model.get_value(iter_cliente, 0)
                apellidos = model.get_value(iter_cliente, 1)
                nombre = model.get_value(iter_cliente, 2)
                fecha = model.get_value(iter_cliente, 3)
                if fecha is not None:
                    codigo = funciones_clientes.select_cliente(dni)
                    variables.labels_informativos[1].set_text(str(codigo[0]))
                    variables.fila_clientes[0].set_text(str(dni))
                    variables.fila_clientes[1].set_text(str(apellidos))
                    variables.fila_clientes[2].set_text(str(nombre))
                    variables.fila_clientes[3].set_text(str(fecha))
                    # Labels de la página de reservas
                    variables.labels_informativos[3].set_text(str(apellidos))
                    variables.labels_informativos[4].set_text(str(dni))
                    variables.labels_informativos[2].set_text('')
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_entry_dni_focus_out_event(self, widget):
        try:
            variables.labels_informativos[2].set_text('')
            dni = variables.fila_clientes[0].get_text()
            if util.validar_dni(dni):
                variables.labels_informativos[0].set_text('')
                pass
            else:
                variables.labels_informativos[0].set_text('Error')
        except Exception:
            traceback.print_exc()

    ####################################################################################################################
    #                                                                                                                  #
    #                                            EVENTOS HABITACIONES                                                  #
    #                                                                                                                  #
    ####################################################################################################################

    @staticmethod
    def on_btn_alta_hab_clicked(widget):
        try:
            numero_habitacion = variables.fila_habitaciones[0].get_text()
            precio = variables.fila_habitaciones[1].get_text()
            precio = precio.replace(',', '.')
            precio = float(precio)
            precio = round(precio, 2)
            if variables.radiobtn_habitaciones[0].get_active():
                tipo = 'Simple'
            elif variables.radiobtn_habitaciones[1].get_active():
                tipo = 'Doble'
            elif variables.radiobtn_habitaciones[2].get_active():
                tipo = 'Familiar'

            if variables.switch_libre.get_active():
                libre = 'SI'
            else:
                libre = 'NO'
            habitacion = (numero_habitacion, tipo, precio, libre)
            if numero_habitacion is not None:
                funciones_habitaciones.insertar_habitacion(habitacion)
                funciones_habitaciones.cargar_habitaciones(variables.list_habitaciones)
                funciones_habitaciones.lista_numero_habitaciones_combo()
                util.limpiar_entries(variables.fila_habitaciones)
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_btn_baja_hab_clicked(widget):
        try:
            numero_habitacion = variables.fila_habitaciones[0].get_text()
            if numero_habitacion != '':
                funciones_habitaciones.borrar_habitacion(numero_habitacion)
                util.limpiar_entries(variables.fila_habitaciones)
                funciones_habitaciones.cargar_habitaciones(variables.list_habitaciones)
                funciones_habitaciones.lista_numero_habitaciones_combo()
            else:
                pass
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_btn_modificar_hab_clicked(widget):
        try:
            numero_habitacion = variables.fila_habitaciones[0].get_text()
            precio = variables.fila_habitaciones[1].get_text()
            if variables.radiobtn_habitaciones[0].get_active():
                tipo = 'Simple'
            elif variables.radiobtn_habitaciones[1].get_active():
                tipo = 'Doble'
            elif variables.radiobtn_habitaciones[2].get_active():
                tipo = 'Familiar'
            if variables.switch_libre.get_active():
                libre = 'SI'
            else:
                libre = 'NO'
            habitacion = (tipo, precio, libre)
            if numero_habitacion != '':
                funciones_habitaciones.actualizar_habitacion(habitacion, numero_habitacion)
                util.limpiar_entries(variables.fila_habitaciones)
                funciones_habitaciones.cargar_habitaciones(variables.list_habitaciones)
                funciones_habitaciones.lista_numero_habitaciones_combo()
            else:
                pass
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_tree_habitaciones_cursor_changed(widget):
        try:
            model, iter_habitacion = variables.tree_habitaciones.get_selection().get_selected()
            # model es el modelo de la tabla de datos
            # iter es el número que identifica a la fila que marcamos
            util.limpiar_entries(variables.fila_habitaciones)
            if iter_habitacion is not None:
                numero_habitacion = model.get_value(iter_habitacion, 0)
                tipo = model.get_value(iter_habitacion, 1)
                precio = model.get_value(iter_habitacion, 2)
                precio = round(precio, 2)
                variables.fila_habitaciones[0].set_text(str(numero_habitacion))
                variables.fila_habitaciones[1].set_text(str(precio))
                if tipo == str('Simple'):
                    variables.radiobtn_habitaciones[0].set_active(True)
                elif tipo == str('Doble'):
                    variables.radiobtn_habitaciones[1].set_active(True)
                elif tipo == str('Familiar'):
                    variables.radiobtn_habitaciones[2].set_active(True)
                libre = model.get_value(iter_habitacion, 3)
                if libre == str('SI'):
                    variables.switch_libre.set_active(True)
                else:
                    variables.switch_libre.set_active(False)
                pass
        except Exception:
            traceback.print_exc()

    ####################################################################################################################
    #                                                                                                                  #
    #                                            EVENTOS RESERVAS                                                      #
    #                                                                                                                  #
    ####################################################################################################################

    @staticmethod
    def on_btn_checkin_clicked(widget):
        try:
            variables.semaforo = 2
            variables.ventana_calendario.connect('delete-event', lambda w, e: w.hide() or True)
            variables.ventana_calendario.show()
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_btn_checkout_clicked(widget):
        try:
            variables.semaforo = 3
            variables.ventana_calendario.connect('delete-event', lambda w, e: w.hide() or True)
            variables.ventana_calendario.show()
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_btn_refresh_reservas_clicked(widget):
        try:
            variables.combo_habitaciones.set_active(-1)
            funciones_habitaciones.lista_numero_habitaciones_combo()
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_btn_alta_reservas_clicked(widget):
        try:
            if variables.reserva == 1:
                dni = variables.labels_informativos[4].get_text()
                checkin = variables.fila_reservas[2].get_text()
                checkout = variables.fila_reservas[3].get_text()
                noches = int(variables.labels_informativos[5].get_text())
                reserva = (dni, variables.numero_habitacion_reservada, checkin, checkout, noches)
                if funciones_reservas.es_libre(variables.numero_habitacion_reservada):
                    funciones_reservas.insertar_reservas(reserva)
                    funciones_reservas.cargar_reservas(variables.list_reservas)
                    libre = ['NO']
                    funciones_habitaciones.cambiar_estado_habitacion(libre, variables.numero_habitacion_reservada)
                    funciones_habitaciones.cargar_habitaciones(variables.list_habitaciones)
                    util.limpiar_entries(variables.fila_reservas)
                    util.limpiar_entries(variables.fila_habitaciones)
                    variables.combo_habitaciones.set_active(-1)
                else:
                    variables.labels_informativos[7].set_text('La habitación no disponible')
                    print('Habitación ocupada')
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_combo_habitacion_changed(widget):
        try:
            index = variables.combo_habitaciones.get_active()
            if index is not -1:
                model = variables.combo_habitaciones.get_model()
                item = model[index]
                variables.numero_habitacion_reservada = item[0]
                if funciones_reservas.es_libre(variables.numero_habitacion_reservada):
                    variables.labels_informativos[7].set_text('')
                else:
                    variables.labels_informativos[7].set_text('La habitación no disponible')
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_btn_baja_reservas_clicked(widget):
        try:
            funciones_reservas.borrar_reservas(variables.codigo_reserva)
            util.limpiar_entries(variables.fila_reservas)
            funciones_reservas.cargar_reservas(variables.list_reservas)
            libre = ['SI']
            funciones_habitaciones.cambiar_estado_habitacion(libre, variables.numero_habitacion_reservada)
            funciones_habitaciones.cargar_habitaciones(variables.list_habitaciones)
            variables.combo_habitaciones.set_active(-1)
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_btn_modificar_reservas_clicked(widget):
        if variables.codigo_reserva is not None and variables.labels_informativos[4].get_text() is not '':
            dni = variables.labels_informativos[4].get_text()
            checkin = variables.fila_reservas[2].get_text()
            checkout = variables.fila_reservas[3].get_text()
            noches = int(variables.labels_informativos[5].get_text())
            reserva = (dni, variables.numero_habitacion_reservada, checkin, checkout, noches)
            funciones_reservas.actualizar_reservas(reserva, variables.codigo_reserva)
            funciones_reservas.cargar_reservas(variables.list_reservas)
            util.limpiar_entries(variables.fila_reservas)
            util.limpiar_entries(variables.fila_habitaciones)
            variables.combo_habitaciones.set_active(-1)

    @staticmethod
    def on_tree_reservas_cursor_changed(widget):
        try:
            model, iter_reservas = variables.tree_reservas.get_selection().get_selected()
            # model es el modelo de la tabla de datos
            # iter es el número que identifica a la fila que marcamos
            util.limpiar_entries(variables.fila_reservas)
            if iter_reservas is not None:
                variables.codigo_reserva = model.get_value(iter_reservas, 0)
                dni = model.get_value(iter_reservas, 1)
                apellidos = funciones_reservas.buscar_cliente_apellido_por_dni(str(dni))
                nombre = funciones_reservas.buscar_cliente_nombre_por_dni(str(dni))
                numero_habitacion = model.get_value(iter_reservas, 2)
                lista = funciones_habitaciones.lista_numero_habitaciones()
                m = -1
                for i, x in enumerate(lista):
                    if str(x[0]) == str(numero_habitacion):
                        m = i
                variables.combo_habitaciones.set_active(m)
                variables.labels_informativos[7].set_text('')
                checkin = model.get_value(iter_reservas, 3)
                checkout = model.get_value(iter_reservas, 4)
                numero_noches = model.get_value(iter_reservas, 5)
                variables.numero_noches = numero_noches
                variables.labels_informativos[4].set_text(str(dni))
                variables.labels_informativos[3].set_text(str(apellidos[0]))
                variables.labels_informativos[5].set_text(str(numero_noches))
                variables.fila_reservas[2].set_text(str(checkin))
                variables.fila_reservas[3].set_text(str(checkout))
                # set_text() para todas las labels que necesitan los datos de la reserva en la página de servicios y
                # facturacion
                variables.labels_servicios[0].set_text(str(variables.codigo_reserva))
                variables.labels_servicios[1].set_text(str(numero_habitacion))
                variables.labels_facturacion[4].set_text(str(dni))
                variables.labels_facturacion[5].set_text(str(apellidos[0]))
                variables.labels_facturacion[6].set_text(str(nombre[0]))
                variables.labels_facturacion[7].set_text(str(variables.codigo_reserva))
                variables.labels_facturacion[8].set_text(str(numero_habitacion))
                variables.labels_facturacion[9].set_text(str(datetime.datetime.now().strftime("%d/%m/%Y")))
                funciones_servicios.cargar_servicios_reserva(variables.list_servicios)
                util.mostrar_servicios_reserva()
        except Exception:
            traceback.print_exc()

    ####################################################################################################################
    #                                                                                                                  #
    #                                            EVENTOS BACKUP                                                        #
    #                                                                                                                  #
    ####################################################################################################################

    @staticmethod
    def on_btn_backup_ventana_clicked(widget):
        try:
            destino = variables.ventana_backup.get_filename()
            variables.labels_informativos[6].set_text(str(destino))
            if shutil.move(str(variables.backup_path), str(destino)):
                print('Copia de Seguridad creada correctamente')
            variables.ventana_backup.connect('delete-event', lambda w, e: w.hide() or True)
            variables.ventana_backup.hide()
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_btn_cerrar_backup_ventana_clicked(widget):
        try:
            os.remove(variables.backup_path)
            variables.ventana_backup.connect('delete-event', lambda w, e: w.hide() or True)
            variables.ventana_backup.hide()
        except Exception:
            traceback.print_exc()

    ####################################################################################################################
    #                                                                                                                  #
    #                                       EVENTOS PRECIOS SERVICIOS                                                  #
    #                                                                                                                  #
    ####################################################################################################################

    @staticmethod
    def precios_servicios_basicos():
        try:
            precios = funciones_genericas.lista_precios_servicios()
            concepto = ''
            unidades = ''
            precio = ''
            total = ''
            calculo = None
            if variables.numero_noches is not None:
                if variables.check_servicios[1].get_active():
                    concepto = concepto + '\nDesayuno\n'
                    unidades = unidades + '\n' + str(variables.numero_noches) + '\n'
                    precio = precio + '\n' + str(precios[1]) + '\n'
                    calculo = float(precios[1]) * int(variables.numero_noches)
                    total = total + '\n' + str(calculo) + '\n'
                if variables.check_servicios[0].get_active():
                    concepto = concepto + '\nComida\n'
                    unidades = unidades + '\n' + str(variables.numero_noches) + '\n'
                    precio = precio + '\n' + str(precios[0]) + '\n'
                    calculo = float(precios[0]) * int(variables.numero_noches)
                    total = total + '\n' + str(calculo) + '\n'
                if variables.check_servicios[2].get_active():
                    concepto = concepto + '\nParking\n'
                    unidades = unidades + '\n' + str(variables.numero_noches) + '\n'
                    precio = precio + '\n' + str(precios[2]) + '\n'
                    calculo = float(precios[2]) * int(variables.numero_noches)
                    total = total + '\n' + str(calculo) + '\n'
                # Almaceno el valor que tiene la label
                variables.concepto_basico = concepto
                variables.unidades_basico = unidades
                variables.precio_basico = precio
                variables.total_basico = total
                util.mostrar_servicios_reserva()
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_btn_aceptar_precios_clicked(widget):
        try:
            funciones_genericas.actualizar_precios_servicios()
            Eventos.precios_servicios_basicos()
            variables.ventana_precios_servicios.connect('delete-event', lambda w, e: w.hide() or True)
            variables.ventana_precios_servicios.hide()
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_btn_cancelar_precios_clicked(widget):
        try:
            variables.ventana_precios_servicios.connect('delete-event', lambda w, e: w.hide() or True)
            variables.ventana_precios_servicios.hide()
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_bnt_alta_servicios_basicos_clicked(widget):
        try:
            Eventos.precios_servicios_basicos()
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_bnt_alta_servicios_adicionales_clicked(widget):
        try:
            entry_concepto = variables.fila_servicios[0].get_text()
            entry_precio = variables.fila_servicios[1].get_text()
            servicio = (entry_concepto, variables.codigo_reserva, entry_precio)
            if variables.codigo_reserva is not None and entry_concepto is not '' and entry_precio is not '':
                # Doy de alta el servicio adicional, cargo la lista de servicios y obtengo su lista
                funciones_servicios.insertar_servicios(servicio)
                util.mostrar_servicios_reserva()
                util.limpiar_entries(variables.fila_servicios)
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_bnt_eliminar_servicio_clicked(widget):
        try:
            if variables.codigo_servicio is not None:
                funciones_servicios.borrar_servicio(variables.codigo_servicio)
                funciones_servicios.cargar_servicios_reserva(variables.list_servicios)
                util.mostrar_servicios_reserva()
                variables.codigo_servicio = None
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_tree_servicios_cursor_changed(widget):
        try:
            model, iter_servicios = variables.tree_servicios.get_selection().get_selected()
            # model es el modelo de la tabla de datos
            # iter es el número que identifica a la fila que marcamos
            if iter_servicios is not None:
                variables.codigo_servicio = model.get_value(iter_servicios, 0)
        except Exception:
            traceback.print_exc()

    @staticmethod
    def on_btn_imprimir_clicked(widget):
        try:
            imprimir.factura()
        except Exception:
            traceback.print_exc()
