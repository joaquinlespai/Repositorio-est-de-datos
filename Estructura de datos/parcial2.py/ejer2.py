class Nodo:
    def __init__(self, codigo, nombre, descripcion, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad

class Circular:
    def __init__(self):
        self.articulos = []

    def agregar_articulo(self, codigo, nombre, descripcion, cantidad):
        nuevoarticulo = Nodo(codigo, nombre, descripcion, cantidad)
        self.articulos.append(nuevoarticulo)

    def eliminar_articulo(self, codigo):
        for articulo in self.articulos:
            if articulo.codigo == codigo:
                self.articulos.remove(articulo)

    def buscar_articulo(self, codigo):
        for articulo in self.articulos:
            if articulo.codigo == codigo:
                print("Código: {}".format(articulo.codigo))
                print("Nombre: {}".format(articulo.nombre))
                print("Descripción: {}".format(articulo.descripcion))
                print("Cantidad disponible: {}".format(articulo.cantidad))
                return

        print("Artículo no encontrado")

    def actualizar_cantidad(self, codigo, nueva_cantidad):
        for articulo in self.articulos:
            if articulo.codigo == codigo:
                articulo.cantidad = nueva_cantidad
                return

        print("Artículo no encontrado")

    def mostrar_articulos(self):
        self.articulos.sort(key=lambda articulo: articulo.codigo)

        for articulo in self.articulos:
            print("Código: {}".format(articulo.codigo))
            print("Nombre: {}".format(articulo.nombre))
            print("Descripción: {}".format(articulo.descripcion))
            print("Cantidad disponible: {}".format(articulo.cantidad))
            print()

inventario = Circular()
inventario.agregar_articulo("12313", "Manzanas", "Manzanas Rojas", 13)
print(inventario)
inventario.agregar_articulo("14532", "Peras", "Pera granel", 1)
print(inventario)
inventario.agregar_articulo("23531", "Platanos", "Planatos verdes", 25)
print(inventario)


inventario.mostrar_articulos()
print("Buscar artículo por código:")

inventario.buscar_articulo("12313")
print(inventario)

inventario.eliminar_articulo("23531")
print(inventario)

inventario.actualizar_cantidad("12313", 33)
print(inventario)
    
print("Todos los artículos del inventario:")
inventario.mostrar_articulos()
