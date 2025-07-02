import tkinter as tk
from staff import staff
import GastroSoft_principal
from tkinter import messagebox
from tkinter import ttk
def volver1(anterior, actual):
    GastroSoft_principal.volver(anterior,actual)
datos=GastroSoft_principal.leer_datos("claves_ingreso.json")

#facade fachada para las clasese que contienen las funciones que puede realizar el administrador.
class Administrador(staff):
    def __init__(self):
        self.clave=Clave()
        self.reporte=Reporte()
        self.editar_empleados=Editar_empleados()
    
    def Edicion_clave(self):
        self.clave.editar_clave()
    def Ver_reporte(self):
        self.reporte.ver_reporte()
    def Editar_empleados(self):
        self.editar_empleados.edicion_empleados()

#Cada clase contiene una funcion que puede realizar el administrador 
class Clave:
    def editar_clave(self):
        interfaz_administrador.withdraw()
        interfaz_claves=tk.Toplevel()
        interfaz_claves.title("GastroSoft Claves")
        interfaz_claves.geometry("700x600")
        for clave in datos:
                if clave["Marcador"]=="Clave":
                    texto_categoria = tk.Label(interfaz_claves, text=f"Clave actual: {clave["Clave"]}", font=("Times New Roman", 10))
                    texto_categoria.pack() 
        tk.Label(interfaz_claves, pady=20, text="Nueva clave").pack()
        nueva_clave = tk.Entry(interfaz_claves)
        nueva_clave.pack()

        def confirmar_edicion():
            for clave in datos:
                if clave["Marcador"]=="Clave":
                    try:    
                        clave_nueva = nueva_clave.get()
                    except ValueError:
                        messagebox.showerror("Error, ingreso de datos erroneo")
                        return
                    clave["Clave"]=clave_nueva
                    GastroSoft_principal.guardar_datos(datos,"claves_ingreso.json")
                    nueva_clave.delete(0, tk.END)
                    messagebox.showinfo("Éxito!", "nueva clave agregada correctamente.")
        
        boton3 = tk.Button(interfaz_claves, text="confirmar", width=25, font=("Times New Roman", 10), command=confirmar_edicion)
        boton3.pack(pady=20)
        boton2 = tk.Button(interfaz_claves, text="Volver", width=25, font=("Times New Roman", 10), command=lambda:volver1(interfaz_administrador,interfaz_claves))
        boton2.pack(pady=20)
        
        
class Reporte:
    def ver_reporte(self):
        from reporte import reporte
        mostrar2=reporte(1,"e",2,3)
        mostrar2.mostrar_reporte(interfaz_administrador)

