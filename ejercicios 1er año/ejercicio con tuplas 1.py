#Confeccionar un programa con las siguientes funciones:
#1)Cargar una lista de 5 enteros.
#2)Retornar el mayor y menor valor de la lista mediante una tupla.
#Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.

def carga():
    v1=[]
    cont=0
    while cont!=5:
        lista=int(input("Ingrese numero: "))
        v1.append(lista)
        cont=cont+1
    tupla1=tuple(sorted(v1))
    tuplamayorymenor=(tupla1[4],tupla1[0])
    lista2=list(tupla1)
    print("imprimo la tupla generada a partir de la lista cargada: ", tupla1)
    print("retorno de una tupla con los valores mayor y menor de la lista ",tuplamayorymenor)
    print("descompuse la tupla y retorno el mayor y menor valor de la lista",lista2[4],lista2[0],sep="/ ")

carga()