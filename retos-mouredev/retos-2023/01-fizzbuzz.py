
#  * Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".


# mi solucion
def es_multiplo(numero, divisor):
    return numero % divisor == 0


for i in range(1, 101):
    if es_multiplo(i, 3) and es_multiplo(i, 5):
        i = "fizzbuzz"
    elif es_multiplo(i, 3):
        i = "fizz"
    elif es_multiplo(i, 5):
        i = "buzz"
    print(i)

# solucion mouredev
# def fizzbuzz():

#     for number in range(1, 101):

#         if number % 3 == 0 and number % 5 == 0:
#             print("fizzbuzz")
#         elif number % 3 == 0:
#             print("fizz")
#         elif number % 5 == 0:
#             print("buzz")
#         else:
#             print(number)


# fizzbuzz()
