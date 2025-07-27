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
        interfaz_claves.state('zoomed')



        for clave in datos:
                if clave["Marcador"]=="Clave":
                    texto_categoria = tk.Label(interfaz_claves, text=f"CLAVE ACTUAL: {clave["Clave"]}", font=("Arial Black", 17,"bold"),fg="white", bg="#97B2F6")
                    texto_categoria.pack(pady=50) 
                    barra_lateral_derecha = tk.Frame(interfaz_claves, bg="#97B2F6", width=250)
                    barra_lateral_derecha.pack(side="left", fill="both", expand=True)

                    barra_lateral_izquierda = tk.Frame(interfaz_claves, bg="#97B2F6", width=250)
                    barra_lateral_izquierda.pack(side="right", fill="both", expand=True)

        tk.Label(interfaz_claves, pady=20,padx=60, text="Nueva clave").pack()
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
                    if clave_nueva.isdigit() and clave_nueva != "":
                        clave["Clave"]=clave_nueva
                        GastroSoft_principal.guardar_datos(datos,"claves_ingreso.json")
                        nueva_clave.delete(0, tk.END)
                        messagebox.showinfo("Éxito!", "nueva clave agregada correctamente.")
                    else:
                        messagebox.showerror("Error!","Ingreso de datos no valido")
        
        boton3 = tk.Button(interfaz_claves, text="confirmar", width=25, font=("Times New Roman", 10), command=confirmar_edicion)
        boton3.pack(pady=20,padx=60)
        interfaz_Actual=interfaz_claves
        icono_volver = Image.open("image.png").resize((60, 50))
        imagen_volver = ImageTk.PhotoImage(icono_volver)
        interfaz_Actual.imagen_volver = ImageTk.PhotoImage(icono_volver)
        boton6 = tk.Button(interfaz_Actual,text="Volver",image=interfaz_Actual.imagen_volver,compound="top",font=("Times New Roman", 10),fg="white",command=lambda: volver1(interfaz_administrador, interfaz_Actual)
)

        esquina = interfaz_Actual.winfo_screenheight()
        boton6.place(x=50, y=esquina - 150)
        
        
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
        interfaz_edicion_empleados.state('zoomed')
    
        texto = tk.Label(interfaz_edicion_empleados, text=f"EDICION DE EMPLEADOS", font=("Arial Black", 17,"bold"),fg="white", bg="#9DF8AC")
        texto.pack(pady=50) 

        barra_lateral_derecha = tk.Frame(interfaz_edicion_empleados, bg="#9DF8AC", width=250)
        barra_lateral_derecha.pack(side="left", fill="both", expand=True)

        barra_lateral_izquierda = tk.Frame(interfaz_edicion_empleados, bg="#9DF8AC", width=250)
        barra_lateral_izquierda.pack(side="right", fill="both", expand=True)

        def agregar_empleados():
            interfaz_edicion_empleados.withdraw()
            interfaz_agregar_empleados=tk.Toplevel()
            interfaz_agregar_empleados.title("GastroSoft Edicion de empleados")
            interfaz_agregar_empleados.geometry("600x500")
            interfaz_agregar_empleados.state('zoomed')
            
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
            boton2 = tk.Button(interfaz_agregar_empleados, text="Cancelar", width=25, font=("Times New Roman", 10), command=lambda:volver1(interfaz_administrador,interfaz_Actual))
            boton2.pack(pady=20)
        def editar_empleados():
            interfaz_edicion_empleados.withdraw()
            interfaz_editar_empleados = tk.Toplevel()
            interfaz_editar_empleados.title("GastroSoft Edición de empleados")
            interfaz_editar_empleados.geometry("600x500")
            interfaz_editar_empleados.state('zoomed')

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
            tk.Button(interfaz_editar_empleados, text="Cargar datos", command=cargar_info).pack(pady=15,padx=20)
            tk.Button(interfaz_editar_empleados, text="Guardar cambios", command=guardar_cambios).pack(pady=15,padx=20)
            tk.Button(interfaz_editar_empleados, text="Eliminar usuario", command=eliminar_empleado).pack(pady=15,padx=20)
            boton2 = tk.Button(interfaz_editar_empleados, text="Cancelar", width=25, font=("Times New Roman", 10),
                            command=lambda: volver1(interfaz_edicion_empleados, interfaz_editar_empleados))
            boton2.pack(pady=20)

        boton3 = tk.Button(interfaz_edicion_empleados, text="1. Agregar un empleado", width=25, font=("Times New Roman", 10), command=agregar_empleados)
        boton3.pack(pady=20,padx=60)
        boton1 = tk.Button(interfaz_edicion_empleados, text="2. Editar un empleado", width=25, font=("Times New Roman", 10), command=editar_empleados)
        boton1.pack(pady=20,padx=60)
        interfaz_Actual=interfaz_edicion_empleados
        icono_volver = Image.open("image.png").resize((60, 50))
        imagen_volver = ImageTk.PhotoImage(icono_volver)
        interfaz_Actual.imagen_volver = ImageTk.PhotoImage(icono_volver)
        boton6 = tk.Button(interfaz_Actual,text="Volver",image=interfaz_Actual.imagen_volver,compound="top",font=("Times New Roman", 10),fg="white",command=lambda: volver1(interfaz_administrador, interfaz_Actual)
)

        esquina = interfaz_Actual.winfo_screenheight()
        boton6.place(x=50, y=esquina - 150)
        
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

        label = tk.Label(interfaz_administrador, text=f"BIENVENIDO ADMINISTRADOR {nombre_administrador}", font=("Arial Black", 25,"bold"), fg='#B73939')
        label.pack(pady=50)
        
        barra_lateral_derecha = tk.Frame(interfaz_administrador, bg="#D97B7B", width=250)
        barra_lateral_derecha.pack(side="left", fill="both", expand=True)

        barra_lateral_izquierda = tk.Frame(interfaz_administrador, bg="#D97B7B", width=250)
        barra_lateral_izquierda.pack(side="right", fill="both", expand=True)

        frame_botones = tk.Frame(interfaz_administrador)
        frame_botones.pack()

        boton1 = tk.Button(frame_botones, text="1. Mostrar menú", width=25, font=("Times New Roman", 10),
                        command=lambda: objeto_staff.ver_menu(interfaz_administrador))
        boton1.grid(row=0, column=0, padx=20, pady=100)

        boton2 = tk.Button(frame_botones, text="2. Claves", width=25, font=("Times New Roman", 10),
                        command=admin.Edicion_clave)
        boton2.grid(row=0, column=1, padx=20, pady=100)

        boton3 = tk.Button(frame_botones, text="3. Reportes", width=25, font=("Times New Roman", 10),
                        command=admin.Ver_reporte)
        boton3.grid(row=0, column=2, padx=20, pady=100)

        boton4 = tk.Button(frame_botones, text="4. Menú", width=25, font=("Times New Roman", 10),
                        command=lambda: objeto_staff.edicion_platos(interfaz_administrador))
        boton4.grid(row=1, column=0, padx=20, pady=20)

        boton5 = tk.Button(frame_botones, text="5. Empleados", width=25, font=("Times New Roman", 10),
                        command=admin.Editar_empleados)
        boton5.grid(row=1, column=1, padx=20, pady=20)

        interfaz_Actual=interfaz_administrador
        icono_volver = Image.open("image.png").resize((60, 50))
        imagen_volver = ImageTk.PhotoImage(icono_volver)
        interfaz_Actual.imagen_volver = ImageTk.PhotoImage(icono_volver)
        boton6 = tk.Button(interfaz_Actual,text="Volver",image=interfaz_Actual.imagen_volver,compound="top",font=("Times New Roman", 10),fg="white",command=lambda: volver1(interfaz_anterior, interfaz_administrador)
)

        esquina = interfaz_Actual.winfo_screenheight()
        boton6.place(x=50, y=esquina - 150)


        # Cerrar con la X también vuelve
        interfaz_administrador.protocol("WM_DELETE_WINDOW", lambda: volver1(interfaz_anterior, y))
