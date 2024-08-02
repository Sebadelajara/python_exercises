
# EJERCICIO:
# Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
# una petición a la web que tú quieras, verifica que dicha petición
# fue exitosa y muestra por consola el contenido de la web.
#  *
# DIFICULTAD EXTRA (opcional):
# Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
# terminal al que le puedas solicitar información de un Pokémon concreto
# utilizando su nombre o número.
# - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
# - Muestra el nombre de su cadena de evoluciones
# - Muestra los juegos en los que aparece
# - Controla posibles errores
import requests

pokemon = input('Introduce un nombre o número del Pokémon a buscar: ').lower()
response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
if response.status_code == 200:
    print("conexion exitosa")  # Muestra la respuesta en formato JSON
else:
    print("Error en la petición:, response.status_code")

data = response.json()

name = data['species']['name']
id_pokemon = data['id']
weight = data['weight']
height = data['height']


species_url = data['species']['url']

print(
    f'Name pokemon: {name}, id: {id_pokemon}, weight: {weight}, height {height}')
print('Tipo:')
for type in data['types']:
    print(type['type']['name'])

print('Juegos en que aparece:')
list_game = []
for game in data['game_indices']:
    list_game.append(game['version']['name'])
print(list_game)

response = requests.get(species_url)
if response.status_code == 200:
    print(f'Conexión exitosa a {species_url}')
    species_data = response.json()
    evolution_chain_url = species_data['evolution_chain']['url']
    response = requests.get(evolution_chain_url)
    if response.status_code == 200:
        evolution_data = response.json()
        current_stage = evolution_data['chain']

        # Imprimir la especie base
        print(f"Especie base: {current_stage['species']['name']}")

        # Iterar a través de todas las evoluciones
        while current_stage['evolves_to']:
            for evolution in current_stage['evolves_to']:
                print(f"Siguiente evolución: {evolution['species']['name']}")
                current_stage = evolution  # Actualizar el 'current_stage' para la siguiente iteración
    else:
        print(
            f'Error al obtener la cadena de evolución: {response.status_code}')
else:
    print(f'Error: {response.status_code}')
