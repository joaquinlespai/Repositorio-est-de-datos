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

class Banco:
    def __init__(self):
        self.cola_clientes = cola()

    def agregar_cliente(self, nombre_cliente):
        self.cola_clientes.encolar(nombre_cliente)

    def atender_siguiente_cliente(self):
        if self.cola_clientes.esta_vacia():
            print("no hay clientes en espera")
        else:
            cliente = self.cola_clientes.desencolar()
            print("atendinedo cliente:", cliente)

    def mostar_clientes_en_espera(self):
        print("clientes en espera:", self.cola_clientes)


banco = Banco()


banco.agregar_cliente("cliente 1")
banco.agregar_cliente("cliente 2")
banco.agregar_cliente("cliente 3")
banco.agregar_cliente("cliente 4")
banco.agregar_cliente("cliente 5")
banco.agregar_cliente("cliente 6")

banco.mostar_clientes_en_espera()

banco.atender_siguiente_cliente()

banco.mostar_clientes_en_espera()