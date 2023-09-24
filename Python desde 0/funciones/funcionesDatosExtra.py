#Creando una función de 3 parametros
def frase(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

#Utilizando keywords agumentos
frase1 = frase(nombre = "Lionel", apellido = "Messi", adjetivo="GOAT")
print(frase1)