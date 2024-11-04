productos = {
    "Camiseta": 15,
    "Pantalon": 25,
    "Zapatos": 30,
    "Gorra": 10,
    "Cinturon": 20,
}
info_productos = productos.items()
limit=int(input("Introduzca el maximo a gastar en un  producto"))
for producto in info_productos:
    if(producto[1]<=limit):
        print(producto[0] + " : " + str(producto[1]) + "€")
