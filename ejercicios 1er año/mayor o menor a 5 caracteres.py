#Definir una lista que almacene por asignación los nombres de 5 personas. 
# Contar cuantos de esos nombres tienen 5 o más caracteres.
lista=[]
mayor=[]
menor=[]
for x in range(8):
    nombres=input("ingrese el nombre: ")
    lista.append(nombres)
    if len(nombres)<5:
        menor.append(nombres)
    if len(nombres)>=5:
        mayor.append(nombres)
print("la lista de nobres son: ", lista)        
print("la lista de nombres superiores a 5 caracteres son:", mayor)
print("la lista de nombres menores a 5 caracteres son: ", menor)
print("el total de nombres mayores a 5 caracteres es: ", len(mayor))
print("el total de nombres inferiores a 5 caracteres es:", len(menor))