#Hacer un pseudocódigo que cuente las veces que aparece una determinada
#letra en una frase que se introduce por teclado
frase = input("ingrese una valorfrase o palabra ")
palabra = input("ingrese la letra a contar ")
print ("la cantidad de veces que se repite", palabra.upper(), "son", (frase.count(palabra)))