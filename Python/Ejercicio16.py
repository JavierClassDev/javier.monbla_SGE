salir = True
while salir:
    print("Diga “SI” para continuar")
    pregunta = input()
    if(pregunta.upper()==str("SI")):
        salir=False
        print("¡Hasta la vista!")