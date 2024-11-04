productos = {
 "Leche": 10,
 "Pan": 8,
 "Huevos": 20,
 "Queso": 4,
 "Mantequilla": 6
}

for i in productos:
    num = int(input(f"Cuantas unidades de '{i}' desea?"))
    if int(productos[i]) < num:
        print(f"No hay suficientes unidades de {i} en inventario. Solo hay {productos[i]} unidades disponibles.")
        productos[i]=0
    if int(productos[i]) == num:
        print(f"¡Atención! El producto {i} se ha agotado.")
        productos[i]=0
    if int(productos[i]) > num:
        print(f"Pedido de unidades de {i} realizado.")
        productos[i]-=num

print()
print("Inventario:")
for i in productos:
    print(f"{i}:{productos[i]} unidades")