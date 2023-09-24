contactos = {
    "James": 42,
    "Amy": 24,
    "John": 31,
    "Amanda": 63,
    "Bob": 18
}

# Pide al usuario una clave para buscar en el diccionario
clave = input("Introduce una clave: ")

# Busca si la clave está presente en el diccionario
if clave in contactos:
    print( clave, "is", contactos[clave])
else:
    print("La clave", clave, "no se encontró en el diccionario.")