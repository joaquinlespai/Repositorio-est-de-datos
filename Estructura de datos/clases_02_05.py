import random

filas = int(input("ingrese la cantidad de filas: "))
columnas = int(input("ingrese la cantidad de columnas: "))
filas2 = int(input("ingrese la cantidad de filas: "))
columnas2 = int(input("ingrese la cantidad de columnas: "))

matriz1 = [[random.randrange(1 , 5)for j in range(columnas)]for i in range(filas)]
matriz2 = [[random.randrange(1 , 5)for j in range(columnas2)]for i in range(filas2)]
