#Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista.
#  Mostrar el nombre de persona menor en orden alfabético.
lista=[]
for x in range(5):
    nom=input("ingrese un nombre: ")
    lista.append(nom)
ini=lista[0]

ordenado=[]   
for x in range(1,5):
    if lista[x]<ini:
        ini=lista[x]
print( "la lista de nombres es:")
print(lista)
print("el primer nombre ordenado alfabeticamente es: ")
print(ini)