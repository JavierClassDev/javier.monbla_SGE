n1=1
n2=input("Introduce un número: ")
while n1<=10:
    print(str(n1),"*",str(n2),"=",str(int(n1)*float(n2)))
    n1=float(n1)+1
print("Terminado")