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
with open('sebadlj.txt', 'w') as file:
    file.write('Sebastian\n')
    file.write('33\n')
    file.write('Python\n')
    file.write('Rolo')


# este codigo lee el archivo y lo imprime por consola
with open('sebadlj.txt', 'r') as file:
    read_file = file.read()
    print(read_file)


os.remove('sebadlj.txt')

# DIFICULTAD EXTRA \\
