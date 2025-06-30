from personas import Persona
import tkinter as tk
from tkinter import messagebox
import GastroSoft_principal
from tkinter import ttk, messagebox
def volver1(anterior, actual):
    GastroSoft_principal.volver(anterior,actual)
datos=GastroSoft_principal.leer_datos("claves_ingreso.json")
datos_platos=GastroSoft_principal.leer_datos("platos.json")
datos_categorias=GastroSoft_principal.leer_datos("categorias.json")
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
    #Este diccionario contiene los nombres de las clases que contienen cada categoria
    global Nombres_de_categorias_en_clases
    Nombres_de_categorias_en_clases = {
    "Bebidas": "CategoriaBebida"}
    
    # Función que inyecta la fábrica según categoría
    global Creador_de_categoria
    def Creador_de_categoria(nombre_categoria):
        clase_factory = Nombres_de_categorias_en_clases.get(nombre_categoria)
        if clase_factory:
            return clase_factory()
        else:
            return CategoriaGenerica(nombre_categoria)
    
    #Aqui seleccionamos la categoria para determinar que clase vamos a inyectar
    def seleccion_categoria():
        interfaz_edicion_platos.withdraw
        Interfaz_seleccion_categoria = tk.Tk()
        Interfaz_seleccion_categoria.title("Seleccionar Categoría")
        Interfaz_seleccion_categoria.geometry("350x250")

        tk.Label(Interfaz_seleccion_categoria, text="Seleccione una categoría:").pack(pady=10)

        categorias = list({emp.get("Categoria") for emp in datos_categorias if emp.get("Categoria")})

        seleccion = tk.StringVar()
        seleccion_categoria = ttk.Combobox(interfaz_agregar, textvariable=seleccion, values=categorias, state="readonly")
        seleccion_categoria.pack(pady=10)
        seleccion_categoria.set("Selecciona una categoria")
        

        entrada_nueva = tk.Entry(Interfaz_seleccion_categoria)
        entrada_nueva.pack(pady=10)
        entrada_nueva.pack_forget()

        # Solo muestra la entrada si elige "Otro"
        def mostrar_entrada(event):
            if seleccion.get() == "Otro":
                entrada_nueva.pack()
            else:
                entrada_nueva.pack_forget()

        seleccion_categoria.bind("<<ComboboxSelected>>", mostrar_entrada)

        def continuar():
            seleccionada = seleccion.get()

            if seleccionada == "Otro":
                nueva = entrada_nueva.get().strip()
                if not nueva:
                    messagebox.showerror("Error", "Ingrese una nueva categoría.")
                    return
                fabrica = CategoriaGenerica(nueva)
            else:
                fabrica = Creador_de_categoria(seleccionada)

            crear_plato(fabrica)

        tk.Button(Interfaz_seleccion_categoria, text="Continuar", command=continuar).pack(pady=10)
        boton2 = tk.Button(interfaz_agregar, text="Volver", width=25, font=("Times New Roman", 10), command=lambda:volver1(interfaz_edicion_platos,Interfaz_seleccion_categoria))
        boton2.pack(pady=20)
    #Aqui se ingresn los datos para crear el plato
    global crear_plato
    def crear_plato(fabrica,interfaz_anterior):
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

            messagebox.showinfo("Éxito", f"Plato agregado: {plato['Nombre del plato']} ({plato['Categoria del plato']})")

            tk.Button(interfaz_agregar, text="Agregar Plato", command=agregar_plato).pack(pady=20)

            boton2 = tk.Button(interfaz_agregar, text="Volver", width=25, font=("Times New Roman", 10), command=lambda:volver1(interfaz_anterior,interfaz_agregar))
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

    def Eliminar_categoria(self):
        pass
    
    def edicion_platos (self,interfaz_anterior):
            interfaz_anterior.withdraw()
            global interfaz_edicion_platos
            interfaz_edicion_platos=tk.Toplevel()
            interfaz_edicion_platos.title("GastroSoft Edicion de platos")
            interfaz_edicion_platos.geometry("700x600")

            boton3 = tk.Button(interfaz_edicion_platos, text="1. Agregar un plato", width=25, font=("Times New Roman", 10), command=lambda:staff.seleccion_categoria("e"))
            boton3.pack(pady=20)
            boton1 = tk.Button(interfaz_edicion_platos, text="2. Eliminar un plato", width=25, font=("Times New Roman", 10), command=lambda:staff.eliminar_platos("e"))
            boton1.pack(pady=20)
            boton4 = tk.Button(interfaz_edicion_platos, text="3. Actualizar un plato", width=25, font=("Times New Roman", 10), command=lambda:staff.editar_platos("e"))
            boton4.pack(pady=20)
            boton6= tk.Button(interfaz_edicion_platos, text="5. Eliminar categoría", width=25,font=("Times New Roman",10), command=lambda:staff.Eliminar_categoria())
            boton6.pack(pady=20) 
            boton2 = tk.Button(interfaz_edicion_platos, text="Volver", width=25, font=("Times New Roman", 10), command=lambda:volver1(interfaz_anterior,interfaz_edicion_platos))
            boton2.pack(pady=20)
        
    