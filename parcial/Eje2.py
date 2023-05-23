import random
import numpy as np

matriz1 = np.random.randint(-10 , -4, size=(3,3))
matriz2 = np.random.randint(-10 , -4, size=(3,3))

print("La matriz 1 es:", matriz1)
print("La matriz 2 es:", matriz2)

Matrizresul = (matriz1 * matriz2)

print("La matriz resultante seria: ", Matrizresul)

MatrizI = np.identity(3)

print("La matriz identidad es:", MatrizI)

Matrizfinal = (Matrizresul * MatrizI)

print("La matriz final seria:", Matrizfinal)