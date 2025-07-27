

import tkinter as tk
from tkinter import messagebox
from orden_pago import OrdenPago

class Pedido:
    def __init__(self, platos):
        self.platos = platos

    def calcular_total(self):
        return sum(p["precio"] * p["cantidad"] for p in self.platos)

    def resumen(self):
        resumen = "\n".join(
            f"{p['nombre']} x{p['cantidad']} = ${p['precio'] * p['cantidad']:.2f}"
            for p in self.platos
        )
        total = self.calcular_total()
        return f"{resumen}\n\nTOTAL: ${total:.2f}"

    @staticmethod
    def crear_interfaz(callback_confirmacion):
        platos = [
            {"Nombre del plato": "pato al horno", "Precio del plato": 32.0, "Codigo del plato": 1, "Categoria del plato": "Almuerzo"},
            {"Nombre del plato": "pollo al horno", "Precio del plato": 10.0, "Codigo del plato": 2, "Categoria del plato": "Almuerzo"},
            {"Nombre del plato": "guatita", "Precio del plato": 3.25, "Codigo del plato": 3, "Categoria del plato": "Almuerzo"},
            {"Nombre del plato": "Pollo en salsa de champiñones", "Precio del plato": 3.0, "Codigo del plato": 4, "Categoria del plato": "Almuerzo"},
            {"Nombre del plato": "Jugo de limon", "Precio del plato": 0.5, "Codigo del plato": 5, "Categoria del plato": "Bebidas"},
            {"Nombre del plato": "Bolon", "Precio del plato": 1.5, "Codigo del plato": 6, "Categoria del plato": "Desayunos"},
            {"Nombre del plato": "Fresas con crema", "Precio del plato": 1.5, "Codigo del plato": 48, "Categoria del plato": "Postres"}
        ]

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
            comprobante = OrdenPago(seleccion, callback_confirmacion)
            comprobante.generar()

        tk.Button(ventana_pedido, text="Confirmar orden", command=confirmar_pedido,
                  bg="green", fg="white", font=("Arial", 12)).pack(pady=20)
        ventana_pedido.mainloop()
