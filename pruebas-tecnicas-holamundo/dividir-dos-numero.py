# dividir 2 numeros sin utilizar simbolo de division y multiplicacion

# mi solucion
dividendo = int(input("Ingresa el dividendo: "))
divisor = int(input("Ahora ingresa el divisor: "))

if dividendo > divisor:
    result = 0
    while dividendo >= divisor:
        dividendo -= divisor
        result += 1
    print(result)
elif dividendo < divisor:
    print(0)
elif dividendo == divisor:
    print(1)
else:
    print("Error")

# respuesta de copilot


# def dividir(dividendo, divisor):
#     contador = 0
#     while dividendo >= divisor:
#         dividendo -= divisor
#         contador += 1
#     return contador
