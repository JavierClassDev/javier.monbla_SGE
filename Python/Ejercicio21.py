c = int(input("Introduce el capital inicial: "))
x = int(input("Introduce la tasa de interés: "))
n = int(input("Introduce el numero de anios: "))

Cn= c * (1 + (x / 100)) ** n
print(f"El beneficio despues de {n} años es {Cn}")