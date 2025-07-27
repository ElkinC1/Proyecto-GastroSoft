# estrategia_descuento.py

class DescuentoEstudiante:
    def aplicar_descuento(self, precio):
        return precio * 0.90

class DescuentoProfesor:
    def aplicar_descuento(self, precio):
        return precio * 0.95

class SinDescuento:
    def aplicar_descuento(self, precio):
        return precio

class AplicarDescuento:
    def __init__(self, pedido, numero_pedido, callback_confirmacion, interfaz_tipo_cliente, interfaz_orden_de_pago):
        self.pedido = pedido
        self.numero_pedido = numero_pedido
        self.callback_confirmacion = callback_confirmacion
        self.interfaz_tipo_cliente = interfaz_tipo_cliente
        self.interfaz_orden_de_pago = interfaz_orden_de_pago

    def aplicar_y_confirmar(self, estrategia):
        for plato in self.pedido:
            plato["precio"] = estrategia.aplicar_descuento(plato["precio"])
        self.interfaz_tipo_cliente.destroy()
        self.interfaz_orden_de_pago.destroy()
        self.callback_confirmacion(self.pedido, self.numero_pedido)
