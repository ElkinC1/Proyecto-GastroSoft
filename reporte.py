import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime
from collections import Counter

class reporte():
    def __init__(self, cantidad_venta=0, plato_mas_vendido="N/A", ingresos_obtenidos=0, fecha_reporte=None):
        self.cantidad_venta = cantidad_venta
        self.plato_mas_vendido = plato_mas_vendido
        self.ingresos_obtenidos = ingresos_obtenidos
        self.fecha_reporte = fecha_reporte if fecha_reporte else datetime.now().strftime("%Y-%m-%d")

    def elegir_fecha(self):
        pass

    @staticmethod
    def mostrar_reporte(interfaz_anterior):
        ventana_reporte = tk.Toplevel()
        ventana_reporte.title("Reporte de Ventas")
        ventana_reporte.geometry("600x400")
        ventana_reporte.configure(background='black')

        tk.Label(ventana_reporte, text="Reporte de Ventas", font=("Times New Roman", 20, "bold"), bg='black', fg='white').pack(pady=20)

        try:
            with open('facturas_registradas.json', 'r') as f:
                facturas = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            facturas = []
            messagebox.showwarning("Aviso", "No se encontraron facturas registradas para generar el reporte.")
            
        total_ventas = len(facturas)
        ingresos_totales = sum(f.get('total_con_iva', 0) for f in facturas)
        
        platos_vendidos = Counter()
        for factura_data in facturas:
            for plato in factura_data.get('platos', []):
                platos_vendidos[plato.get('nombre', 'Desconocido')] += plato.get('cantidad', 0)
        
        plato_mas_vendido = "N/A"
        if platos_vendidos:
            plato_mas_vendido = platos_vendidos.most_common(1)[0][0]

        reporte_data = {
            "cantidad_ventas": total_ventas,
            "plato_mas_vendido": plato_mas_vendido,
            "ingresos_totales": ingresos_totales,
            "fecha_reporte": datetime.now().strftime("%Y-%m-%d")
        }

        tk.Label(ventana_reporte, text=f"Fecha del Reporte: {reporte_data['fecha_reporte']}", bg='black', fg='white').pack(anchor='w', padx=20, pady=5)
        tk.Label(ventana_reporte, text=f"Cantidad de Ventas: {reporte_data['cantidad_ventas']}", bg='black', fg='white').pack(anchor='w', padx=20, pady=5)
        tk.Label(ventana_reporte, text=f"Plato Más Vendido: {reporte_data['plato_mas_vendido']}", bg='black', fg='white').pack(anchor='w', padx=20, pady=5)
        tk.Label(ventana_reporte, text=f"Ingresos Obtenidos: ${reporte_data['ingresos_totales']:.2f}", bg='black', fg='white').pack(anchor='w', padx=20, pady=5)

        def cerrar_reporte():
            ventana_reporte.destroy()
            interfaz_anterior.deiconify()

        tk.Button(ventana_reporte, text="Cerrar", command=cerrar_reporte).pack(pady=20)
        ventana_reporte.mainloop()