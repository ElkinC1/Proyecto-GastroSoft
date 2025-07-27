import tkinter as tk
from tkinter import messagebox
import json
from clientes import Clientes 
from factura import Factura 

class cdatos(Clientes): # Heredando de Clientes
    def __init__(self, sesion=None, nombre=None, cedula=None, direccion=None, correo=None):
        super().__init__(sesion, nombre, cedula, direccion, correo)

    def mostrar_interfaz_ingreso_datos(self, pedido_info=None):
        import GastroSoft_principal # Mantener esta importación aquí si solo se usa dentro de esta función
        interfaz_datos_cliente = tk.Toplevel()
        interfaz_datos_cliente.title("Registro de Datos del Cliente")
        interfaz_datos_cliente.geometry("500x400")
        interfaz_datos_cliente.configure(background='black')

        tk.Label(interfaz_datos_cliente, text="Ingrese sus Datos:", font=("Times New Roman", 16), bg='black', fg='white').pack(pady=10)

        frame_entradas = tk.Frame(interfaz_datos_cliente, bg='black')
        frame_entradas.pack(pady=10, padx=10)

        tk.Label(frame_entradas, text="Nombre:", bg='black', fg='white').grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_nombre = tk.Entry(frame_entradas, width=40)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_entradas, text="Cédula:", bg='black', fg='white').grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_cedula = tk.Entry(frame_entradas, width=40)
        self.entry_cedula.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_entradas, text="Dirección:", bg='black', fg='white').grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_direccion = tk.Entry(frame_entradas, width=40)
        self.entry_direccion.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame_entradas, text="Correo:", bg='black', fg='white').grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.entry_correo = tk.Entry(frame_entradas, width=40)
        self.entry_correo.grid(row=3, column=1, padx=5, pady=5)

        def guardar_datos_cliente():
            nombre = self.entry_nombre.get()
            cedula = self.entry_cedula.get()
            direccion = self.entry_direccion.get()
            correo = self.entry_correo.get()

            if not all([nombre, cedula, direccion, correo]):
                messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")
                return

            try:
                cedula_int = int(cedula)
            except ValueError:
                messagebox.showerror("Cédula Inválida", "La cédula debe ser un número entero.")
                return

            datos_cliente_a_guardar = {
                "nombre": nombre,
                "cedula": cedula_int,
                "correo": correo,
                "direccion": direccion
            }

            datos_clientes_existentes = GastroSoft_principal.leer_datos("clientes.json")
            datos_clientes_existentes.append(datos_cliente_a_guardar)
            GastroSoft_principal.guardar_datos(datos_clientes_existentes, "clientes.json")

            messagebox.showinfo("Éxito", "Datos del cliente guardados correctamente.")
            
            if pedido_info:
                factura_instancia = Factura(datos_cliente_a_guardar, pedido_info.get('platos_seleccionados', []), pedido_info.get('iva_porcentaje', 0)) # Nombre de clase corregido
                factura_instancia.visualizar_factura()

        tk.Button(interfaz_datos_cliente, text="Guardar Datos", command=guardar_datos_cliente).pack(pady=20)
        tk.Button(interfaz_datos_cliente, text="Volver", command=interfaz_datos_cliente.destroy).pack(pady=5)

        interfaz_datos_cliente.mainloop()

    def agregar_nombre(self):
        pass
    def agregar_cedula(self):
        pass
    def agregar_direccion(self):
        pass
    def agregra_correo(self):
        pass