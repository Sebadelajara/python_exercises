#
#  EJERCICIO:
#  Entiende el concepto de recursividad creando una función recursiva que imprima
#  números del 100 al 0.
#
#  DIFICULTAD EXTRA (opcional):
#  Utiliza el concepto de recursividad para:
#  - Calcular el factorial de un número concreto (la función recibe ese número).
#  - Calcular el valor de un elemento concreto (según su posición) en la
#    sucesión de Fibonacci (la función recibe la posición).

def cien_a_cero(n):
    if n == 0:
        print(n)
    else:
        print(n)
        cien_a_cero(n - 1)


# cien_a_cero(100)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# print(factorial(5))

def posicion_fibonacci(n):
    if n == 0:
        return 0
    else:
        if n == 1:
            return 1
        else:
            return posicion_fibonacci(n - 1) + posicion_fibonacci(n - 2)


print(posicion_fibonacci(6))
