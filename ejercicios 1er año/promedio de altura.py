#Cargar por teclado y almacenar en una lista las alturas de 5 personas 
# (valores float)
#Obtener el promedio de las mismas.
 #Contar cuántas personas son más altas que el promedio y cuántas más bajas.
altura=[]
menor=[]
mayor=[]
for x in range(5):
    ingreso=float(input("ingrese una altura: "))
    altura.append(ingreso)
    suma=sum(altura)
promedio=float(suma/5)
for x in range(5):
    if altura[x]<promedio:
        menor.append(altura[x])
    if altura[x]>promedio:
            mayor.append(altura[x])
print("las alturas ingresadas son: ", altura)
print("el promedio de las alturas es: ", promedio)
print("las alturas mayores al promedio son: ", mayor)
print("las alturas menores al promedio son: ", menor)