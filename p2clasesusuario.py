# =====================================================================
# 2. DEFINIR LA CLASE USUARIO
# =====================================================================
class Usuario:
    def __init__(self, id, nombre, correo_electronico, contrasena):
        self.id = id
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena

    # Método GET: para simular que consultamos el perfil del usuario
    def getUsuario(self):
        print("Consultando datos de acceso del usuario:", self.nombre, "(GET).")

# Definir instancias de la clase usuario
user1 = Usuario(1, "Carlos López", "carlos@gmail.com", "12345")
user2 = Usuario(2, "Ana Gómez", "anag@gmail.com", "abcde")
user3 = Usuario(3, "Pedro Ruíz", "pedror@gmail.com", "qwerty")

# Imprimir los datos de los registros
print(type(user1))
print(user1.id, user1.nombre, user1.correo_electronico, user1.contrasena)
print(user2.id, user2.nombre, user2.correo_electronico, user2.contrasena)
print(user3.id, user3.nombre, user3.correo_electronico, user3.contrasena)

# Llamar al método get
user1.getUsuario()

print("-" * 50)