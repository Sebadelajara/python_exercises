"""Juego adivina el numero"""

# Ejercicio: Adivina el número
# Escribe un programa en Python que genere un número aleatorio entre 1 y 100,
# y le pida al usuario que adivine el número. El programa debe dar pistas al usuario indicando
# si el número a adivinar es mayor o menor que el número ingresado. El juego debe continuar hasta que
# el usuario adivine el número correcto.
# Puedes utilizar la función random.randint() para generar el número aleatorio.
# Asegúrate de importar el módulo random al inicio de tu programa.

import random
import time

num_random = random.randint(1, 100)
encontrado = False
intentos = 0
while not encontrado:

    time.sleep(1)
    num_user = int(
        float(input('adivina el numero entre 1 y 100 : \ningresa tu numero >>> ')))
    intentos += 1
    time.sleep(1)
    if 1 <= num_user <= 100:

        if num_user == num_random:
            print(f'Felicidades!! acertaste al numero en {intentos} intentos')

            encontrado = True
        elif num_user > num_random:
            print('UPS! tu numero es mayor al numero incognito')
        elif num_user < num_random:
            print('UPS tu numero es menor al numero incognito')
    else:
        print('el numero ingresado esta fuera del rango ')
