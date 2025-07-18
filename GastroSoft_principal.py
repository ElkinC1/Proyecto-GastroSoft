#primer cambio
from clientes import clientes
import tkinter as tk
from tkinter import messagebox
import json
from PIL import Image, ImageTk
#primercambio
#segundocambio
#tercercambio
#new world
#Manipulacion de ficheros Json
def leer_datos(fichero):
    try:
        with open(fichero, 'r') as file:
            datos = json.load(file)
    except FileNotFoundError:
        datos = []
    return datos
def guardar_datos(datos,fichero):
    with open(fichero, 'w') as file:
        json.dump(datos, file, indent=4)


#mostrar el menu desde la vista de un cliente
def mostrar_como_cliente ():
    mostrar1= clientes("h","a",1,"s","d")
    mostrar1.ver_menu(Interfaz_clientes) #retorna la interfaz a la clase cliente
def salir():
    principal.destroy()

def volver (Interfaz_Anterior,Interfaz_Actual):
        Interfaz_Actual.destroy()
        Interfaz_Anterior.deiconify()
        Interfaz_Anterior.state('zoomed') #permite que la ventana anterior se maximize al momento de volver a aparecer
def realizar_pedido():
    from pedido import Pedido
    from clientes import clientes
    
    temp_cliente_instance = clientes("a","a","a","a","a")
    
    Pedido.crear_interfaz(temp_cliente_instance._post_pedido_acciones)

#Ventana para los clientes
def coprincipal_2 ():

    
    principal.withdraw()  # Oculta la ventana principal
    global Interfaz_clientes
    Interfaz_Anterior=principal #guarda la ventana principal para volverla a mostrar 
    Interfaz_clientes = tk.Toplevel()
    Interfaz_clientes.title("GatrosSoft")
    Interfaz_clientes.geometry("1280x720")
    Interfaz_clientes.configure(background='black')
    Interfaz_clientes.state('zoomed')

    imagen_fondo_clientes = Image.open("Fondo2.jpg")  
    imagen_fondo_clientes = imagen_fondo_clientes.resize((900, 700)) #Para el tamaño de la imagen
    fondo_tk = ImageTk.PhotoImage(imagen_fondo_clientes)

    label_fondo = tk.Label(Interfaz_clientes, image=fondo_tk)
    label_fondo.image = fondo_tk  
    label_fondo.pack(side="right") 

    Interfaz_Actual= Interfaz_clientes #Guarda la interfaz en la variable para luego poderla eliminar 

    titulo = tk.Label(Interfaz_clientes, text="Clientes", font=("Times New Roman", 45), background="black", fg="white")
    titulo.pack(pady=60)

    boton6 = tk.Button(Interfaz_clientes, text="1. Mostrar menu", width=25, font=("Times New Roman", 10), command=mostrar_como_cliente)
    boton6.pack(pady=20)
    boton4 = tk.Button(Interfaz_clientes, text="2. Realizar pedido", width=25, font=("Times New Roman", 10), command=realizar_pedido)
    boton4.pack(pady=20)
    boton5 = tk.Button(Interfaz_clientes, text="3. Volver", width=25, font=("Times New Roman", 10), command=lambda:volver(Interfaz_Anterior,Interfaz_Actual))
    boton5.pack(pady=20)
