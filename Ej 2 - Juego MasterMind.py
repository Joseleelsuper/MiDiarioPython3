#Escribe un programa que te permita jugar a una versión simplificada del
#juego Master Mind. El juego consistirá en adivinar una cadena de números
#distintos. Al principio, el programa debe pedir la longitud de la cadena (de 2
#a 9 cifras). Después el programa debe ir pidiendo que intentes adivinar la
#cadena de números. En cada intento, el programa informará de cuántos números
#han sido acertados (el programa considerará que se ha acertado un número si
#coincide el valor y la posición).

import random
import time

def main():
    x = int(input("Introduce la longitud de la cadena: "))
    #generar cadena
    cadena = ""
    for i in range(x):
        cadena += str(random.randint(0,9))
    
    y = ""
    while y != cadena:
        y = input("Introduce la cadena: ")
        if y != cadena:
            aciertos = 0
            for i in range(x):
                if y[i] == cadena[i]:
                    aciertos += 1
            print("Has acertado", aciertos, "números, continua intentándolo")
        else:
            print("Acertaste!")

    
main()

