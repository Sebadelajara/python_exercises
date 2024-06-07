import random
# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
# - Longitud: Entre 8 y 16.
# - Con o sin letras mayúsculas.
# - Con o sin números.
# - Con o sin símbolos.
# (Pudiendo combinar todos estos parámetros entre ellos)

letras = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k',
          'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'w', 'y', 'z']
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def password_generator():

    password_generated = ''
    character = list('abcdefghijklmnñopqrstwxyz')

    length = int(input('elije un largo entre 8 y 16 caracteres: '))
    upper = str(input('quieres agregar mayusculas escribe; si o no: '))
    symbols = str(input('quieres agregar simbolos? si o no: '))
    number = str(input('quieres agregar numeros? si o no: '))

    if upper == 'si':
        character.extend(list('ABCDFGHIJKLMNÑOPQRSTWXYZ'))
    elif upper == 'no':
        pass

    if symbols == 'si':
        character.extend(list('(-!#$%&()*,./:;?@[]^_`{|}~+<=>)'))
    elif symbols == 'no':
        pass

    if number == 'si':
        character.extend(list('0123456789'))
    elif number == 'no':
        pass

    if 8 <= length <= 16:
        for i in range(length):
            password_generated += random.choice(character)

    return print(password_generated)


password_generator()
