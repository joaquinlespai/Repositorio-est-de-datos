class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

class listaCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.len = 0

    def agregarvideo(self, dato):
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

    def eliminarvideo(self, num):
        aux = self.primero
        auxnum = 0
        if num == 0:
            self.ultimo.siguiente = aux.siguiente
            self.primero = self.ultimo.siguiente
            self.len -= 1
            
            del aux
            return
        
        while True:
            if num == auxnum+1:
                aux.siguiente = aux.siguiente.siguiente
                self.len -= 1
            elif num == auxnum:
                del aux
                return
            aux = aux.siguiente
            auxnum += 1
                
            
    def __str__(self):
        aux = self.primero
        for i in range(self.len):
            print(aux.dato)
            aux = aux.siguiente
        return "  "

if __name__ == "__main__":
    reproducir = listaCircular()
    reproducir.agregarvideo("video 1" " 1:33 " "el nano")
    print(reproducir)
    reproducir.agregarvideo("video 2" " 3:33 " "checo")
    print(reproducir)
    reproducir.agregarvideo("video 3" " 4:44 " "lewis")
    print(reproducir)
    reproducir.eliminarvideo(1)
    print(reproducir)