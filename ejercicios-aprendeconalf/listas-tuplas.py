# Ejercicios de Listas y Tuplas


# Ejercicio 1
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

# asignaturas = []

# while True:
#     asignatura = input('ingresa una asignatura o para salir escribe "salir": ')
#     if asignatura == 'salir':
#         print('saliste del programa')
#         break
#     else:
#         asignaturas.append(asignatura)

# print(asignaturas)


# Ejercicio 2
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
asignaturas = []

# while True:
#     asignatura = input('ingresa una asignatura o para salir escribe "salir": ')
#     if asignatura == 'salir':
#         print('saliste del programa')
#         break
#     else:
#         asignaturas.append(asignatura)

# for i in range(len(asignaturas)):
#     print(f'yo estudio {asignaturas[i]}')


# Ejercicio 3
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

# mate = input('que nota tienes en mate: ')
# lenguaje = input('que nota tienes en lenguaje: ')
# quimica = input('que nota tienes en quimica: ')
# fisica = input('que nota tienes en fisica: ')
# biologia = input('que nota tienes en biologia: ')

# asignaturas = [mate, lenguaje, quimica, fisica, biologia]

# for i in range(len(asignaturas)):
#     print(asignaturas[i])


# #solucion
# subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# scores = []
# for subject in subjects:
#     score = input("¿Qué nota has sacado en " + subject + "?")
#     scores.append(score)
# for i in range(len(subjects)):
#     print("En " + subjects[i] + " has sacado " + scores[i])


# Ejercicio 4
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

# loteria = []
# for i in range(1, 7):
#     numero = int(input('ingresa un numero del 1 al 49 para la loteria: '))
#     loteria.append(numero)

# loteria.sort()
# print(loteria)


# Ejercicio 5
# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.


# Ejercicio 6
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.


# Ejercicio 7
# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.


# Ejercicio 8
# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.


# Ejercicio 9
# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.


# Ejercicio 10
# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.


# Ejercicio 11
# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.


# Ejercicio 12
# Escribir un programa que almacene las matrices


# en una lista y muestre por pantalla su producto.
# Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.


# Ejercicio 13
# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
