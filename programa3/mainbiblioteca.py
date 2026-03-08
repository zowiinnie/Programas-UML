from biblioteca import*

libros = [
    libro("Dune", "Frank Herbert", "B", "Chilton Books", 1965, "978-0441172719", "Ciencia Ficcion"),
    libro("Cronica de una muerte anunciada", "Gabriel García Márquez", "B", "La Oveja Negra", 1981, "978-8420471921", "Drama"),
    libro("El resplandor", "Stephen King", "C", "Doubleday", 1977, "978-0307743657", "Terror"),
    libro("El Principito", "Antoine de Saint-Exupéry", "A", "Reynal & Hitchcock", 1943, "978-0156012195", "Infantil"),
    libro("Cien años de soledad", "Gabriel García Márquez", "B", "Sudamericana", 1967, "978-0307474728", "Realismo Magico"),
    libro("Neuromante", "William Gibson", "B", "Ace Books", 1984, "978-0441569595", "Cyberpunk"),
    libro("Harry Potter y la piedra filosofal", "J.K. Rowling", "A", "Bloomsbury", 1997, "978-8478884451", "Fantasia"),
    libro("Dracula", "Bram Stoker", "C", "Archibald Constable & Co.", 1897, "978-0486411095", "Terror Gotico"),
    libro("Sapiens", "Yuval Noah Harari", "A", "Harper", 2011, "978-0062316097", "No Ficcion"),
    libro("Asesinato en el Orient Express", "Agatha Christie", "B", "Collins Crime Club", 1934, "978-0062693655", "Misterio")
]

mi_biblioteca = Biblioteca()
admin = Bibliotecario(1, "Ana")

libro1 = libro("Dune", "Frank Herbert", "L001", "Chilton", 1965)
admin.anadir_libro(mi_biblioteca, libro1)

cliente = Usuarios(101, "Carlos", "carlos@email.com")
mi_biblioteca.registrar_usuario(cliente)
cliente.prestar_libro(libro1)