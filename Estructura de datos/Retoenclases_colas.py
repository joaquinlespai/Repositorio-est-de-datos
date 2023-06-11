class cola:
    def __init__(self):
        self.items = []

    def encolar(self , x):
        self.items.append(x)

    def desencolar(self):
        if self.esta_vacia():
            raise ValueError("la cola esta vacia")
        return self.items.pop(0)
    def esta_vacia(self):
        return len(self.items) == 0
    
    def __str__(self):
        return str(self.items)
items = int(input("ingresa la cantidad de items que tienes: "))