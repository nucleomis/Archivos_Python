from servidor import *

x = leersimbolo('x')

#print(diff(sin(x**3-3*x),x))

class Interfaz:
    def __init__(self, ventana):
        #Inicializar la ventana con un título
        self.ventana=ventana
        self.ventana.title("Derivadas")

        #Agregar una caja de texto para que sea la pantalla de la calculadora
        self.pantalla=Text(ventana, state="disabled", width=40, height=3, background="gray4", foreground="white", font=("Helvetica",15))

        #Ubicar la pantalla en la ventana
        self.pantalla.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        #Inicializar la operación mostrada en pantalla como string vacío
        self.operacion=""

        #Crear los botones de la calculadora
        boton0=self.crearBoton(u"\u005E")
        boton1=self.crearBoton("x")
        boton2=self.crearBoton(u"\u221A")
        boton3=self.crearBoton("π")
        boton4=self.crearBoton("cos")
        boton5=self.crearBoton("(")
        boton6=self.crearBoton(")")
        boton7=self.crearBoton("sin")
        boton8=self.crearBoton(7)
        boton9=self.crearBoton(8)
        boton10=self.crearBoton(9)
        boton11=self.crearBoton(u"\u232B",escribir=False)
        boton12=self.crearBoton(4)
        boton13=self.crearBoton(5)
        boton14=self.crearBoton(6)
        boton15=self.crearBoton(u"\u00F7")
        boton16=self.crearBoton(1)
        boton17=self.crearBoton(2)
        boton18=self.crearBoton(3)
        boton19=self.crearBoton("*")
        boton20=self.crearBoton(".")
        boton21=self.crearBoton(0)
        boton22=self.crearBoton("+")
        boton23=self.crearBoton("-")
        boton24=self.crearBoton("=",escribir=False)
        boton25=self.crearBoton("tan")
        boton26=self.crearBoton("cls")
        
        #Ubicar los botones con el gestor grid
        botones=[boton0,boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton10, boton11, 
                 boton12, boton13, boton14, boton15, boton16, boton17,boton18,boton19,boton20,boton21,boton22,boton23,boton24,boton25,boton26]
        contador=0
        #Ubicar el último botón al principio
        
        for fila in range(1,7):
            for columna in range(4):
                botones[contador].grid(row=fila,column=columna)
                contador+=1
        botones[24].grid(row=8,column=2,columnspan=2)#=
        botones[25].grid(row=8,column=0,columnspan=2)#tan
        botones[26].grid(row=8,column=1,columnspan=2)
        return

    #Crea un botón mostrando el valor pasado por parámetro
    def crearBoton(self, valor, escribir=True, ancho=9, alto=1):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica",15), command=lambda:self.click(valor,escribir))

    #Controla el evento disparado al hacer click en un botón
    def click(self, texto, escribir):
        #Si el parámetro 'escribir' es True, entonces el parámetro texto debe mostrarse en pantalla. Si es False, no.
        if not escribir:
            #Sólo calcular si hay una operación a ser evaluada y si el usuario presionó '='
            if texto=="=" and self.operacion!="":
                #Reemplazar el valor unicode de la división por el operador división de Python '/'
                self.operacion=re.sub(u"\u00F7", "/", self.operacion)
                self.operacion=re.sub("π","pi",self.operacion)
                if self.operacion.__contains__(u"\u221A"):#convierto la raiz en sqr
                    self.operacion=re.sub(u"\u221A","sqrt",self.operacion)
                if self.operacion.__contains__(u"\u005E"):
                    self.operacion=self.operacion.replace(u"\u005E","**")
                if self.operacion.__contains__("0x"):
                    self.operacion=self.operacion.replace("0x","0*x")
                if self.operacion.__contains__("1x"):
                    self.operacion=self.operacion.replace("1x","1*x")
                if self.operacion.__contains__("2x"):
                    self.operacion=self.operacion.replace("2x","2*x")
                if self.operacion.__contains__("3x"):
                    self.operacion=self.operacion.replace("3x","3*x")
                if self.operacion.__contains__("4x"):
                    self.operacion=self.operacion.replace("4x","4*x")
                if self.operacion.__contains__("5x"):
                    self.operacion=self.operacion.replace("5x","5*x")
                if self.operacion.__contains__("6x"):
                    self.operacion=self.operacion.replace("6x","6*x")
                if self.operacion.__contains__("7x"):
                    self.operacion=self.operacion.replace("7x","7*x")
                if self.operacion.__contains__("8x"):
                    self.operacion=self.operacion.replace("8x","8*x")
                if self.operacion.__contains__("9x"):
                    self.operacion=self.operacion.replace("9x","9*x")
                    
                resultado=u"\u0192"+"'(x)= "+str(calculoderivada(self.operacion,x))
                
                #reemplazando resultado
                if resultado.__contains__("sqrt"):
                    resultado=resultado.replace("sqrt",u"\u221A")
                if resultado.__contains__("**"):
                    resultado=resultado.replace("**",u"\u005E")
                if resultado.__contains__("0*x"):
                    resultado=resultado.replace("0*x","0x")
                if resultado.__contains__("1*x"):
                    resultado=resultado.replace("1*x","1x")
                if resultado.__contains__("2*x"):
                    resultado=resultado.replace("2*x","2x")
                if resultado.__contains__("3*x"):
                    resultado=resultado.replace("3*x","3x")
                if resultado.__contains__("4*x"):
                    resultado=resultado.replace("4*x","4x")
                if resultado.__contains__("5*x"):
                    resultado=resultado.replace("5*x","5x")
                if resultado.__contains__("6*x"):
                    resultado=resultado.replace("6*x","6x")
                if resultado.__contains__("7*x"):
                    resultado=resultado.replace("7*x","7x")
                if resultado.__contains__("8*x"):
                    resultado=resultado.replace("8*x","8x")
                if resultado.__contains__("9*x"):
                    resultado=resultado.replace("9*x","9x")
                self.operacion=""
                self.limpiarPantalla()
                self.mostrarEnPantalla(resultado)
            #Si se presionó el botón de borrado, borra los caracteres
            elif texto==u"\u232B":
                aux = self.operacion
                self.limpiarPantalla()
                self.operacion = aux
                self.operacion= self.operacion[:-1]
                self.mostrarEnPantalla(self.operacion)
        #limpia la pantalla de ser necesario
        elif texto=="cls":
            self.limpiarPantalla()
        #Mostrar texto
        else:
            self.operacion+=str(texto)
            self.mostrarEnPantalla(texto)
        return

    #Borra el contenido de la pantalla de la calculadora
    def limpiarPantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state="disabled")
        self.operacion=""
        return

    #Muestra en la pantalla de la calculadora el contenido de las operaciones y los resultados
    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END, valor)
        self.pantalla.configure(state="disabled")
        return


ventana_principal=Tk()
calculadora=Interfaz(ventana_principal)
ventana_principal.mainloop()