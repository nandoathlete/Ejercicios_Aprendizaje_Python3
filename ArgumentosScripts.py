import sys
"""
Generar una tabla de multiplicar, enviando el valor desde el script por medio de la terminal.
"""
if len(sys.argv) == 2:
 try:
  Numero = int(sys.argv[1])
  print(f"\tTABLA DEL {Numero}\n")
  for i in range(0,11):
   print(f"\t{Numero} * {i} = {Numero*i}")
 except ValueError:
  print("El argumento a ingresar debe ser un número entero")
else:
 print("Debe ingresar un argumento")
 
  
 
