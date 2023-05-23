import random

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def generar_matriz_aleatoria(n):
    matriz = []
    for _ in range(n):
        fila = []
        for _ in range(n):
            fila.append(random.randint(1, 10))  # Generar valores aleatorios entre 1 y 10
        matriz.append(fila)
    return matriz

def crear_identidad(n):
    identidad = []
    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        identidad.append(fila)
    return identidad

def intercambiar_filas(matriz, fila1, fila2):
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]

def multiplicar_fila(matriz, fila, constante):
    for i in range(len(matriz[fila])):
        matriz[fila][i] *= constante

def sumar_filas(matriz, fila_destino, fila_origen, constante):
    for i in range(len(matriz[fila_destino])):
        matriz[fila_destino][i] += matriz[fila_origen][i] * constante

def invertir_matriz(matriz):
    n = len(matriz)
    identidad = crear_identidad(n)
    matriz_ampliada = [fila + identidad[i] for i, fila in enumerate(matriz)]

    for i in range(n):
        if matriz_ampliada[i][i] == 0:
            for j in range(i+1, n):
                if matriz_ampliada[j][i] != 0:
                    intercambiar_filas(matriz_ampliada, i, j)
                    break

        pivot = matriz_ampliada[i][i]
        multiplicar_fila(matriz_ampliada, i, 1/pivot)

        for j in range(i+1, n):
            factor = matriz_ampliada[j][i]
            sumar_filas(matriz_ampliada, j, i, -factor)

    for i in range(n-1, 0, -1):
        for j in range(i-1, -1, -1):
            factor = matriz_ampliada[j][i]
            sumar_filas(matriz_ampliada, j, i, -factor)

    matriz_inversa = [fila[n:] for fila in matriz_ampliada]
    return matriz_inversa

# Generar matriz aleatoria de tamaño 3 a 5
n = random.randint(3, 5)
matriz_original = generar_matriz_aleatoria(n)

# Imprimir matriz original
print("Matriz Original:")
imprimir_matriz(matriz_original)

# Invertir la matriz
matriz_inversa = invertir_matriz(matriz_original)

# Imprimir matriz inversa
print("Matriz Inversa:")
imprimir_matriz(matriz_inversa)