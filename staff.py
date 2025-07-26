from personas import Persona
import tkinter as tk
from tkinter import messagebox
import GastroSoft_principal
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod
def volver1(anterior, actual):
    GastroSoft_principal.volver(anterior,actual)
datos=GastroSoft_principal.leer_datos("claves_ingreso.json")
datos_platos=GastroSoft_principal.leer_datos("platos.json")
datos_categorias=GastroSoft_principal.leer_datos("categorias.json")

class Categoria(ABC):
    @abstractmethod
    def crear_plato(self, nombre, precio, codigo):
        pass


class CategoriaGenerica(Categoria):
    def __init__(self, nombre_categoria):
        self.nombre_categoria = nombre_categoria

    def crear_plato(self, nombre, precio, codigo):
        return {
            "Nombre del plato": nombre,
            "Precio del plato": precio,
            "Codigo del plato": codigo,
            "Categoria del plato": self.nombre_categoria
        }



class CategoriaBebida(Categoria):
    def __init__(self,nombre_categoria):
        self.nombre_categoria = nombre_categoria

    def crear_plato(self, nombre, precio, codigo):
        precio=float(precio)
        if precio > 1:
            raise ValueError("Las bebidas no pueden costar más de 1 un dolar.")
        return {
            "Nombre del plato": nombre,
            "Precio del plato": precio,
            "Codigo del plato": codigo,
            "Categoria del plato": self.nombre_categoria
        }


    # Función que inyecta la fábrica según categoría
class Creador_de_categorias:
    def Creador_de_categoria(self,nombre_categoria):
        clase_factory = Nombres_de_categorias_en_clases.get(nombre_categoria)
        if clase_factory:
            return clase_factory(nombre_categoria)
        else:
            return CategoriaGenerica(nombre_categoria)
        
class staff(Persona):
    def __init__(self,sesion, clave,usuario):
        self.sesion=sesion
        self.clave=clave
        self.usuario=usuario
        self.Seleccion_categoria=Seleccion_categoria()
        self.Eliminar_platos=Eliminar_platos()
        self.Editar_platos=Editar_platos()
        self.Ver_menu=Ver_menu()
        self.ELiminar_categoria=Eliminar_categoria()
        self.Edicion_platos=Edicion_platos()
    def seleccion_categoria(self):
        self.Seleccion_categoria.seleccion_categoria_logica()
    def eliminar_platos(self):
        self.Eliminar_platos.eliminar_platos_logica()
    def editar_platos(self):
        self.Editar_platos.editar_platos_logica()
    def ver_menu(self,interfaz_anterior):
        self.Ver_menu.ver_menu_logica(interfaz_anterior)
    def eliminar_categoria(self):
        self.ELiminar_categoria.eliminar_categoria_logico()
    def edicion_platos(self,interfaz_anterior):
        self.Edicion_platos.edicion_platos_logica(interfaz_anterior)


class Realizar_pedido():
    def realizar_pedido_logica(self):
        print("hola")
 
    #Patrones Abstrach factory y Factory Method
    #Este diccionario contiene los nombres de las clases que contienen cada categoria
global Nombres_de_categorias_en_clases
Nombres_de_categorias_en_clases = {
"Bebidas": CategoriaBebida}
    

    
    #Aqui seleccionamos la categoria para determinar que clase vamos a inyectar
