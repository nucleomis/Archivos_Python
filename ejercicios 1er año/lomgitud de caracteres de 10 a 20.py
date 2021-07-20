print("ingrese una clave mayor a 10 caracteres y menor a 20")
a=input(": ")
b=len(a)
if b<20 and b>10:
    print ("correcto")
else:
    print ("error")
print ("longitud =", b)