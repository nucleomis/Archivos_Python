#Almacenar en una lista de 5 elementos tuplas que guarden 
# el nombre de un pais y la cantidad de habitantes.
#Definir tres funciones, en la primera cargar la lista,
#  en la segunda imprimirla y en la tercera mostrar el nombre del país 
# con mayor cantidad de habitantes.

def cargar():
    lista=[]
    while len(lista)!=5:
        nompais=input("ingrese el nombre del pais: ")
        habitantes=int(input("ingrese la cantidad de habitantes: "))
        lista.append((nompais,habitantes))
    return lista

def imprimirla(paises):
    print("la lista queda conformada de la siguiente forma: ")
    for x in range (len(paises)):
        print(paises[x])
    

def mayorhabitantes(paises):
    cont=paises[0][1]
    for x in range(1,len(paises)):
        if paises[x][1]>cont:
            cont=paises[x][1]
            ma=paises[x][0]
    return ma
################################################################################

paises=cargar()
imprimirla(paises)

mayor=mayorhabitantes(paises)
print("El pais con la mayor cantidad de habitantes es: ",mayor)
for x in paises:
    print(x)

