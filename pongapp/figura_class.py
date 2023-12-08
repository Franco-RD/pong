import pygame as pg
from pongapp.utils import *


class Raqueta:
    def __init__(self, pos_x, pos_y, color=COLOR_BLANCO, w=20, h=120):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h
        self.raqueta = None
        self.file_imagenes = {'drcha':["electric00_drcha.png", "electric01_drcha.png", "electric02_drcha.png"], 
                              'izqda':["electric00_izqda.png", "electric01_izqda.png", "electric02_izqda.png"]}
        self.imagenes = self.cargar_imagenes()  #llamar al metodo que devuelve la inicializacion de imagenes
        self._direccion = '' #variable para asignar direccion
        self.imagen_activa = 0  #variable para indicar repeticion

    def cargar_imagenes(self):
        imagenprueba = {}
        for lado in self.file_imagenes:
            imagenprueba[lado] = []
            for nombre_fichero in self.file_imagenes[lado]:
                imagen = pg.image.load(f"pongapp/images/raquetas/{nombre_fichero}")
                imagenprueba[lado].append(imagen)
        return imagenprueba
    
    @property    #hace que la funcion llame una variable. Es un getter. En general las variables con un _ al principio significan que van a tener un setter y un getter (un metodo que la cargue y otro que la llame)
    def direccion(self):
        return self._direccion

    def dibujar(self, surface):
        #pg.draw.rect(surface, self.color, (self.pos_x, self.pos_y-(self.h//2), self.w, self.h))  #Las divisiones en la posicion del draw son para que se dibuje en el medio de la pantalla
        #self.raqueta = pg.image.load(self.imagenes[lado])
        #surface.blit(self.raqueta, (self.pos_x, self.pos_y-(self.h//2)))
        surface.blit(self.imagenes[self.direccion][self.imagen_activa], (self.pos_x, self.pos_y-(self.h//2)))
        self.imagen_activa += 1
        if self.imagen_activa >= len(self.imagenes[self.direccion]):
            self.imagen_activa = 0


    def mover(self, tecaldo_arriba, teclado_abajo, y_max=ALTO, y_min=ALTO_MIN):
        estado_teclado = pg.key.get_pressed()      

        if estado_teclado[tecaldo_arriba] == True and self.pos_y >= y_min+(self.h//2): #Se suma y resta el h//2 ya que la posicion de los objetos se mide desde el centro del obj. Hay que sumarle la mitad del objeto para que los bordes sean los que marquen el limite
            self.pos_y -= 1

        if estado_teclado[teclado_abajo] == True and self.pos_y <= y_max-(self.h//2):
            self.pos_y += 1

    @property  #Me permite llamar a los metodos/funciones sin usar (). Tiene que ir pegado al metodo al que se lo quiero aplicar
    def derecha(self):
        return self.pos_x + (self.w//2)
    
    @property
    def izquierda(self):
        return self.pos_x - (self.w//2)
    
    @property
    def arriba(self):
        return self.pos_y - (self.h//2)
    
    @property
    def abajo(self):
        return self.pos_y + (self.h//2)


class Pelota:
    def __init__(self, pos_x, pos_y, color=COLOR_BLANCO, radio=15, vx=1, vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.radio = radio
        self.vx = vx
        self.vy = vy
        self.sonido = pg.mixer.Sound(SONIDO_PELOTA)
        self.pelota = pg.image.load(IMGPELOTA)
      
    
    def dibujar(self, surface):
        #pg.draw.circle(surface, self.color, (self.pos_x, self.pos_y), self.radio)
        surface.blit(self.pelota, (self.pos_x, self.pos_y))

    def mover(self, x_max=ANCHO, y_max=ALTO):
        self.pos_x += self.vx  #Esto hace que se mueva de manera automatica por los ejes
        self.pos_y += self.vy

        #Colision limite derecho
        if self.pos_x >= x_max+self.radio*10:  #El radio se multiplica por numeros mas grandes que 2 para que la pelota se pierda por mas tiempo fuera de la pantalla tras meter un punto
            self.pos_x = x_max//2  #Esto es para que despues de un gol salga del centro la pelota. Se lo tenemos que dejar para que no rebote por atras de la raqueta y siga metiendo puntos
            self.pos_y = y_max//2
            self.vx *= -1
            self.vy *= -1
            return "right"
        
        #Colision limite izquierdo
        if self.pos_x <= 0-self.radio*10: 
            self.pos_x = x_max//2
            self.pos_y = y_max//2
            self.vx *= -1
            self.vy *= -1
            return "left"

        #Colision vertical
        if self.pos_y >= y_max or self.pos_y <=  0 :
            self.vy *= -1    
  
    @property 
    def derecha(self):
        return self.pos_x + self.radio
    
    @property
    def izquierda(self):
        return self.pos_x - self.radio
    
    @property
    def arriba(self):
        return self.pos_y - self.radio
    
    @property
    def abajo(self):
        return self.pos_y + self.radio
    
    def comprobar_choque(self, r1, r2):
        if self.derecha >= r2.izquierda and self.izquierda <= r2.derecha and self.abajo >= r2.arriba and self.arriba <= r2.abajo:
            self.vx *= -1
        if self.derecha >= r1.izquierda and self.izquierda <= r1.derecha and self.abajo >= r1.arriba and self.arriba <= r1.abajo:
            self.vx *= -1

    def comprobar_choqueV2(self, *raquetas):  #Hecho con parametro *args para ahorrar codigo
         for r in raquetas:
              if self.derecha >= r.izquierda and self.izquierda <= r.derecha and self.abajo >= r.arriba and self.arriba <= r.abajo:
                  self.vx *= -1
                  pg.mixer.Sound.play(self.sonido)