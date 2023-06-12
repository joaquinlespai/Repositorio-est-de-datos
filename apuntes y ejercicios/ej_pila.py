class pilalibros:
    def __init__(self):
        self.libros = []

    def agregar_libros(self, libros):
        self.libros.append(libros)

    def descartar_libros(self):
        if self.esta_vacia():
            print("la pila de libros esta vacia")
        else:
            libro_descartado = self.libros.pop()
            print("se ha descartado el libro:", libro_descartado )

    def esta_vacia(self):
        return len(self.libros) == 0
    
pila = pilalibros()

pila.agregar_libros("libro 1")
pila.agregar_libros("libro 2")
pila.agregar_libros("libro 3")
pila.agregar_libros("libro 4")

while not pila.esta_vacia():
    pila.descartar_libros()