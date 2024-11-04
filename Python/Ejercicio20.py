contactos = {
"Ana": "612 345 678",
"Luis": "622 987 654",
"Marta": "635 555 555",
"Pedro": "645 678 901",
"Lucía": "655 432 123",
"Carlos": "699 876 543",
"Laura": "677 321 890",
"Javier": "689 234 567"
}

telefono = str(input("Ingresa el teléfono del contacto(Formato: 123 456 789):").strip())

encontrado = False
for nombre, num in contactos.items():
    if num==telefono:
        encontrado = True
        break

if encontrado:
    print(f"El número {telefono} pertenece a {nombre}.")
else:
    print(f"El número {telefono} no está registrado")
