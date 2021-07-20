#Definir por asignación una lista con 8 elementos enteros. 
#Contar cuantos de dichos valores almacenan un valor superior a 100.

valores=(18,200,10,400,90,80,5254,570)
total=0
x=0
while x<len(valores):
    if valores[x]>100:
        total=total+1
        print(valores[x])
    x=x+1
print("hay", total, "de valores superiores a 100")    