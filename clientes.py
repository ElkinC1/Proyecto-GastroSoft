from datetime import datetime
import tkinter as tk
from pedido import Pedido
class Clientes:
    def __init__(self, sesion=None, nombre=None, cedula=None, direccion=None, correo=None):
        self.__sesion = sesion
        self.__nombre = nombre
        self.__cedula = cedula
        self.__direccion = direccion
        self.__correo = correo

    @property
    def sesion(self):
        return self.__sesion
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def cedula(self):
        return self.__cedula
    
    @property
    def direccion(self):
        return self.__direccion
    
    @property
    def correo(self):
        return self.__correo

    def realizar_pedido(self):
        Pedido.crear_interfaz(self._post_pedido_acciones)

    def _post_pedido_acciones(self, platos_seleccionados, numero_pedido):
        import GastroSoft_principal 

        pedidos_guardados = GastroSoft_principal.leer_datos("pedidos_guardados.json") 

        numero_pedido = len(pedidos_guardados) + 1
        nuevo_pedido_info = {
            "numero_pedido": numero_pedido,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "platos_seleccionados": platos_seleccionados,
            "total_sin_iva": sum(p["precio"] * p["cantidad"] for p in platos_seleccionados),
            "iva_porcentaje": 12
        }
        pedidos_guardados.append(nuevo_pedido_info)
        GastroSoft_principal.guardar_datos(pedidos_guardados, "pedidos_guardados.json") 

        interfaz_tipo_cliente = tk.Toplevel()
        interfaz_tipo_cliente.title("Tipo de Cliente")
        interfaz_tipo_cliente.geometry("400x300")
        interfaz_tipo_cliente.configure(background='black')

        tk.Label(interfaz_tipo_cliente, text="¿Es un cliente final o desea ingresar sus datos?",
                 font=("Times New Roman", 14), bg='black', fg='white').pack(pady=20)

        def seleccionar_cliente_final():
            from clientefinal import ClienteFinal
            interfaz_tipo_cliente.destroy()
            cliente_final_instancia = ClienteFinal()
            cliente_final_instancia.generar_factura_final(nuevo_pedido_info)

        def seleccionar_cliente_con_datos():
            from clientedatos import cdatos
            interfaz_tipo_cliente.destroy()
            cdatos_instancia = cdatos()
            cdatos_instancia.mostrar_interfaz_ingreso_datos(nuevo_pedido_info)

        tk.Button(interfaz_tipo_cliente, text="Cliente Final", width=20, command=seleccionar_cliente_final).pack(pady=10)
        tk.Button(interfaz_tipo_cliente, text="Ingresar Mis Datos", width=20, command=seleccionar_cliente_con_datos).pack(pady=10)