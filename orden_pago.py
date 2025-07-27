import tkinter as tk
from estrategia_descuento import DescuentoEstudiante, DescuentoProfesor, SinDescuento, AplicarDescuento
import GastroSoft_principal
from datetime import datetime

class OrdenPago:
    def __init__(self, pedido, callback_confirmacion):
        self.pedido = pedido
        self.callback_confirmacion = callback_confirmacion
        self.numero_pedido = self._generar_codigo_unico()

    def _generar_codigo_unico(self):
        pedidos_guardados = GastroSoft_principal.leer_datos("pedidos_guardados.json")
        if not pedidos_guardados:
            return 1
        else:
            ult_codigos = [p.get("numero_pedido", 0) for p in pedidos_guardados]
            return max(ult_codigos) + 1

    def generar(self):
        self._mostrar_comprobante()

    def _mostrar_comprobante(self):
        interfaz_orden_de_pago = tk.Toplevel()
        interfaz_orden_de_pago.title("Orden de pago")
        interfaz_orden_de_pago.geometry("700x600")
        interfaz_orden_de_pago.configure(bg="black")

        resumen = f"--- ORDEN DE PAGO - CODIGO: {self.numero_pedido} ---\n"
        for item in self.pedido:
            resumen += f"{item['cantidad']} x {item['nombre']} - ${item['precio'] * item['cantidad']:.2f}\n"
        resumen += "       Cancelar en caja"

        tk.Label(interfaz_orden_de_pago, text=resumen, bg="white", fg="black", font=("Arial", 12)).pack(pady=10)

        def confirmar_final():
            interfaz_tipo_cliente = tk.Toplevel()
            interfaz_tipo_cliente.title("Tipo de Cliente")
            interfaz_tipo_cliente.geometry("400x300")
            interfaz_tipo_cliente.configure(bg="black")

            tk.Label(interfaz_tipo_cliente, text="Seleccione su tipo de cliente", font=("Arial", 14), bg="black", fg="white").pack(pady=20)

            cas = AplicarDescuento(
                self.pedido,
                self.numero_pedido,
                lambda pedido_desc, cod: self._post_descuento(pedido_desc, cod, interfaz_tipo_cliente, interfaz_orden_de_pago),
                interfaz_tipo_cliente,
                interfaz_orden_de_pago
            )
            tk.Button(interfaz_tipo_cliente, text="Estudiante (10% desc.)", width=30,
                      command=lambda: cas.aplicar_y_confirmar(DescuentoEstudiante())).pack(pady=10)
            tk.Button(interfaz_tipo_cliente, text="Profesor (5% desc.)", width=30,
                      command=lambda: cas.aplicar_y_confirmar(DescuentoProfesor())).pack(pady=10)
            tk.Button(interfaz_tipo_cliente, text="Cliente General (sin desc.)", width=30,
                      command=lambda: cas.aplicar_y_confirmar(SinDescuento())).pack(pady=10)

        tk.Button(interfaz_orden_de_pago, text="Aplicar Descuento", command=confirmar_final,
                  bg="green", fg="white", font=("Arial", 12)).pack(pady=20)

    def _post_descuento(self, pedido_desc, numero_pedido, interfaz_tipo_cliente, interfaz_orden_de_pago):
        # Cierra ventanas
        interfaz_tipo_cliente.destroy()
        interfaz_orden_de_pago.destroy()

        # Vuelve a mostrar comprobante de pago con el descuento aplicado
        resumen = f"--- ORDEN DE PAGO - CODIGO: {numero_pedido} ---\n"
        for item in pedido_desc:
            resumen += f"{item['cantidad']} x {item['nombre']} - ${item['precio'] * item['cantidad']:.2f}\n"
        resumen += "       Cancelar en caja"

        comprobante_ventana = tk.Toplevel()
        comprobante_ventana.title("Comprobante con descuento")
        comprobante_ventana.geometry("700x600")
        comprobante_ventana.configure(bg="black")

        tk.Label(comprobante_ventana, text=resumen, bg="white", fg="black", font=("Arial", 12)).pack(pady=10)
        tk.Button(comprobante_ventana, text="Cerrar", command=comprobante_ventana.destroy,
                bg="red", fg="white").pack(pady=10)

        # Finalmente se guarda y llama el callback real
        self.callback_confirmacion(pedido_desc, numero_pedido)
