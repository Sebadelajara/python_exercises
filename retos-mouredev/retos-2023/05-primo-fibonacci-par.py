import math


# Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
# Ejemplos:
# - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#

number = int(input('Escribe un numero: '))

respuesta = f'{number}, '

if number <= 1:
    respuesta += 'no es primo'
elif number == 2:
    respuesta += 'no es primo'
elif number % 2 == 0:
    respuesta += 'no es primo'
else:
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            respuesta += 'no es primo'
            break
    else:
        respuesta += 'es primo'


raiz1 = math.sqrt((5 * (number**2)) + 4)
raiz2 = math.sqrt((5 * (number**2)) - 4)
# is_integer() verifica si un numero es entero


if raiz1.is_integer() or raiz2.is_integer():
    respuesta += ', es fibonacci'
else:
    respuesta += ', no es fibonacci'


if number % 2 == 0:
    respuesta += ', es par'
else:
    respuesta += ', no es par'

print(respuesta)
