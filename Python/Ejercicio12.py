line=input("Cadena a analizar: ")
res=0
for char in line:
    if char in ["a","e","i","o","u","A","E","I","O","U"]:
        res +=1
print("La cantidad de vocales es:",res)