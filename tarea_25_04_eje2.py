import random
from numpy import matrix
def matriz_random(filas,columnas):
    m = []
    for i in range(filas):
        filas = []
        for j in range(columnas):
            filas.append(random.randint(0, 10))
        m.append(filas)
    return m

filas = int(input("ingrese la cantidad de filas que tiene la matriz: "))
columnas = int(input("ingre la cantiad de columnas que tiene la matriz: "))
escalar = float(input("ingrese un escalar: "))

print("matriz: ")
for filas in matriz_random:
    print(filas)

matriz_resultado = [[elemento * escalar for elemento in fila] for fila in matrix]

print("matriz resultante: ")
for filas in matriz_resultado:
    print(filas)