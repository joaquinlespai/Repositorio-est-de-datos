class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregarAlFinal(self, _dato: str):
        nuevoNodo = Nodo(_dato)
        if self.primero is None:
            self.primero = nuevoNodo
            self.ultimo = nuevoNodo
        else:
            nuevoNodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevoNodo
            self.ultimo = nuevoNodo

    def eliminarDato(self, _dato: str):
        aux = self.primero
        while aux is not None:
            if aux.dato == _dato:
                if aux.siguiente is not None:
                    aux.siguiente.anterior = aux.anterior
                else:
                    self.ultimo = aux.anterior

                if aux.anterior is not None:
                    aux.anterior.siguiente = aux.siguiente
                else:
                    self.primero = aux.siguiente

                del aux
                return

            aux = aux.siguiente

    def __str__(self):
        aux = self.primero
        res = ""
        while aux is not None:
            res += aux.dato + ", "
            aux = aux.siguiente

        return res

if __name__ == "__main__":
    lista = ListaDoblementeEnlazada()
    lista.agregarAlFinal("Canción 1" " " "Artista 1")
    print(lista)
    lista.agregarAlFinal("Canción 2" " " "Artista 2")
    print(lista)
    lista.agregarAlFinal("Canción 3" " " "Artista 3")
    print(lista)
    lista.eliminarDato("Canción 2" " " "Artista 2")
    print(lista)
