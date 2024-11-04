estudiantes = (("José", 5), ("Ana", 8), ("Luis", 6), ("María", 9),("Pedro", 4))
for estudiante in estudiantes:
    if(estudiante[1]>=5):
        print("El estudiante " + estudiante[0] + "ha aprobado con un " + str(estudiante[1]))

