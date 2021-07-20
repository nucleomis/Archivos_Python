#Crear una lista y almacenar los nombres de 5 países.
#  Ordenar alfabéticamente la lista e imprimirla
paises=[]
for x in range(5):
    lista=input("ingrese el pais: ")
    paises.append(lista)
print("paises:", paises)
for k in range(4):
    for x in range(4-k):
        if paises[x]>paises[x+1]:
            aux=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux
print("los paises ordenados alfabeticamente:")
print(paises)