
#Creando una funcion que nos devuelva los numeros primos
#entre 0 y el argumento que pasamos

#Crear una función que verifique si un numero es primo
def es_primo(num):
    #Verificamos que el numero pasado no puedad dividirse
    #por ningún numero entre 2 y ese mismo numero -1
    for i in range (2,num-1):
        #si el numero es retornable por alguno retornamos false y terminamos el bucle
        if num%i==0: return False
    #si termina el bucle, significa que no fue divisible entonces es primo
    return True

#Crear una función que cree una lista con todos los primos
def primos_hasta(num):
    primos = []
    for i in range(1,num+1):
        #verificamos la lista
        resultado = es_primo(i)
        #En caso de que sea lo agregamos a la lista
        if resultado == True: primos.append(i)
    #Devolvemos la lista
    return primos 
#Creamos el restultado llamando a la función y lo creamos
resultado = primos_hasta(50)
print(resultado)