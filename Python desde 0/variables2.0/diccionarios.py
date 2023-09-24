#creando diccionarios con dic()
diccionario = dict(nombre = "José", Apellido = "Gonzalez", edad = 17)

#las listas no pueden ser claves y usamos frozenset([]) para meter conjuntos
diccionario = {frozenset(["José", "the best"]): "jajajaj"}

#Creando un diccionario con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre", "apellido"])

#Creando un diccionario con fromkeys() cambiando el valor por defecto a: "no se"
diccionario = dict.fromkeys(["nombre", "apellido"], "No se")

print(diccionario)