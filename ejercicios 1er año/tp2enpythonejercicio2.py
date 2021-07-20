#Definir una lista por asignación con 5 enteros. 
# Mostrar por pantalla solo los elementos con valor iguales o superiores a 7.

numeros=[]
for x in range(5):
    lista=int(input("ingrese un numero: "))
    numeros.append(lista)
aux=[]
for x in range(5):
    if numeros[x]>=7:
        lista=numeros[x]
        aux.append(lista)
print("-----------------------------")
print("los numeros cargados mayores o iguales a 7 son:")
print(aux)