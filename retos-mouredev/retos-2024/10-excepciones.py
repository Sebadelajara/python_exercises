# EJERCICIO:
# Explora el concepto de manejo de excepciones según tu lenguaje.
# Fuerza un error en tu código, captura el error, imprime dicho error
# y evita que el programa se detenga de manera inesperada.
# Prueba a dividir "10/0" o acceder a un índice no existente
# de un listado para intentar provocar un error.

# number1 = int(input("escribe un numero dividendo: "))
# number2 = int(input("escribe un numero divisor "))

# ejemplo1
# def divide_for_2(num1, num2):
#     try:
#         return print(num1 / num2)
#     except ZeroDivisionError:
#         print("no se puede divir por 0")


# divide_for_2(num1=number1, num2=number2)

# ejemplo2
# name = ["seba", "rolo", "nachito"]


# def find_index(iter):
#     try:
#         return print(iter[3])
#     except IndexError:
#         print("El indice no ha sido encontrado")


# find_index(name)

# DIFICULTAD EXTRA (opcional):
# Crea una función que sea capaz de procesar parámetros, pero que también
# pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
# corresponderse con un tipo de excepción creada por nosotros de manera
# personalizada, y debe ser lanzada de manera manual) en caso de error.
# - Captura todas las excepciones desde el lugar donde llamas a la función.
# - Imprime el tipo de error.
# - Imprime si no se ha producido ningún error.
# - Imprime que la ejecución ha finalizado.

# my_list = [1, 2, 3, 4, 5]


# def proces_params(parameters: list):

#     if len(parameters) < 3:
#         raise IndexError

#     print(parameters[2])


# proces_params(my_list)
# proces_params([5, 3])
# proces_params([5, 3, 2, 12, 2])


print('bienvenido a la calculadora de areas')
figura_geo = int(input(
    '¿que figura geometrica quieres calcular el area? \n 1.cuadrado \n 2.rectangulo \n 3.triangulo \n>>>'))

if figura_geo == 1:
    lado = int(input('¿cual es el lado del cuadrado?'))
    area = lado * lado
    print('el area del cuadrado es', area)
elif figura_geo == 2:
    pass
elif figura_geo == 3:
    pass
else:
    print('No ingresaste una opcion valida, ingresa 1, 2 o 3')
