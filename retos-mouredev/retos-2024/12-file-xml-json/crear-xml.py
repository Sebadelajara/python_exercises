"""Forma con modulo de crear archivo XML"""
import xml.etree.ElementTree as xml
import os

data = {
    'nombre': 'sebas',
    'edad': '33',
    'fecha_nacimiento': '15-09-1990',
    'lenguajes_programacion': ['python', 'rust', 'javascript']
}

xml_file = 'seba.xml'


def save_xml():

    root = xml.Element('data')

    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(xml_file)


save_xml()
with open(xml_file, "r") as xml_data:
    print(xml_data.read())

os.remove(xml_file)


"""Forma manual de crear archivo XML"""
# nombre = 'sebas'
# edad = '33'
# fecha_nacimiento = '15-09-1990'
# lenguajes_programacion = ['python', 'rust', 'javascript']

# # Iniciar la cadena XML con la declaración y el elemento raíz
# xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
# xml_content += '<persona>\n'

# # Añadir los datos personales
# xml_content += f'    <nombre>{nombre}</nombre>\n'
# xml_content += f'    <edad>{edad}</edad>\n'
# xml_content += f'    <fecha_nacimiento>{fecha_nacimiento}</fecha_nacimiento>\n'

# # Añadir la lista de lenguajes de programación
# xml_content += '    <lenguajes_programacion>\n'
# for lenguaje in lenguajes_programacion:
#     xml_content += f'        <lenguaje>{lenguaje}</lenguaje>\n'
# xml_content += '    </lenguajes_programacion>\n'

# # Cerrar el elemento raíz
# xml_content += '</persona>'

# # Escribir el contenido en un archivo XML
# with open('persona.xml', 'w', encoding='utf-8') as file:
#     file.write(xml_content)
