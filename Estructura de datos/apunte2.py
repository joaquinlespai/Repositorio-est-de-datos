import numpy as np


print("ingresando los elemntos de la matris 1 :")
m1 = np.zeros((filas ,columnas))
for i in range(filas):
    for j in range(columnas):
        elem = int(input(f"ingrese el elemento [{i}][{j}]"))
        m1[i][j] = elem


print("ingresando los elemntos de la matris 2 :")
m2 = np.zeros((filas ,columnas))
for i in range(filas):
    for j in range(columnas):
        elem = int(input(f"ingrese el elemento [{i}][{j}]"))
        m2[i][j] = elem

m_final_suma = suma(m1,m2)
print("\nLa matriz resultado de la suma es: ")
print(m_final_suma)

m_final_resta = resta(m1,m2)
print("\nLa matriz resultado de la resta es: ")
print(m_final_resta)