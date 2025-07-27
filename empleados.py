from staff import staff
import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog
import json
import GastroSoft_principal

def volver1(anterior, actual):
    GastroSoft_principal.volver(anterior, actual)

class empleados(staff):
    def __init__(self, sesion, clave_ingreso, usuario):
        super().__init__(sesion, clave_ingreso, usuario)

    def emitir_factura_por_codigo(self):
        import tkinter.simpledialog as simpledialog
        codigo = simpledialog.askinteger("Buscar Pedido", "Ingrese el código de pedido:")
        if codigo is None:
            return
        pedidos_guardados = GastroSoft_principal.leer_datos("pedidos_guardados.json")
        pedido_encontrado = next((p for p in pedidos_guardados if p["numero_pedido"] == codigo), None)
        if pedido_encontrado is None:
            messagebox.showerror("Error", "Código de pedido no encontrado.")
            return
        from clientefinal import ClienteFinal
        cliente_final_instancia = ClienteFinal()
        cliente_final_instancia.generar_factura_final(pedido_encontrado)


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
            objeto_staff=staff("a","a","a")
            objeto_staff.edicion_platos(interfaz_empleado)

    def realizar_pedido(self):
        # Esta función no necesita solicitar clave
        super().realizar_pedido()
    
    def mostrar_menu(self):
        objeto_staff=staff("a","a","a")
        objeto_staff.ver_menu(interfaz_empleado)

def funcion_interfaz_de_empleado(interfaz_anterior, usuario):
    global interfaz_empleado
    interfaz_anterior.withdraw()
    interfaz_empleado = tk.Toplevel()
    interfaz_empleado.title("GastroSoft Empleado")
    interfaz_empleado.geometry("700x600")
    interfaz_empleado.configure(background='black') 
    
    label = tk.Label(interfaz_empleado, text=f"Hola {usuario}!!", font=("Times New Roman", 25), bg='black', fg='white')
    label.pack(pady=50)
    
    empleado_instancia = empleados("sesion_empleado", "clave_placeholder", usuario)

    boton_agregar_plato = tk.Button(interfaz_empleado, text="1. Editar platos", width=25, font=("Times New Roman", 10), command=empleado_instancia.editar_plato)
    boton_agregar_plato.pack(pady=20)

    boton_realizar_pedido = tk.Button(interfaz_empleado, text="2. Realizar pedido", width=25, font=("Times New Roman", 10), command=empleado_instancia.realizar_pedido)
    boton_realizar_pedido.pack(pady=20)

    boton_menu = tk.Button(interfaz_empleado, text="3. Ver menú", width=25, font=("Times New Roman", 10), command=empleado_instancia.mostrar_menu)
    boton_menu.pack(pady=20)

    # Nuevo botón para emitir factura por código
    boton_emitir_factura = tk.Button(interfaz_empleado, text="4. Emitir factura por código", width=25, font=("Times New Roman", 10), command=empleado_instancia.emitir_factura_por_codigo)
    boton_emitir_factura.pack(pady=20)
    
    boton_volver = tk.Button(interfaz_empleado, text="5. Volver", width=25, font=("Times New Roman", 10), command=lambda: volver1(interfaz_anterior, interfaz_empleado))
    boton_volver.pack(pady=20)
