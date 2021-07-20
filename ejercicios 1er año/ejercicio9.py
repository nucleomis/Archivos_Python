a=int(input("ingrese un valor"))
if a>99 and a<1000:
    print("el numero tiene 3 cifras")
else:
    if a<100 and a>9:
        print("el numero tiene 2 cifras")
    else:
        if a<10:
            print ("el numero tiene 1 cifra")
        else:
            print ("error el numero supera las 3 cifras")    
    