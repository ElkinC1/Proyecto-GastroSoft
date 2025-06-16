import tkinter as tk
from tkinter import messagebox
from personas import Persona
import json
from datetime import datetime
import random

class clientes(Persona):
    def __init__(self, sesion, nombre, cedula, direccion, correo):
        super().__init__(sesion)
        self.nombre=nombre
        self.cedula=cedula
        self.direccion=direccion
        self.correo=correo

    def realizar_pedido(self):
        from pedido import Pedido
        Pedido.crear_interfaz(self._post_pedido_acciones)

    def _post_pedido_acciones(self, platos_seleccionados):
        import GastroSoft_principal
        from clientedatos import cdatos
        from clientefinal import cfinal
        
        try:
            pedidos_guardados = GastroSoft_principal.leer_datos('pedidos.json')
        except FileNotFoundError:
            pedidos_guardados = []

        numero_pedido = len(pedidos_guardados) + 1
        
        nuevo_pedido_info = {
            "numero_pedido": numero_pedido,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "platos_seleccionados": platos_seleccionados,
            "total_sin_iva": sum(p["precio"] * p["cantidad"] for p in platos_seleccionados),
            "iva_porcentaje": 12
        }
        pedidos_guardados.append(nuevo_pedido_info)
        GastroSoft_principal.guardar_datos(pedidos_guardados, 'pedidos.json')

        interfaz_tipo_cliente = tk.Toplevel()
        interfaz_tipo_cliente.title("Tipo de Cliente")
        interfaz_tipo_cliente.geometry("400x300")
        interfaz_tipo_cliente.configure(background='black')

        tk.Label(interfaz_tipo_cliente, text="¿Es un cliente final o desea ingresar sus datos?", font=("Times New Roman", 14), bg='black', fg='white').pack(pady=20)

        def seleccionar_cliente_final():
            interfaz_tipo_cliente.destroy()
            cliente_final_instancia = cfinal()
            cliente_final_instancia.generar_factura_final(nuevo_pedido_info)

        def seleccionar_cliente_con_datos():
            interfaz_tipo_cliente.destroy()
            cdatos_instancia = cdatos()
            cdatos_instancia.mostrar_interfaz_ingreso_datos(nuevo_pedido_info)

        tk.Button(interfaz_tipo_cliente, text="Cliente Final", width=20, command=seleccionar_cliente_final).pack(pady=10)
        tk.Button(interfaz_tipo_cliente, text="Ingresar Mis Datos", width=20, command=seleccionar_cliente_con_datos).pack(pady=10)
        
        interfaz_tipo_cliente.mainloop()
    
    def ver_menu(self, interfaz_anterior):
        from menu import menu
        mostrar=menu("hola",1)
        mostrar.mostrar_menu(interfaz_anterior)   

    def cancelar_pedido(self):
        ventana_cancelar = tk.Toplevel()
        ventana_cancelar.title("Cancelar pedido")
        ventana_cancelar.geometry("500x300")
        import GastroSoft_principal
        pedidos = GastroSoft_principal.leer_datos('pedidos.json')

        if not pedidos:
            messagebox.showwarning("Aviso", "No hay pedidos para cancelar.")
            return

        ultimo_pedido = pedidos.pop()
        GastroSoft_principal.guardar_datos(pedidos, 'pedidos.json')

        messagebox.showinfo("Pedido Cancelado", f"Se canceló el pedido #{ultimo_pedido['numero_pedido']}")
        tk.Button()