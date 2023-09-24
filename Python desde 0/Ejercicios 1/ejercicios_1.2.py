#le pedimos al usuario que nos diga una frase (o varias)
frase = input("Dime una frase y te calculo cuanto tardas diciendolo: ")

#creamos una lista con todas las palabras de la frase
palabras_separadas = frase.split(" ")

#usamos len para poder cntar la cantidad de palabras que dijo el usuario
cantidad_de_palabras = len(palabras_separadas)

#en caso de que tarde mas de un minuto le decimos esto:
if cantidad_de_palabras > 120:
    print("Dale flaco, vas a tardar una vida")

#calculamos cuantas palabras tiene y cuanto tardaría en decir su frase y se lo decimos
print(f"dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/2} segundos en decirlo")
print(f"Yo lo diría en {cantidad_de_palabras/2*0.3} segundos ")
