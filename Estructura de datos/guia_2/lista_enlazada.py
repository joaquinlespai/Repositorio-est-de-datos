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