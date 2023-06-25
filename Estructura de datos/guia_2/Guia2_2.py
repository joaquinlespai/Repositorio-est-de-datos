class Cliente:
    def __init__(self,num,caja):
        self.num = num
        self.caja = caja

class Caja:
    def __init__(self,caja1):
        self.caja1 = caja1
        self.sig = None

class Lista_c:
    def __init__(self):
        self.first = None
        self.last = None
    def agregar(self,caja1):
        nuevacaja = Caja(caja1)
        if self.first is None:
            self.first = nuevacaja
            self.last = nuevacaja
            nuevacaja.sig = self.first
        else:
            nuevacaja.sig = self.first
            self.last.sig = nuevacaja
            self.last = nuevacaja

aux = Lista_c()
aux.agregar(1)