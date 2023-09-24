animales = ["perro", "gato", "monkey", "horse"]
numeros = [10, 11, 12 , 14, 15]

#recorriendo la lista animales
for animal in animales:
    print(f"Ahora la varialble animal es igual a: {animal}")

#recorriendo la lista numeros
for numero in numeros:
    print(numero*2)
    
#iterando 2 o mas elementos de una lista con la función zip()
for numero,animal in zip(animales,numeros):
    print(f"Recorriendo lista1: {animal}")
    print(f"Recorriendo lista2: {numero}")

#forma no optima de recorrer una lista
for num in range(len(numeros)):
    print(num)
    
#forma optima de recorrer una lista
for num in enumerate(numeros):
    indice = num[0]
    valor = num [1]
    print(f"El indice es: {indice} y el valor es: {valor}")
    
    