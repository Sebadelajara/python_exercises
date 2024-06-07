
# Crea 3 funciones, cada una encargada de detectar si una cadena de
# texto es un heterograma, un irama sogo un pangrama.
# - Debes buscar la definición de cada uno de estos términos.


palabra = 'The quick brown fox jumps over a lazy dog'


def heterograma(word):
    for i in range(len(word)):
        for j in range(i + 1, len(word)):
            if word[i] == word[j]:
                return 'no es heterograma'
    return 'es heterograma'


print(heterograma(palabra))


def isograma(word):
    for i in range(len(word)):
        if word[i] == ' ':
            continue
        for j in range(i + 1, len(word)):
            if word[j] == ' ':
                continue
            if word[i] == word[j]:
                return 'no es isograma'
    return 'es hisograma'


print(isograma(palabra))


# def pangrama(word):
#     # alf = 'abcdefghijklmnopqrstwyz'
#     conjunto = ''
#     for i in word:
#         for j in conjunto:
#             if i == j:

#     return

def pangrama(word):
    # Convertir la palabra a minúsculas
    word = word.lower()

    # Crear un conjunto de letras únicas
    conjunto = set(word)

    # Verificar si el conjunto tiene todas las letras del alfabeto
    if len(conjunto) == 26:
        return 'La palabra es un pangrama'
    else:
        return 'La palabra no es un pangrama'


print(pangrama(palabra))

# Heterograma: Un heterograma es una palabra o frase en la que no se repite ninguna letra. Es decir, cada letra aparece solo una vez en la palabra o frase. Un ejemplo de heterograma en español es la palabra "murciélago".

# Isograma: Un isograma es una palabra o frase en la que no se repite ninguna letra, pero a diferencia de un heterograma, también puede incluir espacios y signos de puntuación. En otras palabras, un isograma es más general y puede ser una secuencia de caracteres que no repiten ninguna letra. Un ejemplo de isograma podría ser "Amo la pizza" (ignorando los espacios).

# Pangrama: Un pangrama es una oración que utiliza todas las letras del alfabeto al menos una vez. El objetivo es mostrar todas las letras de una lengua en una sola frase o palabra. Un ejemplo clásico en inglés es "The quick brown fox jumps over a lazy dog" que utiliza todas las letras del alfabeto inglés.
