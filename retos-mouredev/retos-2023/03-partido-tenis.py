#  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#  * gane cada punto del juego.
#  *
#  * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#  * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#  *   15 - Love
#  *   30 - Love
#  *   30 - 15
#  *   30 - 30
#  *   40 - 30
#  *   Deuce
#  *   Ventaja P1
#  *   Ha ganado el P1
#  * - Si quieres, puedes controlar errores en la entrada de datos.
#  * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.punto = 0
        self.puntaje = 'love'

    def __str__(self) -> str:
        return f'{self.puntaje}'

    def win_point(self):
        self.punto += 1

        if self.punto == 0:
            self.puntaje = 'love'
        elif self.punto == 1:
            self.puntaje = '15'
        elif self.punto == 2:
            self.puntaje = '30'
        elif self.punto == 3:
            self.puntaje = '40'
        else:
            self.puntaje = 'AD'


player_1 = Player('p1')
player_2 = Player('p2')


def tenis_game(player1, player2):
    if player1.punto - player2.punto == 2 and player1.punto + player2.punto > 6:
        print('gana p1')
    elif player2.punto - player1.punto == 2 and player2.punto + player1.punto > 6:
        print('gana p2')
    elif player1.punto > 3 and player2.punto <= 3:
        print('ventaja p1')
    elif player2.punto > 3 and player1.punto <= 3:
        print('ventaja p2')
    elif player1.punto >= 3 and player2.punto >= 3:
        print('deuce')
    else:
        print(f'{player_1} - {player_2}')


# secuencia = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']
secuencia = ['P1', 'P1', 'P1', 'P1', 'P1', 'P1', 'P1', 'P2']

for i in secuencia:
    if i == 'P1':
        player_1.win_point()

    elif i == 'P2':
        player_2.win_point()

    tenis_game(player_1, player_2)
    # print(f'{player_1} - {player_2}')
