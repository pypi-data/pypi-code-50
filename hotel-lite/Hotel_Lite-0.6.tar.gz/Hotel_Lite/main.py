# -*- coding: utf-8 -*-
"""
Clase principal
"""
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from Hotel_Lite import FuncionesHab, FuncionesCli, Eventos, Variables, Conexion, FuncionesRes

'''
El main contiene los elementos necesarios para lanzar la aplicacion asi como la declaracion de los widgets que se usaran.
Tambien los modulos que tenemos que importar
'''

class Empresa:
    def __init__(self):  # iniciamos libreria

        self.b = Gtk.Builder()
        self.b.add_from_file('ventana.glade')

        # vamos cargando los widgets a utilizar en los eventos (declaracion de widgets)
        self.toolbar = self.b.get_object('toolb')
        self.venprin = self.b.get_object('venPrincipal')
        self.entdni = self.b.get_object('EntDni')
        self.entapel = self.b.get_object('EntApel')
        self.entnome = self.b.get_object('EntNome')
        self.lblcodcli = self.b.get_object('lblCodCli')
        self.lblerrordni = self.b.get_object('lblErrordni')
        self.ventcalendar = self.b.get_object('vent_calendar')
        self.calendar = self.b.get_object('calendar')
        self.entr_fecha = self.b.get_object('entr_fecha')
        self.btn_altahabitacion = self.b.get_object('btn_AltaHabitacion')
        self.btn_btn_bajahabitacion = self.b.get_object('btn_BajaHabitacion')
        self.btn_modif_hab = self.b.get_object('btn_modif_hab')
        self.btn_salir_tool = self.b.get_object('btn_salir_tool')
        self.entr_numhab = self.b.get_object('entr_Numhab')
        self.rb_simple = self.b.get_object('rb_Simple')
        self.rb_double = self.b.get_object('rb_Double')
        self.rb_family = self.b.get_object('rb_Family')
        self.entr_camas = self.b.get_object('entr_Camas')
        self.entr_npers = self.b.get_object('entr_Npers')
        self.entr_precio = self.b.get_object('entr_precio')
        self.mainnote = self.b.get_object('mainnote')
        self.btn_cli_tool = self.b.get_object('btn_cli_tool')
        self.btn_cal_tool = self.b.get_object('btn_cal_tool')
        self.btn_reservas_tool = self.b.get_object('btn_reservas_tool')
        self.btn_camas_tool = self.b.get_object('btn_camas_tool')
        self.btn_imprimir_tool = self.b.get_object('btn_imprimir_tool')
        self.btn_service_tool = self.b.get_object('btn_service_tool')
        self.btn_limpiar_tool = self.b.get_object('btn_limpiar_tool')
        self.menu_bar_salir = self.b.get_object('on_menu_bar_salir_activate')
        self.btnSalirAcerca = self.b.get_object('on_btnSalirAcerca_clicked')
        self.vent_acerca = self.b.get_object('vent_acerca')
        self.but_backup = self.b.get_object('bk')
        self.bkw = self.b.get_object('bkw')
        self.bk_salir = self.b.get_object('bk_salir')
        self.menubar = self.b.get_object('menuBar')
        self.entr_dnires = self.b.get_object('entr_dnires')
        self.entr_apelidosres = self.b.get_object('entr_apelidosres')
        self.pik_hab_res = self.b.get_object('pik_hab_res')
        self.entr_checkin = self.b.get_object('entr_checkin')
        self.entr_checkout = self.b.get_object('entr_checkout')
        self.entr_nnoches = self.b.get_object('entr_nnoches')
        self.vent_calendarcheckin = self.b.get_object('vent_calendarcheckin')
        self.vent_calendarcheckout = self.b.get_object('vent_calendarcheckout')
        self.calendar_checkin = self.b.get_object('calendar_checkin')
        self.calendar_checkout = self.b.get_object('calendar_checkout')
        self.entr_nnoches = self.b.get_object('entr_nnoches')
        self.btn_error_aceptar = self.b.get_object('btn_error_aceptar')
        self.lbl_fact_dni = self.b.get_object('lbl_fact_dni')
        self.lbl_fact_apelidos = self.b.get_object('lbl_fact_apelidos')
        self.lbl_iva = self.b.get_object('lbl_iva')
        self.lbl_fact_cod_res = self.b.get_object('lbl_fact_cod_res')
        self.lbl_fact_cod_hab = self.b.get_object('lbl_fact_cod_hab')
        self.lbl_fact_unidades = self.b.get_object('lbl_fact_unidades')
        self.lbl_fact_p_unida = self.b.get_object('lbl_fact_p_unida')
        self.lbl_fact_total = self.b.get_object('lbl_fact_total')
        self.del_res_cancel = self.b.get_object('del_res_cancel')
        self.acep_del_res = self.b.get_object('acep_del_res')
        self.on_btn_import_1_clicked = self.b.get_object('on_btn_import_1_clicked')
        self.import_salir = self.b.get_object('import_salir')
        self.menu_bar_importar = self.b.get_object('menu_bar_importar')
        self.menu_bar_exportar = self.b.get_object('menu_bar_exportar')
        self.lbl_fact_concepto = self.b.get_object('lbl_fact_concepto')

        #Servicios
        self.lbl_num_reserva = self.b.get_object('lbl_num_reserva')
        self.rb_Desayuno = self.b.get_object('rb_Desayuno')
        self.rb_Comida = self.b.get_object('rb_Comida')
        self.rb_parking = self.b.get_object('rb_parking')
        self.entr_p_unidad = self.b.get_object('entr_p_unidad')
        self.btn_AltaServicio = self.b.get_object('btn_altaservicio')
        self.btn_BajaServicio = self.b.get_object('btn_bajaservicio')
        self.tipo_servicio = self.b.get_object('tipo_servicio')
        self.entr_precio_seradic = self.b.get_object('entr_precio_seradic')
        self.btn_AltaServicioAdicional = self.b.get_object('btn_AltaServicioAdicional')
        self.treeServicios = self.b.get_object('treeServicios')
        self.list_servicios = self.b.get_object('list_servicios')
        self.lbl_total = self.b.get_object('lbl_total')
        self.lbl_total_iva = self.b.get_object('lbl_total_iva')

        #Variables servicios
        Variables.filaservicios = self.lbl_num_reserva, self.rb_Desayuno, self.rb_Comida, self.rb_parking, self.entr_p_unidad, self.tipo_servicio, self.entr_precio_seradic
        Variables.treeservicios = self.treeServicios
        Variables.listservicios = self.list_servicios

        #Variables factura
        Variables.treeviewfact = self.b.get_object('tree_view_factura_lineas')
        Variables.listfact = self.b.get_object('list_factura')

        Variables.diagdialog = self.b.get_object('diag_dialog')
        Variables.varsfact = self.lbl_fact_dni, self.lbl_fact_apelidos, self.lbl_fact_cod_res, self.lbl_fact_cod_hab, self.lbl_total, self.lbl_total_iva, self.lbl_iva
        Variables.combox = self.pik_hab_res
        Variables.lbl_error = self.b.get_object('lbl_error')
        Variables.ventError = self.b.get_object('err_dialog')
        Variables.comboxlist = self.b.get_object('cmbboxlistres')
        Variables.listreservas = self.b.get_object('listReservas')
        Variables.treereservas = self.b.get_object('treeReservas')
        Variables.habocupada = self.b.get_object('sw_ocupado')
        Variables.filareservas = self.entr_dnires, self.entr_apelidosres, self.pik_hab_res, self.entr_checkin, self.entr_checkout, self.entr_nnoches
        Variables.calendar = self.calendar
        Variables.ventacerca = self.vent_acerca
        Variables.ventbackup = self.bkw
        Variables.ventcalendar = self.ventcalendar
        Variables.filacli = self.lblcodcli, self.entdni, self.entapel, self.entnome, self.lblerrordni, self.entr_fecha
        Variables.listlclientes = self.b.get_object('listClientes')
        Variables.treelclientes = self.b.get_object('treeclientes')
        Variables.filahabitacion = self.rb_simple, self.rb_double, self.rb_family, self.entr_numhab, self.entr_camas, self.entr_npers, self.entr_precio
        Variables.listlhabitaciones = self.b.get_object('listHabitaciones')
        Variables.listreservas = self.b.get_object("listReservas")
        Variables.treehabitaciones = self.b.get_object('treeHabitaciones')
        Variables.vent_calendarcheckin = self.vent_calendarcheckin
        Variables.vent_calendarcheckout = self.vent_calendarcheckout
        Variables.diagimp = self.b.get_object('importw')
        Variables.panel = self.mainnote
        Variables.calcheckin = self.calendar_checkin
        Variables.calcheckout = self.calendar_checkout
        # conectamos y mostramos
        set_styles(self)
        s = Gdk.Screen.get_default()
        x = s.get_width()
        y = s.get_height()
        self.venprin.resize(x,y)
        self.venprin.maximize()
        self.venprin.show()
        self.b.connect_signals(Eventos.Eventos())

        Conexion.abrirDB()
        FuncionesCli.listarcli()
        FuncionesHab.listarhab(Variables.listlhabitaciones)
        FuncionesRes.listarres()
        Conexion.cerrarbbdd()

        FuncionesHab.controlhab()

        # Estilos
        menbarstyle = self.menubar.get_style_context()
        menbarstyle.add_class('menuBar')

def set_styles (self):
    css_provider = Gtk.CssProvider()
    css_provider.load_from_path('estilos.css')
    Gtk.StyleContext().add_provider_for_screen(Gdk.Screen.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

if __name__ == '__main__':
    main = Empresa()
    Gtk.main()