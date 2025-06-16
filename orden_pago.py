class orden_pago:
    def __init__(self, pedido):
        self.pedido = pedido

    def generar(self):
        resumen = "--- COMPROBANTE DE PAGO ---\n"
        resumen += self.pedido.resumen()
        resumen += "       Cancelar en caja"
        return resumen

