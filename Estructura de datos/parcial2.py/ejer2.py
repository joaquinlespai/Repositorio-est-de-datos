class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class circularBi:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.len = 0

    def agregarcontacto(self, dato):
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

    def eliminarcontacto(self, num):
        aux = self.primero
        auxnum = 0
        if auxnum == 0:
            self.ultimo.siguiente = aux.siguiente
            self.primero = self.ultimo.siguiente
            self.len += 1

            del aux
            return
        
        while True:
            if num == auxnum +1:
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
            aux = aux.siguiente
        return "  "
    
if __name__ == "__main__":
    agendar = circularBi()
    agendar.agregarcontacto("Tomas" " +569-31231444 " "tomasteihuel@gmail.com")
    print(agendar)
    agendar.agregarcontacto("Dante" " +569-12341214 " "dantefarfan@gmail.com")
    print(agendar)
    agendar.agregarcontacto("Alan"  "+569-64520987 " "alangutierrez@gmail.com")
    agendar.eliminarcontacto(1)
    print(agendar)