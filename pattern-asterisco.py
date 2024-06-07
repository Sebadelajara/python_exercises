def pattern_4(rows):
    """esta funcion genera un reloj de arena
    con '*' tomando como valor de columnos el numer
    ingresado en 'n'"""
    k = rows - 2
    for i in range(rows, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k += 1
        for j in range(0, i + 1):
            print('*', end=' ')
        print('\r')
    k = 2 * rows - 2
    for i in range(0, rows + 1):
        for j in range(0, k):
            print(end=' ')
        k -= 1
        for j in range(0, i + 1):
            print('*', end=' ')
        print('\r')


# driver code
n = 5
# to take input from user
n = eval(input('enter the number of rows: '))
pattern_4(n)

# print('hola', end=' ')
# print('hola')
