#Creando las listas
lista = ["Patilla", "Mandarina", "Naranja", "Manzana", "Pera", "Ciruela", "Mora"]
cadena = "Te amo Messi"
numeros = [2, 5 , 7 , 10, 8]

#evitando un elemento de la lista con la sentencia continue
for fruta in lista:
    if fruta == "Mora":
        continue
    print(f"Me voy a comer una: {fruta}")
print("------------------------------")

#Evitar que el bucle siga ejecutandose
for fruta in lista:
    if fruta == "Mandarina":
        break
    print(f"Me voy a comer una: {fruta}")
print(" ")
print("Bucle a finalizado")

#Recorrer una cadena de texto
for letra in cadena:
    print(letra)

#for en una sola línea de código (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)