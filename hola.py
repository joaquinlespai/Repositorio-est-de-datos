import random

Filas = int(input("ingresa la cantidad de filas que tiene tu matriz: "))
Columnas = int(input("ingresa la cantidad de columnas de tu matriz: "))

M1 = [[random.randint(1 , 6) for j in range(Columnas)] for i in range(Filas)]
print("su primera matriz es :", M1)

M2 = [[random.randint(1 , 6) for j in range(Columnas)] for i in range(Filas)]
print("su segunda matriz es: ", M2)

Matriz_suma = [[M1[i][j]+ M2 [i][j]]for i in range(Filas) for j in range(Columnas)]
print("las matrices sumadas da: ", Matriz_suma)

Matriz_resta = [[M1[i][j]- M2[i][j]]for i in range(Filas)for j in range(Columnas)]
print("las matrices restadas da: ", Matriz_resta)

Matriz_multiplicada = 