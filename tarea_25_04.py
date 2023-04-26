import random

def matriz_random(filas,columnas):
    m = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(random.randint(0, 5))
        m.append(fila)
    return m

def suma_matriz(m1,m2):
    matriz_final = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            suma = m1 [i][j] + m2[i][j]
            fila.append(suma)
        matriz_final.append(fila)
    return matriz_final

def resta_matriz(m1,m2, m3):
    matriz_final = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            resta = m1 [i][j] + m2[i][j] - m3[i][j]
            fila.append(resta)
        matriz_final.append(fila)
    return matriz_final

filas = int(input("ingrese la cantidad de filas de la matriz: "))
columnas = int(input("ingrese la cantidad de columnas de la matriz: "))
print("creando la primera matriz aleatoria: ")
m1 = matriz_random(filas, columnas)
print(m1, "\n")
print("creando la segunda matriz aleatoria: ")
m2 = matriz_random(filas, columnas)
print(m2, "\n")

print("creando la tercera matriz aleatoria: ")
m3 = matriz_random(filas, columnas)
print(m3, "\n")

m_final_suma = suma_matriz(m1,m2)
print("\nLa matriz resultado de la suma es: ")
print(m_final_suma)

matriz_final = resta_matriz(m1, m2, m3)
print("la resta de las matrices da como resultado la siguiente matriz: ")
for fila in matriz_final:
    print(fila, "\n")