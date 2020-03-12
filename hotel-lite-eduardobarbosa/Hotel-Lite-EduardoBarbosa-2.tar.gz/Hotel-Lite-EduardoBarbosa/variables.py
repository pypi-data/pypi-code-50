# coding=utf-8
"""
Variables necesarias a lo largo de la ejecución del programa.
Como pueden ser las ventanas, ventanas de dialogo, listas, labels etc.
"""

# Diferentes ventanas que serán utilizadas a lo largo del programa.
ventana_calendario = None
calendario = None
ventana_about = None
panel_notebook = None
ventana_backup = None
ventana_dialog_salir = None
ventana_precios_servicios = None

labels_informativos = ()
listado = ()

# Clientes
fila_clientes = ()
list_clientes = ()
tree_clientes = ()

# Habitaciones
fila_habitaciones = ()
list_habitaciones = ()
tree_habitaciones = ()
radiobtn_habitaciones = ()
switch_libre = None

# Reservas
fila_reservas = ()
list_reservas = ()
tree_reservas = ()
combo_habitaciones = None
numero_habitacion_reservada = None
reserva = None
list_combo_habitaciones = ()
codigo_reserva = None

# Servicios
fila_servicios = ()
list_servicios = ()
tree_servicios = ()
labels_servicios = ()
check_servicios = ()

# Facturacion
numero_noches = None
codigo_servicio = None
labels_facturacion = ()
concepto_basico = None
unidades_basico = None
precio_basico = None
total_basico = None
concepto_adicional = None
unidades_adicional = None
precio_adicional = None
total_adicional = None

# Backup
backup_path = None

# Otras
timer = None
semaforo = None
precios = ()
