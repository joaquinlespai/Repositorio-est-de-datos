import numpy as np
import random

matriz = np.random.randint(low=5, high=10, size=(3, 3))

print("La matriz es:", matriz)

determinante = np.linalg.det(matriz)

print("Y su determinante es:", determinante)