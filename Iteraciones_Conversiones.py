"""
1. Pida al usuario que digite un número entero que esté entre 0 y 9.
2. Genere una lista que contenga los múltiplos del número entre 0 y 100.
"""
Multiplos = []
Numero = int(input("Digite un valor: "))
while (Numero < 0 or Numero > 9):
 Numero = int(input("Digite un valor: "))
Multiplos = list(range(0,101,Numero))

print(Multiplos)