Interfaz_Staff=None
#Ventana para los del Staff
def coprincipal_1 ():
        
        global Interfaz_Staff
        
        principal.withdraw()  # Oculta la ventana principal
        anterior=principal
        Interfaz_Staff = tk.Toplevel()
        Interfaz_Staff.title("GastroSoft")
        Interfaz_Staff.geometry("1280x720")
        Interfaz_Staff.configure(background='black')
        Interfaz_Staff.state('zoomed')

        

        titulo = tk.Label(Interfaz_Staff, text="Staff", font=("Times New Roman", 45), background="black", fg="white")
        titulo.pack(pady=20)

            
       
        imagen_usuario = Image.open("imagen_usuario.jpg").resize((30, 30)) #aqui cargas la imagen
        imagen_usuario_tk = ImageTk.PhotoImage(imagen_usuario) #aqui le agregas la funcion para integrarla a tkinter
        Interfaz_Staff.imagen_usuario_tk = imagen_usuario_tk
        
        imagen_contraseña= Image.open("imagen_contraseña.jpg").resize((30,30))
        imagen_contraseña_tk=ImageTk.PhotoImage(imagen_contraseña)
        Interfaz_Staff.imagen_contraseña_tk = imagen_contraseña_tk
        # Campo para los ingresos
        tk.Label(Interfaz_Staff, text="Usuario", image=imagen_usuario_tk, compound="left", background="#000000", fg="white").place(x="565",y="184")
        usuario = tk.Entry(Interfaz_Staff)
        usuario.place(x="665",y="190") 

        tk.Label(Interfaz_Staff,  text="Contraseña", image=imagen_contraseña_tk,compound="left", background="#000000", fg="white").place(x="565",y="234")
        contraseña = tk.Entry(Interfaz_Staff)
        contraseña.place(x="665",y="240")

          # Cierra con X también vuelve
        Interfaz_Staff.protocol("WM_DELETE_WINDOW", lambda: volver(anterior, Interfaz_Staff))

        def ingresar_credenciales():
            datos =leer_datos("claves_ingreso.json")
            try:    
                usuario1 = usuario.get()
            
                clave1 = contraseña.get()
            except ValueError:
                messagebox.showerror("Error, ingreso de datos erroneo")
                return

            for clave in datos:
                if clave["Usuario"] == usuario1 and clave["Clave"]== clave1:
                        if clave["Marcador"]=="Admin":
                             #La importacion se realiza dentro de la funcion para evitar problemas de importaciones ciclicas
                            import administrador
                            administrador.funcion_interfaz_admin(Interfaz_Staff,usuario1) #retorna la interfaz a la funcion que se encuentra en administrador 

                            messagebox.showinfo("Éxito", f"Ingreso correcto Don administrador.")
                            usuario.delete(0, tk.END)
                            contraseña.delete(0, tk.END)
                            return
                        else:
                             import empleados 
                             empleados.funcion_interfaz_de_empleado(Interfaz_Staff,usuario1)
                             messagebox.showinfo("Éxito", f"Ingreso correcto Don empleado.")
                             usuario.delete(0, tk.END)
                             contraseña.delete(0, tk.END)
                             return
                             

            messagebox.showerror("Error", "Usuario no encontrado")
            
        boton2=tk.Button(Interfaz_Staff, text="Ingresar", width=25, font=("Times New Roman", 10), command=ingresar_credenciales)
        boton2.pack(pady=250)
        boton4 = tk.Button(Interfaz_Staff, text="Volver", width=25, font=("Times New Roman", 10), command=lambda:volver(anterior,Interfaz_Staff))
        boton4.place(x="590",y="415")
principal=None
#principal ventana
def iniciar_principal():
    global principal
    principal = tk.Tk()
    principal.title("GastroSoft")
    principal.geometry("1270x683")
    principal.configure(background="#A8B0B5")
    principal.state('zoomed')

    # Cargar imagen de fondo
    imagen_fondo = Image.open("Fondo_principal.jpg")  
    imagen_fondo = imagen_fondo.resize((800, 700)) #Para el tamaño de la imagen
    fondo_tk = ImageTk.PhotoImage(imagen_fondo)

    label_fondo = tk.Label(principal, image=fondo_tk)
    label_fondo.image = fondo_tk  
    label_fondo.pack(side="left") #Alinea la imagen a la izquierda


    titulo = tk.Label(principal, text="GASTROSOFT", font=("Arial Black", 37,"bold"), fg="#B73939" , bg="#A8B0B5") #bg es para el fondo, fg para la fuente
    titulo.place(x=900, y=65) #especifica la ubicacion del texto

    # Permite ubicas los botones encima de la imagen
    imagen_icono = Image.open("trabajadores.jpeg").resize((110, 100)) #aqui cargas la imagen
    imagen_icono_tk = ImageTk.PhotoImage(imagen_icono) #aqui le agregas la funcion para integrarla a tkinter
    boton1 = tk.Button(principal, text="1. Trabajadores", image=imagen_icono_tk, compound="top", font=("Times New Roman", 12),bg="#002031", fg="white", command=coprincipal_1)
    boton1.place(x=920, y=200)

    imagen_icono1 = Image.open("cliente.jpeg").resize((110, 100))
    imagen_icono_tk1 = ImageTk.PhotoImage(imagen_icono1)
    boton = tk.Button(principal, text="2. Clientes", image=imagen_icono_tk1, compound="top", font=("Times New Roman", 12),bg="#002031", fg="white",command=coprincipal_2)  
    boton.place(x=1120, y=200)

    boton3 = tk.Button(principal, text="3. Cerrar aplicación", width=25, font=("Times New Roman", 12),bg="#002031", fg="white", command=salir)
    boton3.place(x=980, y=400)

    principal.mainloop()
if __name__ == '__main__':
    iniciar_principal()

