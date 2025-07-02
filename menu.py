import json
import tkinter as tk
import GastroSoft_principal

def volver1(anterior, actual):
    GastroSoft_principal.volver(anterior, actual)

class menu():
    def __init__(self, nombre_plato, precio_plato):
        self.nombre_plato = nombre_plato
        self.precio_plato = precio_plato

    def mostrar_menu(self, interfaz_anterior):
        interfaz_anterior.withdraw()

        interfaz_mostrar = tk.Toplevel()
        interfaz_mostrar.title("Mostrar menú por categorías")
        interfaz_mostrar.geometry("500x600")

        datos = GastroSoft_principal.leer_datos("platos.json")

        texto = tk.Text(interfaz_mostrar, wrap="word", width=60, height=30)
        texto.pack(pady=10)

        # Agrupar platos por "Categoria del plato"
        categorias = {}
        for plato in datos:
            categoria = plato.get("Categoria del plato", "Sin categoría")
            if categoria not in categorias:
                categorias[categoria] = []
            categorias[categoria].append(plato)

        # Mostrar platos agrupados por categoría
        for categoria, platos in categorias.items():
            texto.insert("end", f"\n{'='*15} {categoria.upper()} {'='*15}\n")
            texto.insert("end", f"{'Nombre del plato':<25} {'Precio':<10} {'Código':<10}\n")
            texto.insert("end", "-" * 55 + "\n")
            for plato in platos:
                texto.insert("end", f"{plato['Nombre del plato']:<25} {plato['Precio del plato']:<10.2f} {plato['Codigo del plato']:<10}\n")

        boton5 = tk.Button(interfaz_mostrar, text="3. Volver", width=25, font=("Times New Roman", 10), command=lambda: volver1(interfaz_anterior, interfaz_mostrar))
        boton5.pack(pady=20)

        interfaz_mostrar.protocol("WM_DELETE_WINDOW", lambda: volver1(interfaz_anterior, interfaz_mostrar))
