CM_EN_M=100
M_EN_KM=1000

def simplificacion(cantidadCM):
    metros = cantidadCm // CM_EN_M
    centimetros = cantidadCm % CM_EN_M
    kilometros = metros // M_EN_KM
    metros = metros % M_EN_KM
    return kilometros, metros, centimetros

cantidadCm = int(input("Inserte el número de centímetros que desea simplificar: "))
kilometros, metros, centimetros = simplificacion(cantidadCm)
print(f"{cantidadCm} centimetros son {kilometros} kilometros, {metros} metros y {centimetros} centimetros")