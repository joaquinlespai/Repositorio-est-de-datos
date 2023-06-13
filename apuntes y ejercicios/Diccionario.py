paciente = {}

for i in range(4):
    nombre = input("ingrese nombre del paciente: ")
    edad = int(input("ingrese edad del pacinete: "))
    peso = float(input("ingtrese peso del paciente: "))
    sintomas = [input("sintomas: "),input(""),input("")]

    paciente[nombre] = {
        "edad" : edad,
        "peso" : peso,
        "sintomas" : sintomas
    }


print("Información del pacinete:")
for paciente, info in paciente.items():
    if input("ingrese paciente que busca: ") == paciente: 
        print(f"paciente: {paciente}")
        print(f"edad: {info['edad']}")
        print(f"peso: {info['peso']}")
        print(f"sintomas: {info['sintomas']}")
        print()
    else:
        print("no se encuentra tal paciente")