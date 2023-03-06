import pygame
import random

def show_matrix(matrix,n):

    # Define los parámetros de la ventana
    cell_size = 400/n
    margin = 10

    # Define los colores
    background_color = (255, 255, 255) # Blanco

    # Crea la ventana
    n = len(matrix)
    screen_size = (n*cell_size + (n+1)*margin, n*cell_size + (n+1)*margin)
    screen = pygame.display.set_mode(screen_size)

    # Crea un diccionario para mapear valores únicos en la matriz a colores aleatorios
    unique_values = set(sum(matrix, []))
    color_dict = {}
    for value in unique_values:
        if(value == -1):
            # El color de la casilla vacía es negro
            color_dict[value] = (0, 0, 0) 
        elif(value == 0): 
            # El color de una casilla sin nada es blanco 
            color_dict[value] =(200,200,200)
        else:
            # El color de las casillas con números es aleatorio
            color_dict[value] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Dibuja la matriz en la ventana
    screen.fill(background_color)
    for x in range(n):
        for y in range(n):
            value = matrix[y][x]
            color = color_dict[value]
            rect = pygame.Rect((margin + cell_size) * x + margin, (margin + cell_size) * y + margin, cell_size, cell_size)
            pygame.draw.rect(screen, color, rect)
    pygame.display.flip()


    
