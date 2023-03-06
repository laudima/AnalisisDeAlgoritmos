import random
import pygame 
from matriz import show_matrix

"""
Problema: Se desea adoquinar una cuadrícula de m x m con adoquines en forma de L de tamaño 1 x 2.
En la cuadrícula existirá un espacio vacío que no podrá ser ocupado por ningún adoquín.
"""

#Leemos el tamaño de la matriz (la entrada es una potencia de 2)
n = int(input())

#Creamos la matriz 
matriz = [[0 for i in range(n)] for j in range(n)]

#Obtenemos una casilla al azar
casilla_i = random.randint(0,n-1)
casilla_j = random.randint(0,n-1)

#Marcamos la casilla como ocupada
matriz[casilla_i][casilla_j] = -1 



"""
Resolveremos el problema de forma recursiva, 
para ello, definimos una función que recibe como parámetros
la matriz, el tamaño de la matriz, la fila y columana donde empieza el cuadrado, y 
la fila y la columna de la casilla vacía. 

Primero colocamos una pieza en el centro de manera que dejamos un hueco en el cuadrante 
que se encontraba la casilla vacía. De esta manera los 4 cuadrantes ahora tienen un hueco. 
Aplicamos la  función recursivamente sobre cada uno de los cuadrantes. 
"""
ladrillo = 0 #Contador de ladrillos
global matrices 
matrices = []

#Imprimimos la matriz
def imprimir(matriz):
    for i in range(n):
        for j in range(n):
            print(matriz[i][j], end=" ")
        print()

def pintar(centro_i, centro_j, x1, y1, x2, y2, x3, y3): 
    global ladrillo 
    ladrillo+=1
    matriz[centro_i + x1][centro_j + y1] = ladrillo
    matriz[centro_i + x2][centro_j + y2] = ladrillo
    matriz[centro_i + x3][centro_j + y3] = ladrillo

def resolver(matriz, n,x,y, casilla_i, casilla_j):
    
    global ladrillo
    #Si el tamaño de la matriz es 2, entonces no podemos dividirla más
    if n == 2:
        #Recorremos la matriz
        ladrillo+=1 
        for k in range(2):
            for l in range(2):
                #Si la casilla no está ocupada, la marcamos como ocupada
                if matriz[x+k][y+l] == 0:
                    matriz[x+k][y+l] = ladrillo 

        print("Ladrillo :", ladrillo)
        imprimir(matriz)
        print()

        show_matrix(matriz,len(matriz)) 
        pygame.time.wait(1000)

        return matriz

    #Si el tamaño de la matriz es mayor que 2, entonces la dividimos en 4 submatrices
    else:
        #Obtenemos la mitad del tamaño de la matriz
        mitad = n//2
        
        #Obtenemos el espacio ocupado 
        for i in range(x,x+n):
            for j in range(y,y+n): 
                if(matriz[i][j] != 0): 
                    casilla_i = i 
                    casilla_j = j 

        centro_i = x+int(mitad) 
        centro_j = y+int(mitad)

        #Si la casilla vacía está en el cuarto cuadrante, entonces rellenamos
        if(casilla_i >= x+mitad and casilla_j >= y+mitad):
            #Podemos un ladrillo en el centro de la matriz donde no este la casilla vacía   
            pintar(centro_i, centro_j, -1, 0, 0, -1, -1,-1)
        
        #Si la casilla vacía está en el primer cuadrante
        elif(casilla_i < x+mitad and casilla_j < y+mitad):
            pintar(centro_i, centro_j, 0, -1, 0, 0, -1, 0)
        
        #Si la casilla vacía está en el segundo cuadrante
        elif(casilla_i < x+mitad and casilla_j >= y+mitad):
            pintar(centro_i, centro_j, 0, -1, 0, 0, -1, -1)
        
        #Si la casilla vacía está en el tercer cuadrante
        elif(casilla_i >= x+mitad and casilla_j < y+mitad):
            pintar(centro_i, centro_j, -1, 0, 0, 0, -1, -1)
        
        print("Ladrillo :", ladrillo)
        imprimir(matriz)
        print()

        show_matrix(matriz,len(matriz)) 
        pygame.time.wait(1000)

        matrices.append(matriz)

        #Llamamos a la función recursivamentes
        resolver(matriz, mitad, x+int(mitad), y, casilla_i, casilla_j) #Segundo cuadrante
        resolver(matriz, mitad, x, y, casilla_i, casilla_j) #Primer cuadrante
        resolver(matriz, mitad, x, y+int(mitad), casilla_i, casilla_j) #Tercer cuadrante
        resolver(matriz, mitad, x+int(mitad), y+int(mitad), casilla_i, casilla_j) #Cuarto cuadrante
        

        return matriz 


#Llamamos a la función
pygame.init()
matriz = resolver(matriz, n, 0, 0,casilla_i, casilla_j)

# Espera a que se cierre la ventana
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()




