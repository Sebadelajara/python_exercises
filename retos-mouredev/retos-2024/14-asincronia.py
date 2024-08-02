
# EJERCICIO:
# Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
# asíncrona una función que tardará en finalizar un número concreto de
# segundos parametrizables. También debes poder asignarle un nombre.
# La función imprime su nombre, cuándo empieza, el tiempo que durará
# su ejecución y cuando finaliza.
# DIFICULTAD EXTRA (opcional):
# Utilizando el concepto de asincronía y la función anterior, crea
# el siguiente programa que ejecuta en este orden:
# - Una función C que dura 3 segundos.
# - Una función B que dura 2 segundos.
# - Una función A que dura 1 segundo.
# - Una función D que dura 1 segundo.
# Las funciones C, B y A se ejecutan en paralelo.
# La función D comienza su ejecución cuando las 3 anteriores han finalizado.

import asyncio
from datetime import datetime


async def task(name: str, seg: int):
    print(f'tarea: {name}, duracion: {seg}s, inicio: {datetime.now()} ')
    await asyncio.sleep(seg)
    print(f'tarea: {name}, duracion: {seg}s, fin: {datetime.now()} ')


# asyncio.run(task('tarea1', 3))


async def main():
    tarea_c = task('tarea c', 3)
    tarea_b = task('tarea b', 3)
    tarea_a = task('tarea a', 1)
    tarea_d = task('tarea d', 1)

    await asyncio.gather(tarea_c, tarea_b, tarea_a)

    await tarea_d

asyncio.run(main())
