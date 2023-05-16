import random
import numpy as np

filas = int(input("ingresa la cantidad de filas que usaras: "))
columnas = int(input("ingresa la cantidad de filas que usaras: "))

matriz1 = [[random.randint(1, 5) for j in range(columnas)] for i in range(filas)]
matriz2 = [[random.randint(1, 5) for j in range(columnas)] for i in range(filas)]

matrizfinal = [[matriz1[i][j] + matriz2[i][j] ] for i in range(filas) for j in range(columnas)]

print("matriz resultante", matrizfinal)

escalar = int(input("ingresa un numero escalar del 1 al 10: "))
matrizpor= np.array(matrizfinal) * escalar
print("el resultado es", matrizpor)

filas3= int(input("ingrese la cantidad de filas de su nueva matriz: "))
columnas3 = int(input("ingrese la cantidad de columnas de su nueva matriz:"))
matriz3 = [filas3 , columnas3]

matrizmax = np.array(matrizpor) * matriz3
print("su matriz final es: ", matrizmax)