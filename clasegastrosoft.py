"""class Staff:
    def agregar_platos(self,plato=str,precio=float,codigo=int):
        if isinstance (plato,str) and isinstance (precio,float) and isinstance (codigo,int):
            precio1 = str(precio)
            codigo1 = str(codigo)
            return codigo1+  " " + plato + " " + precio1 +" dólares "
        else:
            return "operacion incorrecta"
por=Staff()
print (por.agregar_platos("Pollo",5.5,3))"""

class Staff:
    def agregar_platos(self,x,plato="pollo",precio=2.50,codigo=101):
        if isinstance (x,str):
            plato=x
            precio1 = str(precio)
            codigo1 = str(codigo)
            return codigo1+  " - " + plato + " -  $" + precio1 +" dólares "
        elif isinstance(x,int):
            codigo=x
            precio1 = str(precio)
            codigo1 = str(codigo)
            return codigo1+  " - " + plato + " -  $" + precio1 +" dólares "
        elif isinstance(x,float):
            precio=x
            precio1 = str(precio)
            codigo1 = str(codigo)
            return codigo1+  " - " + plato + " -  $" + precio1 +" dólares "

por=Staff()
y=int(input("""1. Codigo
2. nombre
3. precio
Que dato deseas cambiar?:  """))
if y==1:
    x=int(input("Nuevo codigo: "))    
elif y==2:
    x=str(input("Nuevo nombre: ")) 
elif y==3:
    x=float(input("NUevo precio: "))
print (por.agregar_platos(x))