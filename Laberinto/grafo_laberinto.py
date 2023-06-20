import pygame
import random

# Dimensiones del laberinto
ANCHO = 800
ALTO = 600
CELDA_SIZE = 40
ANCHO_CELDA = ANCHO // CELDA_SIZE
ALTO_CELDA = ALTO // CELDA_SIZE

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Inicializar Pygame
pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Laberinto")

# Clase para representar una celda del laberinto
class Celda:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.visitada = False
        self.paredes = [True, True, True, True]  # [arriba, derecha, abajo, izquierda]

    def dibujar(self):
        x = self.columna * CELDA_SIZE
        y = self.fila * CELDA_SIZE
        if self.paredes[0]:
            pygame.draw.line(ventana, BLANCO, (x, y), (x + CELDA_SIZE, y))
        if self.paredes[1]:
            pygame.draw.line(ventana, BLANCO, (x + CELDA_SIZE, y), (x + CELDA_SIZE, y + CELDA_SIZE))
        if self.paredes[2]:
            pygame.draw.line(ventana, BLANCO, (x + CELDA_SIZE, y + CELDA_SIZE), (x, y + CELDA_SIZE))
        if self.paredes[3]:
            pygame.draw.line(ventana, BLANCO, (x, y + CELDA_SIZE), (x, y))

    def obtener_vecinos(self):
        vecinos = []
        if self.fila > 0 and not celdas[self.fila - 1][self.columna].visitada:
            vecinos.append(celdas[self.fila - 1][self.columna])
        if self.columna < ANCHO_CELDA - 1 and not celdas[self.fila][self.columna + 1].visitada:
            vecinos.append(celdas[self.fila][self.columna + 1])
        if self.fila < ALTO_CELDA - 1 and not celdas[self.fila + 1][self.columna].visitada:
            vecinos.append(celdas[self.fila + 1][self.columna])
        if self.columna > 0 and not celdas[self.fila][self.columna - 1].visitada:
            vecinos.append(celdas[self.fila][self.columna - 1])
        return vecinos

    def quitar_pared(self, vecino):
        if self.fila == vecino.fila - 1:  # Vecino está arriba
            self.paredes[2] = False
            vecino.paredes[0] = False
        elif self.columna == vecino.columna + 1:  # Vecino está a la derecha
            self.paredes[3] = False
            vecino.paredes[1] = False
        elif self.fila == vecino.fila + 1:  # Vecino está abajo
            self.paredes[0] = False
            vecino.paredes[2] = False
        elif self.columna == vecino.columna - 1:  # Vecino está a la izquierda
            self.paredes[1] = False
            vecino.paredes[3] = False

# Crear las celdas del laberinto
celdas = [[Celda(fila, columna) for columna in range(ANCHO_CELDA)] for fila in range(ALTO_CELDA)]

# Generar el laberinto utilizando el algoritmo de búsqueda de profundidad primero
pila = [(0, 0)]
celdas[0][0].visitada = True

while pila:
    celda_actual = celdas[pila[-1][0]][pila[-1][1]]
    vecinos_no_visitados = [vecino for vecino in celda_actual.obtener_vecinos() if not vecino.visitada]
    if vecinos_no_visitados:
        vecino_aleatorio = random.choice(vecinos_no_visitados)
        vecino_aleatorio.visitada = True
        celda_actual.quitar_pared(vecino_aleatorio)
        pila.append((vecino_aleatorio.fila, vecino_aleatorio.columna))
    else:
        pila.pop()

# Función para dibujar el laberinto en la ventana
def dibujar_laberinto():
    ventana.fill(NEGRO)
    for fila in celdas:
        for celda in fila:
            celda.dibujar()
    pygame.display.update()

# Bucle principal del juego
jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    dibujar_laberinto()

# Salir del juego
pygame.quit()