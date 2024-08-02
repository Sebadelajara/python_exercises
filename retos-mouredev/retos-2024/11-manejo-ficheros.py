#
# IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
#
# EJERCICIO:
# Desarrolla un programa capaz de crear un archivo que se llame como
# tu usuario de GitHub y tenga la extensión .txt.
# Añade varias líneas en ese fichero:
# - Tu nombre.
# - Edad.
# - Lenguaje de programación favorito.
# Imprime el contenido.
# Borra el fichero.
#
# DIFICULTAD EXTRA (opcional):
# Desarrolla un programa de gestión de ventas que almacena sus datos en un
# archivo .txt.
# - Cada producto se guarda en una línea del archivo de la siguiente manera:
#   [nombre_producto], [cantidad_vendida], [precio].
# - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
#   actualizar, eliminar productos y salir.
# - También debe poseer opciones para calcular la venta total y por producto.
# - La opción salir borra el .txt.


import os
# este codigo creo el archivo y escribe, cada vez que se ejecuta
# with open('sebadlj.txt', 'w') as file:
#     file.write('Sebastian\n')
#     file.write('33\n')
#     file.write('Python\n')
#     file.write('Rolo')


# # este codigo lee el archivo y lo imprime por consola
# with open('sebadlj.txt', 'r') as file:
#     read_file = file.read()
#     print(read_file)


# os.remove('sebadlj.txt')

# DIFICULTAD EXTRA \\

file_name = 'ventas.txt'

open(file_name, 'a')

while True:
    print("1. añade un producto")
    print("2. consultar productos")
    print("3. editar productos")
    print("4. calcular valor por producto")
    print("5. calcular valor total")
    print("6. eliminar producto")
    print("7. mostrar productos")
    print("8. Salir")

    option = input("ingresa tu opcion: ")

    if option == '1':  # agregar producto
        name = input('nombre: ')
        quantity = input('cantidad: ')
        price = input('precio: ')
        with open(file_name, 'a') as file:
            file.write(f'{name}, {quantity}, {price}\n')

    elif option == '2':  # consultar producto
        name = input('nombre: ')
        with open(file_name, 'r') as file:
            for line in file.readlines():
                if line.split(", ")[0] == name:
                    print(line)

    elif option == '3':  # editar producto
        name = input('nombre: ')
        quantity = input('cantidad: ')
        price = input('precio: ')
        with open(file_name, 'r') as file:
            lines = file.readlines()
        with open(file_name, 'w') as file:
            for line in lines:
                if line.split(', ')[0] == name:
                    file.write(f'{name}, {quantity}, {price}\n')
                else:
                    file.write(line)
    elif option == '4':  # calcular valor x producto
        name = input('nombre: ')
        total = 0
        with open(file_name, 'r') as file:
            for line in file.readlines():
                components = line.split(', ')
                if components[0] == name:
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
                    break
        print(total)
    elif option == '5':  # calcular valor total
        total = 0
        with open(file_name, 'r') as file:
            for line in file.readlines():
                components = line.split(', ')
                quantity = int(components[1])
                price = float(components[2])
                total += quantity * price
        print(total)
    elif option == '6':  # eliminar producto
        name = input('nombre: ')
        with open(file_name, 'r') as file:
            lines = file.readlines()
        with open(file_name, 'w') as file:
            for line in lines:
                if line.split(', ')[0] != name:
                    file.write(line)
    elif option == '7':  # mostrar productos
        with open(file_name, 'r') as file:
            print(file.read())
    elif option == '8':  # salir y borrar fichero
        print('Saliste del programa')
        # os.remove(file_name)
        break
    else:
        print('Debes elegir una opcion')
