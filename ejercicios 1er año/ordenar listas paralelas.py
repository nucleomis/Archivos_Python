#Crear y cargar en un lista los nombres de 5 países 
# y en otra lista paralela la cantidad de habitantes del mismo. 
# Ordenar alfabéticamente e imprimir los resultados.
#  Por último ordenar con respecto a la cantidad de habitantes
#  (de mayor a menor) e imprimir nuevamente.
paises=[]
cantpais=[]
for x in range(5):
    lista1=input("ingrese el pais: ")
    paises.append(lista1)
    lista2=int(input("ingrese la cantidad de habitantes: "))
    cantpais.append(lista2)
for k in range(4):
    for x in range(4-k):
        if paises[x]>paises[x+1]:
            aux=paises[x+1]
            aux2=cantpais[x+1]
            paises[x+1]=paises[x]
            cantpais[x+1]=cantpais[x]
            paises[x]=aux
            cantpais[x]=aux2
print("lista ordenada alfabeticamente: ")
for x in range(5):
    print(paises[x],":",cantpais[x])
for k in range(4):
    for x in range(4-k):
        if cantpais[x]>cantpais[x+1]:
            aux=paises[x+1]
            aux2=cantpais[x+1]
            paises[x+1]=paises[x]
            cantpais[x+1]=cantpais[x]
            paises[x]=aux
            cantpais[x]=aux2
print("lista ordenada segun cantidad de habitantes: ")
for x in range(5):
    print(paises[x],":",cantpais[x])