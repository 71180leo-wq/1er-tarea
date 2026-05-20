# =====================================================================
# 4. DEFINIR LA CLASE TRANSACCION
# =====================================================================
class Transaccion:
    def __init__(self, id, pedido_id, monto, medio_pago):
        self.id = id
        self.pedido_id = pedido_id
        self.monto = monto
        self.medio_pago = medio_pago
        self.estado = "Aprobada"

    # Método DELETE: para simular la cancelación o reembolso del dinero
    def deleteTransaccion(self):
        self.estado = "Cancelada/Reembolsada"
        print("La transacción", self.id, "por un monto de", self.monto, "ha sido eliminada (DELETE).")

# Definir instancias de la clase transaccion
trans1 = Transaccion(901, 501, 12500.00, "Tarjeta")
trans2 = Transaccion(902, 502, 3500.50, "PayPal")
trans3 = Transaccion(903, 503, 850.00, "Efectivo")

# Imprimir los datos de los registros
print(type(trans1))
print(trans1.id, trans1.pedido_id, trans1.monto, trans1.medio_pago, trans1.estado)
print(trans2.id, trans2.pedido_id, trans2.monto, trans2.medio_pago, trans2.estado)
print(trans3.id, trans3.pedido_id, trans3.monto, trans3.medio_pago, trans3.estado)

# Llamar al método delete
trans1.deleteTransaccion()

print("-" * 50)