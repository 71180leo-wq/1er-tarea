# =====================================================================
# 5. DEFINIR LA CLASE CATEGORÍA
# =====================================================================
class Categoria:
    def __init__(self, id, nombre_categoria, descripcion):
        self.id = id
        self.nombre_categoria = nombre_categoria
        self.descripcion = descripcion
        self.activa = True

    # Método para simular que se actualiza o desactiva la categoría
    def desactivarCategoria(self):
        self.activa = False
        print("La categoría", self.nombre_categoria, "ha sido desactivada.")

# Definir instancias de la clase categoría
cat1 = Categoria(1, "Electrónica", "Dispositivos electrónicos y cómputo")
cat2 = Categoria(2, "Tecnología", "Componentes de hardware modernos")
cat3 = Categoria(3, "Accesorios", "Periféricos y complementos de PC")

# Imprimir los datos de los registros
print(type(cat1))
print(cat1.id, cat1.nombre_categoria, cat1.descripcion, cat1.activa)
print(cat2.id, cat2.nombre_categoria, cat2.descripcion, cat2.activa)
print(cat3.id, cat3.nombre_categoria, cat3.descripcion, cat3.activa)

# Llamar al método desactivar
cat1.desactivarCategoria()