class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class listadoblenelazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacio(self):
        return self.primero is None
    
    def agregar_al_final(self, dato):
        nuevonodo = nodo(dato)
        if self.esta_vacio():
            self.primero = nuevonodo
            self.ultimo = nuevonodo
        else:
            nuevonodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevonodo
            self.ultimo = nuevonodo

    def agregar_al_inicio(self, dato):
        nuevonodo = nodo(dato)
        if self.esta_vacio():
            self.primero = nuevonodo
            self.ultimo = nuevonodo
        else:
            nuevonodo.siguiente = self.primero
            self.primero.anterior = nuevonodo
            self.primero = nuevonodo

    def imprimir(self):
        actual = self.primero
        while actual:
            print(actual.dato)
            actual = actual.siguiente

    def obtener_cabecera(self):
        return self.primero.dato if self.primero else None
    
    def obtener_cola(self):
        return self.ultimo.dato if self.ultimo else None
    
    def existe(self, busqueda):
        actual = self.primero
        while actual:
            if actual.dato == busqueda:
                return True
            actual = actual.siguiente
        return False
    
    def eliminar(self, busqueda):
        actual = self.primero
        while actual:
            if actual.dato == busqueda:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.primero = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.ultimo = actual.anterior
                break
            actual = actual.siguiente