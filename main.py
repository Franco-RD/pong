import pygame as pg
from figura_class import *

pg.init()

#Definicion de la pantalla
pantalla_principal = pg.display.set_mode((800, 600))
pg.display.set_caption("PONG")

tasa_refresco = pg.time.Clock()  #Definir tasa de refresco en nuestro bucle de fotogramas. 

#Definicion de objetos para el juego
pelota = Pelota(400, 300, (228,231,19), 10)

raqueta1 = Raqueta(10, 300)  #Raqueta izquierda
raqueta2 = Raqueta(790, 300)  #raqueta derecha


#Bucle del juego principal, el juego corre hasta que se toca cerrar
game_over = True

while game_over:
    
    #Obtener la tasa de refrescos en ms
    valor_tasa = tasa_refresco.tick(400)  #Variable para controlar la velocidad entre fotogramas. A menor numero entre () mas lento es
    print(valor_tasa)

    #Captura de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = False
    

    estado_teclado = pg.key.get_pressed()

    if estado_teclado[pg.K_UP] == True:
        raqueta1.pos_y -= 1
    if estado_teclado[pg.K_DOWN] == True:
        raqueta1.pos_y += 1


    #Seteo de pantalla y dibujo de objetos
    pantalla_principal.fill((27,149,47))
    pg.draw.line(pantalla_principal, (255, 255, 255), (400,0), (400, 600), 15)
    pelota.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)

    pg.display.flip()

pg.quit()

