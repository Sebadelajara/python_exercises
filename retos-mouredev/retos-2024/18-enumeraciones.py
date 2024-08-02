# EJERCICIO:
# Empleando tu lenguaje, explora la definición del tipo de dato
# que sirva para definir enumeraciones (Enum).
# Crea un Enum que represente los días de la semana del lunes
# al domingo, en ese orden. Con ese enumerado, crea una operación
# que muestre el nombre del día de la semana dependiendo del número entero
# utilizado (del 1 al 7).
# DIFICULTAD EXTRA (opcional):
# Crea un pequeño sistema de gestión del estado de pedidos.
# Implementa una clase que defina un pedido con las siguientes características:
# - El pedido tiene un identificador y un estado.
# - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
# - Implementa las funciones que sirvan para modificar el estado:
#   - Pedido enviado
#   - Pedido cancelado
#   - Pedido entregado
#   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
# - Implementa una función para mostrar un texto descriptivo según el estado actual.
# - Crea diferentes pedidos y muestra cómo se interactúa con ellos.

from enum import Enum


# class WeekDay(Enum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     SUNDAY = 7


# def get_day(number: int):
#     print(WeekDay(number).name)

# get_day(1)


# DIFICULTAD EXTRA (opcional):

class Status(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELLED = 4


class Order:

    def __init__(self, id) -> None:
        self.id = id
        self.status = Status.PENDING

    def ship(self):
        if self.status == Status.PENDING:
            self.status = Status.SHIPPED
            print(f"Pedido {self.id} enviado, estado: {self.status.name}")
        else:
            print("Asegurate que el estado del pedido sea Pendiente")

    def delivery(self):
        if self.status == Status.SHIPPED:
            self.status = Status.DELIVERED
            print(f"Pedido {self.id} entregado, estado: {self.status.name}")
        else:
            print("Asegurate que el estado del pedido sea Pendiente")

    def cancel(self):
        if self.status != Status.DELIVERED:
            self.status = Status.CANCELLED
            print(f"Pedido {self.id} cancelado, estado: {self.status.name}")
        else:
            print("Asegurate que el estado del pedido sea Pendiente")

    def display_status(self):
        print(f"El estado del pedido {self.id} es {self.status.name}")


order_1 = Order(232910)
order_1.display_status()
order_1.ship()
order_1.cancel()
order_1.delivery()
