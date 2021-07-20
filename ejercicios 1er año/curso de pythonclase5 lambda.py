personas = [ {"nombre":"harry", "casa": "grffyndor"},{"nombre":"cho", "casa": "revenchaw"},
{"nombre": "draco", "casa": "slyterin"}
]


#con esta funcion retorno el valor de diccionario compuesto con el valor de nombre
def f(nombre):
    return nombre["nombre"]

#------------------------------------------------------------
print("\nimprimo y ordeno la lista usando la funcion tradicional")
personas.sort(key=f)#ordeno el diccionario compuesto con el indice que me retorna la funcion f

print(personas,"\n")

#-----------------------------------------------------------
#con la funcion lamda puedo obtener el indice sin crear una funcion de manera tradicional
print ("imprimo usando lamda pasando como referencia del indice casa")
personas.sort(key= lambda persona : persona["casa"])

print(personas)