import tkinter as tk
from staff import staff
import GastroSoft_principal
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
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
        objeto_staff=staff("a","a","a")
        global interfaz_administrador
        interfaz_anterior.withdraw()
        interfaz_administrador=tk.Toplevel()
        interfaz_administrador.title("GastroSoft Administrador")
        interfaz_administrador.geometry("900x600")
        y=interfaz_administrador
        y.state('zoomed')

        label = tk.Label(interfaz_administrador, text=f"Bienvenido administrador {nombre_administrador}", font=("Times New Roman", 25), bg='white', fg='black')
        label.pack(pady=50)
        
        barra_lateral = tk.Frame(interfaz_administrador, bg="#2D6A4F", width=250)
        barra_lateral.pack(side="left", fill="y",anchor="nw")

        imagen_original = Image.open("interfaz_Administrador.png")
        imagen_redimensionada = imagen_original.resize((120, 120))  # Ajusta tamaño si hace falta
        imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

        label_imagen = tk.Label(barra_lateral, image=imagen_tk, bg="#2D6A4F", bd=0)
        label_imagen.image = imagen_tk
        label_imagen.pack(side="top", anchor="n", pady=0, padx=0)  # Asegura que esté bien arriba

        contenido = tk.Frame(interfaz_administrador, bg="#EDEDED")
        contenido.pack(side="right", fill="both", expand=True)

        frame_botones = tk.Frame(interfaz_administrador)
        frame_botones.pack()

        boton1 = tk.Button(frame_botones, text="1. Mostrar menú", width=25, font=("Times New Roman", 10),
                        command=lambda: objeto_staff.ver_menu(interfaz_administrador))
        boton1.grid(row=0, column=0, padx=10, pady=10)

        boton2 = tk.Button(frame_botones, text="2. Claves", width=25, font=("Times New Roman", 10),
                        command=admin.Edicion_clave)
        boton2.grid(row=0, column=1, padx=10, pady=10)

        boton3 = tk.Button(frame_botones, text="3. Reportes", width=25, font=("Times New Roman", 10),
                        command=admin.Ver_reporte)
        boton3.grid(row=0, column=2, padx=10, pady=10)

        boton4 = tk.Button(frame_botones, text="4. Menú", width=25, font=("Times New Roman", 10),
                        command=lambda: objeto_staff.edicion_platos(interfaz_administrador))
        boton4.grid(row=1, column=0, padx=10, pady=10)

        boton5 = tk.Button(frame_botones, text="5. Empleados", width=25, font=("Times New Roman", 10),
                        command=admin.Editar_empleados)
        boton5.grid(row=1, column=1, padx=10, pady=10)

        boton6 = tk.Button(frame_botones, text="6. Volver", width=25, font=("Times New Roman", 10),
                        command=lambda: volver1(interfaz_anterior, y))
        boton6.grid(row=1, column=2, padx=10, pady=10)

        # Cerrar con la X también vuelve
        interfaz_administrador.protocol("WM_DELETE_WINDOW", lambda: volver1(interfaz_anterior, y))
