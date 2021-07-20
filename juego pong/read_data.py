import sys, random, pygame,admin_archivos
from pygame.version import ver

pygame.init()

ventana= pygame.display.set_mode((750,500))


pygame.display.set_caption('Pong:')

blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0,255,0)
azul = (0, 0, 255)
naranja = (255,125,0)

todo_sprites = pygame.sprite.Group()

#-----------------------------------------------------------------------------------------------
class Grilla(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([670, 80])
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0



class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.recuadro = Grilla ()
        self.recuadro2 = Grilla()
        self.paradeo = random.randrange(1,3) 
        if self.paradeo==1:
            self.color = rojo
        else:
            self.color = blanco

        self.font1 = pygame.font.SysFont('Comic Sans MS', 80)
        self.text1 = self.font1.render('Jugador', False, self.color)
        self.textRect1 = self.text1.get_rect()
        self.textRect1.center = (750 // 2, 125)
        ventana.blit(self.text1, self.textRect1)

        self.font2 = pygame.font.SysFont('Arial', 30)
        self.text2 = self.font2.render(' Nombre:  ', False, blanco)
        self.textRect2 = self.text2.get_rect()
        self.textRect2.center = (750 // 5, 325)
        ventana.blit(self.text2, self.textRect2)


    def correr_menu_carga(self):
        self.nombre = ""
        self.cont=10
        self.recuadro.rect.x = 200
        self.recuadro.rect.y = 280
        self.recuadro2.rect.x =200
        self.recuadro2.rect.y =380
        self.col =0
        self.contador = 0
        self.tamaño = 25
        self.aparecer = negro
        self.guardado = negro
        pygame.draw.rect(self.recuadro.image,self.col,(0,0,350,70),2)
        pygame.draw.rect(self.recuadro2.image,self.col,(0,0,350,70),2)
        while True:
            ventana.fill(negro)
            self.contador +=1
            pygame.time.delay(80)
            self.par = random.randrange(1,4)
            if self.contador<20:
                self.tamaño += 1
            if self.contador >20:
                self.tamaño = self.tamaño - 1
            if self.contador==40:
                self.contador=0
            self.col = azul

            pygame.draw.rect(self.recuadro.image,self.col,(0,0,350,70),2) 
            pygame.draw.rect(self.recuadro2.image,False,(0,0,350,70),2)
            todo_sprites.add(self.recuadro,self.recuadro2)
            todo_sprites.draw(ventana)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit()
            
            self.tecla = pygame.key.get_pressed()
            #permitir el ingreso de 24 caracteres
            #opcion evento para salir de juego
            if self.cont<28:
                if self.tecla[pygame.K_ESCAPE]:
                    if admin_archivos.verificar_jugador(self.nombre):
                        self.aparecer = rojo
                    else:
                        if self.cont >10:
                            self.guardado = verde
                            admin_archivos.cargar_jugador(self.nombre)
                                    
                if self.guardado == verde and self.tecla[pygame.K_SPACE]:
                    return False

                if self.tecla[pygame.K_q]:
                    self.nombre += "q"
                    self.cont += 1
                if self.tecla[pygame.K_w]:
                    self.nombre +="w"
                if self.tecla[pygame.K_e]:
                    self.nombre +="e"
                    self.cont += 1
                if self.tecla[pygame.K_r]:
                    self.nombre +="r"
                    self.cont += 1
                if self.tecla[pygame.K_t]:
                    self.nombre +="t"
                    self.cont += 1
                if self.tecla[pygame.K_y]:
                    self.nombre +="y"
                    self.cont += 1
                if self.tecla[pygame.K_u]:
                    self.nombre +="u"
                    self.cont += 1
                if self.tecla[pygame.K_i]:
                    self.nombre +="i"
                    self.cont += 1
                if self.tecla[pygame.K_o]:
                    self.nombre +="o"
                    self.cont += 1
                if self.tecla[pygame.K_p]:
                    self.nombre +="p"
                    self.cont += 1
                if self.tecla[pygame.K_a]:
                    self.nombre +="a"
                    self.cont += 1
                if self.tecla[pygame.K_s]:
                    self.nombre +="s"
                    self.cont += 1
                if self.tecla[pygame.K_d]:
                    self.nombre +="d"
                    self.cont += 1
                if self.tecla[pygame.K_f]:
                    self.nombre +="f"
                    self.cont += 1
                if self.tecla[pygame.K_g]:
                    self.nombre +="g"
                    self.cont += 1
                if self.tecla[pygame.K_h]:
                    self.nombre +="h"
                    self.cont += 1
                if self.tecla[pygame.K_j]:
                    self.nombre +="j"
                    self.cont += 1
                if self.tecla[pygame.K_k]:
                    self.nombre +="k"
                    self.cont += 1
                if self.tecla[pygame.K_l]:
                    self.nombre +="l"
                    self.cont += 1
                if self.tecla[pygame.K_z]:
                    self.nombre +="z"
                    self.cont += 1
                if self.tecla[pygame.K_x]:
                    self.nombre +="x"
                    self.cont += 1
                if self.tecla[pygame.K_c]:
                    self.nombre +="c"
                    self.cont += 1
                if self.tecla[pygame.K_v]:
                    self.nombre +="v"
                    self.cont += 1
                if self.tecla[pygame.K_b]:
                    self.nombre +="b"
                    self.cont += 1
                if self.tecla[pygame.K_n]:
                    self.nombre +="n"
                    self.cont += 1
                if self.tecla[pygame.K_m]:
                    self.nombre +="m"
                    self.cont += 1
                if self.tecla[pygame.K_SPACE]:
                    self.nombre +=" "
                    self.cont += 1
                if self.tecla[pygame.K_BACKSPACE]:
                    if self.cont>10:
                        self.nombre = self.nombre[0:len(self.nombre)-1]
                        self.cont += -1
                        self.aparecer = negro
            if self.cont>=28 and self.tecla[pygame.K_BACKSPACE]:
                self.cont +=-1
                self.nombre = self.nombre[0:len(self.nombre)-1]
            self.font3 = pygame.font.SysFont('Arial', 30)
            self.text3 = self.font3.render(str(self.nombre), False, blanco)
            self.textRect3 = self.text3.get_rect()
            self.textRect3.center = (750 // 2, 325)
            ventana.blit(self.text3, self.textRect3)

            self.font4 = pygame.font.SysFont('Arial', self.tamaño)
            self.text4 = self.font4.render(' Escape para aceptar  ', False, verde)
            self.textRect4 = self.text4.get_rect()
            self.textRect4.center = (750 // 2, 400)
            ventana.blit(self.text4, self.textRect4)

            self.font5 = pygame.font.SysFont('Arial', 30)
            self.text5 = self.font5.render('ya existe el jugador', False, self.aparecer)
            self.textRect5 = self.text5.get_rect()
            self.textRect5.center = (750 // 2, 250)
            ventana.blit(self.text5, self.textRect5)

            self.font6 = pygame.font.SysFont('Arial', 30)
            self.text6 = self.font6.render('Guardado!! "ESPACIO" para volver al menu', False, self.guardado)
            self.textRect6 = self.text6.get_rect()
            self.textRect6.center = (750 // 2, 370)
            ventana.blit(self.text6, self.textRect6)


            Jugador().__init__()
            pygame.display.update()

    def login(self):
        self.nombre = ""
        self.cont=10
        self.recuadro.rect.x = 200
        self.recuadro.rect.y = 280
        self.recuadro2.rect.x =200
        self.recuadro2.rect.y =380
        self.col =0
        self.contador = 0
        self.tamaño = 25
        self.aparecer = negro
        self.guardado = negro
        pygame.draw.rect(self.recuadro.image,self.col,(0,0,350,70),2)
        pygame.draw.rect(self.recuadro2.image,self.col,(0,0,350,70),2)
        while True:
            ventana.fill(negro)
            self.contador +=1
            pygame.time.delay(80)
            self.par = random.randrange(1,4)
            if self.contador<20:
                self.tamaño += 1
            if self.contador >20:
                self.tamaño = self.tamaño - 1
            if self.contador==40:
                self.contador=0
            self.col = azul

            pygame.draw.rect(self.recuadro.image,self.col,(0,0,350,70),2) 
            pygame.draw.rect(self.recuadro2.image,False,(0,0,350,70),2)
            todo_sprites.add(self.recuadro,self.recuadro2)
            todo_sprites.draw(ventana)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit()
            
            self.tecla = pygame.key.get_pressed()
            #permitir el ingreso de 24 caracteres
            #opcion evento para salir de juego
            if self.cont<28:
                if self.tecla[pygame.K_ESCAPE]:
                    if admin_archivos.verificar_jugador(self.nombre):
                        return True, self.nombre
                    else:
                        self.aparecer = rojo    

                if self.tecla[pygame.K_q]:
                    self.nombre += "q"
                    self.cont += 1
                if self.tecla[pygame.K_w]:
                    self.nombre +="w"
                if self.tecla[pygame.K_e]:
                    self.nombre +="e"
                    self.cont += 1
                if self.tecla[pygame.K_r]:
                    self.nombre +="r"
                    self.cont += 1
                if self.tecla[pygame.K_t]:
                    self.nombre +="t"
                    self.cont += 1
                if self.tecla[pygame.K_y]:
                    self.nombre +="y"
                    self.cont += 1
                if self.tecla[pygame.K_u]:
                    self.nombre +="u"
                    self.cont += 1
                if self.tecla[pygame.K_i]:
                    self.nombre +="i"
                    self.cont += 1
                if self.tecla[pygame.K_o]:
                    self.nombre +="o"
                    self.cont += 1
                if self.tecla[pygame.K_p]:
                    self.nombre +="p"
                    self.cont += 1
                if self.tecla[pygame.K_a]:
                    self.nombre +="a"
                    self.cont += 1
                if self.tecla[pygame.K_s]:
                    self.nombre +="s"
                    self.cont += 1
                if self.tecla[pygame.K_d]:
                    self.nombre +="d"
                    self.cont += 1
                if self.tecla[pygame.K_f]:
                    self.nombre +="f"
                    self.cont += 1
                if self.tecla[pygame.K_g]:
                    self.nombre +="g"
                    self.cont += 1
                if self.tecla[pygame.K_h]:
                    self.nombre +="h"
                    self.cont += 1
                if self.tecla[pygame.K_j]:
                    self.nombre +="j"
                    self.cont += 1
                if self.tecla[pygame.K_k]:
                    self.nombre +="k"
                    self.cont += 1
                if self.tecla[pygame.K_l]:
                    self.nombre +="l"
                    self.cont += 1
                if self.tecla[pygame.K_z]:
                    self.nombre +="z"
                    self.cont += 1
                if self.tecla[pygame.K_x]:
                    self.nombre +="x"
                    self.cont += 1
                if self.tecla[pygame.K_c]:
                    self.nombre +="c"
                    self.cont += 1
                if self.tecla[pygame.K_v]:
                    self.nombre +="v"
                    self.cont += 1
                if self.tecla[pygame.K_b]:
                    self.nombre +="b"
                    self.cont += 1
                if self.tecla[pygame.K_n]:
                    self.nombre +="n"
                    self.cont += 1
                if self.tecla[pygame.K_m]:
                    self.nombre +="m"
                    self.cont += 1
                if self.tecla[pygame.K_SPACE]:
                    self.nombre +=" "
                    self.cont += 1
                if self.tecla[pygame.K_BACKSPACE]:
                    if self.cont>10:
                        self.nombre = self.nombre[0:len(self.nombre)-1]
                        self.cont += -1
                        self.aparecer = negro
            if self.cont>=28 and self.tecla[pygame.K_BACKSPACE]:
                self.cont +=-1
                self.nombre = self.nombre[0:len(self.nombre)-1]
            self.font3 = pygame.font.SysFont('Arial', 30)
            self.text3 = self.font3.render(str(self.nombre), False, blanco)
            self.textRect3 = self.text3.get_rect()
            self.textRect3.center = (750 // 2, 325)
            ventana.blit(self.text3, self.textRect3)

            self.font4 = pygame.font.SysFont('Arial', self.tamaño)
            self.text4 = self.font4.render(' Escape para aceptar  ', False, verde)
            self.textRect4 = self.text4.get_rect()
            self.textRect4.center = (750 // 2, 400)
            ventana.blit(self.text4, self.textRect4)

            self.font5 = pygame.font.SysFont('Arial', 30)
            self.text5 = self.font5.render('NO existe el jugador', False, self.aparecer)
            self.textRect5 = self.text5.get_rect()
            self.textRect5.center = (750 // 2, 250)
            ventana.blit(self.text5, self.textRect5)


            Jugador().__init__()
            pygame.display.update()


#------------------------------------------------------------------------------------