class Seleccion_categoria():
    def seleccion_categoria_logica(self):
        interfaz_edicion_platos.withdraw()
        Interfaz_seleccion_categoria = tk.Toplevel()
        Interfaz_seleccion_categoria.title("Seleccionar Categoría")
        Interfaz_seleccion_categoria.geometry("600x600")

        tk.Label(Interfaz_seleccion_categoria, text="Seleccione una categoría:").pack(pady=10)

        categorias = list({emp.get("Categoria") for emp in datos_categorias if emp.get("Categoria")}) + ["Otro"]

        seleccion = tk.StringVar()
        seleccion_categoria = ttk.Combobox(Interfaz_seleccion_categoria, textvariable=seleccion, values=categorias, state="readonly")
        seleccion_categoria.pack(pady=60)
        seleccion_categoria.set("Selecciona una categoria")
        
        texto_categoria = tk.Label(Interfaz_seleccion_categoria, text="Ingrese la nueva categoria", font=("Times New Roman", 10))
        texto_categoria.pack_forget()
        Categoria_renueva = tk.Entry(Interfaz_seleccion_categoria)
        Categoria_renueva.pack_forget() 

        # Solo muestra la entrada si elige "Otro"
        def mostrar_entrada(*args):
            if seleccion.get() == "Otro":
                texto_categoria.pack(pady=20)
                Categoria_renueva.pack(pady=20)
            else:
                Categoria_renueva.pack_forget() 
                texto_categoria.pack_forget()

        seleccion.trace_add("write", mostrar_entrada)

        def continuar():
            seleccionada = seleccion.get()

            if seleccionada == "Otro":
                nueva = Categoria_renueva.get().strip()
                if not nueva.title():
                    messagebox.showerror("Error", "Ingrese una nueva categoría.")
                    return
                
                fabrica = CategoriaGenerica(nueva.title())
                #Crea la categoria ingresada sin necesidad de tener que agregar un producto
                nueva_categoria={"Categoria":nueva
                                 }
                datos_categorias.append(nueva_categoria)
                GastroSoft_principal.guardar_datos(datos_categorias,"categorias.json")
                messagebox.showinfo("Éxito", f"Categoría: {nueva} agregada con éxito!!")
                Categoria_renueva.delete(0, tk.END)
                seleccion_categoria.set("Selecciona una categoria")
            else:
                fabrica = Creador_de_categorias.Creador_de_categoria("e",seleccionada)
            creacion=Crear_plato()
            creacion.crear_plato("a",fabrica,Interfaz_seleccion_categoria)

        tk.Button(Interfaz_seleccion_categoria, text="Continuar", command=continuar).pack(pady=10)
        boton2 = tk.Button(Interfaz_seleccion_categoria, text="Volver", width=25, font=("Times New Roman", 10), command=lambda:volver1(interfaz_edicion_platos,Interfaz_seleccion_categoria))
        boton2.pack(pady=20)
class Crear_plato():
    #Aqui se ingresn los datos para crear el plato
    global crear_plato
    def crear_plato(self,fabrica,interfaz_anterior):
        interfaz_anterior.withdraw()
        global interfaz_agregar
        interfaz_agregar = tk.Toplevel()
        interfaz_agregar.title("Agregar Plato")
        interfaz_agregar.geometry("400x400")

        tk.Label(interfaz_agregar, text="Nombre del plato").pack()
        entrada_nombre = tk.Entry(interfaz_agregar)
        entrada_nombre.pack()

        tk.Label(interfaz_agregar, text="Precio del plato").pack()
        entrada_precio = tk.Entry(interfaz_agregar)
        entrada_precio.pack()

        tk.Label(interfaz_agregar, text="Código del plato").pack()
        entrada_codigo = tk.Entry(interfaz_agregar)
        entrada_codigo.pack()

        def agregar_plato():
            nombre = entrada_nombre.get()
            try:
                precio = float(entrada_precio.get())
                codigo = int(entrada_codigo.get())
            except ValueError:
                messagebox.showerror("Error", "Precio y código deben ser numéricos.")
                return

            try:
                plato = fabrica.crear_plato(nombre, precio, codigo)
            except Exception as e:
                messagebox.showerror("Error", str(e))
                return

            datos_platos.append(plato)
            GastroSoft_principal.guardar_datos(datos_platos, "platos.json")
            datos_nuevos = "\n".join([f"{clave}: {valor}" for clave, valor in plato.items()])
            
            messagebox.showinfo("Éxito",f"Plato con código {codigo} actualizado correctamente:\n\n{datos_nuevos}")
            entrada_nombre.delete(0, tk.END)
            entrada_precio.delete(0, tk.END)
            entrada_codigo.delete(0, tk.END)

        boton1 = tk.Button(interfaz_agregar, text="Crear plato", width=25, font=("Times New Roman", 10), command=lambda:agregar_plato())
        boton1.pack(pady=20)

        boton2 = tk.Button(interfaz_agregar, text="Volver", width=25, font=("Times New Roman", 10), command=lambda:volver1(interfaz_anterior,interfaz_agregar))
        boton2.pack(pady=20)
            