class Editar_empleados:
    def edicion_empleados (self):
        interfaz_administrador.withdraw()
        interfaz_edicion_empleados=tk.Toplevel()
        interfaz_edicion_empleados.title("GastroSoft Edicion de empleados")
        interfaz_edicion_empleados.geometry("700x600")

        def agregar_empleados():
            interfaz_edicion_empleados.withdraw()
            interfaz_agregar_empleados=tk.Toplevel()
            interfaz_agregar_empleados.title("GastroSoft Edicion de empleados")
            interfaz_agregar_empleados.geometry("600x500")
            
            tk.Label(interfaz_agregar_empleados, pady=20, text="Usuario").pack()
            Usuario_nuevo = tk.Entry(interfaz_agregar_empleados)
            Usuario_nuevo.pack()

            tk.Label(interfaz_agregar_empleados, pady=20, text="Clave").pack()
            clave_nueva = tk.Entry(interfaz_agregar_empleados)
            clave_nueva.pack()
            # Opciones del Combobox
            opciones =["Admin","Empleado"]
            marca = ttk.Combobox(interfaz_agregar_empleados, values=opciones, state="readonly")
            marca.current(1)  # opción por defecto
            marca.pack(padx=10, pady=10) 
            def agrega_empleados():
                try:
                    usuario=Usuario_nuevo.get()
                    clave=clave_nueva.get()
                    marcador=marca.get()
                except ValueError:
                    messagebox.showerror("Error", "El precio debe ser un número válido.")
                    return

                if usuario and clave and marcador:
                    agregar_usuario={
                        "Usuario": usuario,
                        "Clave": clave,
                        "Marcador": marcador
                    }
                    datos.append(agregar_usuario)
                    GastroSoft_principal.guardar_datos(datos,"claves_ingreso.json")
                    Usuario_nuevo.delete(0, tk.END)
                    clave_nueva.delete(0, tk.END)
                    marca.delete(0, tk.END)  # Limpia las entradas para agregar otro plato
                    messagebox.showinfo("Éxito!", "Usuario agregado correctamente.")
                else:
                    messagebox.showerror("Error","Por favor complete todos los campos") 
                   
            boton1 = tk.Button(interfaz_agregar_empleados, text="Confirmar", width=25, font=("Times New Roman", 10), command=agrega_empleados)
            boton1.pack(pady=20)
            boton2 = tk.Button(interfaz_agregar_empleados, text="Cancelar", width=25, font=("Times New Roman", 10), command=lambda:volver1(interfaz_edicion_empleados,interfaz_agregar_empleados))
            boton2.pack(pady=20)
        def editar_empleados():
            interfaz_edicion_empleados.withdraw()
            interfaz_editar_empleados = tk.Toplevel()
            interfaz_editar_empleados.title("GastroSoft Edición de empleados")
            interfaz_editar_empleados.geometry("600x500")

            # Combobox de seleccióm
            seleccion = tk.StringVar()
            usuarios_visibles = [emp["Usuario"] for emp in datos if emp.get("Marcador") != "Clave"]
            Seleccion_usuario = ttk.Combobox(interfaz_editar_empleados, textvariable=seleccion, values=usuarios_visibles, state="readonly")
            Seleccion_usuario.set("Selecciona un usuario")
            Seleccion_usuario.pack(pady=10)

            # Campos de edición
            usuario = tk.StringVar()
            clave = tk.StringVar()

            tk.Label(interfaz_editar_empleados, text="Nombre:").pack()
            usuario_ingreso = tk.Entry(interfaz_editar_empleados, textvariable=usuario)
            usuario_ingreso.pack()

            tk.Label(interfaz_editar_empleados, text="Clave:").pack()
            clave_ingreso = tk.Entry(interfaz_editar_empleados, textvariable=clave)
            clave_ingreso.pack()

            # Cargar datos seleccionados
            def cargar_info():
                seleccionar = seleccion.get()
                for emp in datos:
                    if emp["Usuario"] == seleccionar:
                        usuario.set(emp["Usuario"])
                        clave.set(emp["Clave"])
                        return
                messagebox.showerror("Error", "Empleado no encontrado.")

            # Guardar cambios editados
            def guardar_cambios():
                seleccionar = seleccion.get()
                for emp in datos:
                    if emp["Usuario"] == seleccionar:
                        emp["Usuario"] = usuario.get()
                        emp["Clave"] = clave.get()
                        GastroSoft_principal.guardar_datos(datos, "claves_ingreso.json")
                        messagebox.showinfo("Éxito", "Datos actualizados correctamente.")
                        return
                messagebox.showerror("Error", "Empleado no válido.")

            # Eliminar empleado
            def eliminar_empleado():
                seleccionar = seleccion.get()
                for i, emp in enumerate(datos):
                    if emp["Usuario"] == seleccionar:
                        confirmar = messagebox.askyesno("Confirmar", f"¿Eliminar a {seleccionar}?")
                        if confirmar:
                            datos.pop(i)
                            GastroSoft_principal.guardar_datos(datos, "claves_ingreso.json")
                            messagebox.showinfo("Eliminado", "Empleado eliminado correctamente.")
                        return
                messagebox.showerror("Error", "Empleado no válido.")

            # Botones
            tk.Button(interfaz_editar_empleados, text="Cargar datos", command=cargar_info).pack(pady=5)
            tk.Button(interfaz_editar_empleados, text="Guardar cambios", command=guardar_cambios).pack(pady=5)
            tk.Button(interfaz_editar_empleados, text="Eliminar usuario", command=eliminar_empleado).pack(pady=5)
            boton2 = tk.Button(interfaz_editar_empleados, text="Cancelar", width=25, font=("Times New Roman", 10),
                            command=lambda: volver1(interfaz_edicion_empleados, interfaz_editar_empleados))
            boton2.pack(pady=20)

        boton3 = tk.Button(interfaz_edicion_empleados, text="1. Agregar un empleado", width=25, font=("Times New Roman", 10), command=agregar_empleados)
        boton3.pack(pady=20)
        boton1 = tk.Button(interfaz_edicion_empleados, text="2. Editar un empleado", width=25, font=("Times New Roman", 10), command=editar_empleados)
        boton1.pack(pady=20)
        boton2 = tk.Button(interfaz_edicion_empleados, text="Volver", width=25, font=("Times New Roman", 10), command=lambda:volver1(interfaz_administrador,interfaz_edicion_empleados))
        boton2.pack(pady=20)
        
def funcion_interfaz_admin(interfaz_anterior,nombre_administrador):
        admin=Administrador()
        mostrar1=staff("s","s","sa")
        global interfaz_administrador
        interfaz_anterior.withdraw()
        interfaz_administrador=tk.Toplevel()
        interfaz_administrador.title("GastroSoft Administrador")
        interfaz_administrador.geometry("700x600")
        y=interfaz_administrador
        
        label = tk.Label(interfaz_administrador, text=f"Hola {nombre_administrador}", font=("Times New Roman", 25), bg='black', fg='white')
        label.pack(pady=50)
        #Botones
        boton1 = tk.Button(interfaz_administrador, text="1. Mostrar menu", width=25, font=("Times New Roman", 10), command=lambda:mostrar1.ver_menu(interfaz_administrador))
        boton1.pack(pady=20)
        boton3 = tk.Button(interfaz_administrador, text="2. Claves", width=25, font=("Times New Roman", 10), command=admin.Edicion_clave)
        boton3.pack(pady=20)
        boton3 = tk.Button(interfaz_administrador, text="3. reportes", width=25, font=("Times New Roman", 10), command=admin.Ver_reporte)
        boton3.pack(pady=20)
        boton3 = tk.Button(interfaz_administrador, text="4. Menú", width=25, font=("Times New Roman", 10), command=lambda:mostrar1.edicion_platos(interfaz_administrador))
        boton3.pack(pady=20)
        boton3 = tk.Button(interfaz_administrador, text="5. Empleados", width=25, font=("Times New Roman", 10), command=admin.Editar_empleados)
        boton3.pack(pady=20)
        boton2 = tk.Button(interfaz_administrador, text="6. Volver", width=25, font=("Times New Roman", 10), command=lambda:volver1(interfaz_anterior,y))
        boton2.pack(pady=20)
        # Cierra con X también vuelve
        interfaz_administrador.protocol("WM_DELETE_WINDOW", lambda: volver1(interfaz_anterior, y))    

