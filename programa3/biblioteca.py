class libro:
    def __init__(self, titulo, autor, codigou, editorial, año_publicacion, isbn="S/N", genero="General"):
        self.titulo = titulo
        self.autor = autor
        self.codigounico = codigou
        self.editorial = editorial
        self.año_publicacion = año_publicacion
        self.isbn = isbn
        self.genero = genero
        self.disponible = True
         
    def mostrar_info(self):
        return f"{self.titulo} por {self.autor}, con su código {self.codigounico}"

    def actualizar_disponibilidad(self, disponible):
        self.disponible = disponible
        estado = "disponible" if disponible else "no disponible"
        print(f"El libro {self.titulo} ahora esta {estado}")
    
class Usuarios:
    def __init__(self, id_usuario, nombre, email):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.libros_prestados = []
        
    def prestar_libro(self, libro):
        if libro.disponible:
            self.libros_prestados.append(libro)
            libro.actualizar_disponibilidad(False)
            print(f"Libro {libro.titulo} prestado a {self.nombre}")
        else:
            print(f"'{libro.titulo}' no está disponible.")
            
    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            libro.actualizar_disponibilidad(True)
            print(f"Libro '{libro.titulo}' devuelto por {self.nombre}")
        else:
            print(f"{self.nombre} no tiene el libro '{libro.titulo}'.")
            
class Bibliotecario:
    def __init__(self, id_trabajador, nombre):
        self.id_trabajador = id_trabajador
        self.nombre = nombre

    def anadir_libro(self, biblioteca, libro):
        biblioteca.libros.append(libro) 
        print(f"Libro '{libro.titulo}' añadido correctamente.")
            
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario {usuario.nombre} registrado a biblioteca")
        
    def eliminar_usuario(self, usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
        print(f"Usuario {usuario.nombre} eliminado de biblioteca")
        
    def listar_libros(self):
        for libro in self.libros:
            print(libro.mostrar.info())
            
    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(f"{usuario.nombre}, Email: {usuario.email}") 
            
class Prestamo:
    def __init__(self, id_prestamo, libro, usuario, fecha_prestamo, fecha_devolucion):
        self.id_prestamo = id_prestamo
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        
def finalizar_prestamo(self):
    print(f"Prestamo del libro {self.libro.titulo} finalizado, debe ser devuelto por {self.usuario.nombre} antes de {self.fecha_devolucion}")
        
     
        
    
        
