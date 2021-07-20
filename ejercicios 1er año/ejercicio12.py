#Hacer un pseudocódigo que imprima los números del 1 al 100. Que calcule la
#suma de los números pares, y por otro, los impares
a=0
conpar=0
conimpar=0
while a<100:
    a=a+1
    print (a)
    if (a%2==0):
        conpar=conpar+a
    else:
        conimpar=conimpar+a
print ("la suma de los pares es", conpar)
print ("la suma de los impares es", conimpar)