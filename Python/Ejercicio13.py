CM_EN_PULGADA=2.54

def conversionUds(cantidadP):
    centimetros = cantidadP * CM_EN_PULGADA
    return centimetros

cantidadP = float(input("El número de pulgadas que desea pasar a cm: "))
centimetros = conversionUds(cantidadP)
print(f"{cantidadP} pulgadas son {centimetros} centimetros")