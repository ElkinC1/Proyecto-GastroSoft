from staff import staff
import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog
import json
import GastroSoft_principal

def volver1(anterior, actual):
    actual.destroy()
    anterior.deiconify()

class empleados(staff):
    def __init__(self, sesion, clave_ingreso, usuario):
        super().__init__(sesion, clave_ingreso, usuario)



    def _solicitar_clave(self):
        clave_correcta = None
        datos_claves_ingreso = GastroSoft_principal.leer_datos("claves_ingreso.json") 
        for clave_data in datos_claves_ingreso:
            if clave_data.get("Marcador") == "Clave":
                clave_correcta = clave_data.get("Clave")
                break
        
        if clave_correcta is None:
            messagebox.showerror("Error", "Clave de acción no configurada en claves_ingreso.json.")
            return False

        clave_solicitada = tk.simpledialog.askstring("Solicitar Clave", "Ingrese la clave para realizar esta acción:")
        
        if clave_solicitada == clave_correcta:
            return True
        else:
            messagebox.showerror("Error", "Clave incorrecta.")
            return False

    def editar_plato(self):
        if self._solicitar_clave():
            messagebox.showinfo("Exito", "Clave correcta.")
            mostrar1=staff("e","e","r")
            mostrar1.edicion_platos(interfaz_empleado)

    def realizar_pedido(self):
        # Esta función no necesita solicitar clave
        super().realizar_pedido()

    def cancelar_pedido(self):
        # Esta función no necesita solicitar clave
        messagebox.showinfo("Acción", "Función 'cancelar_pedido' ejecutada con éxito.")


def funcion_interfaz_de_empleado(interfaz_anterior,usuario):
        global interfaz_empleado
        interfaz_anterior.withdraw()
        interfaz_empleado=tk.Toplevel()
        interfaz_empleado.title("GastrSoft Empleado")
        interfaz_empleado.geometry("700x600")
        interfaz_empleado.configure(background='black') 
        
        label = tk.Label(interfaz_empleado, text=f"Hola {usuario}!!", font=("Times New Roman", 25), bg='black', fg='white')
        label.pack(pady=50)

        empleado_instancia = empleados("sesion_empleado", "clave_placeholder", usuario)

        boton_agregar_plato = tk.Button(interfaz_empleado, text="1. Editar platos", width=25, font=("Times New Roman", 10), command=empleado_instancia.editar_plato)
        boton_agregar_plato.pack(pady=20)

        boton_realizar_pedido = tk.Button(interfaz_empleado, text="2. Realizar pedido", width=25, font=("Times New Roman", 10), command=empleado_instancia.realizar_pedido)
        boton_realizar_pedido.pack(pady=20)

        boton_cancelar_pedido = tk.Button(interfaz_empleado, text="3. Cancelar pedido", width=25, font=("Times New Roman", 10), command=empleado_instancia.cancelar_pedido)
        boton_cancelar_pedido.pack(pady=20)
        
        boton2 = tk.Button(interfaz_empleado, text="4. Volver", width=25, font=("Times New Roman", 10), command=lambda:volver1(interfaz_anterior,interfaz_empleado))
        boton2.pack(pady=20)