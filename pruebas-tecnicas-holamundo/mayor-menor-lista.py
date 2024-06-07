# iterando un array solo 1 vez encuentre el mayor y el menor

# mi solucion
num_list = [0, 7, 2, 9, 4, 40, 6, 7, 8, 9, 10, 0]

mayor = num_list[0]
menor = num_list[0]

for i in num_list:
    if i > mayor:
        mayor = i
    elif i < menor:
        menor = i

print(f"el mayor es {mayor}, el menor es {menor}")
