import random
import numpy as np

filas = int(input("ingresa la cantidad de filas que tendra: "))
columnas = int(input("ingresa la cantiad de columnas que tendra: "))

Ma = [[random.randint(1, 5) for j in range(columnas)] for i in range(filas)]

Mai = np.linalg.inv(Ma) 

Mul = np.matmul(Ma, Mai)

Identity = np.eye(filas, columnas)

if np.allclose(Mul, Identity):
    print("La propiedad A × A^-1 = I se cumple.")
else:
    print("La propiedad A × A^-1 = I no se cumple.")