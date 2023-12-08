from figura_class import Raqueta, Pelota
from pongapp.pantallas import Partida
import pygame as pg

"""
objetoRaqueta = Raqueta(0, 500)

objetoPelota = Pelota(0, 300)


print(objetoRaqueta.derecha)
print(objetoRaqueta.izquierda)
print(objetoRaqueta.arriba)
print(objetoRaqueta.abajo)

print(objetoPelota.derecha)
print(objetoPelota.izquierda)
print(objetoPelota.arriba)
print(objetoPelota.abajo)


def datosPersonales(*args):  #El parametro *args es para que una funcion pueda tener una cantidad ilimitada de parametros. Los guarda en una lista args
    for datos in args:
        print(datos)

datosPersonales("Juan", "perez", 25, "algo")


juego = Partida()
juego.bucle_fotograma()

musica = pg.mixer.music.load("C:\Users\Franco\Downloads\En este país ya nadie trabaja.mp3")
"""
file_imagenes = {'drcha':["electric00_drcha.png", "electric01_drcha.png", "electric02_drcha.png"], 
                    'izqda':["electric00_izqda.png", "electric01_izqda.png", "electric02_izqda.png"]}

lado = "drcha"

def prueba(lado):
    imagenprueba = {}
    for lado in file_imagenes:
        imagenprueba[lado] = []
        for nombre_fichero in file_imagenes[lado]:
            imagen = pg.image.load(f"pongapp/images/raquetas/{nombre_fichero}")
            imagenprueba[lado].append(imagen)
    return imagenprueba

respuesta = prueba(lado)