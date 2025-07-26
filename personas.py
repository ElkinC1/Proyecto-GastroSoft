from abc import ABC, abstractmethod

class Persona():
    def __init__(self, sesion):
        self.sesion=sesion

    def realizar_pedido(self):
        pass
    
    @abstractmethod
    def ver_menu(self):
        pass




'''class persona():
    datos=GastroSoft_principal.leer_datos()
    def __init__(self, sesion):
        self.sesion=sesion
    @abstractmethod
    def realizar_pedido(n):
        datos=GastroSoft_principal.leer_datos()
        while True:
            interruptor=""
            x=input("Ingrese el plato que desee: ")
            for plato in datos:
                if plato["Nombre del plato"]==x:
                    print("plato agregado correctamente")

            interruptor= input("Desea seguir agregando platos? ").title
            if interruptor =="No":
                break

    @abstractmethod
    def cancelar_pedido(self):
        pass
    @abstractmethod
    def ver_menu(self):

        mostrar1=menu("hola",1)
        mostrar1.mostrar_menu'''



