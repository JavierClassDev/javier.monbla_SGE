def esBisiesto(año):
    if ((año % 4 == 0 and año % 100 != 0) or año % 400 == 0):
        return True
    else:
        return False

def diasEnMes(mes):
    dias_por_mes = {
        'Enero' : 31,
        'Febrero' : 28,
        'Marzo' : 31,
        'Abril' : 30,
        'Mayo' : 31,
        'Junio' : 30,
        'Julio' : 31,
        'Agosto' : 31,
        'Septiembre' : 30,
        'Octubre' : 31,
        'Noviembre' : 30,
        'Diciembre' : 31,
    }
    if mes in dias_por_mes.keys():
        return int(dias_por_mes.get(mes))
    else:
        return 0
    
def fechaValidar(dia,mes,año):
        diasMes=diasEnMes(mes)
        if (esBisiesto(año)==True) and (diasMes==28):
            diasMes=29
        if diasMes==0:
            print("El mes no existe")
        elif dia>diasMes:
            print("Este día no se encuentra en este mes")
        else:
            print("La fecha es correcta")
        