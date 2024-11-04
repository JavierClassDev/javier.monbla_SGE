alto = int(input("Introduce una altura mayor a cero:"))
ancho = int(input("Introduce un ancho mayor a cero:"))
if alto>0 and ancho>0:
    for i in range(alto):
        for j in range (ancho):
            print("*", end="  ")
        print()
else:
    print("El alto o el ancho es negativo o 0.")