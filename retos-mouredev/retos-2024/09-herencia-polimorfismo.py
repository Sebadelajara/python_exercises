"""
 EJERCICIO:
 Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 implemente una superclase Animal y un par de subclases Perro y Gato,
 junto con una función que sirva para imprimir el sonido que emite cada Animal.
"""


# # superclase
# class Animal:

#     def __init__(self) -> None:
#         pass

#     def sonido(self):
#         pass


# # subclase


# class Perro(Animal):

#     def __init__(self) -> None:
#         super().__init__()

#     def sonido(self):
#         print("Guau Guau!!")


# class Gato(Animal):

#     def sonido(self):
#         print("Miau Miau!!")


# animal = Animal()
# perro_rolo = Perro()
# gato_nublado = Gato()

# animal.sonido()
# perro_rolo.sonido()
# gato_nublado.sonido()

# # polimorfismo explicacion


# def print_sound(animal: Animal):
#     animal.sonido()


# print_sound(perro_rolo)

"""DIFICULTAD EXTRA (opcional):
  Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
  pueden ser Gerentes, Gerentes de Proyectos o Programadores.
  Cada empleado tiene un identificador y un nombre.
  Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
  actividad, y almacenan los empleados a su cargo.
"""


class Employee:
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for i in self.employees:
            print(f"ID: {i.id}, Nombre: {i.nombre}")


class Manager(Employee):
    def coordinate_projects(self):
        print(f"{self.nombre} está coordinando todos los proyectos de la empresa.")


class ProjectManager(Employee):
    def __init__(self, id: int, nombre: str, project: str):
        super().__init__(id, nombre)
        self.project = project

    def coordinate_project(self):
        print(f"{self.nombre} está coordinando su proyecto {self.project}.")


class Programmer(Employee):
    def __init__(self, id: int, nombre: str, language: str):
        super().__init__(id, nombre)
        self.language = language

    def code(self):
        print(f"{self.nombre} está programando en {self.language}.")

    def add(self, employee):
        print(
            f"Un programador no puede tener empleados a su cargo. {employee.nombre} no se añadirá.")


my_manager = Manager(1, "MoureDev")
my_project_manager = ProjectManager(2, "Brais", "Proyecto 1")
my_project_manager2 = ProjectManager(3, "Moure", "Proyecto 2")
my_programmer = Programmer(4, "Kontrol", "Swift")
my_programmer2 = Programmer(5, "Ros", "Cobol")
my_programmer3 = Programmer(6, "Bushi", "Dart")
my_programmer4 = Programmer(7, "Nasos", "Python")

my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)

my_project_manager.add(my_programmer)
my_project_manager.add(my_programmer2)
my_project_manager2.add(my_programmer3)
my_project_manager2.add(my_programmer4)

my_programmer.add(my_programmer2)  # Esto imprimirá un mensaje de error

my_programmer.code()
my_project_manager.coordinate_project()
my_manager.coordinate_projects()
my_manager.print_employees()
my_project_manager.print_employees()
my_programmer.print_employees()  # Esto imprimirá una lista vacía
