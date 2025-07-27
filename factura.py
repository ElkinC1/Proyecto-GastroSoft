
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import uuid

class Factura:
    def __init__(self, datos_cliente, platos_pedido, iva_porcentaje):
        self.datos_cliente = datos_cliente
        self.platos_pedido = platos_pedido
        self.iva_porcentaje = iva_porcentaje
        self.total_sin_iva = self._calcular_total_sin_iva()
        self.iva_calculado = self.total_sin_iva * (self.iva_porcentaje / 100)
        self.total_con_iva = self.total_sin_iva + self.iva_calculado
        self.fecha_factura = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.numero_factura = self._generar_numero_factura()
        self._guardar_registro_factura()

    def _generar_numero_factura(self):
        return str(uuid.uuid4())[:8]

    def _guardar_registro_factura(self):
        # Aquí podrías guardar en JSON, base de datos, etc.
        pass

    def _calcular_total_sin_iva(self):
        total = 0
        for plato in self.platos_pedido:
            try:
                total += plato.get("cantidad", 0) * plato.get("precio", 0)
            except TypeError:
                total += 0
        return total

    def visualizar_factura(self):
        ventana_factura = tk.Toplevel()
        ventana_factura.title("Factura de Compra")
        ventana_factura.geometry("600x700")
        ventana_factura.configure(background='black')

        frame_contenido = tk.Frame(ventana_factura, bg='white', padx=20, pady=20)
        frame_contenido.pack(expand=True, fill='both', padx=20, pady=20)

        tk.Label(frame_contenido, text="FACTURA DE COMPRA", font=("Times New Roman", 20, "bold"), bg='white', fg='black').pack(pady=10)
        tk.Label(frame_contenido, text=f"Número de Factura: {self.numero_factura}", font=("Times New Roman", 12), bg='white', fg='black').pack(anchor='w')
        tk.Label(frame_contenido, text=f"Fecha: {self.fecha_factura}", font=("Times New Roman", 12), bg='white', fg='black').pack(anchor='w', pady=5)

        tk.Label(frame_contenido, text="\nDatos del Cliente:", font=("Times New Roman", 14, "bold"), bg='white', fg='black').pack(anchor='w')
        tk.Label(frame_contenido, text=f"Nombre: {self.datos_cliente.get('nombre', 'N/A')}", bg='white', fg='black', anchor='w').pack(fill='x')
        tk.Label(frame_contenido, text=f"Cédula: {self.datos_cliente.get('cedula', 'N/A')}", bg='white', fg='black', anchor='w').pack(fill='x')
        tk.Label(frame_contenido, text=f"Dirección: {self.datos_cliente.get('direccion', 'N/A')}", bg='white', fg='black', anchor='w').pack(fill='x')
        tk.Label(frame_contenido, text=f"Correo: {self.datos_cliente.get('correo', 'N/A')}", bg='white', fg='black', anchor='w').pack(fill='x')

        tk.Label(frame_contenido, text="\nDetalle del Pedido:", font=("Times New Roman", 14, "bold"), bg='white', fg='black').pack(anchor='w')

        for plato in self.platos_pedido:
            nombre = plato.get('nombre', 'Desconocido')
            cantidad = plato.get('cantidad', 0)
            precio = plato.get('precio', 0)
            tk.Label(frame_contenido, text=f"- {nombre} (x{cantidad}) - ${precio:.2f} c/u", bg='white', fg='black', anchor='w').pack(fill='x')

        tk.Label(frame_contenido, text=f"\nSubtotal: ${self.total_sin_iva:.2f}", font=("Times New Roman", 12, "bold"), bg='white', fg='black').pack(anchor='e', pady=5)
        tk.Label(frame_contenido, text=f"IVA ({self.iva_porcentaje}%): ${self.iva_calculado:.2f}", font=("Times New Roman", 12, "bold"), bg='white', fg='black').pack(anchor='e')
        tk.Label(frame_contenido, text=f"Total a Pagar: ${self.total_con_iva:.2f}", font=("Times New Roman", 16, "bold"), bg='white', fg='black').pack(anchor='e', pady=10)

        def descargar_factura_txt():
            nombre_archivo = f"factura_{self.numero_factura}.txt"
            try:
                with open(nombre_archivo, 'w', encoding='utf-8') as f:
                    f.write(f"FACTURA DE COMPRA\n")
                    f.write(f"Número de Factura: {self.numero_factura}\n")
                    f.write(f"Fecha: {self.fecha_factura}\n\n")
                    f.write(f"Datos del Cliente:\n")
                    f.write(f"Nombre: {self.datos_cliente.get('nombre', 'N/A')}\n")
                    f.write(f"Cédula: {self.datos_cliente.get('cedula', 'N/A')}\n")
                    f.write(f"Dirección: {self.datos_cliente.get('direccion', 'N/A')}\n")
                    f.write(f"Correo: {self.datos_cliente.get('correo', 'N/A')}\n\n")
                    f.write(f"Detalle del Pedido:\n")
                    for plato in self.platos_pedido:
                        nombre = plato.get('nombre', 'Desconocido')
                        cantidad = plato.get('cantidad', 0)
                        precio = plato.get('precio', 0)
                        f.write(f"- {nombre} (x{cantidad}) - ${precio:.2f} c/u\n")
                    f.write(f"\nSubtotal: ${self.total_sin_iva:.2f}\n")
                    f.write(f"IVA ({self.iva_porcentaje}%): ${self.iva_calculado:.2f}\n")
                    f.write(f"Total a Pagar: ${self.total_con_iva:.2f}\n")
                messagebox.showinfo("Descarga Exitosa", f"Factura guardada como {nombre_archivo}")
            except Exception as e:
                messagebox.showerror("Error de Descarga", f"No se pudo guardar la factura: {e}")

        tk.Button(ventana_factura, text="Descargar Factura", command=descargar_factura_txt).pack(pady=10)
        tk.Button(ventana_factura, text="Cerrar", command=ventana_factura.destroy).pack(pady=5)
