print("*** BIENVENIDO AL SISTEMA DE PRODUCTOS ***")


id_recibido = int(input("Introduce el ID: "))
nombre_recibido = input("Introduce el Nombre: ")
precio_recibido = float(input("Introduce el Precio: "))
stock_recibido = int(input("Introduce el Stock: "))
categoria_recibido = input("Introduce la Categoría: ")
class Productos:
    def __init__(self, id, nombre, precio, stock, categoria):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria


    def postProducto(self):
        print("\n--- EJECUTANDO POST ---")
        print("Producto guardado con éxito:")
        print("ID:", self.id)
        print("Nombre:", self.nombre)
        print("Precio:", self.precio)
        print("Stock:", self.stock)
        print("Categoría:", self.categoria)


    def getProducto(self):
        print("\n--- EJECUTANDO GET ---")
        print("Mostrando los datos del producto actual:")
        print("El producto se llama " + self.nombre + " y cuesta " + str(self.precio))


    def putProducto(self, nuevo_precio, nuevo_stock):
        print("\n--- EJECUTANDO PUT ---")
        self.precio = nuevo_precio
        self.stock = nuevo_stock
        print("Datos actualizados. Nuevo precio:", self.precio, "Nuevo stock:", self.stock)


    def deleteProducto(self):
        print("\n--- EJECUTANDO DELETE ---")
        print("El producto " + self.nombre + " ha sido eliminado del sistema.")
        self.id = 0
        self.nombre = ""
        self.precio = 0.0
        self.stock = 0
        self.categoria = ""


class Usuario:
    def __init__(self, id, nombre, correo_electronico, contrasena, fecha_registro):
        self.id = id
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena
        self.fecha_registro = fecha_registro

    def postUsuario(self):
        pass

    def getUsuario(self):
        pass

    def putUsuario(self):
        pass

    def deleteUsuario(self):
        pass



class Pedidos:
    def __init__(self, id, usuario_id, direccion, cerrado):
        self.id = id
        self.usuario_id = usuario_id
        self.direccion = direccion
        self.cerrado = cerrado

    def postPedido(self):
        pass

    def getPedido(self):
        pass

    def putPedido(self):
        pass

    def deletePedido(self):
        pass


class Transaccion:
    def __init__(self, id, pedido_id, usuario_id, monto, medio_pago, estado, fecha):
        self.id = id
        self.pedido_id = pedido_id
        self.usuario_id = usuario_id
        self.monto = monto
        self.medio_pago = medio_pago
        self.estado = estado
        self.fecha = fecha

    def postTransaccion(self):
        pass

    def getTransaccion(self):
        pass

    def putTransaccion(self):
        pass

    def deleteTransaccion(self):
        pass





class Categoria:
    def __init__(self, id, nombre_categoria, descripcion, activa):
        self.id = id
        self.nombre_categoria = nombre_categoria
        self.descripcion = descripcion
        self.activa = activa

    def postCategoria(self):
        pass

    def getCategoria(self):
        pass

    def putCategoria(self):
        pass

    def deleteCategoria(self):
        pass


mi_producto = Productos(id_recibido, nombre_recibido, precio_recibido, stock_recibido, categoria_recibido)


mi_producto.postProducto()
mi_producto.getProducto()
mi_producto.putProducto(500.0, 10) 
mi_producto.deleteProducto()