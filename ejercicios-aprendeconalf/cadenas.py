# Ejercicio 1
# Escribir un programa que pregunte el nombre del
# usuario en la consola y un número entero e imprima por pantalla
# en líneas distintas el nombre del usuario tantas veces como el número introducido.

# nombre = input("escribe tu nombre: ")
# num = int(input("escribe un numero: "))

# print((nombre + "\n") * num)
# fin------------------------------------------------------------


# ejercicio 2
# Escribir un programa que pregunte el nombre completo del usuario en la consola
# y después muestre por pantalla el nombre completo del usuario tres veces,
# una con todas las letras minúsculas, otra con todas las letras mayúsculas y
# otra solo con la primera letra del nombre y de los apellidos en mayúscula.
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

# nombre = input("escribe tu nombre completo: ")

# print(nombre.lower())
# print(nombre.upper())
# print(nombre.title())

# fin--------------------------------------------------------------------------------------------

# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y
# después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n>
# letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n>
# es el número de letras que tienen el nombre.

# name = input("escriba su nombre: ")

# longitud_name = len(name)

# print(f"Su nombre {name} tiene {longitud_name} letras")

# fin---------------------------------------------------------------------------------------

# Ejercicio 4
# Los teléfonos de una empresa tienen el siguiente formato
# prefijo-número-extension donde el prefijo es el código del país +34,
# y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
# Escribir un programa que pregunte por un número de teléfono con este formato y
# muestre por pantalla el número de teléfono sin el prefijo y la extensión.

# cel = input(
#     "Escribe tu numero de telefono con el siguiente formato +34-913724710-56 : \n>>>")

# print(f"tu numero de telefono es {cel[4:12]}")

# ----------------------------------

# Ejercicio 5
# Escribir un programa que pida al usuario que introduzca una frase en la consola
# y muestre por pantalla la frase invertida.
# frase = input("escriba una frase: \n>>> ")

# print(frase[::-1])

# Ejercicio 6
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
# y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

# frase = input("escriba una frase: \n>>> ")
# vocal = input("escriba una vocal: \n>>> ")

# print(frase + vocal.upper())

# frase = input("escriba una frase: \n>>> ")
# vocal = input("escriba una vocal: \n>>> ")

# print(frase.replace(vocal, vocal.upper()))

#
