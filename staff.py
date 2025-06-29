from personas import Persona
import tkinter as tk
from tkinter import messagebox
import GastroSoft_principal
from tkinter import ttk, messagebox
def volver1(anterior, actual):
    GastroSoft_principal.volver(anterior,actual)
datos=GastroSoft_principal.leer_datos("claves_ingreso.json")
class staff(Persona):
    def __init__(self,sesion, clave,usuario):
        super().__init__(sesion)
        self.sesion=sesion
        self.clave=clave
        self.usuario=usuario
    def realizar_pedido(self):
        print("hola")
 
    def cancelar_pedido(self):
        print ("hola")
    def agregar_plato(self):
        datos_platos=GastroSoft_principal.leer_datos("platos.json")
        datos_categorias=GastroSoft_principal.leer_datos("categorias.json")
        def agrega():
            
            Nombre_plato = Nombre.get()
            
            try:
                Precio_plato = float(Precio.get())
            except ValueError:
                messagebox.showerror("Error", "El precio debe ser un número válido.")
                return
            try:
                Codigo_plato = int(Codigo.get())
            except ValueError:
                messagebox.showerror("Error", "El codigo debe ser un número válido.")
            categoria=seleccion_categoria.get()
            if Nombre_plato and Precio_plato:
                agregar_dato = {
                    "Nombre del plato": Nombre_plato,
                    "Precio del plato": Precio_plato,
                    "Codigo del plato": Codigo_plato,
                    "Categoria del plato": categoria
                }
                datos_platos.append(agregar_dato)
                GastroSoft_principal.guardar_datos(datos_platos,"platos.json")
                Nombre.delete(0, tk.END)
                Precio.delete(0, tk.END)
                Codigo.delete(0, tk.END)  # Limpia las entradas para agregar otro plato
                messagebox.showinfo("Éxito!", "Plato agregado correctamente.")
            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")

        interfaz_agregar = tk.Toplevel()
        interfaz_agregar.title("Ingresar")
        interfaz_agregar.geometry("900x700")

        #ingresos
        tk.Label(interfaz_agregar, pady=20, text="Nombre del plato").pack()
        Nombre = tk.Entry(interfaz_agregar)
        Nombre.pack()

        tk.Label(interfaz_agregar, pady=20, text="Precio del plato").pack()
        Precio = tk.Entry(interfaz_agregar)
        Precio.pack()

        tk.Label(interfaz_agregar, pady=20, text="Codigo del plato").pack()
        Codigo = tk.Entry(interfaz_agregar)
        Codigo.pack()

        categorias = list({emp.get("Categoria") for emp in datos_categorias if emp.get("Categoria")})

        seleccion = tk.StringVar()
        seleccion_categoria = ttk.Combobox(interfaz_agregar, textvariable=seleccion, values=categorias, state="readonly")
        seleccion_categoria.set("Selecciona una categoria")
        seleccion_categoria.pack(pady=10)

        #boton para confirmar el ingreso
        tk.Button(interfaz_agregar, text="Agregar el plato", command=agrega).pack()

        boton2 = tk.Button(interfaz_agregar, text="Volver", width=25, font=("Times New Roman", 10), command=lambda:volver1(interfaz_edicion_platos,interfaz_agregar))
        boton2.pack(pady=20)
        

 
    def eliminar_platos(self):
        interfaz_edicion_platos.withdraw()
        def elimina():
            datos=GastroSoft_principal.leer_datos("platos.json")
            codigo_plato = int(codigo.get())
            if codigo_plato:
                for plato in datos:
                    if plato['Codigo del plato'] == codigo_plato:
                        respuesta = messagebox.askyesno("Eliminar plato", f"¿Estas seguro de eliminar el plato: {plato['Nombre del plato']}, codigo:{plato['Codigo del plato'],}, categoria :{plato["Categoria del plato"]}?")
                        if respuesta:
                            datos.remove(plato)
                            GastroSoft_principal.guardar_datos(datos,"platos.json")
                            messagebox.showinfo("Éxito", "El plato fue eliminado correctamente del menú.")
                            codigo.delete(0, tk.END)
                            return
                        else:
                            return
            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")

        interfaz_eliminar = tk.Toplevel()
        interfaz_eliminar.title("Eliminar")
        interfaz_eliminar.geometry("300x300")

        #ingresos
        tk.Label(interfaz_eliminar, text="Ingrese el codigo del plato:").pack(pady=5)
        codigo=tk.Entry(interfaz_eliminar)
        codigo.pack ()

        #boton para confirmar el ingreso
        tk.Button(interfaz_eliminar, text="Eliminar el plato", command=elimina).pack()

        #boton para eliminar
        
        boton2 = tk.Button(interfaz_eliminar, text="Volver", width=25, font=("Times New Roman", 10), command=lambda:volver1(interfaz_edicion_platos,interfaz_eliminar))
        boton2.pack(pady=20)
        
        

   
    def editar_platos(self):
        datos=GastroSoft_principal.leer_datos("platos.json")
        interfaz_edicion_platos.withdraw()
        interfaz_actualizar = tk.Toplevel()
        interfaz_actualizar.title("GastroSoft - Actualizar Plato")
        interfaz_actualizar.geometry("600x500")

        # Etiqueta y entrada para el código del plato
        tk.Label(interfaz_actualizar, pady=10, text="Código del Plato").pack()
        Codigo = tk.Entry(interfaz_actualizar)
        Codigo.pack()

        # Menú desplegable para elegir qué dato cambiar
        tk.Label(interfaz_actualizar, pady=10, text="Dato a modificar").pack()
        opciones = ["Nombre del plato", "Precio del plato", "Codigo del plato"]
        combo_dato = ttk.Combobox(interfaz_actualizar, values=opciones, state="readonly")
        combo_dato.current(0)
        combo_dato.pack()

        # Entrada para el nuevo valor
        tk.Label(interfaz_actualizar, pady=10, text="Nuevo Valor").pack()
        nuevo_valor = tk.Entry(interfaz_actualizar)
        nuevo_valor.pack()

        def actualizar_plato():
            datos=GastroSoft_principal.leer_datos("platos.json")
            codigo = Codigo.get()
            combo = combo_dato.get()
            nuevo_valor1 = nuevo_valor.get()

            if not (codigo and combo and nuevo_valor):
                messagebox.showerror("Error", "Por favor complete todos los campos.")
                return
        
            for plato in datos:
                if str(plato.get("Codigo del plato")) == codigo:
                 
                    if combo == "Precio del plato":
                        try:
                            nuevo_valor1 = float(nuevo_valor1)
                        except ValueError:
                            messagebox.showerror("Error", "El precio debe ser un número.")
                            return
                    plato[combo] = nuevo_valor1
                    # Guarda los datos actualizados
                    GastroSoft_principal.guardar_datos(datos, "platos.json")
                    datos_nuevos = "\n".join([f"{clave}: {valor}" for clave, valor in plato.items()])
            
                    messagebox.showinfo("Éxito",f"Plato con código {codigo} actualizado correctamente:\n\n{datos_nuevos}")
                    Codigo.delete(0, tk.END)
                    nuevo_valor.delete(0, tk.END)
                    return

            messagebox.showerror("Error", f"No se encontró un plato con código {codigo}.")

        
        tk.Button(interfaz_actualizar, text="Confirmar", width=25, command=actualizar_plato).pack(pady=20)
        tk.Button(interfaz_actualizar, text="Cancelar", width=25,command=lambda: volver1(interfaz_edicion_platos, interfaz_actualizar)).pack()

    def ver_menu(self,interfaz_anterior):
            from menu import menu
            mostrar=menu("hola",1)
            mostrar.mostrar_menu(interfaz_anterior)
    def Crear_categoria(self,):
        pass
    def Eliminar_categoria(self):
        pass
    
    def edicion_platos (self,interfaz_anterior):
            interfaz_anterior.withdraw()
            global interfaz_edicion_platos
            interfaz_edicion_platos=tk.Toplevel()
            interfaz_edicion_platos.title("GastroSoft Edicion de platos")
            interfaz_edicion_platos.geometry("700x600")

            boton3 = tk.Button(interfaz_edicion_platos, text="1. Agregar un plato", width=25, font=("Times New Roman", 10), command=lambda:staff.agregar_plato("e"))
            boton3.pack(pady=20)
            boton1 = tk.Button(interfaz_edicion_platos, text="2. Eliminar un plato", width=25, font=("Times New Roman", 10), command=lambda:staff.eliminar_platos("e"))
            boton1.pack(pady=20)
            boton4 = tk.Button(interfaz_edicion_platos, text="3. Actualizar un plato", width=25, font=("Times New Roman", 10), command=lambda:staff.editar_platos("e"))
            boton4.pack(pady=20)
            boton5= tk.Button(interfaz_edicion_platos, text="4. Crear categoría", width=25,font=("Times New Roman",10), command=lambda:staff.Crear_categoria())
            boton5.pack(pady=20) 
            boton6= tk.Button(interfaz_edicion_platos, text="5. Eliminar categoría", width=25,font=("Times New Roman",10), command=lambda:staff.Eliminar_categoria())
            boton6.pack(pady=20) 
            boton2 = tk.Button(interfaz_edicion_platos, text="Volver", width=25, font=("Times New Roman", 10), command=lambda:volver1(interfaz_anterior,interfaz_edicion_platos))
            boton2.pack(pady=20)
        
    