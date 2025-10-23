#Adrián Solís León 2ºDAM

#Clases
class Autor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def mostrar_autor(self):
        return f"{self.nombre} {self.apellidos}"

class Libro:
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = None

    def añadir_autor(self, autor):
        self.autor = autor

    def mostrar_libro(self):
        print("------ Libro ------")
        print(f"Título: {self.titulo}")
        print(f"ISBN: {self.isbn}")
        if self.autor:
            print(f"Autor: {self.autor.mostrar_autor()}")

    def obtener_titulo(self):
        return self.titulo

class Biblioteca:
    def __init__(self):
        self.lista_libros = []
  
    def numero_libros(self):
        return len(self.lista_libros)

    def añadir_libro(self, libro):
        self.lista_libros.append(libro)

    def borrar_libro(self, titulo):
        for libro in self.lista_libros:
            if libro.obtener_titulo().lower() == titulo.lower():
                self.lista_libros.remove(libro)
                print("¡Libro borrado correctamente!")
                return
        print("Libro no encontrado.")

    def mostrar_biblioteca(self):
        print("########################################")
        for libro in self.lista_libros:
            libro.mostrar_libro()
        print("########################################")

#Funciones
def mostrar_menu():
    print("\nMenu")
    print("1) Añadir libro a la biblioteca")
    print("2) Mostrar biblioteca")
    print("3) Borrar libro")
    print("4) ¿Número de libros?")
    print("5) Salir")

def añadir_libro_a_biblioteca(biblioteca):
    titulo = input("Introduzca el título del libro: ")
    isbn = input("Introduzca el ISBN del libro: ")
    nombre_autor = input("Introduzca el nombre del autor: ")
    apellidos_autor = input("Introduzca el apellido del autor: ")

    autor = Autor(nombre_autor, apellidos_autor)
    libro = Libro(titulo, isbn)
    libro.añadir_autor(autor)
    biblioteca.añadir_libro(libro)

def mostrar_biblioteca(biblioteca):
    biblioteca.mostrar_biblioteca()

def borrar_libro(biblioteca):
    titulo = input("Introduzca el título del libro a borrar: ")
    biblioteca.borrar_libro(titulo)

def numero_libros(biblioteca):
    print(f"El número de libros en la biblioteca es: {biblioteca.numero_libros()}")

#Main principal
def main():
    biblioteca = Biblioteca()
    while True:
        mostrar_menu()
        opcion = input("Seleccione opción: ")
        if opcion == "1":
            añadir_libro_a_biblioteca(biblioteca)
        elif opcion == "2":
            mostrar_biblioteca(biblioteca)
        elif opcion == "3":
            borrar_libro(biblioteca)
        elif opcion == "4":
            numero_libros(biblioteca)
        elif opcion == "5":
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

main()