# coding=utf-8
"""
HotelLite
=========
Proyecto para Diseño de Interfaces
El siguiente ejercicio muestra el funcionamiento de un hotel, con sus reservas, altas de clientes, altas de
habitaciones, impresión de facturas etc.
Este módulo contiene los elementos necesarios para lanzar la aplicación (módulos, librerías gráficas)
así como la declaración de los widgets que se usarán.

@author: Eduardo Barbosa Tarrío
@organization: com.github.baaarbz
"""
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import eventos
import conexion
import funciones_clientes
import funciones_genericas
import funciones_reservas
import funciones_habitaciones
import variables


class Empresa:
    def __init__(self):
        """
        Inicialización de la aplicación, donde conectamos la interfaz gráfica con el código, aplicamos estilos,
        conectamos la base de datos, cargamos todos los elementos, etc...
        """
        # Iniciamos la libreria Gtk
        self.b = Gtk.Builder()
        self.b.add_from_file('gui.glade')

        # Cargamos todas la ventanas (información, avisos, etc)
        ventana_principal = self.b.get_object('ventana_principal')
        variables.panel_notebook = self.b.get_object('notebook')
        variables.ventana_about = self.b.get_object('ventana_info')
        variables.ventana_backup = self.b.get_object('ventana_backup')
        variables.ventana_dialog_salir = self.b.get_object('ventana_aviso')
        variables.calendario = self.b.get_object('calendario')
        variables.ventana_calendario = self.b.get_object('ventana_calendario')
        variables.ventana_precios_servicios = self.b.get_object('ventana_precios')

        # Aplicamos estilos al menu bar
        menu_bar = self.b.get_object('menu_bar').get_style_context()

        # Declaración de widgets
        #       Labels
        mensaje_dni = self.b.get_object('mensaje_dni')
        codigo_cliente = self.b.get_object('codigo')
        mensaje_alta_cliente = self.b.get_object('mensaje_informativo')
        apellidos_reserva = self.b.get_object('apellidos_cliente')
        dni_reserva = self.b.get_object('dni_cliente')
        numero_noches = self.b.get_object('numero_noches')
        mensaje_reserva = self.b.get_object('mensaje_reserva')
        directorio_backup = self.b.get_object('directorio_backup')
        variables.labels_informativos = (
            mensaje_dni, codigo_cliente, mensaje_alta_cliente, apellidos_reserva, dni_reserva, numero_noches,
            directorio_backup, mensaje_reserva)

        #       Clientes
        entry_dni = self.b.get_object('entry_dni')
        entry_apellidos = self.b.get_object('entry_apellidos')
        entry_nombre = self.b.get_object('entry_nombre')
        entry_fecha = self.b.get_object('entry_fecha')
        variables.fila_clientes = (entry_dni, entry_apellidos, entry_nombre, entry_fecha)
        variables.list_clientes = self.b.get_object('list_clientes')
        variables.tree_clientes = self.b.get_object('tree_clientes')

        #       Habitaciones
        entry_numero_hab = self.b.get_object('entry_numero_hab')
        entry_precio = self.b.get_object('entry_precio_hab')
        rb_simple = self.b.get_object('rb_simple')
        rb_doble = self.b.get_object('rb_doble')
        rb_familiar = self.b.get_object('rb_familiar')
        variables.fila_habitaciones = (entry_numero_hab, entry_precio)
        variables.radiobtn_habitaciones = (rb_simple, rb_doble, rb_familiar)
        variables.list_habitaciones = self.b.get_object('list_habitaciones')
        variables.tree_habitaciones = self.b.get_object('tree_habitaciones')
        variables.switch_libre = self.b.get_object('switch_libre')

        #       Reservas
        variables.list_combo_habitaciones = self.b.get_object('list_combo_hab')
        variables.combo_habitaciones = self.b.get_object('combo_habitacion')
        variables.list_reservas = self.b.get_object('list_reservas')
        variables.tree_reservas = self.b.get_object('tree_reservas')
        entry_checkin = self.b.get_object('entry_checkin')
        entry_checkout = self.b.get_object('entry_checkout')
        variables.fila_reservas = (entry_dni, entry_apellidos, entry_checkin, entry_checkout)

        #       Servicios
        servicios_cod_reserva = self.b.get_object('servicios_codigo_reserva')
        servicios_habitacion = self.b.get_object('servicios_habitacion')
        check_desayuno = self.b.get_object('check_desayuno')
        check_comida = self.b.get_object('check_comida')
        check_parking = self.b.get_object('check_parking')
        entry_servicio = self.b.get_object('entry_tipo_servicio')
        entry_precio_servicio = self.b.get_object('entry_precio_servicio')
        variables.list_servicios = self.b.get_object('list_servicios')
        variables.tree_servicios = self.b.get_object('tree_servicios')
        variables.fila_servicios = (entry_servicio, entry_precio_servicio)
        variables.labels_servicios = (servicios_cod_reserva, servicios_habitacion)
        variables.check_servicios = (check_comida, check_desayuno, check_parking)

        #       Facturación cliente
        concepto_factura = self.b.get_object('concepto_factura')
        unidades_factura = self.b.get_object('unidades_factura')
        precio_ud_factura = self.b.get_object('precio_ud_factura')
        total_factura = self.b.get_object('total_factura')
        dni_factura = self.b.get_object('dni_factura')
        apellidos_factura = self.b.get_object('apellidos_factura')
        nombre_factura = self.b.get_object('nombre_factura')
        codigo_reserva_factura = self.b.get_object('codigo_reserva_factura')
        habitacion_factura = self.b.get_object('habitacion_factura')
        fecha_factura = self.b.get_object('fecha_factura')
        variables.labels_facturacion = (
            concepto_factura, unidades_factura, precio_ud_factura, total_factura, dni_factura, apellidos_factura,
            nombre_factura, codigo_reserva_factura, habitacion_factura, fecha_factura)

        #       Precios servicios
        entry_precio_desayuno = self.b.get_object('entry_precio_desayuno')
        entry_precio_comida = self.b.get_object('entry_precio_comida')
        entry_precio_parking = self.b.get_object('entry_precio_parking')
        variables.precios = (entry_precio_comida, entry_precio_desayuno, entry_precio_parking)

        # Conectamos los estilos
        self.set_style()
        menu_bar.add_class('menu_bar')

        # Conectamos los aplicacion de la interfaz con el código del programa
        self.b.connect_signals(eventos.Eventos())

        # Mostramos la ventana principal y maximizamos la ventana
        ventana_principal.show_all()
        ventana_principal.maximize()

        # Realizamos la conexion con la base de datos y acto seguido cargamos todos los datos
        conexion.Conexion().abrir_bd()

        funciones_clientes.cargar_clientes(variables.list_clientes)
        funciones_habitaciones.cargar_habitaciones(variables.list_habitaciones)
        funciones_habitaciones.lista_numero_habitaciones_combo()
        funciones_genericas.control_habitaciones()
        funciones_reservas.cargar_reservas(variables.list_reservas)

    @staticmethod
    def set_style():
        """
        Método para aplicar los estilos en la aplicación, estos solo están aplicados a la Menu Bar
        @return:
        """
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('./resources/estilos.css')
        Gtk.StyleContext().add_provider_for_screen(
            Gdk.Screen.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )


if __name__ == '__main__':
    main = Empresa()
    Gtk.main()
