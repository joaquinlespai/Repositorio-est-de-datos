Frutas = ("manzana", "platano", "naranja", "manzana", "pera")
print("La cantidad de frutas es: ", Frutas)
Frutas_sin_repeticion = tuple(set(Frutas))
print("Frutas sin repetirce: ", Frutas_sin_repeticion)

NuevaFruta = input("Ingresa la nueva fruta que quieres ingresar: ")
Frutas = Frutas + (NuevaFruta,)
print("la nueva cantidad de frutas es: ", Frutas)

Frutas = list(Frutas)
Frutas.remove("platano")
frutas = tuple(Frutas)
print(Frutas)

Cantidad_Frutas = len(Frutas)
print(Cantidad_Frutas)