"""
Crear una matriz con datos enteros, donde se deberá
modificar el contenido dinámicamente, sustituyendo todos
los pares por 0 y los impares por 1.
"""
import numpy as np

Array1 = np.array(range(5))
Array2 = np.array(range(6,11))
Matriz = np.array([Array1, Array2])

def Valores(Matriz):
 print("\nValores de la matriz")
 for i in Matriz:
  print(i)
 print()

def Forma1(Matriz):
 print("1. Recorriendo matriz forma 1")
 for i in Matriz:
  for j in i:
   print(j, end = ' ')
 print()
 
def Forma2(Matriz):
 print("\n1. Recorriendo matriz forma 2")
 for i in range(len(Matriz)):
  for j in range(len(Matriz[i])):
   print(Matriz[i][j])
 print()
 
def Solucion(Matriz):
 print("Solución ejercicio de codificación: ")
 x = -1
 y = 0
 for i in Matriz:
  x += 1
  for j in i:
   if (j%2 == 0):
    Matriz[x][y] = 0
    y += 1
   else:
    Matriz[x][y] = 1
    y += 1
  y = 0
 return Matriz

Valores(Matriz)
Forma1(Matriz)
Forma2(Matriz)
print(f"Matriz codificada \n {Solucion(Matriz)}")
