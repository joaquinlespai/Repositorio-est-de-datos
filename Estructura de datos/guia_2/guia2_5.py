class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
        self.empleados = []

    def nuevo_empleado(self, empleado):
        self.empleados.append(empleado)

    def despedir_empleado(self, empleado):
        self.empleados.remove(empleado)

    def info_empleado(self):
        return self.empleados

    def __str__(self):
        return f"{self.nombre}, {self.cargo}"


class JerarquiaEmpleados:
    def __init__(self):
        self.raiz = None

    def mostrar_subordinados(self, empleado, nivel):
        print("  " * nivel + "- " + str(empleado))
        for subordinado in empleado.info_empleado():
            self.mostrar_subordinados(subordinado, nivel + 1)

    def buscar_empleado(self, nombre):
        return self.buscar_en_subordinados(self.raiz, nombre)

    def buscar_en_subordinados(self, empleado, nombre):
        if empleado.nombre == nombre:
            return empleado
        for subordinado in empleado.info_empleado():
            resultado = self.buscar_en_subordinados(subordinado, nombre)
            if resultado:
                return resultado
        return None

    def obtener_jefe_directo(self, nombre):
        return self.buscar_jefe_en_subordinados(self.raiz, nombre)

    def buscar_jefe_en_subordinados(self, empleado, nombre):
        for subordinado in empleado.info_empleado():
            if subordinado.nombre == nombre:
                return empleado
            resultado = self.buscar_jefe_en_subordinados(subordinado, nombre)
            if resultado:
                return resultado
        return None

    def agregar_empleado(self, nombre, cargo, jefe_nombre):
        empleado = Empleado(nombre, cargo)

        if self.raiz is None:
            self.raiz = empleado
        else:
            jefe = self.buscar_empleado(jefe_nombre)
            if jefe:
                jefe.nuevo_empleado(empleado)
            else:
                print("El jefe especificado no existe en la jerarquía.")

    def eliminar_empleado(self, nombre):
        empleado = self.buscar_empleado(nombre)
        if empleado:
            jefe = self.obtener_jefe_directo(nombre)
            if jefe:
                jefe.despedir_empleado(empleado)
                for subordinado in empleado.info_empleado():
                    jefe.nuevo_empleado(subordinado)
                empleado.empleados = []
            else:
                self.raiz = None
        else:
            print("El empleado especificado no existe en la jerarquía.")

jerarquia = JerarquiaEmpleados()

jerarquia.agregar_empleado("Juan", "CEO", "")
jerarquia.agregar_empleado("María", "CFO", "Juan")
jerarquia.agregar_empleado("Pedro", "Gerente de Ventas", "Juan")
jerarquia.agregar_empleado("Ana", "Gerente de Marketing", "María")
jerarquia.agregar_empleado("Luis", "Supervisor de Ventas", "Pedro")
jerarquia.agregar_empleado("Laura", "Especialista en Marketing", "Ana")

jerarquia.mostrar_subordinados(jerarquia.raiz, 0)
print("----------------------")

jerarquia.eliminar_empleado("Pedro")

jerarquia.mostrar_subordinados(jerarquia.raiz, 0)
print("----------------------")

resultado_busqueda = jerarquia.buscar_empleado("María")
if resultado_busqueda:
    print("Empleado encontrado:", resultado_busqueda)
else:
    print("Empleado no encontrado.")

print("----------------------")

resultado_busqueda = jerarquia.buscar_empleado("Luis")
if resultado_busqueda:
    print("Empleado encontrado:", resultado_busqueda)
else:
    print("Empleado no encontrado.")

print("----------------------")

resultado_jefe = jerarquia.obtener_jefe_directo("Ana")
if resultado_jefe:
    print("Jefe directo:", resultado_jefe)
else:
    print("No se encontró el jefe directo.")
