pacientes = []

for i in range(4):
    print(f"Ingrese la información del paciente {i+1}:")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    peso = float(input("Peso: "))
    sintomas = input("Síntomas (separados por comas): ").split(",")
    
    paciente = {
        "Nombre": nombre,
        "Edad": edad,
        "Peso": peso,
        "Síntomas": sintomas
    }
    
    pacientes.append(paciente)

nombre_buscar = input("Ingrese el nombre del paciente que desea buscar: ")

encontrado = False
for paciente in pacientes:
    if paciente["Nombre"] == nombre_buscar:
        print("Ficha personal del paciente:")
        print("Nombre:", paciente["Nombre"])
        print("Edad:", paciente["Edad"])
        print("Peso:", paciente["Peso"])
        print("Síntomas:", ", ".join(paciente["Síntomas"]))
        encontrado = True
        break

if not encontrado:
    print("No se encontró ningún paciente con ese nombre.")
