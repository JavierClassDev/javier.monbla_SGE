cantidad = int(input("Introduce la cantidad de valores a incluir: "))
enteros = []

for i in range(cantidad):
    entero = int(input(f"Valor {i + 1}:"))
    enteros.append(entero)

print(f"Media aritmética: {sum(enteros)/cantidad}")
print(f"Maximo: {max(enteros)}")
print(f"Minimo: {min(enteros)}")