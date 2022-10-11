#Diseñar un sistema de puntos para el juego El reino del dragón:
#Dejo el enlace por si alguien no lo vio: https://pythondiario.com/2013/06/juego-en-python-reino-del-dragon-parte1.html
#La idea es la siguiente: mientras el jugador vaya ganando, ira acumulando puntos.
#Ejemplo: Si el jugador entra en la primera cueva y gana el tesoro, se le acreditan 100 puntos, 
#entra en la segunda cueva y gana el tesoro, se le acreditan otros 100 puntos. 
#Si el jugador pierde, saldrá en pantalla el total de los puntos que realizo y la opción de empezar de nuevo.

import random
import time

def introduccion():
    x = 0
    print ("Estamos en una tierra llena de dragones. Delante de nuestro,")
    print ("se ven dos cuevas. En una cueva, el dragon es amigable")
    print ("y compartira el tesoro contigo. El otro dragon")
    print ("es codicioso y hambriento, y te va a comer ni bien te vea.")
    print ("")

def CambiarCueva():
    cueva = ""
    while cueva != "1" and cueva != "2":
        print ("Ha que cueva quieres entrar? 1 o 2?")
        cueva = input("")
       
    return cueva

def cheqcueva(CambiarCueva):
    print ("Te acercas a la Cueva...")
    time.sleep(2)
    print ("Esta oscuro y tenebroso...")
    time.sleep(2)
    print ("Un gran dragon salta delante tuyo, abre su boca y...")
    print ("")
    time.sleep(2)
   
    FriendlyCueva = random.randint (1, 2)
   
    if CambiarCueva == str(FriendlyCueva):
        print ("Te entrega el tesoro...")
        print("Ganas 100 puntos!")
        x+=100
    else:
        print ("El dragon te come de un bocado....")
        print("Perdiste! Tu puntuación final es: ", x)
   
EmpezarNuevo = ("si")

while EmpezarNuevo == ("s") or EmpezarNuevo == ("si"):
   
    introduccion()
   
    NumCaverna = CambiarCueva()
   
    cheqcueva(NumCaverna)
   
    print ("Quieres jugar de nuevo? (si o no)")
    EmpezarNuevo = input("")