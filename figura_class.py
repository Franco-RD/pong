import pygame as pg

class Raqueta:
    def __init__(self, pos_x, pos_y, color=(255,255,255), w=20, h=120):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h
    
    def dibujar(self, surface):
        pg.draw.rect(surface, self.color, (self.pos_x, self.pos_y-(self.h//2), self.w, self.h))  #Las divisiones en la posicion del draw son para que se dibuje en el medio de la pantalla

    def mover(self, tecaldo_arriba, teclado_abajo):        
        estado_teclado = pg.key.get_pressed()      

        if estado_teclado[tecaldo_arriba] == True and self.pos_y >= 0+(self.h//2): #Se suma y resta el h//2 ya que la posicion de los objetos se mide desde el centro del obj. Hay que sumarle la mitad del objeto para que los bordes sean los que marquen el limite
            self.pos_y -= 1

        if estado_teclado[teclado_abajo] == True and self.pos_y <= 600-(self.h//2):
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
    def __init__(self, pos_x, pos_y, color=(255,255,255), radio=5, vx=1, vy=1) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.radio = radio
        self.vx = vx
        self.vy = vy
        self.contadorDerecho = 0
        self.contadorIzquierdo = 0
    
    def dibujar(self, surface):
        pg.draw.circle(surface, self.color, (self.pos_x, self.pos_y), self.radio)

    def mover(self, x_max=800, y_max=600):
        self.pos_x += self.vx  #Esto hace que se mueva de manera automatica por los ejes
        self.pos_y += self.vy

        #Colision limite derecho
        if self.pos_x >= x_max+self.radio*10:  #El radio se multiplica por numeros mas grandes que 2 para que la pelota se pierda por mas tiempo fuera de la pantalla tras meter un punto
            self.pos_x = x_max//2  #Esto es para que despues de un gol salga del centro la pelota. Se lo tenemos que dejar para que no rebote por atras de la raqueta y siga metiendo puntos
            self.pos_y = y_max//2
            self.vx *= -1
            self.vy *= -1
            self.contadorDerecho += 1
        
        #Colision limite izquierdo
        if self.pos_x <= 0-self.radio*10: 
            self.pos_x = x_max//2
            self.pos_y = y_max//2
            self.vx *= -1
            self.vy *= -1
            self.contadorIzquierdo += 1

        #Colision vertical
        if self.pos_y >= y_max or self.pos_y <=  0 :
            self.vy *= -1
        
    def mostrar_marcador(self, pantalla):
        #fuente = pg.font.SysFont("verdana", 30)  #SysFont toma fuentes del sistema
        fuente = pg.font.Font(None, 30)  #Font toma fuentes de un archivo que las contenga
        marcador1 = fuente.render(str(self.contadorDerecho), True, (255,255,255))  #El .render  devuelve un objeto de tipo surface, que muestra un str seteado con demas parametros
        marcador2 = fuente.render(str(self.contadorIzquierdo), True, (255,255,255))
        pantalla.blit(marcador1, (330,20))  #Blit muestra un objeto de tipo surface en una coordenada
        pantalla.blit(marcador2, (450,20))
    
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