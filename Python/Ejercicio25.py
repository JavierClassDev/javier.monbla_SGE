cantidad = int(input("Introduce la cantidad de valores a sumar: "))
enteros = []

for i in range(cantidad):
    entero = int(input(f"Valor {i + 1}:"))
    enteros.append(entero)

print(f"La suma total es: {sum(enteros)}")