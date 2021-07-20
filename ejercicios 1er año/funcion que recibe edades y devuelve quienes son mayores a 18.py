#Confeccionar una función que reciba una serie de edades y me retorne la cantidad
# que son mayores o iguales a 18 (como mínimo se envía un entero a la función)

def mayor(*v2):
    cont=0
    for x in range(len(v2)):
        if v2[x]>=18:
            cont=cont+1
    return cont

edades=[]
op=int(input("ingrese el cuantas edades quiere agregar: "))
for x in range(op):
    lista=int(input("ingrese edad: "))
    edades.append(lista)
print(mayor(*edades))