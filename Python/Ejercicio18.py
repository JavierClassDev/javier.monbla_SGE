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

nom = str(input("Nombre del contacto a buscar/añadir:").strip())
if nom in contactos.keys():
    print(f"El número de {nom} es <{contactos.get(nom)}>")
else:
    telefono = str(input("Ingresa el teléfono del nuevo contacto(Formato: 123 456 789):").strip())
    d2 = {nom: telefono}
    contactos.update(d2)
    print(f"El número de {nom} es <{contactos.get(nom)}>")