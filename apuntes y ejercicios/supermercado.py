class productos:
    def __init__(self, producto):
        self.producto = producto
    def __str__(self):
        return str(self.producto)
    
class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, x):
        self.items.append(x)

    def descolar(self):
        if self.esta_vacia():
            raise ValueError("la cola esta vacia")
        return self.items.pop(0)
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def invertir_cola(self):
        self.items = self.items[::-1]
    
    def __str__(self):
        for i in self.items:
            print(i)
        return ""
    
Supermercado = Cola()

Produ1 = productos("Jabon")
Produ2 = productos("pasta de dientes")
Produ3 = productos("galletas")
Produ4 = productos("condones")
Produ5 = productos("aceite yes")
Produ6 = productos("aceite extravirgen")

Supermercado.encolar(Produ1)
Supermercado.encolar(Produ2)
Supermercado.encolar(Produ3)
Supermercado.encolar(Produ4)
Supermercado.encolar(Produ5)
Supermercado.encolar(Produ6)

print(Supermercado)

Supermercado.descolar()

print(Supermercado)

Supermercado.invertir_cola
print(Supermercado)