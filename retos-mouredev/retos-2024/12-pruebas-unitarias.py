import unittest
from datetime import datetime, date
#  * EJERCICIO:
#  * Crea una función que se encargue de sumar dos números y retornar
#  * su resultado.
#  * Crea un test, utilizando las herramientas de tu lenguaje, que sea
#  * capaz de determinar si esa función se ejecuta correctamente.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un diccionario con las siguientes claves y valores:
#  * "name": "Tu nombre"
#  * "age": "Tu edad"
#  * "birth_date": "Tu fecha de nacimiento"
#  * "programming_languages": ["Listado de lenguajes de programación"]
#  * Crea dos test:
#  * - Un primero que determine que existen todos los campos.
#  * - Un segundo que determine que los datos introducidos son correctos.
#  */


# def sumar(*args):
#     return sum(args)


# print(sumar(3, 4, 5))

import unittest
from datetime import datetime, date


def sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Los argumentos deben ser enteros o decimales')
    return a + b

# isinstance(a, (int, float)): Verifica que a y b sean de tipo int o float.
# raise ValueError(...): Lanza una excepción si los tipos no son correctos.
# return a + b: Devuelve la suma de a y b.

# Clase de pruebas unitarias para la función sum


class TestSum(unittest.TestCase):
    # Define una clase de prueba que hereda de unittest.TestCase.
    def test_sum(self):
        # Prueba de suma de dos enteros positivos
        self.assertEqual(sum(4, 7), 11)
        # Prueba de suma de un entero positivo y un entero negativo
        self.assertEqual(sum(5, -7), -2)
        # Prueba de suma de dos ceros
        self.assertEqual(sum(0, 0), 0)
        # Prueba de suma de dos números decimales
        self.assertEqual(sum(2.5, 2.4), 4.9)
        # Prueba de suma de un entero y un decimal
        self.assertEqual(sum(2, 2.1), 4.1)
        # Prueba de suma de dos números decimales iguales
        self.assertEqual(sum(2.5, 2.5), 5)

    def test_sum_type(self):
        # Prueba que verifica que se lance ValueError si los argumentos no son números
        with self.assertRaises(ValueError):
            sum('5', 7)
        with self.assertRaises(ValueError):
            sum(5, '7')
        with self.assertRaises(ValueError):
            sum('5', '7')
        with self.assertRaises(ValueError):
            sum('a', 7)
        with self.assertRaises(ValueError):
            sum(None, 7)


"""
Extra: Pruebas unitarias para datos
"""


class TestData(unittest.TestCase):

    def setUp(self) -> None:
        # Configuración inicial antes de cada prueba
        self.data = {
            "name": "Brais Moure",
            "age": 36,
            "birth_date": datetime.strptime("29-04-87", "%d-%m-%y").date(),
            "programming_languages": ["Python", "Kotlin", "Swift"]
        }

    def test_fields_exist(self):
        # Verifica que ciertos campos existan en el diccionario self.data
        self.assertIn('name', self.data)
        self.assertIn('age', self.data)
        self.assertIn('birth_date', self.data)
        self.assertIn('programming_languages', self.data)

    def test_data_is_correct(self):
        # Verifica que los tipos de datos en self.data sean correctos
        self.assertIsInstance(self.data['name'], str)
        self.assertIsInstance(self.data['age'], int)
        self.assertIsInstance(self.data['birth_date'], date)
        self.assertIsInstance(self.data['programming_languages'], list)


# Ejecuta las pruebas si el archivo se ejecuta directamente
if __name__ == '__main__':
    unittest.main()
