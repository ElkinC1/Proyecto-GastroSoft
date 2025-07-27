# clientefinal.py
from clientes import Clientes
from factura import Factura

class ClienteFinal(Clientes):
    def __init__(self, sesion=None, nombre=None, cedula=None, direccion=None, correo=None):
        super().__init__(sesion, nombre, cedula, direccion, correo)

    def generar_factura_final(self, pedido_info=None):
        datos_cliente_final = {
            "nombre": "Cliente Final",
            "cedula": "XXXXXXX",
            "correo": "cliente@final.com",
            "direccion": "Dirección Genérica"
        }

        if pedido_info:
            factura_instancia = Factura(datos_cliente_final, pedido_info.get('platos_seleccionados', []), pedido_info.get('iva_porcentaje', 0))
            factura_instancia.visualizar_factura()
