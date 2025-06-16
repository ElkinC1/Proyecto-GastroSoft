import json
import tkinter as tk
import GastroSoft_principal
def volver1(anterior, actual):
    GastroSoft_principal.volver(anterior,actual)
class menu():
    def __init__(self, nombre_plato, precio_plato):
        self.nombre_plato=nombre_plato
        self.precio_plato=precio_plato
    def mostrar_menu(self,interfaz_anterior):
        interfaz_anterior.withdraw()
        
        
        interfaz_mostrar = tk.Toplevel()
        interfaz_mostrar.title("Mostrar menu")
        interfaz_mostrar.geometry("500x600")

        datos = GastroSoft_principal.leer_datos("platos.json")
        # Crear un cuadro de texto para mostrar los datos
        texto = tk.Text(interfaz_mostrar, wrap="word", width=60, height=30)
        texto.pack(pady=10)

        # Crear un encabezado para el menú
        texto.insert("end", f"{'Nombre del plato':<20} {'Precio del plato':<20}{'Codigo del plato':<10}\n")
        texto.insert("end", "-" * 55 + "\n")
        for plato in datos:
            texto.insert("end", f"{plato['Nombre del plato']:<20} {plato['Precio del plato']:<20.2f}{plato['Codigo del plato']:<10}\n")
        boton5 = tk.Button(interfaz_mostrar, text="3. Volver", width=25, font=("Times New Roman", 10), command=lambda:volver1(interfaz_anterior,interfaz_mostrar))
        boton5.pack(pady=20)
        # Cierra con X también vuelve
        interfaz_mostrar.protocol("WM_DELETE_WINDOW", lambda: volver1(interfaz_anterior, interfaz_mostrar))