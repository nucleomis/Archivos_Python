#Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. Contar la cantidad de vocales. Crear un segundo string con toda la oración en minúsculas 
# para que sea más fácil disponer la condición que verifica que es una vocal.
frase=input("ingrese una frase o palabra: ")
minus=frase.lower()
a=minus.count("a")
e=minus.count("e")
i=minus.count("i")
o=minus.count("o")
u=minus.count("u")
total=a+e+i+o+u
print("la cantidad de vocales que ingreso son", total)
print (minus)  