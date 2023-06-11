class stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("el stack esta vacio")
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
pila = stack()

pila.push("libro 1")
pila.push("libro 2")
pila.push("libro 3")
pila.push("libro 4")
pila.push("libro 5")

print("el estado de la pila despues de apilar los libros: ", pila.stack)

libro = pila.pop()
print("libro sacado de la pila: ", libro)

libro = pila.pop()
print("libro sacado de la pila:", libro)

print("estado de la pila despues de sacar libros: ", pila.stack)