# EJERCICIO:
# Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
# Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
# Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
# Calcula cuántos años han transcurrido entre ambas fechas.

# DIFICULTAD EXTRA (opcional):
# Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
# 10 maneras diferentes. Por ejemplo:
#   Día, mes y año.
#   Hora, minuto y segundo.
#   Día de año.
#   Día de la semana.
#   Nombre del mes.
# (lo que se te ocurra...)
from datetime import datetime


day_now = datetime.now()
birthday = datetime(1990, 9, 15, 7, 30, 0)

print(day_now.year - birthday.year)

print(birthday.strftime(f'fecha año 00: {"%d-%m-%y"}'))
print(birthday.strftime(f'fecha año 0000: {"%d-%m-%Y"}'))
print(birthday.strftime(f'hora, minuto, segundo: {"%H-%M-%S"}'))
print(birthday.weekday())  # devuelve lunes 0 - domingo 6
print(birthday.strftime('%A'))  # devuelve el nombre del dia de la semana
print(birthday.strftime('%B'))  # devuelve el nombre del mes
print(birthday.strftime("%j"))  # devuelve el dia del año (258)
