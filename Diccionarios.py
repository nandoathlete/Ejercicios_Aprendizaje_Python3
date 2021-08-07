"""
1. Añade un Diccionario tal y como se observa:
	[Clave] : [Valor]
	 'Perro': 'Dog'
	 'Gato' : 'Cat'
	 'Rana' : 'Frog'
2. Agrega los siguientes datos:
	[Clave] : [Valor]
       'Caballo': 'Horse'
	 'Vaca' : 'Cow'
3. Elimina del diccionario las claves Rana y Vaca.
4. Imprime el diccionario con su posición, Clave y Valor respectivo.
"""

def Agregar(Dict):
 Dict['Caballo'] = 'Horse'
 Dict['Vaca'] = 'Cow'
 return Dict

def Eliminar(Dict):
 del(Dict['Rana'])
 del(Dict['Vaca'])
 return Dict


def Visualizar(Dict):
 print("\nDICCIONARIO FINAL")
 for Clave, Valor in Dict.items():
  print(f"Clave: {Clave},     Valor: {Valor}")

Diccionario = {
	'Perro':'Dog',
	'Gato':'Cat',
	'Rana':'Frog',
}


print(f"\nDiccionario inicial:\n{Diccionario}\n")
Agregar_Valor = Agregar(Diccionario)
print(f"Diccionario agregar valores:\n{Agregar_Valor}\n")
Eliminar_Valor = Eliminar(Diccionario)
print(f"Diccionario eliminar valores:\n{Eliminar_Valor}\n")
Visualizar(Diccionario)






