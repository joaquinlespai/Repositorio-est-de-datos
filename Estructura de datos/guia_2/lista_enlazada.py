class nodo():
    dato = None
    siguiente = None

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

def agregar_al_final(nodo_inicial, dato):
    nuevo_nodo = nodo(dato)
    if nodo_inicial is None :
        nodo_inicial = nuevo_nodo
        return nodo_inicial
    temporal = nodo_inicial
    while temporal.siguiente :
        temporal = temporal.siguiente
    temporal.siguiente = nuevo_nodo
    return nodo_inicial

def agregar_al_inicio(nodo_inicial, dato):
    nuevo_nodo = nodo(dato)
    nuevo_nodo.siguiente = nodo_inicial
    return nuevo_nodo
def imprimir_lista(nodo):
    while nodo is not None:
        print(f"{nodo.dato}")
        nodo = nodo.siguiente

def existe(nodo, busqueda):
    while nodo is not None:
        if nodo.dato == busqueda:
            return True
        nodo = nodo.siguiente
    return False

def eliminar(nodo, busqueda):
    if nodo is None:
        return
    if nodo.dato == busqueda:
        return nodo.siguiente
    temporal = nodo
    while temporal.siguiente is not None:
        if temporal.siguiente.dato == busqueda:
            if temporal.siguiente.siguiente is not None:
                temporal.siguiente = temporal.siguiente.siguiente
            else:
                temporal.siguiente = None
                return nodo
        temporal = temporal.siguiente
    return nodo