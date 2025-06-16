import tkinter as tk
from tkinter import messagebox
import json
import uuid
from datetime import datetime

class Pedido:
    def __init__(self, platos):
        self.id = str(uuid.uuid4())
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.platos = platos  # lista de dicts con nombre, precio y cantidad

    def calcular_total(self):
        return sum(p["precio"] * p["cantidad"] for p in self.platos)

    def resumen(self):
        resumen = f"Pedido ID: {self.id}\nFecha: {self.fecha}\n\n"
        for p in self.platos:
            subtotal = p["precio"] * p["cantidad"]
            resumen += f"{p['nombre']} x{p['cantidad']} = ${subtotal:.2f}\n"
        resumen += f"\nTOTAL: ${self.calcular_total():.2f}"
        return resumen

    @staticmethod
    def crear_interfaz(callback_confirmacion):
        try:
            with open('platos.json', 'r') as file:
                platos = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No hay platos disponibles.")
            return

        if not platos:
            messagebox.showerror("Error", "No hay platos disponibles.")
            return

        ventana_pedido = tk.Toplevel()
        ventana_pedido.title("Realizar Pedido")
        ventana_pedido.geometry("500x600")
        ventana_pedido.configure(bg="white")

        tk.Label(ventana_pedido, text="Selecciona la cantidad de cada plato:",
                 font=("Arial", 14, "bold"), bg="white").pack(pady=10)

        entradas = []

        for plato in platos:
            frame = tk.Frame(ventana_pedido, bg="white")
            frame.pack(pady=5)

            nombre = plato["Nombre del plato"]
            precio = plato["Precio del plato"]

            tk.Label(frame, text=f"{nombre} - ${precio:.2f}", width=30,
                     anchor="w", bg="white").pack(side="left")

            cantidad = tk.Spinbox(frame, from_=0, to=10, width=5)
            cantidad.pack(side="right")
            entradas.append((plato, cantidad))

        def confirmar_pedido():
            seleccion = []
            for plato, entrada in entradas:
                cantidad = int(entrada.get())
                if cantidad > 0:
                    seleccion.append({
                        "nombre": plato["Nombre del plato"],
                        "precio": plato["Precio del plato"],
                        "cantidad": cantidad
                    })

            if not seleccion:
                messagebox.showwarning("Aviso", "No seleccionaste ningún plato.")
                return

            ventana_pedido.destroy()
            callback_confirmacion(seleccion)

        tk.Button(ventana_pedido, text="Confirmar pedido", command=confirmar_pedido,
                  bg="green", fg="white", font=("Arial", 12)).pack(pady=20)
