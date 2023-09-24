
#creando una lista (estas se pueden modificar)
lista = ["Hola soy Jose Angel", "Tengo 17 años", "jodel"]

#creando una tupla (Estas no se pueden modificar)
tupla = ("Hola soy Jose Angel", "Tengo 17 años", "jodel")

#esto es válido
lista[2] = "te amo"

print(lista[2])

#esto no es válido
#tupla[0] = "Messi"
 
 
#creando un conjunto (set) 
#se pueden redefinir, pero no deja acceder a ningún índice. Ejemplo: print(conjunto[2]) -> no accede al índice
#No permite repedir valores. Ejemplo: "conjunto = {"Hola soy Jose Angel", "Tengo 17 años", "jodel", "jodel"}"
conjunto = {"Hola soy Jose Angel", "Jodel" ,"Tengo 17 años", "jodel", "jodel"}
print(conjunto)

#Creando un diccionario (La estructura es key: value y se separa con comas)
diccionario = {
    "Nombre" : "Lio Messi",
    "Instagram" : "@leomessi",
    "es_el_mejor_de_la_hisoria" : True,
    "altura" : 1.70,
    "dato_duplicado" : "@leomessi"
}

print(diccionario["Nombre"] + " " + lista[2])
