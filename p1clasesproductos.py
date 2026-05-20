# =====================================================================
# 1. DEFINIR LA CLASE PRODUCTOS
# =====================================================================
class Productos:
    def __init__(self, id, nombre, precio, stock, categoria):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    # Método POST: para simular que guardamos el producto
    def postProducto(self):
        print("Producto", self.nombre, "ha sido guardado con éxito (POST).")

# Definir instancias de la clase productos
prod1 = Productos(101, "Laptop HP", 12500.00, 10, "Electrónica")
prod2 = Productos(102, "Monitor Asus 24", 3500.50, 15, "Tecnología")
prod3 = Productos(103, "Teclado Mecánico", 850.00, 30, "Accesorios")

# Imprimir los datos de los registros
print(type(prod1))
print(prod1.id, prod1.nombre, prod1.precio, prod1.stock, prod1.categoria)
print(prod2.id, prod2.nombre, prod2.precio, prod2.stock, prod2.categoria)
print(prod3.id, prod3.nombre, prod3.precio, prod3.stock, prod3.categoria)

# Llamar al método post
prod1.postProducto()

print("-" * 50) # Línea divisoria para separar las clases en consola











