num_multiplos = 0
multiplo = int(input("Introduce un múltiplo de 5:"))
if((multiplo%5)==0):
    num_multiplos =+ 1
continuar=True
while(continuar==True):
    orden=str(input("Desea continuar(NO o N para salir):"))
    if((orden=="no") or (orden=="n") or (orden=="NO") or (orden=="N")):
        continuar=False
    else:
        multiplo = int(input("Introduce un múltiplo de 5:"))
        if((multiplo%5)==0):
            num_multiplos =+ 1
print(f"Has escrito {num_multiplos} números múltiplos de 5.")
