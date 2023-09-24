diccionario= {
    "Nombre" : "Lio Messi",
    "Instagram" : "@leomessi",
    "es_el_mejor_de_la_hisoria" : True,
    "altura" : 1.70
}

#nos devuleve un objeto dict_item
claves = diccionario.keys()
print(claves)

#obteniendo un elemento con get() si no encuentra nada el programa sigue
valor_de_Nombre = diccionario.get("altura")
print(valor_de_Nombre)

#eliminando un elemento del diccionario
diccionario.pop("Instagram", "Nombre")

#obteniendo un elemento dict_item iterable
diccionario_iterable = diccionario.items()


#eliminando todo del diccionario
#diccionario.clear()

print(diccionario_iterable) 