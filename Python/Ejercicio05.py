peso = float(input("Indica tu peso corporal en kilogramos"))
altura = float(input("Indica tu altura en metros"))
imc = peso/altura**2
print("Tu IMC es: " + str(imc))
if imc<18.5:
    print("Bajo Peso")
elif imc<24.9:
    print("Peso normal")
elif imc<29.9:
    print("Sobrepeso")
elif imc<34.9:
    print("Obesidad tip I (Leve)")
elif imc<39.9:
    print("Obesidad tipo II (Moderada)")
elif imc>=40:
    print("Obesidad tipo III (Mórbida)")