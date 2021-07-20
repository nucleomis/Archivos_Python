#Plantear una función que reciba un string en mayúsculas 
# o minúsculas y retorne la cantidad de letras 'a' o 'A'

def cont_de_A(v1):
    contador=v1.count("a")+v1.count("A")
    return contador

palabra=input("ingrese la palabra o frase")

print(cont_de_A(palabra))
