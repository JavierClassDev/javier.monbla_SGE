entero = int(input("Introduce un entero mayor a cero:"))
lista=[]
if entero>0:
    for i in range(entero):
        if i!=0:
            if (entero%i)==0:
                lista.append(i)
    print(f"Los divisores de {entero} son {lista}")
else:
    print("Es menor o igual a cero")
    