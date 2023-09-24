
#creando una función simple
#def saludar():
    #print("Te amo Madre")
#saludar()


#crear una función con parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "Reina"
    elif (sexo == "hombre"):
        adjetivo = "rey"
    else:
        adjetivo = "amor"
        
    print(f"Hola {nombre}, ¿Todo bien mi {adjetivo}?")
saludar("Leo Messi", "Hombre")
saludar ("Antonella", "MUJER")

#Crear una función que retorne valores
def crear_una_contraseña_random(num):
    chars =  "abcdefghij"
    numero_entero = str(num)
    num = int(numero_entero [0])
    c1 = num - 2
    c2 = num
    c3 = num -5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return(contraseña, num)

#desempaquetando la función
password, primer_nmero = crear_una_contraseña_random(221)

#retornando los resultados obtenidos y los numeros utilizados para obtenerlos
print(f"Tu nueva contraseña es: {password}")
print(f"el número usado fue: {primer_nmero}")