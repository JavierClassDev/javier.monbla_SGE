SEGUNDOS_EN_MINUTO=60
MINUTOS_EN_HORA=60

def simplificacion(cantidad):
    minutos = cantidad // SEGUNDOS_EN_MINUTO
    segundos = cantidad % SEGUNDOS_EN_MINUTO
    horas = minutos // MINUTOS_EN_HORA
    minutos = minutos % MINUTOS_EN_HORA
    return horas, minutos, segundos

cantidad = int(input("El número de segundos que desea simplificar: "))
horas, minutos, segundos = simplificacion(cantidad)
print(f"{cantidad} segundos son {horas} horas, {minutos} minutos y {segundos} segundos")