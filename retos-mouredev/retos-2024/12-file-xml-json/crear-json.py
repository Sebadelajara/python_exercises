import json

"""crear json con modulo json python"""
nombre = 'sebas'
edad = '33'
fecha_nacimiento = '15-09-1990'
lenguajes_programacion = ['python', 'rust', 'javascript']

data = {
    "nombre": nombre,
    "edad": edad,
    "fecha_nacimiento": fecha_nacimiento,
    "lenguajes_programacion": lenguajes_programacion
}

json_string = json.dumps(data, ensure_ascii=False, indent=4)
print(json_string)

with open('persona.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)


"""crear json de forma manual con python"""
# nombre = 'sebas'
# edad = '33'
# fecha_nacimiento = '15-09-1990'
# lenguajes_programacion = ['python', 'rust', 'javascript']

# json_content = "{\n"
# json_content += f'    "nombre": "{nombre}",\n'
# json_content += f'    "edad": {edad},\n'
# json_content += f'    "fecha_nacimiento": "{fecha_nacimiento}",\n'
# json_content += '    "lenguajes_programacion": [\n'
# for i, lenguaje in enumerate(lenguajes_programacion):
#     if i == len(lenguajes_programacion) - 1:
#         json_content += f'        "{lenguaje}"\n'
#     else:
#         json_content += f'        "{lenguaje}",\n'
# json_content += '    ]\n'
# json_content += '}'

# print(json_content)

# with open('persona.json', 'w', encoding='utf-8') as file:
#     file.write(json_content)

# Explicación del Código
# Definir los datos: Definimos las variables nombre, edad, fecha_nacimiento y lenguajes_programacion.

# Construir la cadena JSON:

# Comenzamos la cadena json_content con una llave de apertura {.
# Añadimos cada par clave-valor a la cadena, asegurándonos de que las cadenas de texto estén entre comillas dobles.
# Para el arreglo lenguajes_programacion, iteramos sobre los elementos y los añadimos a la cadena JSON.
# Nos aseguramos de que la última entrada en el arreglo no tenga una coma al final.
# Escribir la cadena JSON a un archivo:

# Abrimos (o creamos) un archivo llamado persona.json en modo de escritura ('w') con la codificación UTF-8.
# Escribimos el contenido de la cadena json_content en el archivo.
