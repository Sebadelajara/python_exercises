import re

#  * EJERCICIO:
#  * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
#  * creando una que sea capaz de encontrar y extraer todos los números
#  * de un texto.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea 3 expresiones regulares (a tu criterio) capaces de:
#  * - Validar un email.
#  * - Validar un número de teléfono.
#  * - Validar una url.
#  */

# text = 'Los 123 pájaros volaban en círculos alrededor del árbol, Los 123 pájaros volaban en círculos alrededor del árbol'

# pattern = r"[0-9]+"

# coincidencia = re.findall(pattern, text)
# print(coincidencia)
# print(len(coincidencia))


"""EXTRA"""


def validar_correo(correo: str):
    """
    Valida si el formato de un correo electrónico es correcto.

    Args:
    correo (str): El correo electrónico a validar.

    Returns:
    str: Un mensaje indicando si el formato del correo es válido o no.

    El patrón usado es:
    ^[a-zA-Z0-9.._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

    - ^ y $ delimitan el inicio y el final de la cadena.
    - [a-zA-Z0-9.._%+-]+: Una secuencia de uno o más caracteres alfanuméricos, puntos, guiones bajos, porcentajes, signos más y guiones.
    - @: El símbolo de arroba.
    - [a-zA-Z0-9.-]+: Una secuencia de uno o más caracteres alfanuméricos, puntos y guiones.
    - \.: Un punto literal.
    - [a-zA-Z]{2,}: Dos o más letras.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, correo):
        return f'{correo} es un formato válido de correo'
    else:
        return f'{correo} no es un formato válido de correo'


def validar_numero_cel(numero: str):
    """
    Valida si el formato de un número de teléfono chileno es correcto.

    Args:
    numero (str): El número de teléfono a validar.

    Returns:
    str: Un mensaje indicando si el formato del número es válido o no.

    El patrón usado es:
    ^\+56\d{9}$

    - ^ y $ delimitan el inicio y el final de la cadena.
    - \+56: El prefijo internacional de Chile.
    - \d{9}: Nueve dígitos.
    """
    pattern = r'^\+56\d{9}$'
    if re.match(pattern, numero):
        return f'{numero} es un formato válido para Chile'
    else:
        return f'{numero} no es un formato válido para Chile. Recuerda anteponer +569 seguido de los 9 dígitos.'


def validar_url(url: str):
    """
    Valida si el formato de una URL es correcto.
    Args:
    url (str): La URL a validar.
    Returns:
    str: Un mensaje indicando si el formato de la URL es válido o no.
    El patrón usado es:
    ^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$

    - ^ y $ delimitan el inicio y el final de la cadena.
    - (https?:\/\/)?: Una secuencia opcional de "http://" o "https://".
    - ([\da-z\.-]+): Una secuencia de uno o más dígitos, letras, puntos y guiones.
    - \.: Un punto literal.
    - ([a-z\.]{2,6}): Una secuencia de entre dos y seis letras o puntos.
    - ([\/\w \.-]*)*: Cero o más secuencias de caracteres alfanuméricos, barras, puntos, guiones y espacios.
    - \/?$: Un posible slash al final.
    """
    pattern = r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$'
    if re.match(pattern, url):
        return f'{url} es una URL válida'
    else:
        return f'{url} no es una URL válida'


while True:
    print('Este programa verifica correo, número telefónico y URL válidas')
    to_verificate = input(
        'Ingresa \n 1 - para verificar correo \n 2 - para verificar número \n 3 - para verificar URL \n Ingresa "salir" para terminar el programa\n >>> ')
    if to_verificate.lower() == 'salir':
        print('Programa terminado')
        break
    try:
        option = int(to_verificate)
        if option == 1:
            correo = input('Ingresa un correo: ')
            print(validar_correo(correo))
        elif option == 2:
            cel = input('Ingresa un número telefónico: ')
            print(validar_numero_cel(cel))
        elif option == 3:
            url = input('Ingresa una URL: ')
            print(validar_url(url))
        else:
            print('Debes agregar alguna opción válida')
    except ValueError:
        print('Debes ingresar un número válido o "salir" para terminar el programa.')

# print(validar_url("httpss://www.ejemplo.com"))
