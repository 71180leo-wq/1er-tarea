# =====================================================================
# 3. DEFINIR LA CLASE PEDIDOS
# =====================================================================
class Pedidos:
    def __init__(self, id, usuario_id, direccion, cerrado):
        self.id = id
        self.usuario_id = usuario_id
        self.direccion = direccion
        self.cerrado = cerrado

    # Método PUT: para cambiar el estado del pedido a cerrado
    def putPedido(self):
        self.cerrado = "Sí"
        print("El pedido número", self.id, "ha sido actualizado a Cerrado (PUT).")

# Definir instancias de la clase pedidos
pedido1 = Pedidos(501, 1, "Las Flores #20", "No")
pedido2 = Pedidos(502, 2, "Miraflores #125", "No")
pedido3 = Pedidos(503, 3, "La Escondida #253", "No")

# Imprimir los datos de los registros
print(type(pedido1))
print(pedido1.id, pedido1.usuario_id, pedido1.direccion, pedido1.cerrado)
print(pedido2.id, pedido2.usuario_id, pedido2.direccion, pedido2.cerrado)
print(pedido3.id, pedido3.usuario_id, pedido3.direccion, pedido3.cerrado)

# Llamar al método put
pedido1.putPedido()

print("-" * 50)