#Hacer un pseudocódigo que cuente las veces que aparece una determinada
#letra en una frase que se introduce por teclado
frase=input("Ingrese un palabra o frase:")
letra=input("ingrese la letra a buscar: ")
cantidad=0
x=0
while x<len(frase):
    if frase[x]==letra:
        cantidad=cantidad+1
    x=x+1
print("la cantidad de veces que se repite la letra", letra.upper(), "es: ", cantidad, "veces")