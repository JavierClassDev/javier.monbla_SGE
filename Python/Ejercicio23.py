productos = {
    "payaso": 112,
    "muñeca": 75,
    "robot": 250,
    "peluche": 180,
    "puzzle": 400
}

peso = 0

for i in productos:
    num = input(f"Cuantas unidades de '{i}' contiene el paquete?")
    peso = peso + (int(productos[i]) * int(num))

print(f"El peso total del paquete es de {peso} gr.")