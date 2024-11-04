alto = int(input("Introduce una altura mayor a cero:"))
ancho = int(input("Introduce un ancho mayor a cero:"))
if alto>0 and ancho>0:
    for i in range(alto):
        for j in range (ancho):
            if (i==0) or (i == (alto - 1)) or (j==0) or (j == (ancho - 1)):
                print("*", end="  ")
            else:
                print(" ", end="  ")
        print()
else:
    print("El alto o el ancho es negativo o 0.")