import pygame as pg

pg.init()  #Se agrega aca y se saca de todas las declaraciones de pantalla para que siempre sea importado y funcione el bucle de pantallas de un juego luego de otro. 

ANCHO = 800 #Las mayusculas son para referenciar las variables que no deben modificarse por el programa. Solo en este fichero hay que cambiar los valores
ALTO = 600
ANCHO_MIN = 0
ALTO_MIN = 0

COLOR_PELOTA = (228,231,19)
COLOR_PANTALLA = (27,149,47)
COLOR_BLANCO = (255, 255, 255)
COLOR_AZUL = (2,2,249)
COLOR_NARANJA = (247,112,30)
COLOR_ROJO = (255,0,0)
COLOR_AMARILLO = (250,220,6)
COLOR_GRANATE = (168,6,36)
COLOR_VERDE = (11,241,28)

FONDO_ROJO = (250,18,10)
FONDO_NARANJA = (250,103,12)

TIEMPO_JUEGO = 5000
VELOCIDAD_JUEGO = 600
TIEMPO_LIMIT_1 = 10000
TIEMPO_LIMIT_2 = 5000

FUENTE1 = "pongapp/fonts/PresStart2P.ttf"  #Rutas a las fuentes para poder utilizarlas en cualquier clase
FUENTE2 = "pongapp/fonts/RussoOne.ttf"
SIZE_FUENTE_1 = 15
SIZE_FUENTE_2 = 20
SIZE_FUENTE_3 = 10

IMGFONDO = "pongapp/images/fondomenu.jpg"

SONIDO_MENU = "pongapp/songs/menu.mp3"
SONIDO_PELOTA = "pongapp/songs/pelota.mp3"