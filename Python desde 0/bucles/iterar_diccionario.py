
diccionario = {
    "Nombre": "José",
    "Apellido": "González",
    "Edad": 17,
    "Sueño": "Ser programador"
}

print(diccionario) 
print("------------------------------------")
#Recorriendo un diccionario para obtener la clave
for key in diccionario:
    print(f"La clave es: {key}")
print("------------------------------------")
#Recorriendo un diccionario para obtener el valor
for valor in diccionario.items():
    valores = valor[1]
    print(f"El valor es: {valores}")
print("------------------------------------")
#Recorriendo un diccionario con la funcion itemns() para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(key, value)
    