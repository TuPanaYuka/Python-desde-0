
cadena1 = "hola soy Lio Messi"
cadena2 = "Ladrame perro de agua"

#convierte todo en mayus
mayusc = cadena1.upper()

#convierte a minus
minusc = cadena1.lower()

#primera letra en mayus
priemera_letra_mayusc = cadena1.capitalize()

#bucar una cadena en otra cadena, si no hay coincidencias nos devuelve -1 (te dice en que posición está lo que mandas a buscar)
busqueda_find = cadena1.find("o")

#bucamos una cadena en otra cadena, si no hay coincidencias nos devuelve error
busqueda_index = cadena1.index("a")

#si es numerico, devolvemos true, sino devolvemos false
es_numerico= cadena1.isnumeric()

#si es alfanumerico, devolvemos true, sino devolvemos true
es_alfa_numerico = cadena1.isalpha()

#contamos las concidencias de una cadena dentro de otra cadena, devuleve la cantidad de coincidencias si no se encuentra tira 0
contar_coincidencias = cadena1.count("lasoy")

#cuenta cuantos caracteres tiene una cadena
cuenta_caracteres= len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("hOla")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("pibe")

#Reemplaza un trozo de la cadena dada por otro dado
cadena_nueva= cadena1.replace(" ", ",")

#separar cadenas con la cadena que le pasemos
cadena_separada= cadena1.split(",")

print(contar_coincidencias)