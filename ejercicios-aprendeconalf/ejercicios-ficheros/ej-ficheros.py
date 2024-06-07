# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido.


def guardar_tabla_multiplicar(numero):
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return

    nombre_archivo = f"tabla-{numero}.txt"

    with open(nombre_archivo, 'w') as archivo:
        archivo.write(f"Tabla de multiplicar del {numero}:\n")
        for i in range(1, 11):
            resultado = numero * i
            archivo.write(f"{numero} x {i} = {resultado}\n")

    print(f"Tabla de multiplicar del {numero} guardada en {nombre_archivo}")


try:
    numero = int(input("Introduce un número entre 1 y 10: "))
    guardar_tabla_multiplicar(numero)
except ValueError:
    print("Debes introducir un número válido.")


# Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, done n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

# def mostrar_tabla_multiplicar(numero):
#     if numero < 1 or numero > 10:
#         print("El número debe estar entre 1 y 10.")
#         return

#     nombre_archivo = f"tabla-{numero}.txt"

#     try:
#         with open(nombre_archivo, 'r') as archivo:
#             contenido = archivo.read()
#             print(contenido)
#     except FileNotFoundError:
#         print(f"El archivo {nombre_archivo} no existe.")

# try:
#     numero = int(input("Introduce un número entre 1 y 10: "))
#     mostrar_tabla_multiplicar(numero)
# except ValueError:
#     print("Debes introducir un número válido.")


# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
