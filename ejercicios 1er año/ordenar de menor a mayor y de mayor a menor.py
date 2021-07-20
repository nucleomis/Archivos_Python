#Cargar una lista con 5 elementos enteros. 
# Ordenarla de menor a mayor y mostrarla por pantalla,
# luego ordenar de mayor a menor e imprimir nuevamente.
enteros=[]
for x in range(5):
    lista=int(input("ingrese el numero"))
    enteros.append(lista)
for k in range(4):
    for x in range(4-k):
        if enteros[x]>enteros[x+1]:
            aux=enteros[x]
            enteros[x]=enteros[x+1]
            enteros[x+1]=aux
print(enteros)
for k in range(4):
    for x in range(4-k):
        if enteros[x]<enteros[x+1]:
            aux=enteros[x]
            enteros[x]=enteros[x+1]
            enteros[x+1]=aux
print(enteros)