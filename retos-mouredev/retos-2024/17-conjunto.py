# /*
#  * EJERCICIO:
#  * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
#  * operaciones (debes utilizar una estructura que las soporte):
#  * - Añade un elemento al final.
#  * - Añade un elemento al principio.
#  * - Añade varios elementos en bloque al final.
#  * - Añade varios elementos en bloque en una posición concreta.
#  * - Elimina un elemento en una posición concreta.
#  * - Actualiza el valor de un elemento en una posición concreta.
#  * - Comprueba si un elemento está en un conjunto.
#  * - Elimina todo el contenido del conjunto.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Muestra ejemplos de las siguientes operaciones con conjuntos:
#  * - Unión.
#  * - Intersección.
#  * - Diferencia.
#  * - Diferencia simétrica.
#  */


# datos = ["manzana", "banana", "cereza", "durazno",
#          "fresa", "kiwi", "naranja", "papaya", "piña"]
# print(datos)

# # añadir elemnto al final
# datos.append("mango")
# print(datos)
# # añadir elemnto al principio
# datos.insert(0, "arandanos")
# print(datos)
# # Añade varios elementos en bloque al final.
# datos.extend([1, 2, 3])
# print(datos)
# # añade varios elementos en bloque en una posición concreta.
# datos[3:3] = ['pera', 'uva', 'sandía']
# print(datos)
# # Elimina un elemento en una posición concreta.
# del datos[3]
# print(datos)
# # Actualiza el valor de un elemento en una posición concreta.
# datos[0] = 'blueberry'
# print(datos)
# # Comprueba si un elemento está en un conjunto.
# print('uva' in datos)
# # Comprueba si un elemento no está en un conjunto.
# print('pera' not in datos)
# # Elimina todo el contenido del conjunto.
# datos.clear()
# print(datos)


"""DIFICULTAD EXTRA"""
# Muestra ejemplos de las siguientes operaciones con conjuntos:
set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 2, 3, 4, 6, 7, 8}
# Unión.
print(set_1.union(set_2))
# intersección.
print(set_1.intersection(set_2))
# diferencia.
print(set_1.difference(set_2))
# diferencia simétrica.
print(set_1.symmetric_difference(set_2))
