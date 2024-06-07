"""ejercicios de bucles"""

# """1"""
# # Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

# palabra = input('escribe una palabra: \n>>> ')

# i = 0
# while i < 10:
#     print(f'{palabra} + {i}')
#     i += 1

"""2"""
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha
# cumplido (desde 1 hasta su edad).

# edad = int(input('escribe tu edad: \n>>> '))

# i = 1
# while i <= edad:
#     if i == 1:
#         print(f'cumpliste {i} año')
#     else:
#         print(f'cumpliste {i} años')
#     i += 1

# resolucion
# age = int(input("¿Cuántos años tienes? "))
# for i in range(age):
#     print("Has cumplido " + str(i+1) + " años")


"""3"""
# Escribir un programa que pida al usuario un número entero positivo y
# muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

# mi primer intento
# entero = int(input('escribe un numero: \n>>> '))

# for i in range(entero + 1):
#     if i % 2 == 0:
#         print(f'{i}')
#     else:
#         pass

# con ayuda
# entero = int(input('escribe un numero: \n>>> '))
# impares = []
# if entero > 0:
#     for i in range(1, entero + 1):
#         if i % 2 != 0:
#             impares.append(str(i))
#     print("Números impares:", ", ".join(impares))
# else:
#     print('no es un entero positivo')

# resolucion


""" Ejercicio 4"""
# # Escribir un programa que pida al usuario un número entero positivo y muestre por
# # pantalla la cuenta atrás desde ese número hasta cero separados por comas.

# num = int(input("ingrese un numero entero positivo \n>>> "))

# i = 0
# list = []
# while i <= num:
#     list.append(i)
#     i += 1
# print(list[::-1])

# # resolucion

# n = int(input("Introduce un número entero positivo: "))
# for i in range(n, -1, -1):
#     print(i, end=", ")


# Ejercicio 5
# Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años, y muestre por pantalla el capital
# obtenido en la inversión cada año que dura la inversión.

# cantidad = float(input('ingrese una cantidad a invertir: '))
# interes = float(input('ingrese el interes anual: '))
# number_years = int(input('ingrese el numero de años a invertir: '))


# interes1 = interes + 1/100


# for i in range(number_years):
#     cantidad *= interes1
#     print(cantidad)

# print(f'cantidad de la inversion final es de {cantidad}')


# Ejercicio 6
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un
# triángulo rectángulo como el de más abajo, de altura el número introducido.


# number = int(input('escribe un numero: '))

# for i in range(number):
#     print('*' * (i + 1))

# solucion 2
# n = int(input("Introduce la altura del triángulo (entero positivo): "))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print("")

# Ejercicio 7
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} x {j} = {i * j}')


# Ejercicio 8
# Escribir un programa que pida al usuario un número entero y muestre por
# pantalla un triángulo rectángulo como el de más abajo.
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

# numero = int(input('ingresa un numero: '))

# for i in range(1, numero + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print('')


# Ejercicio 9
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

# password = 'hola1234'
# user_password = ''

# while user_password != password:
#     user_password = input('Adivine la contraseña: ')

# print('¡Contraseña correcta! Bienvenido.')


# Ejercicio 10
# Escribir un programa que pida al usuario un número entero y
# muestre por pantalla si es un número primo o no.


# opcion 1
# number = int(input('ingresa un numero: '))

# if number <= 1:
#     print(f'{number} no es primo')
# elif number == 2:
#     print(f'{number} no es primo')
# elif number % 2 == 0:
#     print(f'{number} no es primo')
# else:
#     for i in range(3, int(number**0.5) + 1, 2):
#         if number % i == 0:
#             print('no es primo')
#             break
#     else:
#         print('es primo ')

# opcion 2
# n = int(input("Introduce un número entero positivo mayor que 2: "))
# i = 2
# while n % i != 0:
#     i += 1
# if i == n:
#     print(str(n) + " es primo")
# else:
#     print(str(n) + " no es primo")


# # opcion 3
# n = int(input("Introduce un número entero positivo mayor que 2: "))
# for i in range(2, n):
#     if n % i == 0:
#         break
# if (i + 1) == n:
#     print(str(n) + " es primo")
# else:
#     print(str(n) + " no es primo")

# Ejercicio 11
# Escribir un programa que pida al usuario una palabra y luego muestre por
# pantalla una a una las letras de la palabra introducida empezando por la última.

# palabra = input('escribe una palabra: ')


# for i in palabra[::-1]:
#     print(i)


# Ejercicio 12
# Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.

# frase = input('escribe una frase: ')
# letra = input('escribre una letra: ')

# count = 0
# for i in frase:
#     if i == letra:
#         count += 1

# print(count)


# Ejercicio 13
# Escribir un programa que muestre el eco de todo lo que el usuario
# introduzca hasta que el usuario escriba “salir” que terminará.


while True:
    eco = input('escribe una palabra: ')
    if eco == 'salir':
        print('saliste del programa')
        break
    else:
        continue
