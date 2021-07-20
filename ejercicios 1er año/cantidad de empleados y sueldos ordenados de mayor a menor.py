#Solicitar por teclado la cantidad de empleados que tiene la empresa. 
# Crear y cargar una lista con todos los sueldos de dichos empleados. 
# Imprimir la lista de sueldos ordenamos de menor a mayor.
cantemp=int(input("ingrese la cantidad de empleados:"))
empleados=[]
sueldos=[]
var=cantemp-1
for x in range(cantemp):
    listanom=input("ingrese el nombre del empleado: ")
    empleados.append(listanom)
    listasuel=int(input("ingrese el sueldo: "))
    sueldos.append(listasuel)
print("lista de empleados:")
for x in range(cantemp):
        print(empleados[x],":",sueldos[x])
for k in range(var):
    for x in range(k-1):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x+1]
            aux2=empleados[+1]
            sueldos[x]=sueldos[x+1]
            empleados[x]=empleados[x+1]
            sueldos[x+1]=aux
            empleados[x+1]=aux2
print("lista de empleados ordenados segun sueldo mayor a menor:")
for x in range(cantemp):
    print(empleados[x],":",sueldos[x])