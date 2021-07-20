#Definir una lista y almacenar los nombres de 3 empleados.
#Por otro lado definir otra lista y almacenar en cada elemento una sublista con 
# los números de días del mes que el empleado faltó.
#Imprimir los nombres de empleados y los días que faltó.
#Mostrar los empleados con la cantidad de inasistencias.
#Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días.

nomemp=[]
diasfalta=[]
#cargo las listas
for k in range(3):
    lista=(input("ingrese el nombre del empleado: "))
    nomemp.append(lista)
    diasfalta.append([])
    cont=1
    veces=0
    while cont!=0:#mientras la opcion no sea 0 se van a ir agregando los valores
        veces=veces+1
        print("ingrese la vez ", veces," que falto en el mes: ")
        sublist=(input())
        diasfalta[k].append(sublist)
        cont=int(input("desea continuar?: 1-si   0-no: "))

#encuentro al empleado que falto menos dias
cantdiasf=[]

    
#listo los empleados y los dias que faltaron          
print("                      LA LISTA QUEDA CONFORMADA DE LA SIGUIENTE MANERA: ")
print("")
for x in range(3):
    print("EMPLEADO: ",nomemp[x])
    print("FALTAS: ",diasfalta[x])
    print("/////////////////////////////////////////")

print("-------------------------------------------")

#imprimo la lista de los empleados y la cantidad de dias que faltaron
print("LOS DIAS LA CANTIDAD DE DIAS QUE FALTRON FUERON: ")
for x in range(3):
    print("empleado:")
    print(nomemp[x])
    print("cantidad de dias: ")
    print(len(diasfalta[x]))
    print("////////////////////////////////////////////////")

print("                    EL O LOS EMPLEADOS QUE FALTARON MENOS DIAS FUERON")
print("")

#busco una variable para poder imprimir los empleados que tengan el mismo valor
menor=len(diasfalta[0])
for x in range(1,3):
    if len(diasfalta[x])<menor:
        menor=len(diasfalta[x])

#recorro la lista y comparo la variable para imprimir solo si son iguales
for x in range(3):
    if len(diasfalta[x])==menor:
        print(nomemp[x]," : faltas: ", len(diasfalta[x]))
        