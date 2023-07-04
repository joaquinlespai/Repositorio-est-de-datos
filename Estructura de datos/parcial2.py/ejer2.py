class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class circularBi:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.len = 0

    def inventarioagregar(self,dato):
        nuevoNodo = Nodo(dato)

        if self.primero is None:
            self.primero = nuevoNodo
            self.ultimo = nuevoNodo
            self.ultimo.siguiente = self.primero
            self.len += 1

        else:
            nuevoNodo.siguiente = self.primero
            self.ultimo.siguiente = nuevoNodo
            self.ultimo = nuevoNodo
            self.len += 1

    def eliminarinventario(self, num):
        aux = self.primero
        auxnum = 0
        if auxnum == 0:
            self.ultimo.siguiente = aux.siguiente
            self.primero = self.ultimo.siguiente
            self.len += 1

            del aux
            return
        
        while True:
            if num == auxnum + 1:
                aux.siguiente = aux.siguiente.siguiente
                self.len -= 1
            elif num == auxnum:
                del aux
                return
            aux = aux.siguiente
            auxnum += 1

    def estavacia(self):
        if self.primero is None:
            return True
        else:
            return False

    def __str__(self):
        aux = self.primero
        for i in range(self.len):
            print(aux.dato)
            aux.siguiente
        return "  "

if __name__ == "__main__":
    inventario = circularBi()
    inventario.inventarioagregar("codigo: 12345" " manzanas " " hay: 5")
    print(inventario)
    inventario.inventarioagregar("codigo: 65432" " platanos " " hay: 10")
    print(inventario)
    inventario.inventarioagregar("codigo: 09765" " peras " " hay: 21")
    print(inventario)
    inventario.eliminarinventario(3)
    print(inventario)