"""
1. Crear un conjunto llamado Grupo conlos siguientes elementos: Miguel, Blanca, Mario, Andrés (tener en cuenta la ortografía)
2. Añade al grupo: Ana, Ramón, Marta, Eric y David.
3. Remueve a: Mario, Miguel, Ramón.
4. Valida si Mario se encuentra en el grupo, si se encuentra imprime un mensaje donde diga "Mario si se encuentra en el grupo", caso contrario "Mario no se encuentra en el grupo"
"""
Grupo = {"Miguel","Blanca","Mario","Andrés"}
print(f"Grupo actual:\n{Grupo}")
Grupo.add("Ana")
Grupo.add("Ramón")
Grupo.add("Marta")
Grupo.add("Eric")
Grupo.add("David")
print("\nGrupo reciente:\n",Grupo)
Grupo.remove("Mario")
Grupo.remove("Miguel")
Grupo.remove("Ramón")
print(f"\nGrupo final \n{Grupo}")
print("\n¿Mario se encuentra dentro del grupo?")
if ("Mario" in Grupo):
 print("Si, Mario si se encuentra dentro del grupo")
else:
 print("No, Mario no se encuentra dentro del grupo")



