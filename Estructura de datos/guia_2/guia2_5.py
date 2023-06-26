class empleados:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
        self.subordinado = []

    def agregarsub(self, empleado):
        self.subordinado.append(empleado)
    
    def eliminarempleado(self, empleado):
        self.subordinado.remove(empleado)

    def __str__(self):
        return f"{self.nombre, self.cargo}"
    
nombre = int(input("ingrese su nombre:"))
cargo = "mantencion"