"""
Cree una variable llamada Tupla que contenga valores aleatorios e imprima:
1. El último elemento de la Tupla.
2. El número de elementos que contiene la Tupla (Longitud).
3. La posiciòn donde se encuentra el número 123 de la Tupla.
4. Una lista con los primeros 3 elementos de la Tupla
5. El elemento que hay en la posición 4 de la Tupla.
6. El número de veces que aparece el 4 en la Tupla
"""
Tupla = ("Hola",4,2,3,45,"Mundo",4,123,"Python",["Tupla","2021"])

print(f"Ùltimo elemento: \"{Tupla[-1]}\" es de tipo {type(Tupla[-1])}") 
print(f"Numero de elementos de la tupla {len(Tupla)}")
print(f"El número {Tupla[7]} se encuentra en la posiciòn '{Tupla.index(123)}'")
Lista = list(Tupla[0:3])
print(f"Lista con los 3 primeros elementos -> {Lista}")
print(f"El elementos de la posición 4 es: '{Tupla[4]}'")
print(f"El número 4 se repite '{Tupla.count(4)}' veces")

