#Crear y cargar dos listas con los nombres de 5 productos en una 
# y sus respectivos precios en otra. Definir dos listas paralelas. 
# Mostrar cuantos productos tienen un precio mayor 
# al primer producto ingresado.
productos=[]
precios=[]
for x in range(5):
    listpro=input("ingrese un producto: ")
    productos.append(listpro)
    lispre=input("ingrese un precio: ")
    precios.append(lispre)
compara=precios[0]
contador=0
for x in range(1,5):
    if compara<precios[x]:
        contador=contador+1
print("hay ",contador, "productos superiores al primer producto cargado: ",productos[0])