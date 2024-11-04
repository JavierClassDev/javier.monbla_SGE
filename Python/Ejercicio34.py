bucle=True
while bucle:
    orden = input("Introduce un número ('*' para salir): ")
    if orden == '*':
        print("Programa terminado.")
        bucle=False
    else:
        try:
            numero = int(orden)
            if numero > 0:
                print("Número positivo")
            elif numero == 0:
                print("Igual a 0")
            else:
                print("Número negativo")
        except ValueError:
            print("Por favor, introduce un número.")