class Eliminar_platos(): 
    def eliminar_platos_logica(self):
        
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
        
        

   
class Editar_platos():
    def editar_platos_logica(self):
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

class Ver_menu():
    def ver_menu_logica(self,interfaz_anterior):
        from menu import menu
        mostrar=menu("hola",1)
        mostrar.mostrar_menu(interfaz_anterior)  

class Eliminar_categoria():
    def eliminar_categoria_logico(self):
        interfaz_edicion_platos.withdraw()
        def elimina_categoria():
            seleccionada = seleccion.get()
            if Categoria:
                    for dato in datos_categorias:
                        if dato['Categoria'] == seleccionada:
                            respuesta = messagebox.askyesno("Eliminar Categoria", f"¿Estas seguro de eliminar la categoria: {dato["Categoria"]}?")
                            if respuesta:
                                datos_categorias.remove(dato)
                                GastroSoft_principal.guardar_datos(datos_categorias,"categorias.json")
                                messagebox.showinfo("Éxito", f"La categoria {Categoria} fue eliminada correctamente.")
                                categorias.delete(0, tk.END)
                                return
                            else:
                                return
        
                    
            else:
                    messagebox.showerror("Error", "Por favor, complete todos los campos.")

        interfaz_eliminar_categoria = tk.Toplevel()
        interfaz_eliminar_categoria.title("Eliminar")
        interfaz_eliminar_categoria.geometry("300x300")

        #ingresos
        categorias = list({emp.get("Categoria") for emp in datos_categorias if emp.get("Categoria")}) + ["Otro"]

        seleccion = tk.StringVar()
        seleccion_categoria = ttk.Combobox(interfaz_eliminar_categoria, textvariable=seleccion, values=categorias, state="readonly")
        seleccion_categoria.pack(pady=10)
        seleccion_categoria.set("Selecciona una categoria")

        #boton para confirmar el ingres
        tk.Button(interfaz_eliminar_categoria, text="Eliminar categoria", command=lambda:elimina_categoria()).pack()

        #boton para eliminar
        boton2 = tk.Button(interfaz_eliminar_categoria, text="Volver", width=25, font=("Times New Roman", 10), command=lambda:volver1(interfaz_edicion_platos,interfaz_eliminar_categoria))
        boton2.pack(pady=20)
        
class Edicion_platos(): 
    def edicion_platos_logica (self,interfaz_anterior):
            interfaz_anterior.withdraw()
            global interfaz_edicion_platos
            interfaz_edicion_platos=tk.Toplevel()
            interfaz_edicion_platos.title("GastroSoft Edicion de platos")
            interfaz_edicion_platos.geometry("700x600")

            objeto_staff=staff("a","a","a")

            boton3 = tk.Button(interfaz_edicion_platos, text="1. Agregar", width=25, font=("Times New Roman", 10), command=lambda:objeto_staff.seleccion_categoria())
            boton3.pack(pady=20)
            boton1 = tk.Button(interfaz_edicion_platos, text="2. Eliminar un plato", width=25, font=("Times New Roman", 10), command=lambda:objeto_staff.eliminar_platos())
            boton1.pack(pady=20)
            boton4 = tk.Button(interfaz_edicion_platos, text="3. Actualizar un plato", width=25, font=("Times New Roman", 10), command=lambda:objeto_staff.editar_platos())
            boton4.pack(pady=20)
            boton6= tk.Button(interfaz_edicion_platos, text="4. Eliminar categoría", width=25,font=("Times New Roman",10), command=lambda:objeto_staff.eliminar_categoria())
            boton6.pack(pady=20) 
            boton2 = tk.Button(interfaz_edicion_platos, text="Volver", width=25, font=("Times New Roman", 10), command=lambda:volver1(interfaz_anterior,interfaz_edicion_platos))
            boton2.pack(pady=20)
        
    