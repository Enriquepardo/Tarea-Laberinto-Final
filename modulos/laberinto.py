from modulos.muros import *
FILA = 5 
COlUMNA = 7

def imprimir_laberinto(laberinto):
    for fila in laberinto:
        for celda in fila:
            print(celda, end=' ')
        print()
