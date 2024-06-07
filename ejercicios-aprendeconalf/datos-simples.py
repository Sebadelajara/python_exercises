# Escribir un programa que pregunte al usuario por el número de horas trabajadas
# y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.


# coste_horas = float(input("ingresa el costo por hora!"))
# horas_trabajadas = float(input("cuantas horas trabajaste?"))
# pago_total = coste_horas * horas_trabajadas


# print(f"tu pago corresponde a: {pago_total} dolares")
# fin-------------------------------------------------------------

# # Escribir un programa que lea un entero positivo,
# , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta
# . La suma de los
#  primeros enteros positivos puede ser calculada de la siguiente forma: n(n+1)/2

# n = int(input("ingresa un entero positivo"))

# n_resultado = n * (n + 1) / 2

# print(f"tu resultado es {n_resultado}")
# fin---------------------------------------


# Escribir un programa que pida al usuario su peso (en kg) y
# estatura (en metros), calcule el índice de masa corporal y
# lo almacene en una variable, y muestre por pantalla la frase
# Tu índice de masa corporal es <imc> donde <imc> es el índice de
# masa corporal calculado redondeado con dos decimales.


# Escribir un programa que pida al usuario dos números enteros y
# muestre por pantalla la
# <n> entre <m> da un cociente <c> y un resto <r>
# donde <n> y <m> son los números introducidos por el usuario,
# y <c> y <r> son el cociente y el resto de la división entera respectivamente.

# a = int(input("escribe un numero entero: "))
# b = int(input("escribe otro numero entero: "))

# modulo_division = a / b

# resto_division = a % b

# print(
#     f"El cociente del resultado de a divido b es: {modulo_division}, y el resto es {resto_division}, gracias")
# fin-----------------------------------------------------------------------------------

# Ejercicio 9
# Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años,
# y muestre por pantalla el capital obtenido en la inversión.

cantidad_inversion = int(input("ingrese la cantidad que desea invertir: "))
interes = float(input("ingrese la tasa de interes anual: "))
años = float(input("ingrese la cantidad de años: "))

valor_final = cantidad_inversion * (1 + interes) * años

print(f"el valor final de su inversion sera {valor_final}")
