#  * EJERCICIO:
#  * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
#  * atributos y una función que los imprima (teniendo en cuenta las posibilidades
#  * de tu lenguaje).
#  * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
#  * utilizando su función.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
#  * en el ejercicio número 7 de la ruta de estudio)
#  * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
#  *   retornar el número de elementos e imprimir todo su contenido.

class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def __str__(self) -> str:
        return str(self.stack)


stack_1 = Stack()
stack_1.push("elemento 1")
print(stack_1)


class Qeuque:
    def __init__(self) -> None:
        self.queuque = []
