#Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados 
# (4 por la mañana y 4 por la tarde) 
# Confeccionar un programa que permita almacenar 
# los sueldos de los empleados agrupados en dos listas.
# Imprimir las dos listas de sueldos.
tarde=[]
manana=[]
for x in range(4):
    starde=float(input("ingrese los sueldos del turno tarde: "))
    tarde.append(starde)
for x in range(4):
    smanana=float(input("ingrese los sueldos del turno manana: "))
    manana.append(smanana)
print("la lista de los sueldo de la tarde son:")
print(tarde)
print("la lista de los sueldos de la mañana son: ")
print(manana)