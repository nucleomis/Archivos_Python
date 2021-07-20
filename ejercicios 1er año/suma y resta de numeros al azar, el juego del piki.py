import random
import os
def limpiar():
    os.system("cls")

def bienvenida(puntaje,nivel,vidas):
    print("                                BIENVENIDO AL JUEGO DE LA SUMA")
    print("")
    print("        vidas: ",vidas,"             nivel: ",nivel,"       Puntaje: ", puntaje)
    print("")
    print("")


#---------------------------bloque principal---------------------------------------------------------

limpiar()
vidas=3
punt=0
nivel=1
bienvenida(punt,nivel,vidas)
num1=random.randint(1,99)
num2=random.randint(1,99)



while vidas!=0:
   #               nivel 1
    try:
        while nivel==1:
            limpiar()
            bienvenida(punt,nivel,vidas)
            print("escriba el resultado de la suma")
            suma=num1+num2
            print(num1,"+",num2)
            respuesta=int(input("Resultado: "))
            if respuesta==suma:
                print("muy bien!!! SIGUE ASI!!")
                punt=punt+1000
                continuar=input("continuar: ")
                if continuar=="":
                    limpiar()
                    bienvenida(punt,nivel,vidas)
                    num1=random.randint(1,99)
                    num2=random.randint(1,99)
            else:
                print("TE EQUIVOCASTE")
                vidas=vidas-1
                print("TE QUEDAN ",vidas," vidas")
                continuar=input("continuar: ")
                num1=random.randint(1,99)
                num2=random.randint(1,99)
                if continuar=="":
                    limpiar()
                    bienvenida(punt,nivel,vidas)
            if punt==10000:
                nivel=2
                break               
            if vidas==0:
                print("  TE QUEDASTE SIN VIDAS!!\n TU PUNTAJE ES DE: ",punt,"\n            FIN DEL JUEGO")
                salir=input("presione enter para salir: ")
                if salir=="":
                    limpiar()
                    break
    except:
        limpiar()
        print("APRETASTE LA TECLA QUE NO ERA\nVAMOS DE NUEVO")
        op=input("APRETA ENTER")
        limpiar()
 #---------------------------------------------------------
 #                 nivel2
    if vidas>=1 and nivel==2 and punt>=10000:
        try:
            limpiar()
            bienvenida(punt,nivel,vidas)
            print("EXELENTE!!! VAMOS A SUBIR EL NIVEL!!")
            cont=input("--presione enter--")
            limpiar()
            bienvenida(punt,nivel,vidas)
            num1=random.randint(100,1000)
            num2=random.randint(100,1000)
            while nivel==2:
                print("escriba el resultado de la suma")
                suma=num1+num2
                print(num1,"+",num2)
                respuesta=int(input("Resultado: "))
                if respuesta==suma:
                    print("MUY BIEN!!! SIGUE ASI")
                    punt=punt+1000
                    continuar=input("continuar: ")
                    if continuar=="":
                        limpiar()
                        bienvenida(punt,nivel,vidas)
                        num1=random.randint(100,1000)
                        num2=random.randint(100,1000)
                else:
                    print("TE EQUIVOCASTE")
                    vidas=vidas-1
                    print("TE QUEDAN ",vidas," vidas")
                    continuar=input("continuar: ")
                    num1=random.randint(100,1000)
                    num2=random.randint(100,1000)
                    if continuar=="":
                        limpiar()
                        bienvenida(punt,nivel,vidas)
                if punt==20000:
                    nivel=3               
                if vidas==0:
                    print("  TE QUEDASTE SIN VIDAS!!\n TU PUNTAJE ES DE: ",punt,"\n            FIN DEL JUEGO")
                    salir=input("presione enter para salir: ")
                    if salir=="":
                        limpiar()
                        break
        except:
            limpiar()
            print("APRETASTE LA TECLA QUE NO ERA\nVAMOS DE NUEVO")
            op=input("APRETA ENTER")
            limpiar()