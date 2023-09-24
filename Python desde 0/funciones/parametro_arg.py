#forma no optima de sumer valores
#def suma(lista):
#    numeros_sumados = 1
#    for numero in lista:
#        numeros_sumados = numeros_sumados + numero
#    return numeros_sumados

#resultado = suma([5,3,9,8])

#Forma optima de sumer valores
def suma_total(*numeros):
    return sum(*numeros)

resultado2 = suma_total ([5,4,9,10,11,12])
print(f" La nueva suma de tus numeros es: {resultado2}")

#Los mismo de arriba pero utilizando el operador * como parametro (*args)

def suma(nombre, *numeros):
    return f"{nombre} La suma de tus numeros es: {sum(numeros)}"
    
resultado = suma("José", 5,4,8,7,10)
print(resultado)
