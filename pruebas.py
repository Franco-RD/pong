from figura_class import Raqueta, Pelota
from pantallas import Partida
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
"""

juego = Partida()
juego.bucle_fotograma()